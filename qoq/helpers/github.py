
from flask import current_app as app
from github import Github
import logging
import sys

class GithubHelper:
  def __init__(self, token):
    try:
      self.g = Github(token)
      self.username = self.g.get_user().login
      app.logger.info("Initialised connection to github with user: %s", self.username)
      return None

    except Exception as e:
      app.logger.error("Unable to initialise connection to Github api: %s", repr(e))
      return None
  
  def get_own_repos(self, include_branches=False):
    try:
      own_repos= []
      res= self.g.search_repositories("user:" + self.g.get_user().login)
  
      for repo in res:
        if (include_branches):
          branches = self.get_branches(repo.full_name)
          
          own_repos.append({
            "name": repo.full_name,
            "branches": branches
          })

        else:
          own_repos.append({ "name": repo.full_name })
        
      return own_repos
    except Exception as e:
      app.logger.error("Unable to get own repositories for %s: %s", self.g.get_user().login, repr(e))
      return []

  def get_branches(self, repository):
    try:
      
      branches= []
      for branch in self.g.get_repo(repository).get_branches():
        branches.append(branch.name)

      return branches
    except Exception as e:
      app.logger.error("Unable to get branches for repo %s : %s", repository, repr(e))
      return []