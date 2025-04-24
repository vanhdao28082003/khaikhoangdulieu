def print_df(df,num = 5):
    print(df.head(num).to_string())


def print_missing_data(df):
    missing_data = df.isnull().sum()
    print("\nDữ liệu thiếu của các cột:")
    print(missing_data[missing_data > 0])
def print_rows_with_nan(df):
    rows_with_nan = df[df.isna().any(axis=1)]
    print(rows_with_nan.to_string())