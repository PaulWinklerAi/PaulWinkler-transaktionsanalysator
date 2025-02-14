import pandas as pd
import requests
import os

def read_transactions(file_path):
    """Läser in transaktionsdata från en CSV-fil."""
    if not os.path.exists(file_path):
        print("Filen finns inte. Skapa en transactions.csv först.")
        return None
    return pd.read_csv(file_path)

def convert_currency(amount, from_currency, to_currency="SEK"):
    """Konverterar en valör till en annan med hjälp av en API-förfrågan."""
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(api_url)
    if response.status_code != 200:
        print("Misslyckades med att hämta valutakurser.")
        return amount
    rates = response.json()["rates"]
    return amount * rates.get(to_currency, 1)

def analyze_expenses(df):
    """Analyserar utgifter genom att gruppera efter kategori."""
    if df is None:
        return None
    return df.groupby("Kategori")["Belopp"].sum()

def main():
    file_path = "data/transactions.csv"
    df = read_transactions(file_path)
    
    if df is not None:
        print("Utgiftsanalys per kategori:")
        print(analyze_expenses(df))
        
        df["Belopp i SEK"] = df.apply(lambda row: convert_currency(row["Belopp"], row["Valuta"]), axis=1)
        print("Uppdaterad transaktionslista med SEK:")
        print(df)

if __name__ == "__main__":
    main()
