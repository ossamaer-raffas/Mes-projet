import pandas as pd
import sqlite3
import requests

print("======================================")
print("        EXTRACTION DES DONNÉES")
print("======================================")

# ======================================================
# 1. EXTRACTION DU FICHIER CSV
# ======================================================

print("\n========== SOURCE 1 : CSV ==========\n")

csv = pd.read_csv("data/ventes.csv")

print("Nombre de lignes :", len(csv))
print(csv)

# ======================================================
# 2. EXTRACTION SQLITE
# ======================================================

print("\n========== SOURCE 2 : SQLITE ==========\n")

conn = sqlite3.connect("database/clients.db")

clients = pd.read_sql_query("SELECT * FROM clients", conn)

print("Nombre de clients :", len(clients))
print(clients)

conn.close()

# ======================================================
# 3. EXTRACTION API OPEN-METEO
# ======================================================

print("\n========== SOURCE 3 : API METEO ==========\n")

url = (
    "https://api.open-meteo.com/v1/forecast?"
    "latitude=33.5731"
    "&longitude=-7.5898"
    "&hourly=temperature_2m,"
    "relative_humidity_2m,"
    "wind_speed_10m,"
    "pressure_msl,"
    "cloud_cover"
    "&forecast_days=16"
)

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    if "hourly" in data:

        meteo = pd.DataFrame({
            "date": data["hourly"]["time"],
            "temperature": data["hourly"]["temperature_2m"],
            "humidite": data["hourly"]["relative_humidity_2m"],
            "vent": data["hourly"]["wind_speed_10m"],
            "pression": data["hourly"]["pressure_msl"],
            "nuages": data["hourly"]["cloud_cover"]
        })

        print("Nombre d'enregistrements :", len(meteo))
        print(meteo)

    else:
        print("Erreur dans les données reçues :")
        print(data)

else:
    print("Erreur HTTP :", response.status_code)
    print(response.text)

print("\n======================================")
print("Extraction terminée avec succès.")
print("======================================")