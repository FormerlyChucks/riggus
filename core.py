import requests, random, yaml, praw, ruqqus

with open("config.yaml") as config_file:
    config = yaml.safe_load(config_file)
    linux = config["linux"]
    programming = config["programming"]
    politics = config["politics"]
    internet = config["internet"]
    gaming = config["gaming"]
    censorship = config["censorship"]
    r_id = config["reddit_id"]
    reddit_secret = config["reddit_secret"]
    reddit_agent = config["reddit_agent"]
    ruqqus_id = config["ruqqus_id"]
    ruqqus_secret = config["ruqqus_secret"]
    ruqqus_access_token = config["ruqqus_access_token"]
    
hn_url = 'https://hacker-news.firebaseio.com/v0/{}.json'
reddit = praw.Reddit(client_id=r_id,client_secret=reddit_secret,user_agent=reddit_agent)
ruqqus = ruqqus.RuqqusClient(client_id=ruqqus_id,client_secret=ruqqus_secret,access_token=ruqqus_access_token)

def randstory():
    stories = hn_url.format("newstories")
    get_stories = requests.get(stories).json()
    if get_stories is not None:
        story = random.choice(list(get_stories))
        story_data = hn_url.format('item/{}'.format(story))
        if story_data is not None:
            get_story = requests.get(story_data).json()
            title = get_story['title']
            url = get_story['url']
            text = '{} {}'.format(url,title)
            return text
        else:
            return 'error'
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

def reddit2ruqqus(sub_guild):
    subreddit = reddit.subreddit(sub_guild)
    submissions = list(subreddit.top('all', limit=None))
    submission = random.choice(submissions)
    title = submission.title
    url = submission.url
    ruqqus.submit_post(guild=sub_guild, url=url, title=title)
    return 'success'
