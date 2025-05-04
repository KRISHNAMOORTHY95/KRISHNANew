import pandas as pd
import sqlite3

def create_database():
    conn = sqlite3.connect('food.db')

    providers = pd.read_csv('data/providers_data.csv')
    receivers = pd.read_csv('data/receivers_data.csv')
    listings = pd.read_csv('data/food_listings_data.csv')
    claims = pd.read_csv('data/claims_data.csv')

    providers.to_sql('providers', conn, if_exists='replace', index=False)
    receivers.to_sql('receivers', conn, if_exists='replace', index=False)
    listings.to_sql('food_listings', conn, if_exists='replace', index=False)
    claims.to_sql('claims', conn, if_exists='replace', index=False)

    conn.close()

if __name__ == "__main__":
    create_database()
