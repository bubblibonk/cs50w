from django.shortcuts import render
import praw

reddit = praw.Reddit(
        client_id="_gQ8_dtZvjsTfhLRFS_6Mg",
        client_secret="2K82int92L6912UFfutbF6XmdIM_cg",
        username = "MeowForMeBish",
        password = "bonkbonk123",
        user_agent = "meow"
        )

subReddit = reddit.subreddit('mumbai')
hot_posts =reddit.subreddit("mumbai").hot(limit=10)
def index(request):
    return render(request,"reddit/index.html",{
        "hot_posts":hot_posts
        })

# Create your views here.
