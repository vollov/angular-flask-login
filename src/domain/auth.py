# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Sequence, Boolean
from orm.database import Base

from itsdangerous import URLSafeTimedSerializer
from utils.prod_setting import configuration

class AnonymousUser:
    #############################################################
    # method required by flask-login
    #############################################################
    
    def is_authenticated(self):
        return False
    
    def is_anonymous(self):
        return True
    
    def is_active(self):
        return False
    
    def get_id(self):
        return None
    
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer,Sequence('user_id_seq'), primary_key=True)
    name = Column(String(16), unique=True)
    password = Column(String(16))
    active = Column(Boolean, unique=False, default=True)
    
    def __init__(self, name=None, password=None, is_active=True, oid=None):
        self.name = name
        self.password = password
        self.active = is_active
        self.id = oid
    
    def get_auth_token(self):
        """
        Encode a secure token for cookie
        """
        login_serializer = URLSafeTimedSerializer(configuration.get('auth', 'secret_key'))
        data = [str(self.id), self.password]
        return login_serializer.dumps(data)
    
    def __repr__(self):
        return "<User('%d', %s', '%s')>" % (self.id, self.name, self.password)

    def dict(self):
        return {'id':self.id, 'name':self.name, 'password':self.password, 'active': self.active}
    
    #############################################################
    # method required by flask-login
    #############################################################
    
    def is_authenticated(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def is_active(self):
        return self.active
    
    def get_id(self):
        return unicode(self.id)