#!flask/bin/python
from migrate.versioning import api
from congfig import SQLALCHEMY_DATABASE_URI
from congfig import SQLALCHEMY_MIGRATE_REPO
v=api.db_version(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPPO)
api.downgrade(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO,v - 1)
print 'Current database version: ' + str(api.db_version(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO))
