##pupper pic scraper
import praw
from redditSubmissionScraper import redditSubmissionScraper
class pupperScraper():
    def __init__(self):
        ##creates pic scraper
        self.subScraper = redditSubmissionScraper("client_id","secret_id","script for redditPicScraper bot by /u/pupperoniBot")
        ## adding chosen subreddits
        self.subScraper.addSubreddit("rarepuppers")
        self.subScraper.addSubreddit("dogswithjobs")
        self.subScraper.addSubreddit("Corgi")
        self.subScraper.addSubreddit("whatswrongwithyourdog")
        ##takes top 3 submissions
        self.submissionList = self.subScraper.scrapeSubmissions('top',3)

        self.pupperList=[]
        for submission in self.submissionList:
            ##only adds images
            if ".jpg" or ".png" in submission.title:
                ##puts them into tuple with subreddit display_name submission title and submission url for easy access
                pupperTuple = (submission.subreddit.display_name,submission.title,submission.url)
                self.pupperList.append(pupperTuple)

    def retPupperList(self):
        return self.pupperList
    