import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year, country_code):
    # Load the CSV data into a Pandas DataFrame
    df = pd.read_csv('./big-mac-full-index.csv')

    # Filter DataFrame by year and country_code
    filtered_df = df[(df['date'] == year) & (df['iso_a3'] == country_code)]

    # Calculate the mean price and round it to 2 decimal places
    mean_price = round(filtered_df['dollar_price'].mean(), 2)

    return mean_price

# def get_big_mac_price_by_country(country_code):
#     # Load the CSV data into a Pandas DataFrame
#     df = pd.read_csv('big_mac_data.csv')

#     # Filter DataFrame by country_code
#     filtered_df = df[df['iso_a3'] == country_code]

#     # Calculate the mean price and round it to 2 decimal places
#     mean_price = round(filtered_df['dollar_price'].mean(), 2)

#     return mean_price

# def get_the_cheapest_big_mac_price_by_year(year):
#     # Load the CSV data into a Pandas DataFrame
#     df = pd.read_csv('big_mac_data.csv')

#     # Filter DataFrame by year to find the row with the cheapest Big Mac
#     cheapest_row = df[df['year'] == year].nsmallest(1, 'dollar_price')

#     # Extract country name, country code, and price
#     country_name = cheapest_row['name'].values[0]
#     country_code = cheapest_row['iso_a3'].values[0]
#     dollar_price = cheapest_row['dollar_price'].values[0]

#     return f'{country_name}({country_code}): ${dollar_price:.2f}'

# def get_the_most_expensive_big_mac_price_by_year(year):
#     # Load the CSV data into a Pandas DataFrame
#     df = pd.read_csv('big_mac_data.csv')

#     # Filter DataFrame by year to find the row with the most expensive Big Mac
#     expensive_row = df[df['year'] == year].nlargest(1, 'dollar_price')

#     # Extract country name, country code, and price
#     country_name = expensive_row['name'].values[0]
#     country_code = expensive_row['iso_a3'].values[0]
#     dollar_price = expensive_row['dollar_price'].values[0]

#     return f'{country_name}({country_code}): ${dollar_price:.2f}'

if __name__ == "__main__":
    year = 2008
    country_code = 'MYS'
    print(f'Mean Big Mac price in {year} for {country_code}: ${get_big_mac_price_by_year(year, country_code)}')

    # country_code = 'MYS'
    # print(f'Mean Big Mac price in {country_code}: ${get_big_mac_price_by_country(country_code)}')

    # year = 2008
    # print(get_the_cheapest_big_mac_price_by_year(year))

    # year = 2003
    # print(get_the_most_expensive_big_mac_price_by_year(year))