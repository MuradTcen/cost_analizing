import pandas as pd

CSV = 'avito.csv'


def read_csv(csv):
    df = pd.read_csv(csv, header=None)
    return df

def cleaning_df(df):

    return df


def main():
    df = read_csv(CSV)
    df = df.drop_duplicates()
    df = df.dropna()
    print(df)
    # print(df.duplicated())
    print(df[1].mean())


if __name__ == '__main__':
    main()
