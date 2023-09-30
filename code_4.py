import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv('big_mac_file')
    year_countrycode = df[(df['year'] == year) & (df['iso_a3'] == country_code)]
    avg_price = round(df['dollar_price'].mean(), 2)

    return avg_price

def get_big_mac_price_by_country(country_code):
    pass # Remove this line and code your function

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    print(get_big_mac_price_by_year)