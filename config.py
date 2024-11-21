import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28578880"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5f8c87efde57e01d12c0ce98ffdf5928")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://swapan9641:7DqQqG+3z$c5*7V@cluster0.mi3nd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
