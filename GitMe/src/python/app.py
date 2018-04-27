from flask import Flask, render_template, request
from flask_restful import Resource, Api, abort
from flask_jsonpify import jsonify
import json
import pymysql as PyMySQL
from toDB import write_to_repository, write_to_user


## DB connection information
cnx =	{
		'host': "gitme.cnolzaujohll.us-east-2.rds.amazonaws.com",
		'username' : "James",
		'password' : "password",
		'db' : "GitMe"
		}

#db = PyMySQL.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])
app = Flask(__name__)
api = Api(app)


class Users(Resource):
	def get(self):
		# connect to DB
		db = PyMySQL.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])

		try: 
			with db.cursor() as cursor:
				sql = "SELECT username FROM user"
				cursor.execute(sql)
				result = cursor.fetchone()
				print(result) 
		finally:
			db.close()
		# Get users
		# return user jsonify()
		return result

	def post(self, username=None, password=None):
		args = request.args

		try:
			username = args['username']
			password = args['password']
		except KeyError:
			# TODO "Tell them something bad happened"
			print("What a Terrible Failure: username and password not given: USERS POST")
			pass

		write_to_user(username=username, password=password)
		pass


class User(Resource):
	def get(self, username):
		# connect to DB
		db = PyMySQL.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])
		
		try: 
			with db.cursor() as cursor:
				sql = "SELECT * FROM user WHERE username = %s"
				cursor.execute(sql, (username))
				result = cursor.fetchone()
		finally:
			db.close()

		return result
		# get user information
		# return user jsonify()
		

class CalendarAssignments(Resource):
	def get(self, username):
		db = PyMySQL.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])

		try:
			with db.cursor() as cursor:
				sql = "SELECT * FROM calendar_assignment WHERE username = %s"
				cursor.execute(sql, username)
				result = cursor.fetchone()

		finally:
			db.close()

		return result
		# connect to DB
		# Query for all the CalendarAssignments of a certain user
		

	def post(self, username, description, title, date):
		# connect to DB
		# insert new CalendarAssignment
		pass

	def put(self, username, description, title, date, id):
		# connect to DB
		# update the given calendarAssignment (ID)
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

	def post(self, username=None, password=None):
		args = request.args

		try:
			username = args['username']
			password = args['password']
		except KeyError:
			# TODO "Tell them something bad happened"
			print("What a Terrible Failure: username and password not given: REPO POST")
			pass

		write_to_repository(username=username, password=password)

class RepositoryByUser(Resource):
	def get(self, username):
		# get URLs and names for all the repositories of a certain user
		pass

	def post(self, username=None, password=None):
	args = request.args

	try:
		username = args['username']
		password = args['password']
	except KeyError:
		# TODO "Tell them something bad happened"
		print("What a Terrible Failure: username and password not given: REPO POST")
		pass

	write_to_repository(username=username, password=password)
	
class FeedEntity(Resource):
	def get(self, repository):
		# connect to DB
		# return all Feed_Entities for a repository
		pass

class Update(Resource):
	def put(self, username=None, password=None):
		# connect to DB
		# insert all the relevant infromation for user into database
		pass



api.add_resource(Users, '/users') # Route_1
api.add_resource(User, '/users/<username>')
api.add_resource(CalendarAssignments, '/users/<username>/calendar_assignments')
api.add_resource(ProjectGroupsByUser, '/users/<username>/project_groups')
api.add_resource(Repository, '/repository')
api.add_resource(RepositoryByUser, '/<username>/repository')
api.add_resource(FeedEntity, '/<repository>/feed_entity')
api.add_resource(Update, '/update/<username>')

if __name__ == '__main__':
	app.run(debug=True)
