import pandas as pd
import sqlite3
import requests

print("======================================")
print("     TRANSFORMATION DES DONNÉES")
print("======================================")

# ===================================================
# 1. TRANSFORMATION DU CSV
# ===================================================

print("\n===== Transformation CSV =====")

csv = pd.read_csv("data/ventes.csv")

print("\nAvant :")
print(csv)

# Nettoyage
csv = csv.drop_duplicates()
csv = csv.dropna()

csv["produit"] = csv["produit"].astype(str).str.upper().str.strip()
csv["categorie"] = csv["categorie"].astype(str).str.upper().str.strip()

csv["prix"] = pd.to_numeric(csv["prix"], errors="coerce")
csv["quantite"] = pd.to_numeric(csv["quantite"], errors="coerce")

csv["date"] = pd.to_datetime(csv["date"], dayfirst=True, errors="coerce")

csv = csv.dropna()

print("\nAprès :")
print(csv)

csv.to_csv("data/ventes_nettoyees.csv", index=False)

print("\nCSV transformé :", len(csv), "lignes")


# ===================================================
# 2. TRANSFORMATION SQLITE
# ===================================================

print("\n===== Transformation SQLite =====")

conn = sqlite3.connect("database/clients.db")

clients = pd.read_sql_query("SELECT * FROM clients", conn)

print("\nAvant :")
print(clients)

# Nettoyage
clients = clients.drop_duplicates()
clients = clients.dropna()

clients["nom"] = clients["nom"].astype(str).str.upper().str.strip()
clients["ville"] = clients["ville"].astype(str).str.upper().str.strip()

if "email" in clients.columns:
    clients["email"] = clients["email"].astype(str).str.lower().str.strip()

print("\nAprès :")
print(clients)

# IMPORTANT : sauvegarder les CLIENTS et non le CSV
clients.to_csv("database/clients_nettoyes.csv", index=False)

conn.close()

print("\nClients transformés :", len(clients), "lignes")


# ===================================================
# 3. TRANSFORMATION API METEO
# ===================================================

print("\n===== Transformation API =====")

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

    meteo = pd.DataFrame({
        "date": data["hourly"]["time"],
        "temperature": data["hourly"]["temperature_2m"],
        "humidite": data["hourly"]["relative_humidity_2m"],
        "vent": data["hourly"]["wind_speed_10m"],
        "pression": data["hourly"]["pressure_msl"],
        "nuages": data["hourly"]["cloud_cover"]
    })

    print("\nAvant :")
    print(meteo)

    meteo = meteo.drop_duplicates()
    meteo = meteo.dropna()

    meteo["temperature"] = meteo["temperature"].round(1)
    meteo["humidite"] = meteo["humidite"].round(0)
    meteo["vent"] = meteo["vent"].round(1)
    meteo["pression"] = meteo["pression"].round(0)

    print("\nAprès :")
    print(meteo)

    meteo.to_csv("data/meteo_nettoyee.csv", index=False)

    print("\nMétéo transformée :", len(meteo), "lignes")

else:
    print("Erreur HTTP :", response.status_code)

print("\n======================================")
print("Transformation terminée avec succès.")
print("======================================")