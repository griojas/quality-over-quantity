"""
jira.py
  - Uses JIRA python library to fetch development issue information
  - JIRA JQL reference https://confluence.atlassian.com/jirasoftwarecloud/advanced-searching-fields-reference-764478339.html
  - JIRA REST API reference https://docs.atlassian.com/software/jira/docs/api/REST/8.3.1/
"""

from flask import current_app as app
from jira import JIRA
from datetime import datetime, date,timedelta
import logging
import sys

class JiraHelper:

  def __init__(self, url, user=None, api_key=None, default_fields= None):
    self.url= url
    self.user= user
    self.default_fields= default_fields

    try:
      self.jira= JIRA(server=url, basic_auth=(user, api_key))
      app.logger.info("Successfully connected to: %s", url)

    except Exception as e:
      app.logger.error("Error connecting to JIRA: %s", e, exc_info=True)
      raise e
  
  def projects(self):
    available_projects=  self.jira.projects()
    response= []
    
    for project in available_projects:
      response.append({
        "name": project.name,
        "key": project.key,
        "avatar": project.avatarUrls.__dict__['48x48']
      })

    return response
  
  # Returns ALL jql matching tickets along with the requested fields.
  def search(self, jql, fields):
    try:
      issues=[]
      total = 0
      start_at= 0
      max_results= 50
      end_of_query= False

      while (end_of_query==False):

        query= self.jira.search_issues(
          jql,
          startAt=start_at,
          maxResults=max_results,
          fields=fields,
          json_result=False
        )

        if (not query):
          end_of_query= True
          total= query.total
        else:
          issues.extend(query)
          start_at+= max_results

      query_result= JiraHelper.QueryResult(jql, total, issues, max_results, self.default_fields)

      return query_result

    except Exception as e:
      app.logger.error("Unable to execute JQL: %s", jql)
      app.logger.error(e, exc_info=True)
      raise(e)
      
  class QueryResult:
    def __init__(self, jql, total, matches, max_results, fields):
      self.jql= jql
      self.total= total
      self.matches= matches
      self.max_results= max_results
      self.fields= fields