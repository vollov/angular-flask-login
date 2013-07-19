# -*- coding: utf-8 -*-

from flask import Flask, request
from flask.ext import restful
import re

app = Flask(__name__)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False

api = restful.Api(app)


############################################################
# global view mapping end
############################################################

def register_blueprints(application, api):
    #register angularjs front end
    from front_end import front
    application.register_blueprint(front)
    
    from api.auth_api import UserApi
    api.add_resource(UserApi, '/api/users')
    
register_blueprints(app, api)

if __name__ == '__main__':
    app.run(debug=False)