from ddgs import DDGS


def search_competitors(query):

    results = []

    with DDGS() as ddgs:

        search_results = ddgs.text(
            query,
            max_results=5
        )

        for r in search_results:

            results.append(
                r.get("title")
            )

    return results