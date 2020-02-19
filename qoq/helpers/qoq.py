
from flask import current_app as app

from .github import GithubHelper
from .circleci import CircleCIHelper

import logging
import sys


def fetch_vcs_repositories(vcs_token):
  try:
    github_session= GithubHelper(vcs_token)
    app.logger.info("Fetching VCS repositories")
    return github_session.get_own_repos(include_branches=False)
  except Exception as e:
    app.logger.error("Unable to fetch user VCS repositories: %s", repr(e))
    return []

def fetch_ci_projects(ci_token):
  try:
    ci_session= CircleCIHelper(ci_token)
    app.logger.info("Fetching CI projects")
    return ci_session.get_own_projects(include_branches=False)
  except Exception as e:
    app.logger.error("Unable to fetch user CI projects: %s", repr(e))
    return []
  

# Returns a list of VCS repositories with CI builds incl. build general stats
def correlate_vcs_and_ci(repositories, projects):
  try:

    vcs_ci_repos = []
    app.logger.info("Correlating %i VCS repositories against %i CI projects", len(repositories), len(projects))

    for repo in repositories:

      # Search for matching repos within the list of Circle CI projects fetched
      if any(repo['name'] in project['name'] for project in projects):
        vcs_ci_repos.append({ "name": repo['name'] })
    
    return vcs_ci_repos

  except Exception as e:
    app.logger.error("Unable to correlated VCS/CI stats: %s", repr(e))
    return []


def fetch_ci_project_stats(token, projects):
  try:
    ci_session= CircleCIHelper(token)
    
    project_stats = []
    
    for project in projects:
      username = project['name'].split('/')[0]
      reponame = project['name'].split('/')[1]

      app.logger.info("Fetching '%s' project stats", project['name'])

      builds = ci_session.get_latest_project_builds(username, reponame)
      project_stats.append({
        "name": project['name'],
        "builds": builds
      })
    
    return project_stats

  except Exception as e:
    app.logger.error("Unable to fetch CI project details: %s", repr(e))
    return []
