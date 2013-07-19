# -*- coding: utf-8 -*-

from flask import Blueprint, Response, request
from flask.ext.restful import Resource

from domain.auth import User
from orm.database import db_session
from utils.json_utils import JsonUtil

class UserApi(Resource):
    def get(self):
        
        try:
            users = User.query.all()
            return Response(JsonUtil.listToJson(users), mimetype='application/json')
            
        except Exception as e:
            print e
            return '', 500
        
        
    