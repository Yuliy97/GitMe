from flask import Flask, render_template
from flask_restful import Resource, Api, abort
from flask_jsonpify import jsonify
import json
import pymysql as PyMySQL


## DB connection information
cnx =	{
		'host': "gitme.cnolzaujohll.us-east-2.rds.amazonaws.com",
		'username' : "James",
		'password' : "password",
		'db' : "GitMe"
		}

db = PyMySQL.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])
app = Flask(__name__)
api = Api(app)


class Users(Resource):
	def get(self):
		# connect to DB
		# Get users with query (GitHub_username)
		# return user jsonify()
		pass

class User(Resource):
	def get(self, username, password):
		# connect to DB

		# get user information
		# return user jsonify()
		pass

	def post(self):
		#receive username????????
		#return token to identify user???????
		pass

class CalendarAssignments(Resource):
	def get(self, username):
		# connect to DB
		# Query for all the CalendarAssignments of a certain user
		pass

	def post(self, username, description, title, date):
		# connect to DB
		# insert new CalendarAssignment
		pass

	def put(self, username, description, title, date, id):
		# connect to DB
		# update the given calendarAssignment (ID)
		pass


class ProjectGroups(Resource):
	def get(self):
		# connect to DB
		# Get project information for username
		# return project_group jsonify()
		pass

class ProjectGroupsByUser(Resource):
	def get(self, username):
		# connect to DB
		# Query Contributes for repositories and group names
		pass

	def post(self, username, repository, group_name):
		# connect to DB
		# insert the new project_group tuple)
		pass

class Repository(Resource):
	def get(self):
		# get URLs and names for all the repositories
		pass

class RepositoryByUser(Resource):
	def get(self, username):
		# get URLs and names for all the repositories of a certain user
		pass

class FeedEntity(Resource):
	def get(self, repository):
		# connect to DB
		# return all Feed_Entities for a repository
		pass

class Update(Resource):
	def put(self, username):
		# connect to DB
		# insert all the relevant infromation for user into database
		pass



api.add_resource(Users, '/users') # Route_1
api.add_resource(User, '/<username>')
api.add_resource(CalendarAssignments, '/<username>/calendar_assignments')
api.add_resource(ProjectGroups, '/project_groups')
api.add_resource(ProjectGroupsByUser, '/<username>/project_groups')
api.add_resource(Repository, '/repository')
api.add_resource(RepositoryByUser, '/<username>/repository')
api.add_resource(FeedEntity, '/<repository>/feed_entity')

if __name__ == '__main__':
	app.run(debug=True)
