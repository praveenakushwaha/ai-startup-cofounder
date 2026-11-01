import praw


def get_reddit_posts():

    reddit = praw.Reddit(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        user_agent="startup_agent"
    )

    posts = []

    for post in reddit.subreddit(
        "startups"
    ).hot(limit=5):

        posts.append(
            post.title
        )

    return posts