
import os
import json

from flask import request, jsonify, abort, Response, Blueprint, render_template

blueprint= Blueprint('reviews', __name__, template_folder='templates')

app_title= "Quality over Quantity"

@blueprint.route('/')
def show_index():
  profile_data= None

  try:
    return render_template('index.html', app_title=app_title)
    
  except Exception as e:
    return render_template('index.html', app_title=app_title)

