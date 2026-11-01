from pytrends.request import TrendReq


def get_trends(keyword):

    pytrends = TrendReq(
        hl="en-US",
        tz=330
    )

    pytrends.build_payload(
        [keyword],
        timeframe="today 12-m"
    )

    data = pytrends.interest_over_time()

    return data.tail()