import pymysql as mysql
from GitHubInfoGrabber import *

# DB connection information
cnx = {
  'host': "gitme.cnolzaujohll.us-east-2.rds.amazonaws.com",
  'username': "Kirtan",
  'password': "password",
  'db': "GitMe"
}


# remove row(s) from calendar_assignment table given username
def remove_from_calendar_assignment(id):
    connection = mysql.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])

    try:
        with connection.cursor() as cursor:
            title = cursor.execute("SELECT title FROM calendar_assignment WHERE id=%s", id)
            cursor.execute("DELETE FROM calendar_assignment WHERE id=%s", id)
        print("Successfully deleted", title, "from CALENDAR_ASSIGNMENT")
        connection.commit()
    finally:
        connection.close()


# remove row(s) from contributions table given username
def remove_from_contributions(username, repository):
    connection = mysql.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])

    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM contributions WHERE username=%s AND repository=%s", username, repository)
        print("Successfully deleted", repository, "from CONTRIBUTIONS")
        connection.commit()
    finally:
        connection.close()


# remove row(s) from feed_entity table given username
def remove_from_feed_entity(id):
    connection = mysql.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])

    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM feed_entity WHERE id=%s", id)
        print("Successfully deleted", id, "from FEED_ENTITY")
        connection.commit()
    finally:
        connection.close()


# remove row(s) from following table given username
def remove_from_following(username):
    connection = mysql.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])

    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM following WHERE username=%s", username)
        print("Successfully deleted", username, "from FOLLOWING")
        connection.commit()
    finally:
        connection.close()


# remove row(s) from repository table given username
def remove_from_repository(url):
    connection = mysql.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])

    try:
        with connection.cursor() as cursor:
            name = cursor.execute("SELECT name FROM repository WHERE url=%s", url)
            cursor.execute("DELETE FROM repository WHERE url=%s", url)
        print("Successfully deleted", name, "from REPOSITORY")
        connection.commit()
    finally:
        connection.close()


# remove row(s) from user table given username
def remove_from_user(username):
    connection = mysql.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])

    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM user WHERE username=%s", username)
        print("Successfully deleted", username, "from USER")
        connection.commit()
    finally:
        connection.close()


# add entry to calendar_assignment table given username and password
def write_to_calendar_assignment(user_info=None, username=None, password=None):
    connection = mysql.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])

    if user_info is None:
        user_info = get_relevant_user_info(username, password)

    user_name = user_info['login']

    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO calendar_assignment VALUES(%s, %s, %s, %s, %s)", (user_name))
        print("Successfully added", username, "to CALENDAR_ASSIGNMENT")
        connection.commit()
    finally:
        connection.close()


# add entry to contributions table given username and password
def write_to_contributions(user_info=None, username=None, password=None):
    connection = mysql.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])

    if user_info is None:
        user_info = get_relevant_user_info(username, password)

    user_name = user_info['login']

    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO contributions VALUES(%s, %s, %s)", (user_name))
        print("Successfully added", username, "to CONTRIBUTIONS")
        connection.commit()
    finally:
        connection.close()


# add entry to feed_entity table given username and password
def write_to_feed_entity(user_info=None, username=None, password=None):
    connection = mysql.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])

    if user_info is None:
        user_info = get_relevant_user_info(username, password)

    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO feed_entity VALUES(%s, %s, %s, %s, %s, %s)", ())
        print("Successfully added", username, "to FEED_ENTITY")
        connection.commit()
    finally:
        connection.close()


# add entries to following table given username and password
def write_to_following(user_info=None, username=None, password=None):
    connection = mysql.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])

    if user_info is None:
        user_info = get_relevant_user_info(username, password)

    user_name = user_info['login']
    followers = user_info['follower_info']

    try:
        with connection.cursor() as cursor:
            for follower in followers:
                cursor.execute("INSERT INTO following VALUES(%s, %s)", (user_name, follower))
                print("Successfully added", follower, "to FOLLOWING")
        connection.commit()
    finally:
        connection.close()


# add entry to repository table given username and password
def write_to_repository(user_info=None, username=None, password=None):
    connection = mysql.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])

    if user_info is None:
        user_info = get_relevant_user_info(username, password)

    user_name = user_info['login']
    repos = user_info['repos_html']
    names = [key for key in repos.keys()]
    urls = [url for url in repos.items()]

    try:
        with connection.cursor() as cursor:
            for name, url in zip(names, urls):
                cursor.execute("INSERT INTO repository VALUES(%s, %s, %s)", (name, url, user_name))
                print("Successfully added", name, "to REPOSITORY")
        connection.commit()
    finally:
        connection.close()


# add entry to user table given username and password
def write_to_user(user_info=None, username=None, password=None):
    connection = mysql.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])

    if user_info is None:
        user_info = get_relevant_user_info(username, password)

    user_name = user_info["login"]
    total_commits = user_info["total_commits"]
    avatar_url = user_info['avatar_url']
    user_url = user_info["html_url"]

    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO user VALUES(%s, %s, %s, %s)", (user_name, total_commits, avatar_url, user_url))
        print("Successfully added", username, "to USER")
        connection.commit()
    finally:
        connection.close()


# get user info and populate all tables
def write_user_info(username, password):
    user_info = get_relevant_user_info(username, password)
    # write_to_calendar_assignment(user_info)
    # write_to_contributions(user_info)
    # write_to_feed_entity(user_info)
    write_to_following(user_info)
    write_to_repository(user_info)
    write_to_user(user_info)


























