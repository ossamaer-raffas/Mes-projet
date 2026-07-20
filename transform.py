import pandas as pd

# Lire le fichier CSV
df = pd.read_csv("data/ventes.csv")

print("Avant transformation")
print(df)

# Supprimer les doublons
df = df.drop_duplicates()

# Supprimer les lignes vides
df = df.dropna()

# Uniformiser les noms des produits
df["produit"] = df["produit"].str.upper()

print("\nAprès transformation")
print(df)

# Sauvegarder les données nettoyées
df.to_csv("data/ventes_nettoyees.csv", index=False)

print("\nTransformation terminée.")