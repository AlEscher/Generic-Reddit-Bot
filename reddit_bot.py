import praw
import pdb
import re
import os

# open reddit instance with settings specified in your praw.ini under "[GeneralInfoBot]"
reddit = praw.Reddit("GeneralInfoBot")
# this file will be created in the current working directory
log_filename = "mentions_replied_to.txt"
new_post_ids = []

# check if the file where we log posts we replied to already exists
if not os.path.isfile(log_filename):
    mentions_replied_to = []
else:
    with open(log_filename, "r") as f:
        mentions_replied_to = f.read()
        # the file contains post ids separated by a newline
        mentions_replied_to = mentions_replied_to.split("\n")
        # filter out empty elements
        mentions_replied_to = list(filter(None, mentions_replied_to))

# go through our mentions and reply
for mention in reddit.inbox.mentions():
    if mention.id not in mentions_replied_to:
        mention_author = mention.author
        
        # find comment from user with highest/lowest score
        highest_score = mention.score
        lowest_score = mention.score
        # start with None so that if the mention is the best / worst comment, it won't be appended to the reply
        best_comment = None
        worst_comment = None
        # Reddit's API limits this to 1000
        comments = mention_author.comments.new(limit=1000)
        for comment in comments:
            if comment.score > highest_score:
                best_comment = comment
                highest_score = comment.score
            elif comment.score < lowest_score:
                worst_comment = comment
                lowest_score = comment.score
        
        print(10*'-' + "Info" + 10*'-')
        print("Replying to: " + mention_author.name + "\nComment ID: " + mention.id + "\nContent: " + mention.body)
        print(24*'-')
        
        # start building our response
        reply = "Hello u/" + mention_author.name + " \n\nYou gained " + str(mention_author.link_karma) + " karma from posts and " + str(mention_author.comment_karma) + " from your comments\n"
        # if the user has a comment other than the initial mention with more than 1 upvote, this should not be None
        if best_comment is not None:
            reply = reply + " \n[Your best-scoring comment](" + best_comment.permalink + ")"
        # if the user has a comment other than the initial mention with less than 1 upvote, this should not be None
        if worst_comment is not None:
            reply = reply + " \n\n[Your worst-scoring comment](" + worst_comment.permalink + ")"
        mention.reply(reply)
        # update both our lists with the new ID
        mentions_replied_to.append(mention.id)
        new_post_ids.append(mention.id)

# update our file of post IDs we replied to
with open(log_filename, "a") as f:
    for post_id in new_post_ids:
        f.write(post_id + "\n")