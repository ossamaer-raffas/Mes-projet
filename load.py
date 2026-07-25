from pymongo import MongoClient
import pandas as pd

# Connexion MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["DataWarehouse"]

print("Connexion à MongoDB réussie.")

# ===========================
# VENTES
# ===========================

print("\nChargement des ventes...")

ventes = pd.read_csv("data/ventes_nettoyees.csv")

collection_ventes = db["ventes"]
collection_ventes.delete_many({})
collection_ventes.insert_many(ventes.to_dict("records"))

print(len(ventes), "ventes insérées.")

# ===========================
# CLIENTS
# ===========================

print("\nChargement des clients...")

clients = pd.read_csv("database/clients_nettoyes.csv")   # <-- Vérifie ce nom

collection_clients = db["clients"]
collection_clients.delete_many({})
collection_clients.insert_many(clients.to_dict("records"))

print(len(clients), "clients insérés.")

# ===========================
# METEO
# ===========================

print("\nChargement de la météo...")

meteo = pd.read_csv("data/meteo_nettoyee.csv")

collection_meteo = db["meteo"]
collection_meteo.delete_many({})
collection_meteo.insert_many(meteo.to_dict("records"))

print(len(meteo), "enregistrements météo insérés.")

print("\n===== Vérification =====")

print("Ventes  :", collection_ventes.count_documents({}))
print("Clients :", collection_clients.count_documents({}))
print("Météo   :", collection_meteo.count_documents({}))

client.close()