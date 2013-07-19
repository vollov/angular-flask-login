# -*- coding: utf-8 -*-
import unittest,sqlalchemy
from domain.auth import User
from orm.database import db_session, engine, Base

class UserUt(unittest.TestCase):
    '''A Unit Test Demo'''

    def setUp(self):
        Base.metadata.drop_all(engine)
        import domain
        Base.metadata.create_all(engine) 

        
#     def tearDown(self):
#         Base.metadata.drop_all(engine)
        
#     def test_version(self):
#         self.assertEquals('0.8.1',sqlalchemy.__version__,\
#                           'version number not match')

    def test_insert_user(self):
        db_session.add_all([
                         User('wendy', 'foobar', True),
                         User('mary', 'passwd', False),
                         User('fred', 'blah', True)])
        db_session.commit()
        user = User.query.filter(User.id == 1).first()
        print user
        user = User.query.filter(User.id == 12).first()
        print user

if __name__=='__main__': unittest.main()