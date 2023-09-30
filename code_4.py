import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'


def get_big_mac_price_by_year(year, country_code):
    df = pd.read_csv(big_mac_file)
    query_text = f"(date >= '{year}-01-01') and (date <= '{year}-12-31') and (iso_a3 == '{country_code}'.upper())"
    df = df.query(query_text)
    mean = df['dollar_price'].mean()
    final_mean = round(mean, 2)
    return final_mean


def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)

    query_text = f"(iso_a3 == '{country_code}'.upper())"
    df = df.query(query_text)
    mean = df['dollar_price'].mean()
    final_mean = round(mean, 2)
    return final_mean

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    query_text = f"(date >= '{year}-01-01') and (date <= '{year}-12-31')"
    df = df.query(query_text)
    id_cheapest = df['dollar_price'].idxmin()
    min_country = df.loc[id_cheapest]
    min_mac = round(min_country['dollar_price'], 2)
    final = f"{min_country['name']}({min_country['iso_a3']}): ${min_mac}"
    return final

def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    query_text = f"(date >= '{year}-01-01') and (date <= '{year}-12-31')"
    df = df.query(query_text)
    id_expensive = df['dollar_price'].idxmax()
    max_country = df.loc[id_expensive]
    max_mac = round(max_country['dollar_price'], 2)
    final = f"{max_country['name']}({max_country['iso_a3']}): ${max_mac}"
    return final

if __name__ == "__main__":
    print(get_big_mac_price_by_year(2010, "ARG"))
    print(get_big_mac_price_by_country("mex"))
    print(get_the_cheapest_big_mac_price_by_year(2008))
    print(get_the_most_expensive_big_mac_price_by_year(2014))