# -*- coding: utf-8 -*-

from flask import Flask, request
from flask.ext import restful
from flask_login import LoginManager
from itsdangerous import URLSafeTimedSerializer
from domain.auth import User
from datetime import timedelta

from utils.prod_setting import configuration

login_manager = LoginManager()


app = Flask(__name__)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
app.secret_key = configuration.get('auth', 'secret_key')
login_serializer = URLSafeTimedSerializer(app.secret_key)
api = restful.Api(app)

############################################################
# global view mapping start
############################################################


############################################################
# flask login api call back methods
############################################################
@login_manager.user_loader
def load_user(userid):
    return User.query.filter(User.id == userid).first()

@login_manager.token_loader
def load_token(token):
    max_age = app.config["REMEMBER_COOKIE_DURATION"].total_seconds()
    #Decrypt the Security Token, data = [username, hashpass]
    data = login_serializer.loads(token, max_age=max_age)
    #Find the User
    user = User.query.filter(User.id == data[0]).first()
    
    print 'calling load_token()-->', data
    print 'query user and got->', user
    
    if user and data[1] == user.password:
        return user
    return None

############################################################
#  Restful api registration strat
############################################################

def register_blueprints(application, api):
    #register angularjs front end
    from front_end import front
    application.register_blueprint(front)
    
    from api.auth_api import UserApi
    api.add_resource(UserApi, '/api/users')
    
register_blueprints(app, api)

if __name__ == '__main__':
    app.config["REMEMBER_COOKIE_DURATION"] = timedelta(days=14)
    login_manager.setup_app(app)
    app.run(debug=False)