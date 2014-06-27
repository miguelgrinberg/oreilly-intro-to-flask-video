import unittest
from app import create_app, db
from app.models import User


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_ctx = self.app.app_context()
        self.app_ctx.push()
        db.create_all()

    def tearDown(self):
        db.drop_all()
        self.app_ctx.pop()

    def test_password(self):
        u = User(username='john')
        u.set_password('cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))

    def test_registration(self):
        User.register('john', 'cat')
        u = User.query.filter_by(username='john').first()
        self.assertIsNotNone(u)
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))