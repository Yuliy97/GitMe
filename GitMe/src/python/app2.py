from flask import Flask, request
from flask_restful import Resource, Api, abort
from flask_jsonpify import jsonify
from flask_cors import CORS
import json
import pymysql as PyMySQL
from toDB import write_to_all_info, authorize

cnx =	{
		'host': "gitme.cnolzaujohll.us-east-2.rds.amazonaws.com",
		'username' : "James",
		'password' : "password",
		'db' : "GitMe"
		}

app = Flask(__name__)
CORS(app)
api = Api(app)


def connect():
    return PyMySQL.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])

class Authenticate(Resource):
    def put(self, username=None, password=None):
        args = request.args
        try:
            username = args['username']
            password = args['password']
        except KeyError:
            return "Invalid credentials"
        return authorize(username, password)

api.add_resource(Authenticate, '/authorize')
        

class Users(Resource):
    def get(self):
        db = connect()

        try: 
            with db.cursor() as cursor:
                sql = "SELECT username FROM user"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally: 
            db.close()

        return result

api.add_resource(Users, '/user')

class User(Resource):
    def get(self, username):
        db = connect()

        try:
            with db.cursor() as cursor:
                sql = "SELECT * FROM user WHERE username=%s"
                cursor.execute(sql, username)
                result = cursor.fetchone()
                user = {}
                user['username'] = result[0]
                user['total_commits'] = result[1]
                user['avatar'] = result[2]
                user['html_url'] = result[3]
        finally:
            db.close()

        return user

api.add_resource(User, '/users/<username>')

class Repository(Resource):
    def get(self, username=None):
        db = connect()
        try:
            with db.cursor() as cursor:
                sql = "SELECT R.name, R.url, C.username, C.group_name FROM repository R JOIN (SELECT * FROM contributions WHERE username = %s) C ON R.url = C.repository" 
                cursor.execute(sql, username)
                result = cursor.fetchall()
                repos = []
                for repo in result:
                    t_repo = {}
                    t_repo['repo_name'] = repo[0]
                    t_repo['html_url'] = repo[1]
                    t_repo['username'] = repo[2]
                    t_repo['group_name'] = repo[3]
                    repos.append(t_repo)
        finally:
            db.close()


        return repos

    def post(self, username=None, repo_url=None, group_name=None):
        db = connect()
        args = request.args

        try:
            username = args['username']
            repo_url = args['repo_url']
            group_name = args['group_name']
        except:
            print("What a Terrible Failure: Repository Post")
        try: 
            with db.cursor() as cursor:
                sql = "UPDATE contributions SET group_name = %s WHERE username = %s AND repository = %s"
                cursor.execute(sql, (group_name, username, repo_url))
                db.commit()
        finally:
            db.close()
        


api.add_resource(Repository, '/users/<username>/repository')

class FeedEntity(Resource):
    def get(self, username=None):
        db = connect()
        #sql = "SELECT R.name, R.url, C.username, C.group_name FROM repository R JOIN (SELECT * FROM contributions WHERE username = %s) C ON R.url = C.repository" 
        sql = "SELECT E.id, E.content, E.date, E.url, E.type, E.repo_url FROM feed_entity E JOIN (SELECT * FROM contributions WHERE username = %s) C ON E.repo_url = C.repository"
        try:
            with db.cursor() as cursor:
                cursor.execute(sql, username)
                result = cursor.fetchall()
                feed_entities = []
                for entity in result:
                    t_entity = {}
                    t_entity['id'] = entity[0]
                    t_entity['content'] = entity[1]
                    t_entity['date'] = entity[2]
                    t_entity['html_url'] = entity[3]
                    t_entity['type'] = entity[4]
                    t_entity['repo_url'] = entity[5]
                    feed_entities.append(t_entity)
        except Exception as err:
            print(err)
            print("What a Terrible Failure: FeedEntity get")
        finally:
            db.close()


        return feed_entities

api.add_resource(FeedEntity, '/users/<username>/feed_entity')

class CalendarAssignments(Resource):
    def get(self, username=None):
        db = connect()
        sql = "SELECT * FROM calendar_assignment WHERE username=%s"
        try:
            with db.cursor() as cursor:
                cursor.execute(sql, username)
                result = cursor.fetchall()
                calendar_assignments = []
                for assignment in result:
                    t_ca = {}
                    t_ca['id'] = assignment[0]
                    t_ca['description'] = assignment[1]
                    t_ca['title'] = assignment[2]
                    t_ca['username'] = assignment[3]
                    t_ca['date'] = str(assignment[4])
                    calendar_assignments.append(t_ca)
        except:
            print("Wtf CalendarAssignments get")

        return calendar_assignments

    def post(self, username=None, description=None, title=None, date=None):
        db = connect()
        args = request.args

        try:
            username = args['username']
            description = args['description']
            title = args['title']
            date = args['date']
        except:
            print("What a Terrible Failure: CA Post")
        try: 
            with db.cursor() as cursor:
                sql = "INSERT INTO calendar_assignment (description, title, username, date) VALUES(%s, %s, %s, %s)"
                cursor.execute(sql, (description, title, username, date))
                db.commit()
        finally:
            db.close()

    def delete(self, username=None, id=None):
        db = connect()
        args = request.args

        try:
            username = args['username']
            _id = args['id']
        except:
            print("Wtf: CA delete")
        try:
            with db.cursor() as cursor:
                sql = "DELETE FROM calendar_assignment WHERE id = %s"
                cursor.execute(sql, _id)
                db.commit()
        finally:
            db.close()

    def put(self, username=None, id=None, description=None, title=None, date=None):
        db = connect()
        args = request.args

        try:
            username = args['username']
            description = args['description']
            title = args['title']
            date = args['date']
            _id = args['id']
        except:
            print("What a Terrible Failure: CA Post")

        try:
            with db.cursor() as cursor:
                sql = "UPDATE calendar_assignment SET description=%s, title=%s, date=%s"
                cursor.execute(sql, (description, title, date))
                db.commit()
        finally:
            db.close()

api.add_resource(CalendarAssignments, '/users/<username>/calendar_assignments')

class follower(Resource):
    def get(self, username=None):
        db = connect()

        try:
            with db.cursor() as cursor:
                sql = "SELECT follower FROM following WHERE username=%s"
                cursor.execute(sql, username)
                result = cursor.fetchall()
                followers = []
                for follower in result:
                    followers.append(follower[0])

        finally:
            db.close()
        

        return followers      
        
api.add_resource(follower, '/users/<username>/follower')

class following(Resource):
    def get(self, username=None):
        db = connect()
        try:
            with db.cursor() as cursor:
                sql = "SELECT username FROM following WHERE follower=%s"
                cursor.execute(sql, username)
                result = cursor.fetchall()
                followings = []
                for following in result:
                    followings.append(following[0])
        finally:
            db.close()

        return followings

api.add_resource(following, '/users/<username>/following')


class Update(Resource):
    def post(self, username=None, password=None):
        args = request.args

        try: 
            username = args['username']
            password = args['password']
        except KeyError:
            # TODO Tell them something bad happened
            print("Wtf Error: UPDATE POST")

        write_to_all_info(username=username, password=password)

api.add_resource(Update, '/update')

# TODO FOLLOWER AND FOLLOWING  (LIST OF USERNAME)



if __name__ == '__main__':
    app.run(debug=True)