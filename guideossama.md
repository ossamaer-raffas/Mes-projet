# Guide d'utilisation du projet ETL Pipeline avec MongoDB

## 1. Introduction

Ce guide explique comment installer, configurer et exécuter le projet **ETL Pipeline avec MongoDB**.

Le pipeline suit les trois étapes classiques :

* **Extract (Extraction)** : récupération des données depuis plusieurs sources.
* **Transform (Transformation)** : nettoyage et préparation des données.
* **Load (Chargement)** : insertion des données dans MongoDB.

À la fin du traitement, des statistiques sont générées grâce aux requêtes d'agrégation MongoDB.

---

# 2. Prérequis

Avant d'exécuter le projet, installer :

* Python 3
* MongoDB Community Server
* MongoDB Compass (optionnel mais recommandé)
* Visual Studio Code (ou un autre éditeur)

Vérifier Python :

```bash
py --version
```

Vérifier MongoDB :

```bash
mongod --version
```

---

# 3. Installation des bibliothèques

Depuis le dossier du projet :

```bash
pip install -r requirements.txt
```

ou

```bash
pip install pandas
pip install pymongo
pip install requests
pip install schedule
```

---

# 4. Structure du projet

```text
ETL_Project
│
├── data
│   ├── ventes.csv
│   └── ventes_nettoyees.csv
│
├── database
│   └── magasin.db
│
├── logs
│
├── extract.py
├── transform.py
├── load.py
├── scheduler.py
├── dashboard.py
├── requirements.txt
└── README.md
```

---

# 5. Description des fichiers

## extract.py

Extraction des données depuis :

* fichier CSV
* base SQLite
* API REST

---

## transform.py

Transformation des données :

* suppression des doublons
* suppression des valeurs manquantes
* conversion des noms des produits en majuscules

---

## load.py

Chargement des données dans MongoDB.

Base :

```
DataWarehouse
```

Collection :

```
ventes
```

---

## scheduler.py

Automatise l'exécution du pipeline.

Ordre d'exécution :

```
extract.py

↓

transform.py

↓

load.py
```

Les exécutions sont enregistrées dans :

```
pipeline_logs
```

---

## dashboard.py

Affiche des statistiques :

* nombre total de produits ;
* prix moyen ;
* quantité totale vendue ;
* produits par catégorie ;
* produit le plus cher ;
* valeur totale des ventes.

---

# 6. Sources de données

Le projet utilise trois sources différentes.

## Source 1 : CSV

```
data/ventes.csv
```

Contient les informations sur les produits.

---

## Source 2 : SQLite

```
database/magasin.db
```

Contient la table :

```
clients
```

---

## Source 3 : API REST

```
https://jsonplaceholder.typicode.com/users
```

Les informations des utilisateurs sont récupérées automatiquement via Internet.

---

# 7. Exécution du projet

## Étape 1 : Extraction

Commande :

```bash
py extract.py
```

Cette étape affiche les données provenant des trois sources.

---

## Étape 2 : Transformation

Commande :

```bash
py transform.py
```

Le fichier :

```
ventes_nettoyees.csv
```

est créé automatiquement.

---

## Étape 3 : Chargement

Commande :

```bash
py load.py
```

Les données sont enregistrées dans MongoDB.

---

## Étape 4 : Dashboard

Commande :

```bash
py dashboard.py
```

Affichage des statistiques.

---

## Étape 5 : Automatisation

Commande :

```bash
py scheduler.py
```

Le pipeline est exécuté automatiquement toutes les minutes.

Pour arrêter le scheduler :

```
Ctrl + C
```

---

# 8. Vérification dans MongoDB Compass

Ouvrir MongoDB Compass.

La base suivante doit apparaître :

```
DataWarehouse
```

Elle contient les collections :

```
ventes

pipeline_logs
```

La collection **ventes** contient les produits.

La collection **pipeline_logs** contient l'historique des exécutions du pipeline.

---

# 9. Résultats attendus

Après l'exécution complète :

* les données sont extraites depuis trois sources ;
* les données sont nettoyées ;
* les données sont stockées dans MongoDB ;
* les statistiques sont calculées ;
* les exécutions sont enregistrées dans les logs.

---

# 10. Conclusion

Ce projet démontre la réalisation d'un pipeline ETL complet avec Python et MongoDB.

Il met en œuvre :

* l'extraction de données depuis plusieurs sources ;
* la transformation avec Pandas ;
* le chargement dans MongoDB ;
* l'automatisation avec Schedule ;
* l'analyse grâce aux agrégations MongoDB.

Cette architecture peut être enrichie par la suite avec d'autres sources de données, des tableaux de bord graphiques ou des outils de visualisation comme Streamlit ou Power BI.
