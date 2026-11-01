import pandas as pd


def export_to_excel(
    result,
    output_file
):

    df = pd.DataFrame(
        result.items(),
        columns=[
            "Section",
            "Content"
        ]
    )

    df.to_excel(
        output_file,
        index=False
    )