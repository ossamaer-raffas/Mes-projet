import schedule
import time
import subprocess
from pymongo import MongoClient
from datetime import datetime

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["DataWarehouse"]
logs = db["pipeline_logs"]

# Fonction du pipeline
def pipeline():

    print("===== Début du pipeline =====")

    try:
        subprocess.run(["py", "extract.py"], check=True)
        subprocess.run(["py", "transform.py"], check=True)
        subprocess.run(["py", "load.py"], check=True)

        log = {
            "date": datetime.now(),
            "status": "SUCCESS"
        }

        logs.insert_one(log)

        print("Pipeline exécuté avec succès")

    except Exception as e:

        log = {
            "date": datetime.now(),
            "status": "FAILED",
            "error": str(e)
        }

        logs.insert_one(log)

        print(e)

# Exécuter toutes les minutes
schedule.every(1).minutes.do(pipeline)

print("Scheduler démarré...")

while True:
    schedule.run_pending()
    time.sleep(1)