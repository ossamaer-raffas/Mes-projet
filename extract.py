import pandas as pd
import sqlite3
import requests

# ==========================
# 1. Lire le fichier CSV
# ==========================

print("===== Données CSV =====")

csv_data = pd.read_csv("data/ventes.csv")

print(csv_data)


# ==========================
# 2. Lire SQLite
# ==========================

print("\n===== Données SQLite =====")

conn = sqlite3.connect("database/magasin.db")

sql_data = pd.read_sql_query("SELECT * FROM clients", conn)

print(sql_data)

conn.close()


# ==========================
# 3. Lire une API REST
# ==========================

print("\n===== Données API =====")

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

api_data = response.json()

for user in api_data:
    print(user["id"], user["name"], user["email"])