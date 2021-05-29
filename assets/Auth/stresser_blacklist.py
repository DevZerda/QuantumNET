# Modules
from _typeshed import SupportsWrite
import os, sys, time

# Files

class StresserBlacklist:
    def CheckDB4IP(ip):
        stresserBL = open("./assets/db/stresser_blacklist.db", "r").read()
        BLips = stresserBL.split("\n")

        for ip in BLips:
            if len(ip) > 4:
                if ip.startswith(f"('{ip}"):
                    fix = ip.replace("('", "")
                    fix2 = fix.replace("')","")
                    return True

        return False

    def addIP(ip):
        stresserBL = open("./assets/db/stresser_blacklist.db", "a")
        stresserBL.write(f"('{ip}')\n")
        stresserBL.close()
        return f"[+] IP: {ip} sucessfully blacklisted\r\n"

    def removeIP(ip):
        stresserBL = open("./assets/db/stresser_blacklist.db", "r").read()
        BLips = stresserBL.split("\n")

        new_db = ""

        for ipadd in BLips:
            if len(ipadd) > 4:
                if ipadd.startswith(f"('{ip}"):
                    print(f"IP {ip} Sucessfully removed!\r\n")
                else:
                    new_db += ipadd + "\n"

        stresserBL_w = open("./assets/db/stresser_blacklist.db", "w")
        stresserBL_w.write(new_db)
        stresserBL_w.close()
        return f"[+] IP: {ip} successfully removed!\r\n"