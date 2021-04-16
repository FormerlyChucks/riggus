import traceback, time, feedparser, random, praw, requests, raw

#vars
ruqqus_access_token = ''
ruqqus_id = ''
ruqqus_secret = ''
ruqqus_refresh_token = ''
reddit_id = ''
reddit_secret = ''
reddit_agent = ''

#lists
rssguilds = ['politics', 'news', 'conservative']
feeds = ['https://www.thegatewaypundit.com/feed/', 'https://bigleaguepolitics.com/feed/', 'https://www.dailywire.com/feeds/rss.xml']
guild_list = ['dankmemes', 'memes', '4chan', 'tumblrinaction', 'okbuddyretard', 'averageredditor']

#ruqqus instance
ruqqus = raw.Ruqqus(client_id=ruqqus_id,
                    client_secret=ruqqus_secret,
                    user_agent=reddit_agent,
                    access_token=ruqqus_access_token,
                    refresh_token=ruqqus_refresh_token,
                    token_file='/tmp/token')

#reddit instance
reddit = praw.Reddit(client_id=reddit_id,
                     client_secret=reddit_secret,
                     user_agent=reddit_agent)

def reddit2ruqqus(sub_guild):
    subreddit = reddit.subreddit(sub_guild)
    submissions = list(subreddit.top('all', limit=None))
    submission = random.choice(submissions)
    title = submission.title
    url = submission.url
    p = {'board': sub_guild,'title': title,'url': url}
    post = ruqqus.post('/api/v1/submit',data=p)
    return 'success'

while True:
    try:
        #parse rss and submit to rightoid guilds
        feed = random.choice(feeds)
        rssguild = random.choice(rssguilds)
        for entry in feedparser.parse(feed).entries:
            text = '{} {}'.format(entry.link,entry.title)
            with open('articles','a') as f:
                f.write(text + "\n")
        else:
            with open('articles.txt') as f:
                lines = [l.rstrip() for l in f]
                randent = random.choice(lines)
                rsslink = randent.split()[0]
                rsstitle = randent.replace(rsslink,'')
                rssparams = {'board': rssguild,
                             'title': rsstitle,
                             'url': rsslink}
                submit = ruqqus.post('/api/v1/submit', data=rssparams)
                print('SUBMITTED TO +{} | ({})'.format(rssguild,'RSS FEEDS'))
            open('articles', 'r+').truncate(0)
        #steal shit from reddit
        ourint = random.randint(0,99)
        if ourint % 2 == 0:
            gl = random.choice(guild_list)
            post = reddit2ruqqus(sub_guild=gl)
            print('SUBMITTED TO +{} | ({})'.format(gl,'REDDIT'))
        time.sleep(60)
    except Exception:
        print(traceback.format_exc())
        time.sleep(60)
    except KeyboardInterrupt:
        print('shutting down :(')
        quit()
