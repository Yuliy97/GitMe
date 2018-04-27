import json
import requests
import datetime

root = 'https://api.github.com/'

auth_boolean = False
auth = []

####################################################################
# Util funcs
####################################################################

# Sends a request at URL for
def get_request(url, username="def", password='def'):
    global auth_boolean
    global auth
    if auth_boolean:
        r = requests.get(url, auth=(auth[0], auth[1]))
    elif username == 'def' or password == 'def':
        r = requests.get(url)
    else:
        auth_boolean = True
        r = requests.get(url, auth=(username, password))
        auth.append(username)
        auth.append(password)
    return r

def authorize(username="def", password="def"):
    url = "https://api.github.com"

    r = requests.get(url, auth=(username, password))
    message = json.loads(r.content)
    
    try:
        mes = message['message']
        if mes == "Bad credentials":
            return "Bad credentials"
    except KeyError:
        return "Authorized"

####################################################################
# For getting specific information about a user
####################################################################

# Gets all the User information I currently believe is necessary for the project
# Returns it as a dictionary
def get_relevant_user_info(username, password='def'):
    url = root + 'users/' + username
    r = get_request(url, username, password)
    user = json.loads(r.content)

    user_info = {}
    user_info['login'] = user['login']
    user_info['html_url'] = user['html_url']
    user_info['follower_info'] = get_user_followers_url(username, password)
    user_info['follwing_info'] = get_user_following_url(username, password)
    user_info['total_commits'] = int(count_user_commits(username, password))
    user_info['repos_html'] = get_user_repos_html_urls(username, password)
    user_info['repos_url'] = get_user_repos_urls(username, password)
    user_info['avatar_url'] = get_user_avatar(username, password)
    # user_info['comments'] = get_comments_for_user_repos(username, password)
    # TODO Get the feed_entities

    return user_info


# Returns a dictionary of a user's repositories as dictionary[name] = html_url
def get_user_repos_html_urls(username, password='def'):
    repo_urls = {}
    for repo in __get_user_repos(username, password):
        repo_urls[repo['name']] = (repo['html_url'])
    return repo_urls

    #url = root + 'users/' + username + '/repos'
    #r = get_request(url, username, password)
    #repos = json.loads(r.content)
    #repo_urls = {}
    #for repo in repos:
    #    repo_urls[repo['name']] = (repo['html_url'])
    #return repo_urls

# Returns a list of user's api urls
def get_user_repos_urls(username, password='def'):
    repo_urls = []
    for repo in __get_user_repos(username, password):
        repo_urls.append(repo['url'])
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

def get_user_following_url(username, password='def'):
    following_urls = {}
    for following in __get_user_following(username, password):
        following_urls[following['login']] = following['html_url']
    return following_urls

# Returns all the comments in the repos for a user
def get_comments_for_user_repos(username, password='def'):
    comments = []
    for repo in __get_user_repos(username, password):
        comments = comments + (get_repo_commit_comments(repo['comments_url'].replace("{/number}","")))
    return comments


####################################################################
# For getting information about a repo
####################################################################

def get_relevant_repo_info(repo_url):
    r = get_request(repo_url)
    repo = json.loads(r.content)
    repo_info = {}
    repo_info['html_url'] = repo['html_url']
    repo_info['name'] = repo['name']
    repo_info['comments'] = get_repo_commit_comments(repo_url + '/comments')
    repo_info['pull_requests'] = get_pull_requests(repo_url + '/pulls')
    repo_info['issues'] = get_repo_issues(repo_url + '/issues')

    return repo_info

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

def get_pull_requests(pulls_url, pull_list=None):
    if pull_list is None:
        pull_list = []
    r = get_request(pulls_url)
    pulls = json.loads(r.content)
    for pull in pulls:
        pull_list.append(__get_pull_info(pull))

    link = r.headers.get('link')
    if link is None:
        return pull_list

    next_url = __find_next(r.headers['link'])
    if next_url is None:
        return pull_list

    return get_pull_requests(next_url, pull_list)


# Gets all the comments for a repo and returns a list of dictionaries
def get_repo_commit_comments(comments_url, comment_list=None):
    if comment_list is None:
        comment_list = []
    r = get_request(comments_url)
    comments = json.loads(r.content)
    for comment in comments:
        comment_list.append(__get_comment_info(comment))

    link = r.headers.get('link')
    if link is None:
        return comment_list

    next_url = __find_next(r.headers['link'])
    if next_url is None:
        return comment_list

    return get_repo_commit_comments(next_url, comment_list)

def get_repo_issues(issues_url, issues_list=None):
    if issues_list is None:
        issues_list = []
    r = get_request(issues_url)
    issues = json.loads(r.content)
    for issue in issues:
        issues_list.append(__get_issue_info(issue))

    link = r.headers.get('link')
    if link is None:
        return issues_list

    next_url = __find_next(r.headers['link'])
    if next_url is None:
        return issues_list

    return get_repo_issues(next_url, issues_list)

####################################################################
# Private Methods
####################################################################

# Gets the REST API information for all of a user's repos one at a time
# Includes starred repos
def __get_user_repos(username, password='def'):
    url = root + "users/" + username + '/repos'
    r = get_request(url, username, password)
    repos = json.loads(r.content)
    for repo in repos:
        yield repo
    # Includes starred repos
    url = root + "users/" + username + '/starred'
    r2= get_request(url, username, password)
    star_repos = json.loads(r2.content)
    for star_repo in star_repos:
        yield star_repo

def __get_comment_info(comment):
    t_comment = {}
    t_comment['id'] = comment['id']
    t_comment['body'] = comment['body']
    t_comment['html_url'] = comment['html_url']
    t_comment['user'] = comment['user']['login']
    t_comment['user_html_url'] = comment['user']['html_url']
    t_comment['date'] = comment['created_at']

    return t_comment

    #who asked for pull: user[login]
    #title of pull request: title
    #date: created_at
def __get_pull_info(pull):
    t_pull = {}
    try:
        t_pull['user'] = pull['assignee']['login']
    except:
        t_pull['user'] = 'jgormley6'
    t_pull['title'] = pull['title']
    t_pull['date'] = pull['created_at']
    t_pull['html_url'] = pull['html_url']
    return t_pull

def __get_issue_info(issue):
    t_issue = {}
    t_issue['title'] = issue['title']
    t_issue['state'] = issue['state']
    t_issue['date'] = issue['created_at']
    t_issue['html_url'] = issue['html_url']

    return t_issue

# Gets the REST API infromation fro all of a user's followers one at a time
def __get_user_followers(username, password='def'):
    url = root + 'users/' + username + '/followers'
    r = get_request(url, username, password)
    followers = json.loads(r.content)
    if len(followers) == 0:
        return None
    for follower in followers:
        yield follower
        
def __get_user_following(username, password='def'):
    print(username)
    url = root + 'users/' + username + '/following'
    r = get_request(url, username, password)
    followings = json.loads(r.content)
    if len(followings) == 0:
       return None
    for follower in followings:
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
    user_info = get_relevant_user_info(username, password)
    print(json.dumps(user_info,indent=4))
    print(get_user_avatar(username, password))

    # for repo in user_info['repos_url']:
    #     repo_info = get_relevant_repo_info(repo)
    #     print(json.dumps(repo_info, indent=4))

def single_tests():

    username = "jgormley6"
    password = "JG9671166soccerfan"

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

    print("get_comments_for_user_repos")
    print(json.dumps(get_comments_for_user_repos(username, password), indent=4))
# Uncomment to test
# test()
