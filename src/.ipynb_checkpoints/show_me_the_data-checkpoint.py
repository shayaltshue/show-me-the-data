def first_look(df, title=""):
    
    if title:
        print(title)
        print("========================================")
        print("\n")
        
    print("Data Size:")
    print("--------------------------------")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    print("\n")
    
    print("Data Types:")
    print("--------------------------------")
    print(df.dtypes)
    print("\n")
    
    print("Missing Data:")
    print("--------------------------------")
    print(df.isna().sum())
    overall_percentage_missing = df.isna().sum().sum() / len(df)
    print("Overall percentage of missing data from all columns: {:.2%}".format(overall_percentage_missing))