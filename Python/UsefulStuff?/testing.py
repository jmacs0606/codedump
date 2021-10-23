#! /Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9
import praw
import pandas as pd


#connecting to reddit API
reddit = praw.Reddit(client_id='DA4lc6KxY-dIXA', \
                     client_secret='5TZEhmf6AdsXTHNgnjhJJGsEFmQ', \
                     user_agent='Mimifur', \
                     username='HereComesTheMoneyyy', \
                     password='EggSalami7')

#Wallstreetbets
subreddit = reddit.subreddit('wallstreetbets')

top_subreddit = subreddit.top(limit=10)


#storage dict
topics_dict = { "title":[], 
                "score":[], 
                "id":[], "url":[],  
                "comms_num": [], 
                "created": [], 
                "body":[]}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)