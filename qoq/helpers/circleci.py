
from flask import current_app as app
from circleci.api import Api
import logging
import sys

class CircleCIHelper:
  def __init__(self, token):
    try:
      self.ci = Api(token)
      self.username = self.ci.get_user_info()['login']
      app.logger.info("Initialised connection to Circleci with user: %s", self.username)
      return None

    except Exception as e:
      app.logger.error("Unable to initialise connection to CircleCi api: %s", repr(e))
      return None
  
  def get_own_projects(self, include_branches=False):
    try:
      projects = []
      
      for project in self.ci.get_projects():
        
        if (include_branches):
          branches = []
          for branch in project['branches']:
            branches.append(branch)

          projects.append({
            "name": project['username'] + "/" + project['reponame'],
            "branches": branches
          })
        else:
          projects.append({
            "name": project['username'] + "/" + project['reponame']
          })

      return projects      
    except Exception as e:
      app.logger.error("Unable to get user own projects: %s", repr(e))
      return []


  def get_latest_project_builds(self, username, project):
    try:
      recent_builds = []

      for build in self.ci.get_project_build_summary(username, project):
        recent_builds.append({
          "build_num": build['build_num'],
          "branch": build['branch'],
          "status": build['status'],
          "build_time_ms": build['build_time_millis'],
          "start_time": build['start_time']
        })

      return recent_builds

    except Exception as e:
      app.logger.error("Unable to get user '%s' latest project '%s' builds: %s", username, project, repr(e))
      return []
