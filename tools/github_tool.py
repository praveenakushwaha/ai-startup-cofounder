import requests


def search_github_projects(query):

    url = f"https://api.github.com/search/repositories?q={query}"

    response = requests.get(url)

    data = response.json()

    results = []

    for repo in data.get("items", [])[:5]:

        results.append(
            repo["full_name"]
        )

    return results