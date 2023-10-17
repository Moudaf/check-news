# Utilisez une image Windows Server Core comme base
# FROM mcr.microsoft.com/windows/servercore:ltsc2022
# FROM nginx:alpine
FROM rasa/rasa:3.0.0

# Copiez votre projet Rasa dans le conteneur
COPY . /app

# Définissez le répertoire de travail
WORKDIR /app

# Installez Rasa et ses dépendances (adapté pour Windows)
# RUN pip install -U pip
# RUN pip install rasa

# Exécutez votre chatbot Rasa
CMD ["rasa", "run", "-m", "models", "--endpoints", "endpoints.yml"]
