import os, sys, time

from discord_webhook import DiscordWebhook

class Discord():
	# webhooks = {
	# 	"screen": "https://discord.com/api/webhooks/844855350801072159/xPsomucP4neo4dOdGLBaIbRmz8ldvCr9617c2FcWgDjrwrvuemlc2shLtl5TJCjq6zi7",
	# 	"login": "https://discord.com/api/webhooks/844148531052412968/_uiWklaFSMI79_3NcKt45ZKumn6hvktS-mUSDnwxp_H630EIK8brKi74WWdcET_6HmH1",
	# 	"action": "https://discord.com/api/webhooks/844148531052412968/_uiWklaFSMI79_3NcKt45ZKumn6hvktS-mUSDnwxp_H630EIK8brKi74WWdcET_6HmH1",
	# 	"attack": "https://discord.com/api/webhooks/844148531052412968/_uiWklaFSMI79_3NcKt45ZKumn6hvktS-mUSDnwxp_H630EIK8brKi74WWdcET_6HmH1"
	# } # Exo

	def send_notice(msg):
		# types = ["screen", "login", "attack", "action"]
		# if type in types:
		webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/844855350801072159/xPsomucP4neo4dOdGLBaIbRmz8ldvCr9617c2FcWgDjrwrvuemlc2shLtl5TJCjq6zi7', content=msg)
		webhook.execute()
		# else: 
			# print("Unable to send request!")


class DiscordFunc():
	def netStartUp(host, port, time):
		notice = f"Quantum NET has successfully started\n\nHost: {host} | Port: {port}\nTime: {time}"
		Discord.send_notice(notice)

	def LoginLog(username, time):
		notice = f"[+] Login Attempted!\n\nUser: {username} | Time: {time}"
		Discord.send_notice(notice)

	def LogAttack(username, ip, port, time):
		notice = ""

	def LogCmd():
		notice = ""
