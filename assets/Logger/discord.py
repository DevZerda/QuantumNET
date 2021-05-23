import os, sys, time

from discord_webhook import DiscordWebhook

class Discord:
	def send_news(msg):
		msg = f"```{msg}```"
		webhook = DiscordWebhook(url='https://discord.com/api/webhooks/846082323158138881/l6AGbp9UMQqxeeetqzi5QHDkug1ftcdCiUFSkPynSrDkxZgBJzLGM-v4-aBz2tVoaLBm', content=msg)
		webhook.execute()

	def send_status(msg):
		msg = f"```{msg}```"
		webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/844855350801072159/xPsomucP4neo4dOdGLBaIbRmz8ldvCr9617c2FcWgDjrwrvuemlc2shLtl5TJCjq6zi7', content=msg)
		webhook.execute()

	def send_attack(msg):
		msg = f"```{msg}```"
		webhook = DiscordWebhook(url='https://discord.com/api/webhooks/846080791829282846/WokclMPaJ8G3UGtS5huyMvqbAPDobwJDq-K_B4Nxe5khoJKTwPt9wB2m_FllKTbQcPa6', content=msg)
		webhook.execute()

	def send_login(msg):
		msg = f"```{msg}```"
		webhook = DiscordWebhook(url='https://discord.com/api/webhooks/846081409659699211/dSkGHSLzYIrPrBcwqdfzBUqRKAkzme2Ibae0Wm-fjA6pmcRxzoy1naPYrf0Am5ItU7Mw', content=msg)
		webhook.execute()

	def send_logs(msg):
		msg = f"```{msg}```"
		webhook = DiscordWebhook(url='https://discord.com/api/webhooks/844893815772282880/r20oO4fg-CkbmxLs_QhsmS0AHe_kQ4BzkvfTTYZx9Zmp7SKQqBRDCUfTDcUK5dsPC8-L', content=msg)
		webhook.execute()