# Humanoid

**A reddit bot, made to act like a human**

## Description

The bot currently does this:

To make comments:
- Checks subreddit for new submissions
- Searches subreddit for the submission's title
- Compares the searched title and the submission's title
- Checks if the result has a certain amount of comments
- Grabs a random comment from the result
- Checks if the comment's author is in a list
- Checks if the comment has been deleted
- Replies with a random comment from the result
To make submissions:
- Checks Hacker News's "new" tab
- If url has certain words and isn't in the datase, submit to set subreddit

## Running the bot

It should be pretty easy to run the bot yourself

- Install Python
- Install pip
- Install Git
- Clone the repo:


      git clone https://github.com/Mr-Steal-Your-Script/Humanoid
    
Change into the bot's directory:

    cd Humanoid
    
Install the needed packages:

    pip3 install -r requirements.txt
    
Create reddit app [here](https://reddit.com/prefs/apps)

- Select script
- Fill out the rest

Open config.py and enter your credentials:

- 'sub' is the subreddit(s) you wish to look at:
   - ```python
     'AskReddit' #will only look at /r/AskReddit
     'AskReddit+AdviceAnimals' #will check /r/AskReddit and /r/AdviceAnimals
     ```
- cid is your personal use script
- ua is your user agent
- cs is your secret
- u is your username
- p is your password

Save the file and run the bot:

    python3 main.py
