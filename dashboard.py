from pymongo import MongoClient

# ==========================================
# Connexion MongoDB
# ==========================================

client = MongoClient("mongodb://localhost:27017/")
db = client["DataWarehouse"]

# ==========================================
# COLLECTION VENTES
# ==========================================

ventes = db["ventes"]

print("===================================")
print("      STATISTIQUES DES VENTES")
print("===================================")

print("\n===== Quantité totale vendue =====")

pipeline = [
    {
        "$group": {
            "_id": None,
            "TotalQuantite": {"$sum": "$quantite"}
        }
    }
]

for x in ventes.aggregate(pipeline):
    print(x)

print("\n===== Prix moyen =====")

pipeline = [
    {
        "$group": {
            "_id": None,
            "PrixMoyen": {"$avg": "$prix"}
        }
    }
]

for x in ventes.aggregate(pipeline):
    print(x)

print("\n===== Nombre de produits par catégorie =====")

pipeline = [
    {
        "$group": {
            "_id": "$categorie",
            "Nombre": {"$sum": 1}
        }
    }
]

for x in ventes.aggregate(pipeline):
    print(x)


# ==========================================
# COLLECTION CLIENTS
# ==========================================

clients = db["clients"]

print("\n\n===================================")
print("      STATISTIQUES DES CLIENTS")
print("===================================")

print("\n===== Nombre total de clients =====")

pipeline = [
    {
        "$count": "TotalClients"
    }
]

for x in clients.aggregate(pipeline):
    print(x)

print("\n===== Nombre de clients par ville =====")

pipeline = [
    {
        "$group": {
            "_id": "$ville",
            "Nombre": {"$sum": 1}
        }
    },
    {
        "$sort": {"Nombre": -1}
    }
]

for x in clients.aggregate(pipeline):
    print(x)

print("\n===== Nombre de clients par première lettre =====")

pipeline = [
    {
        "$project": {
            "PremiereLettre": {
                "$substr": ["$nom", 0, 1]
            }
        }
    },
    {
        "$group": {
            "_id": "$PremiereLettre",
            "Nombre": {"$sum": 1}
        }
    },
    {
        "$sort": {"_id": 1}
    }
]

for x in clients.aggregate(pipeline):
    print(x)


# ==========================================
# COLLECTION METEO
# ==========================================

meteo = db["meteo"]

print("\n\n===================================")
print("      STATISTIQUES MÉTÉO")
print("===================================")

print("\n===== Température moyenne =====")

pipeline = [
    {
        "$group": {
            "_id": None,
            "TemperatureMoyenne": {"$avg": "$temperature"}
        }
    }
]

for x in meteo.aggregate(pipeline):
    print(x)

print("\n===== Humidité moyenne =====")

pipeline = [
    {
        "$group": {
            "_id": None,
            "HumiditeMoyenne": {"$avg": "$humidite"}
        }
    }
]

for x in meteo.aggregate(pipeline):
    print(x)

print("\n===== Vitesse moyenne du vent =====")

pipeline = [
    {
        "$group": {
            "_id": None,
            "VentMoyen": {"$avg": "$vent"}
        }
    }
]

for x in meteo.aggregate(pipeline):
    print(x)

print("\n===== Pression moyenne =====")

pipeline = [
    {
        "$group": {
            "_id": None,
            "PressionMoyenne": {"$avg": "$pression"}
        }
    }
]

for x in meteo.aggregate(pipeline):
    print(x)

print("\n===== Température maximale =====")

pipeline = [
    {
        "$group": {
            "_id": None,
            "TemperatureMax": {"$max": "$temperature"}
        }
    }
]

for x in meteo.aggregate(pipeline):
    print(x)

print("\n===== Température minimale =====")

pipeline = [
    {
        "$group": {
            "_id": None,
            "TemperatureMin": {"$min": "$temperature"}
        }
    }
]

for x in meteo.aggregate(pipeline):
    print(x)

client.close()