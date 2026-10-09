import os

# Fix SAST CWE-798: secrets lus depuis l'environnement, plus de valeurs en dur
DB_PASSWORD = os.environ["DB_PASSWORD"]
AWS_SECRET = os.environ["AWS_SECRET"]

def connect():
    return DB_PASSWORD
