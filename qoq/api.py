
import os
from flask import current_app as app
from flask import request, jsonify, abort, Response, send_file, Blueprint
from flask_restplus import Api, Resource, Namespace, fields, reqparse
from .helpers.qoq import correlate_vcs_and_ci, fetch_vcs_repositories, fetch_ci_projects, fetch_ci_project_stats

blueprint= Blueprint('api', __name__)

api = Api(blueprint)

input_sources= api.model('Input Sources', {
  'ci_token': fields.String,
  'vcs_token': fields.String
})

@api.route('/stats')
class VCSResource(Resource):

  @api.response(200, 'Success')
  @api.response(400, 'Service error')
  @api.doc(description='Get overview statistics of repositories (Github) and builds (CircleCI)')
  @api.expect(input_sources)
  def post(self):
    try:
      ci_token = request.get_json()['ci_token']
      vcs_token = request.get_json()['vcs_token']

    except Exception as e:
      app.logger.error("Missing VCS/CI token from payload: %s", repr(e))
      abort(400, "Missing VCS/CI token from payload")


    try:
      repositories = fetch_vcs_repositories(vcs_token)
      projects = fetch_ci_projects(ci_token)
      repos_with_builds = correlate_vcs_and_ci(repositories, projects)
      stats = fetch_ci_project_stats(ci_token, repos_with_builds)
      
      return stats, 200
    except Exception as e:
      app.logger.error("Unable to correlate VCS and CI data to generate stats: %s", repr(e))
      abort(400,"Unable to correlate VCS and CI data to generate stats")
