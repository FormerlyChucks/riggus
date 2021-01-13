import time, praw, yaml, random, hackernews, traceback, difflib

with open("config.yaml") as config_file:
    config = yaml.safe_load(config_file)
    client_id = config["client_id"]
    client_secret = config["client_secret"]
    username = config["username"]
    password = config["password"]
    user_agent = config["user_agent"]
    usernames = config["usernames"]
    subs = config["sub_list"]
    python = config["python"]
    linux = config["linux"]
    programming = config["programming"]
    politics = config["politics"]
    internet = config["internet"]
    gaming = config["gaming"]

def get_sub():
    for word in python:
        if word in title:
            return 'python'
            break
    for word in linux:
        if word in title:
            return 'linux'
            break
    for word in programming:
        if word in title:
            return 'programming'
            break
    for word in politics:
        if word in title:
            return 'politics'
            break
    for word in internet:
        if word in title:
            return 'internet'
            break
    for word in gaming:
        if word in title:
            return 'gaming'
            break

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     password=password,
                     username=username)

reddit.validate_on_submit = True
x = random.randint(0,1)

while True:
    try:
        for submission in reddit.subreddit(subs).stream.submissions(skip_existing=True):
            for results in reddit.subreddit(subs).search(submission.title):
                similarity = difflib.SequenceMatcher(None, submission.title,results.title).ratio()
                if results.num_comments >= 2 and similarity >= .8:
                    comment = results.comments[x]
                    if comment.author not in usernames and comment.body != '[deleted]':
                        submission.reply(comment.body)
                        break

        new_stories = hackernews.HackerNews().new_stories(limit=1)
        item_id = str(new_stories).replace('[<hackernews.Item: ','').split(" -",1)[0]
        item = hackernews.HackerNews().get_item(item_id)
        title = item.title.lower()
        url = item.url
        print(title,url)
        with open('db.txt') as db:
            if url not in db.read():
                continue
            if get_sub() is not None:
                reddit.submit(get_sub(), title, url)
                else:
                    print('no sub found')
                with open('db.txt', 'a') as f:
                    f.write(url + '\n')
            else:
                print('url is in database')
        time.sleep(60)
    except Exception:
        print(traceback.format_exc())
        time.sleep(60)
    except KeyboardInterrupt:
        print('shutting down :(')
        quit()
