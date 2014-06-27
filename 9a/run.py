#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User

if __name__ == '__main__':
    config_name = os.environ.get('FLASK_CONFIG') or 'development'
    print(' * Loading configuration "{0}"'.format(config_name))
    app = create_app(config_name)
    with app.app_context():
        db.create_all()
        if app.config['DEBUG'] and \
                User.query.filter_by(username='john').first() is None:
            User.register('john', 'cat')
    app.run()
