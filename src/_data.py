import pandas as pd

def preprocess(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)

    df.columns = [c.strip().lower() for c in df.columns.tolist()]
    df.drop("customerid", axis=1, inplace=True)

    x = df.isnull().sum(axis=0)\
            .to_frame("sum").query("sum != 0").index.tolist()
    print(x)

    return df
