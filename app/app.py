from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST', 'postgres'),
            database=os.getenv('DB_NAME', 'testdb'),
            user=os.getenv('DB_USER', 'pmihai'),
            password=os.getenv('DB_PASS', 'parola123')
        )
        return "Conexiune la baza de date reușită! GitOps funcționează!"
    except Exception as e:
        return f"Eroare la conexiune: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
