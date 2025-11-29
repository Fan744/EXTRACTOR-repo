import os
from os import getenv

# =================== API CONFIG ===================
API_ID = int(getenv("API_ID", "30157302"))
API_HASH = getenv("API_HASH", "0052039fb2fca727868d0228cdaad569")
BOT_TOKEN = getenv("BOT_TOKEN", "7652541867:AAGLI0feS-21ctCZ-0KRoJUZd6yScVsGwXQ")
BOT_USERNAME = getenv("BOT_USERNAME", "@Coursebot16_bot")  # ADD THIS

# =================== USER CONFIG ===================
OWNER_ID = int(getenv("OWNER_ID", "6940228989"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6126688051 6039166844 5840594311 7621154046 7793979196 5798579221").split()))

# =================== DATABASE ===================
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://daxxop:daxxop@daxxop.dg3umlc.mongodb.net/?retryWrites=true&w=majority")

# =================== CHANNELS ===================
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003407124877"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1003407124877"))
