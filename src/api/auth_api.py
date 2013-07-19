# -*- coding: utf-8 -*-

from flask import Blueprint, Response, request
from flask.ext.restful import Resource

import json

class UserApi(Resource):
    def get(self):
        
        try:
            users =  [{
                "id": "1",
                "name": "dustin",
                'password': 'pass1'
              },
              {
                'id': '2',
                'name': 'leah',
                'password': 'Pass2'
              }
            ]
            
            return users
        except Exception as e:
            print e
            return '', 500
        
        
    