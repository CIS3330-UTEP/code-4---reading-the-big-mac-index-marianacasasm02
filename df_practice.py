import pandas as pd
filename = "big-mac-full-index.csv"
df = pd.read_csv(filename)

# query = f"(iso_a3 == 'MEX')"
# mxn_df = df.query(query)

# print(mxn_df['dollar_price'].median())

print(df['dollar_price'])

query = f"(iso_a3 == 'MEX')"
mxn_df = df.query(query)

print(mxn_df['dollar_price'].min())
