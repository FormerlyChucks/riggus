import requests

hn_url = 'https://hacker-news.firebaseio.com/v0/{}.json'

class randstory():
    def __init__(self):
        stories = hn_url.format("newstories")
        get_stories = requests.get(hnurl).json()
        if r is not None:
            story = random.choice(r)
            story_data = hn_url.format('item/{}'.format(sid))
            get_story = requests.get(story_data).json
            title = get_story['title']
            url = get_story['url']
            text = '{} {}'.format(url,title)
            return text
        else:
            return 'error'

def get_guild(title):
    for word in linux:
        if word in title:
            return 'linux'
    for word in programming:
        if word in title:
            return 'programming'
    for word in politics:
        if word in title:
            return 'politics'
    for word in internet:
        if word in title:
            return 'internet'
    for word in gaming:
        if word in title:
            return 'gaming'
    for word in censorship:
        if word in title:
            return 'censorship'
    return 'internet'

def get_reddit(sub):
    subreddit = reddit.subreddit(sub)
    submissions = list(subreddit.top('all', limit=None))
    submission = random.choice(submissions)
    title = submission.title
    url = submission.url
    text = '{} {}'.format(url,title)
    return text

def r2r(subreddit,guild):
    post_data = get_reddit(sub=subreddit)
    post = post_data.split()
    post_url = post[0]
    post_title = post_data.replace(post_url,'')
    ruqqus.submit_post(guild=guild, url=post_url, title=post_title)
    return 'success'

def figure(glist):
    guild = random.choice(guild_list)
    if guild == 'dankmemes': r2r(subreddit='dankmemes',guild='dankmemes')
    elif guild == 'memes': r2r(subreddit='memes',guild='memes')
    elif guild == '4chan': r2r(subreddit='4chan',guild='4chan')
    elif guild == 'tia': r2r(subreddit='tumblrinaction', guild='tumblrinaction')
    elif guild == 'okbr': r2r(subreddit='okbuddyretard', guild='okbuddyretard')
    elif guild == 'avgr': r2r(subreddit='averageredditor', guild='averageredditor')
    else: return 'fuck'
    return guild
