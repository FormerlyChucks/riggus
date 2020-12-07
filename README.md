# Humanoid

**A reddit bot, made to act like a human**

## About

Q: How does the bot make comments?

A: It searches old posts in subreddit every time a new post comes up. If the old post's title and the new post's title have a close match, take a random comment and reply to the new post

Q: How does the bot make submissions?

A: It streams the Hacker News /newest page. If the title contains words that are in the lists in config.yaml, submit to the determined subreddit

## Running the bot

- Install Python, Pip, Git

- Clone the repo, change into the bot directory:

      git clone https://github.com/Mr-Steal-Your-Script/Humanoid && cd Humanoid
    
Install the needed packages:

    pip3 install -r requirements.txt
    
Create reddit app [here](https://reddit.com/prefs/apps)

- Select script
- Fill out the rest

Open config.yaml and enter your credentials:

- 'sub_list' is the subreddit(s) you wish to look at:
- 'client_id' is your personal use script
- 'user_agent' is your user agent
- 'client_secret' is your secret
- 'username' is your username
- 'password' is your password

Save the file and run the bot:

    python3 main.py
