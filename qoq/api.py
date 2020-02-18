
import os

from flask import request, jsonify, abort, Response, send_file, Blueprint
from flask import current_app as app
from flask_restplus import Api, Resource, Namespace, fields, reqparse
from datetime import datetime, date, timedelta

from .helpers.jira import JiraHelper

blueprint= Blueprint('api', __name__)

api = Api(blueprint)

@api.route('/issues')
class IssuesResource(Resource):

  @api.response(200, 'Sucesss')
  @api.response(400, 'Error')
  @api.doc('teams')
  @api.doc(description='Get all issues with a quality overview')
  def get(self):
    try:
      return [], 200
    except Exception as e:
      app.logger.error(e, exc_info=True)
      abort(400, 'Unable to get teams available')
    
