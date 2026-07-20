from pymongo import MongoClient
import pandas as pd

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")

db = client["DataWarehouse"]

collection = db["ventes"]

# Lire le fichier nettoyé
df = pd.read_csv("data/ventes_nettoyees.csv")

# Supprimer les anciennes données
collection.delete_many({})

# Insérer les nouvelles données
collection.insert_many(df.to_dict("records"))

print("Données chargées dans MongoDB.")