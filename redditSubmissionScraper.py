
"""
scrapes pictures of reddit and does various things to them
created for use in my reddit pic scraper for dog pictures

"""
from typing import List
import logging
import praw
class redditSubmissionScraper():
    sortList = ['controversial','gilded','hot','new','rising','top']
    def __init__(self,client_id,client_secret,user_agent):
        ##starting variables
        self.c_id = client_id
        self.c_secret = client_secret
        self.user_ag = user_agent
        self.subreddits = []
        
        ##sets up log
        #logging.basicConfig(filename='redPicScraper.log',level=logging.debug)
       
        ##sets up read only instance of reddit ## to do other things the params are different
        self.reddit_inst = praw.Reddit(client_id = self.c_id, client_secret =self.c_secret, user_agent = self.user_ag )
        
        ##tests read only connection
        if self.reddit_inst.read_only == False:
            #logging.warning("Problem creating reddit instance")
            print("problem creating reddit instance")

    ##need to add error checking if sub is not valid
    def addSubreddit(self, subredditName: str):
        subreddit = self.reddit_inst.subreddit(subredditName)
        self.subreddits.append(subreddit)

    def test_connect (self):
        if self.reddit_inst.read_only == False:
            #logging.debug("Not connected ot reddit")
            print("Not connected to reddit")

    def scrapeSubmissions(self,sortMethod: str, numPosts: int) -> List[object]:
        ##returns list of submissions
        ##sortMethod can be either 'controversial','gilded','hot','new','rising','top'
        self.sorter=sortMethod
        self.retList=[]
        if sortMethod not in self.sortList:
            return self.retList
        if numPosts<=0:
           # logging.warning("numPics less than or equal to 0")
            return self.retList
        ##checks if subreddits is empty
        if numPosts>20:
            #logging.warning("numPics larger than 20")
            self.scrapeSubmissions(self.sorter,20)
        if not self.subreddits: ##ie subreddits is empty
            #logging.info("scrapePicsURL subreddits empty")
            return self.retList
        
        for subreddit in self.subreddits:
            #logging.info("scraping subreddit: "+subreddit.display_name+"...")
            for submission in subreddit.top(limit = numPosts):
                self.retList.append(submission)
        return self.retList



