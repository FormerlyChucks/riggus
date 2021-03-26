import core, yaml, ruqqus, traceback, time, feedparser, random, praw

with open("config.yaml") as config_file:
    config = yaml.safe_load(config_file)
    ruqqus_id = config["ruqqus_id"]
    ruqqus_secret = config["ruqqus_secret"]
    ruqqus_access_token = config["ruqqus_access_token"]
    linux = config["linux"]
    programming = config["programming"]
    politics = config["politics"]
    internet = config["internet"]
    gaming = config["gaming"]
    censorship = config["censorship"]
    r_id = config["reddit_id"]
    reddit_secret = config["reddit_secret"]
    reddit_agent = config["reddit_agent"]
    guilds = config['guilds']
    feeds = config['feeds']
    guild_list = config['guild_list']
    
ruqqus = ruqqus.RuqqusClient(client_id=_id,client_secret=secret,access_token=access_token)
reddit = praw.Reddit(client_id=r_id,client_secret=reddit_secret,user_agent=reddit_agent)
  
while True:
    try:
        #parse rss and submit to rightoid guilds
        feed = random.choice(feeds)
        guild = random.choice(guilds)
        for entry in feedparser.parse(feed).entries:
            text = '{} {}'.format(entry.link,entry.title)
            with open('articles','a') as f:
                f.write(text + "\n")
        else:
            with open('articles') as f:
                lines = [l.rstrip() for l in f]
                randent = random.choice(lines)
                rsslink = randent.split()[0]
                rsstitle = randent.replace(rsslink,'')
                ruqqus.submit_post(guild=guild, url=rsslink, title=rsstitle)
        open('articles', 'r+').truncate(0)
        print('SUBMITTED TO +{} | ({})'.format(guild,'RSS FEEDS'))
        #get links from hn to whore that tasty rep
        story = core.randstory()
        if story != 'error':
            hnlink = story.split()[0]
            hntitle = story.replace(hnlink,'')
            with open('db.txt') as db:
                if hnlink not in db.read():
                    g = core.get_guild(title=hntitle)
                    ruqqus.submit_post(guild=g, url=hnlink, title=hntitle)
                    with open('db.txt', 'a') as f:
                        f.write(hnlink + '\n')
                    print('SUBMITTED TO +{} | ({})'.format(g,'HACKER NEWS'))
                else:
                    print('URL ALREADY IN DATABASE')
        #steal shit from reddit
        ourint = random.randint(0,99)
        if ourint % 2 == 0:
            fig = core.figure(glist=guild_list)
            print('submitted to +{}'.format(fig))
        time.sleep(60)
    except Exception:
        print(traceback.format_exc())
        #time.sleep(60)
    except KeyboardInterrupt:
        print('shutting down :(')
        quit()
