import os
import requests

from dotenv import load_dotenv

load_dotenv()


def get_startup_news():

    api_key = os.getenv(
        "NEWS_API_KEY"
    )

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q=startup&"
        f"pageSize=5&"
        f"sortBy=publishedAt&"
        f"apiKey={api_key}"
    )

    response = requests.get(
        url,
        timeout=10
    )

    data = response.json()

    articles = []

    for article in data.get(
        "articles",
        []
    )[:5]:

        articles.append(
            article["title"]
        )

    return articles
