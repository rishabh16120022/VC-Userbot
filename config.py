import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION", "BQF0Ou0Amyh5_9fQPfz6hDtBSHIHjuQ2xOG8UmymM-qo2a7mVAH-cbQbjcAlUQNJuo5Lnj2iyTTnK0XBqz3abcrPR59Zyv8FGBrmZ8lqrtpFZODpe3AG4n6EKCo6oApbVTBzu8Si30bhqxoLTbRe27Af_-Er7sTvSBf4LTLO2j-IAReaRtWaBNEeABSajpioyxFX-i-8WFjPlv0bySg9O0TU2Ey01oTSB_JX0aBdnLMyQcVUJ1i2dbiWmFkao4EEs8f458tg0dhgyZAlnq7qq4texL0sSjKEZl3rjo0Zf-vBnteDzDKQuDu6zA2twN1KsxgcjiGGtpyWKcy3YOpKnyK2yjhWmwAAAAGWSmGJAA")
HNDLR = os.getenv("HNDLR", "/")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "5516578116").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicRioUserbot"))
call_py = PyTgCalls(bot)
# © 2022 GitHub, Inc.
# Terms
# Privacy
# Security
