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
linux = ['debian', 'linus', 'linux', 'redhat', 'torvalds', 'ubuntu']
programming = ['guido van rossum', 'pycon', 'python', '.py', 'bash', 'c++', 'code', 'coding', 'emacs lisp', 'git', 'golang', 'graphql', 'javascript', 'jquery', 'json', 'jupyter notebook', 'laravel', 'malware', 'npm', 'operating system', 'open source', 'php', 'programming', 'rss', 'software', 'sql', 'windows', 'yaml', '.js']
politics = ['ballot', 'biden', 'democrat', 'gop', 'government', 'melania', 'pelosi', 'politics', 'president', 'republican', 'sanders', 'senate', 'senator', 'trump']
internet = ['artificial intelligence', 'facebook', 'google', 'instagram', 'internet', 'reddit', 'snapchat', 'twitter']
gaming = ['call of duty', 'gaming', 'minecraft', 'nintendo', 'playstation', 'ps3', 'ps4', 'video game', 'wii', 'xbox']
censorship = ['censor']
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

def get_guild(title):
    for word in linux:
        if word in title: return 'linux'
    for word in programming:
        if word in title: return 'programming'
    for word in politics:
        if word in title: return 'politics'
    for word in internet:
        if word in title: return 'internet'
    for word in gaming:
        if word in title: return 'gaming'
    for word in censorship:
        if word in title: return 'censorship'
    return 'internet'

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
        feed = random.choice(feeds)
        rssguild = random.choice(rssguilds)
        #steal shit from reddit
        ourint = random.randint(0,99)
        if ourint % 2 == 0:
            gl = random.choice(guild_list)
            post = reddit2ruqqus(sub_guild=gl)
            print('SUBMITTED TO +{} | ({})'.format(gl,'REDDIT'))
        #get links from hn to whore that tasty rep
        hn_feed = 'https://hnrss.org/newest'
        for entry in feedparser.parse(hn_feed).entries:
            hntext = '{} {}'.format(entry.link,entry.title)
            with open('hnstuff','a') as hn:
                hn.write(hntext + "\n")
        else:
            with open('hnstuff') as hn:
                hnlines = [l.rstrip() for l in hn]
                randhn = random.choice(hnlines)
                hnlink = randhn.split()[0]
                hntitle = randhn.replace(hnlink,'')
                gg = get_guild(title=hntitle)
                hnp = {'board': gg,
                       'title': hntitle,
                       'url': hnlink}
                ruqqus.post('/api/v1/submit', data=hnp)
                print('SUBMITTED TO +{} | ({})'.format(gg,'RSS FEEDS'))
            open('hnstuff','r+').truncate(0)
        time.sleep(60)
    except Exception:
        print(traceback.format_exc())
        time.sleep(60)
    except KeyboardInterrupt:
        print('shutting down :(')
        quit()
