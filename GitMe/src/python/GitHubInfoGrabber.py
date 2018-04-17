import json
import requests
import datetime

root = 'https://api.github.com/'


####################################################################
# Util funcs
####################################################################

# Sends a request at URL for
def get_request(url, username="def", password='def'):
    if username == 'def' or password == 'def':
        r = requests.get(url)
    else:
        r = requests.get(url, auth=(username, password))
    return r

####################################################################
# For getting specfic information about a user
####################################################################

# Gets all the User infromation I currently believe is necessary for the project
# Returns it as a dictionary
def get_relevant_user_info(username, password='def'):
    url = root + 'users/' + username
    r = get_request(url, username, password)
    user = json.loads(r.content)
    user_info = {}
    user_info['login'] = user['login']
    user_info['html_url'] = user['html_url']
    user_info['follower_info'] = get_user_followers_url(username, password)
    user_info['total_commits'] = count_user_commits(username, password)
    user_info['repos_html'] = get_user_repos_urls(username, password)

    # TODO Get the feed_entities

    return user_info

# TODO: Get the feed_entities

# Returns a list of a users repositories as dictionary[name] = html_url
def get_user_repos_urls(username, password='def'):
    url = root + 'users/' + username + '/repos'
    r = get_request(url, username, password)
    repos = json.loads(r.content)
    repo_urls = {}
    for repo in repos:
        repo_urls[repo['name']] = (repo['html_url'])
    return repo_urls

# Returns the HTML url of a user (aka their personal page)
def get_user_url(username, password='def'):
    url = root +'users/' + username
    r = get_request(url, username, password)
    user = json.loads(r.content)
    return user['html_url']

# Returns the avatar url of a user
def get_user_avatar(username, password='def'):
    url = root + 'users/' + username
    r = get_request(url, username, password)
    user = json.loads(r.content)
    return user['avatar_url']

# Returns the number of commits a user has made in total
def count_user_commits(username, password='def'):
    total = 0
    for repo in __get_user_repos(username, password):
        n = count_repo_commits(repo['url'] + '/commits')
        total += n
    return total

# Returns the usernames of a users followers as a list
def get_user_followers_username(username, password='def'):
    follower_names = []
    for follower in __get_user_followers(username, password):
        follower_names.append(follower['login'])
    return follower_names

# Returns the urls of a users followers as a dictionary[username] =html_url
def get_user_followers_url(username, password='def'):
    follower_urls = {}
    for follower in __get_user_followers(username, password):
        follower_urls[follower['login']] = (follower['html_url'])
    return follower_urls

####################################################################
# For getting information about a repo
####################################################################

# Counts the number of commits for a certain repo (can take /user/repo or /repo)
def count_repo_commits(commits_url, _acc=0):
    r = get_request(commits_url)
    commits = json.loads(r.content)
    n = len(commits)
    if n == 0:
        return _acc
    link = r.headers.get('link')
    if link is None:
        return _acc + n
    next_url = __find_next(r.headers['link'])
    if next_url is None:
        return _acc + n
    return count_repo_commits(next_url, _acc + n)

####################################################################
# Private Methods
####################################################################

# Gets the REST API infromation for all of a user's repos one at a time
def __get_user_repos(username, password='def'):
    url = root + "users/" + username + '/repos'
    r = get_request(url, username, password)
    repos = json.loads(r.content)
    for repo in repos:
        yield repo

# Gets the REST API infromation fro all of a user's followers one at a time
def __get_user_followers(username, password='def'):
    url = root + 'users/' + username + '/followers'
    r = get_request(url, username, password)
    followers = json.loads(r.content)
    if len(followers) == 0:
        return None
    for follower in followers:
        yield follower

# given a link header from github, find the link for the next url which they use for pagination
def __find_next(link):
    for l in link.split(','):
        a, b = l.split(';')
        if b.strip() == 'rel="next"':
            return a.strip()[1:-1]


####################################################################
# Test Cases
####################################################################

def test():
    username = "jgormley6"
    password = "JG9671166soccerfan"


    print("get_relevant_user_info")
    print(json.dumps(get_relevant_user_info(username, password), indent=4))

    print("get_user_repos_urls")
    print(json.dumps(get_user_repos_urls(username, password), indent=4))

    print("get_user_url")
    print(get_user_url(username, password))

    print("get_user_avatar")
    print(get_user_avatar(username, password))

    print("count_user_commits")
    print(count_user_commits(username, password))

    print("get_user_followers_username")
    print(get_user_followers_username(username, password))

    print("get_user_followers_url")
    print(json.dumps(get_user_followers_url(username, password), indent=4))

# Uncomment to test
# test()
