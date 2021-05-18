import os, sys, time

class CRUD:
    def GetUser(Finduser):
        db = open("./assets/db/users.db", "r").read()
        users = db.split("\n")

        user_found = False
        user_line = ""

        for user in users:
            if len(user) > 4:
                if Finduser in user:
                    user_found = True
                    new = user.replace("('", "")
                    new1 = new.replace("')", "")
                    user_line = new1.replace("','", ",")
        
        if user_found:
            return user_line
        else:
            return "[x] Error, No user found!"

    def CreateUser(user, ip, password, level, maxtime, admin):
        db = open("./assets/db/users.db", "a")
        db.write("('{user}','{ip}','{passwrd}','{level}','{maxtime}','{admin}')\n")
        db.close()
        return "[+] User: {user} successfully added!\r\n"
    
    def RemoveUser(user):
        db = open("./assets/db/users.db", "r").read()
        users = db.split("\n")

        new_db = ""

        for u in users:
            if len(u) > 4:
                if user in u:
                    print("User found and removed!")
                else:
                    new_db += u + "\n"

        w_db = open("./assets/db/users.db", "w")
        w_db.write(new_db)
        w_db.close()
        return "[x] User: {user} successfully updated!\r\n"