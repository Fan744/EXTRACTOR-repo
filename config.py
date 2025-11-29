"""
from os import getenv


API_ID = int(getenv("API_ID", "30157302"))
API_HASH = getenv("API_HASH", "0052039fb2fca727868d0228cdaad569")
BOT_TOKEN = getenv("BOT_TOKEN", "8211241815:AAHfRY0Y13AeZvaQcfl5Y9njvi31B22fR-I")
OWNER_ID = int(getenv("OWNER_ID", "6940228989"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6126688051 6039166844").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://daxxop:daxxop@daxxop.dg3umlc.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003407124877"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1003407124877"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5840594311 7621154046 7793979196 5798579221").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS"))

