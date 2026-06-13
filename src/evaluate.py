import pandas as pd

def show_top_features():

    df = pd.read_csv(
        "data/feature_importance.csv"
    )

    print(df.head(20))