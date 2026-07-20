from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["DataWarehouse"]

collection = db["ventes"]

print("===== Nombre total de produits =====")

pipeline = [
    {
        "$group": {
            "_id": None,
            "TotalQuantite": {
                "$sum": "$quantite"
            }
        }
    }
]

for x in collection.aggregate(pipeline):
    print(x)

print("\n===== Prix moyen =====")

pipeline = [
    {
        "$group": {
            "_id": None,
            "PrixMoyen": {
                "$avg": "$prix"
            }
        }
    }
]

for x in collection.aggregate(pipeline):
    print(x)

print("\n===== Produits par catégorie =====")

pipeline = [
    {
        "$group": {
            "_id": "$categorie",
            "Nombre": {
                "$sum": 1
            }
        }
    }
]

for x in collection.aggregate(pipeline):
    print(x)