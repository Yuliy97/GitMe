import pymysql as mysql
from GitHubInfoGrabber import *

# DB connection information
cnx = {
  'host': "gitme.cnolzaujohll.us-east-2.rds.amazonaws.com",
  'username': "Kirtan",
  'password': "password",
  'db': "GitMe"
}

global feed_id
global cal_id

connection = mysql.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])
try:
    with connection.cursor() as cursor:
        feed_id = cursor.execute("SELECT MAX(id) FROM feed_entity")
        if not cursor.rowcount:
            feed_id = 0
    connection.commit()
finally:
    connection.close()

connection = mysql.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])
try:
    with connection.cursor() as cursor:
        cal_id = cursor.execute("SELECT MAX(id) FROM calendar_assignment")
        if not cursor.rowcount:
            cal_id = 0
    connection.commit()
finally:
    connection.close()


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
def write_to_contributions(user_info=None, group_name=None, username=None, password=None):
    connection = mysql.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])
    count = 0
    if user_info is None:
        user_info = get_relevant_user_info(username, password)
    user_name = user_info['login']
    try:
        with connection.cursor() as cursor:
            for repo in user_info['repo_url']:
                repo_name = get_relevant_repo_info(repo)
                if group_name is None:
                    group_name = 'Group ' + str(count)
                    count += 1
                cursor.execute("INSERT INTO contributions VALUES(%s, %s, %s)",
                               (user_name, repo_name['title'], group_name))
        print("Successfully added", username, "to CONTRIBUTIONS")
        connection.commit()
    finally:
        connection.close()


# add entry to feed_entity table given username and password
def write_to_feed_entity(user_info=None, username=None, password=None):
    global feed_id
    connection = mysql.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])

    if user_info is None:
        user_info = get_relevant_user_info(username, password)

    url = get_user_url(username, password)
    repo_url = user_info['repos_url']

    try:
        with connection.cursor() as cursor:
            for repo in repo_url:
                repo_info = get_relevant_repo_info(repo)
                repo_html_url = repo_info['html_url']
                content = repo_info['comments']
                pulls = repo_info['pull_requests']
                issues = repo_info['issues']

                c_list = []
                c_date = []
                p_list = []
                p_date = []
                i_list = []
                i_date = []

                for c in content:
                    c_list.append(c['body'])
                    c_date.append(c['date'])
                for p in pulls:
                    p_list.append(p['title'])
                    p_date.append(p['date'])
                for i in issues:
                    i_list.append(i['title'])
                    i_date.append(i['date'])

                for c, d in zip(c_list,c_date):
                    feed_id += 1
                    cursor.execute("INSERT INTO feed_entity VALUES(%s, %s, %s, %s, %s, %s)",
                                   (id, c, d, repo_html_url,'commit', repo))
                for p, d in zip(p_list, p_date):
                    feed_id += 1
                    cursor.execute("INSERT INTO feed_entity VALUES(%s, %s, %s, %s, %s, %s)",
                                   (id, p, d, repo_html_url, 'pull', repo))
                for i, d in zip(i_list, i_date):
                    feed_id += 1
                    cursor.execute("INSERT INTO feed_entity VALUES(%s, %s, %s, %s, %s, %s)",
                                   (id, i, d, repo_html_url, 'issue', repo))

                print("Successfully added", repo_info['name'], "to FEED_ENTITY")
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
            sql = "INSERT INTO repository VALUES(%s, %s)"
            for name, url in repos.items():
                cursor.execute(sql, (name, url))
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

# add entry to repository table given username and password
def write_to_all_info(user_info=None, username=None, password=None):
    connection = mysql.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'], charset='utf8')

    if user_info is None:
        user_info = get_relevant_user_info(username, password)

    # user table info
    user_name = user_info["login"]
    total_commits = user_info["total_commits"]
    avatar_url = user_info['avatar_url']
    user_url = user_info["html_url"]
    followers = user_info['follower_info']
    following = user_info['follwing_info']

    # repository table info and contributions
    repos = user_info['repos_html']

    # Get repository information 
    # repo_url = "https://api.github.com/users/%s/%s"
    repo_list = []
    for name, url in repos.items():
        owner = parse_owner(url)
        repo_url = "https://api.github.com/repos/{}/{}".format(owner, name)
        repo_list.append(get_relevant_repo_info(repo_url))
    # feed_entity table info

    try:
        with connection.cursor() as cursor:
            # write to user_table
            sql_user = "INSERT INTO user VALUES(%s, %s, %s, %s)"
            try:
                cursor.execute(sql_user, (user_name, total_commits, avatar_url, user_url))
            except:
                pass
            # write to repository_table
            sql_repository = "INSERT INTO repository VALUES(%s, %s)"
            for name, url in repos.items():
                try:
                    cursor.execute(sql_repository, (name, url))
                except:
                    pass
            # write to contributions
            sql_contributions = "INSERT INTO contributions VALUES(%s, %s, %s)" 
            for name, url in repos.items():
                try:
                    cursor.execute(sql_contributions, (user_name, url, "default"))
                except:
                    pass
            # write to follower
            sql_follower = "INSERT INTO following VALUES(%s, %s)"
            for name, url in followers.items():
                try:
                    cursor.execute(sql_follower, (user_name, name))
                except:
                    pass
            # write to follower for following
            for name, url in following.items():
                try:
                    cursor.execute(sql_follower, (name, user_name))
                except:
                    pass
            # write to feed_entity
            sql_feed_entity = "INSERT INTO feed_entity (content, date, url, type, repo_url) VALUES(%s, %s, %s, %s, %s)"
            # content, date, url, type, repo_url
            for repo_info in repo_list:
                for comment in repo_info['comments']:
                    try:
                        cursor.execute(sql_feed_entity, (comment['body'], comment['date'], comment['html_url'], 'comment', repo_info['html_url']))
                    except:
                        pass
                for pull_request in repo_info['pull_requests']:
                    try:
                        cursor.execute(sql_feed_entity, (pull_request['title'], pull_request['date'], pull_request['html_url'], 'pull_request', repo_info['html_url']))
                    except:
                        pass
                for issue in repo_info['issues']:
                    try:
                        cursor.execute(sql_feed_entity, (issue['title'], issue['date'], issue['html_url'], "issue", repo_info['html_url']))
                    except:
                        pass
            connection.commit()
    finally:
        connection.close()


# get user info and populate all tables
def write_user_info(username, password):
    user_info = get_relevant_user_info(username, password)
    # write_to_calendar_assignment(user_info)
    # write_to_contributions(user_info)
    write_to_feed_entity(user_info)
    write_to_following(user_info)
    write_to_repository(user_info)
    write_to_user(user_info)

def parse_owner(url):
    elements = url.split("/")
    return elements[3]


























