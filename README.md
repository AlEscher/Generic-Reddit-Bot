# Generic-Reddit-Bot

A python bot for Reddit meant to automate tasks such as finding the highest / lowest scoring comment of a user.
Upon being summoned the bot replies to you with a short list of stats.
The bot isn't hosted on a server, so it won't be online often. This is just a test-bot I wrote for fun.

## Requirements
* I'm using Python 3.7.2
* You will need to `pip3 install praw` for an easy access to the Reddit API

### Setting the bot up for yourself
If you want to set up your own bot with this code you will need 2 things:
* [Register](https://www.reddit.com/prefs/apps/) your application (You can follow [this tutorial](https://www.pythonforengineers.com/build-a-reddit-bot-part-1/) under "Create Reddit App")
* You will need to configure your own `praw.ini` which is also explained in the tutorial

## Usage
If the bot is online, commenting `u/All_isGone` under any post will trigger the bot.
If you host the bot yourself, write `u/BOTS_USERNAME` instead.
While testing the bot, ***please*** use this [subreddit](https://www.reddit.com/r/pythonforengineers/) as it was made exactly for that and won't get the bot banned.

## Preview

![PreviewPic](https://github.com/AlEscher/Generic-Reddit-Bot/blob/master/preview.png)