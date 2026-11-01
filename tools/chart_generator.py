import os
import matplotlib.pyplot as plt


def create_score_chart(scores):

    labels = [
        "Market",
        "Competition",
        "Finance",
        "Risk",
        "Overall"
    ]

    values = [
        scores.get("market_score", 0),
        scores.get("competition_score", 0),
        scores.get("finance_score", 0),
        scores.get("risk_score", 0),
        scores.get("overall_score", 0)
    ]

    plt.figure(figsize=(8, 5))

    bars = plt.bar(
        labels,
        values,
        color=[
            "green",
            "orange",
            "blue",
            "red",
            "purple"
        ]
    )

    plt.ylim(0, 10)

    plt.ylabel("Score")

    plt.title(
        "Startup Analysis Scores"
    )

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 0.2,
            str(height),
            ha="center"
        )

    os.makedirs(
        "reports",
        exist_ok=True
    )

    plt.savefig(
        "reports/startup_chart.png"
    )

    plt.close()
