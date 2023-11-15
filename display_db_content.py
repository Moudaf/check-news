import sqlite3
import json
import re

# Connectez-vous à la base de données
conn = sqlite3.connect('conversation.db')
cursor = conn.cursor()

# Exécutez une requête pour récupérer les données de suivi
cursor.execute("SELECT data FROM events WHERE type_name IN ('user', 'bot');")


# Récupérez les résultats
results = cursor.fetchall()

def remove_text_between_slash_and_curly_brace(text):
    return re.sub(r'\/.*?(?=\{)', '', text)

# Affichez les résultats
for row in results:
    data_json = json.loads(row[0])

    if data_json["event"] == "user":
        user_text = remove_text_between_slash_and_curly_brace(data_json['text']).strip()
        print(f"\033[94mUtilisateur: {user_text}\033[0m")
    elif data_json["event"] == "bot":
        bot_text = remove_text_between_slash_and_curly_brace(data_json['text']).strip()
        print(f"\033[92mBot: {bot_text}\033[0m")

    print("")


# Fermez la connexion
conn.close()
