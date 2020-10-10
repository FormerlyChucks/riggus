import praw, time, config, random, difflib, requests

reddit = praw.Reddit(client_id=config.cid, client_secret=config.cs, user_agent=config.ua, password=config.p, username=config.u)
subreddit = reddit.subreddit(config.sub)
reddit.validate_on_submit = True
x = random.randint(0,2)

while True:
    try:
        for submission in subreddit.stream.submissions(skip_existing=True):
            for results in subreddit.search(submission.title):
                similarity = difflib.SequenceMatcher(None, submission.title,results.title).ratio()
                if results.num_comments >= 3 and similarity >= .8:
                    comment = results.comments[x]
                    if comment.author not in config.usernames and comment.body != '[deleted]':
                        submission.reply(comment.body)
                        break
                        
        link = 'https://hacker-news.firebaseio.com/v0/newstories.json'
        stories = json.loads(requests.get(link).text)
        s = str(stories[0])
        story = json.loads(requests.get('https://hacker-news.firebaseio.com/v0/item/' + s + '.json').text)
        title = story['title']
        url = story['url']
        normalized_title = title.lower()
        if 'hn' not in normalized_title:
            for word in config.programming:
                with open("database.txt", "r") as db:
                    if word in normalized_title and url not in db.read():
                        submit = reddit.subreddit("programming").submit(title, url=url)
                        with open("database.txt", "a") as f:
                            f.write(url + "\n")
                            time.sleep(600)
            for word in config.internet:
                with open("database.txt", "r") as db:
                    if word in normalized_title and url not in db.read():
                        submit = reddit.subreddit("internetisbeautiful").submit(title, url=url)
                        with open("database.txt", "a") as f:
                            f.write(url + "\n")
                            time.sleep(600)
                            
            for word in config.politics:
                with open("database.txt", "r") as db:
                    if word in normalized_title and url not in db.read():
                        submit = reddit.subreddit("politics").submit(title, url=url)
                        with open("database.txt", "a") as f:
                            f.write(url + "\n")
                            time.sleep(600)
            for word in config.gaming:
                with open("database.txt", "r") as db:
                    if word in normalized_title and url not in db.read():
                        submit = reddit.subreddit("gaming").submit(title, url=url)
                        with open("database.txt", "a") as f:
                            f.write(url + "\n")
                            time.sleep(600)
                            
            for word in config.science:
                with open("database.txt", "r") as db:
                    if word in normalized_title and url not in db.read():
                        submit = reddit.subreddit("science").submit(title, url=url)
                        with open("database.txt", "a") as f:
                            f.write(url + "\n")
                            time.sleep(600)
                                                
    except Exception:
        with open("errors.txt", "a") as f:
            f.write(str(traceback.format_exc()) + "\n")
            time.sleep(60)
