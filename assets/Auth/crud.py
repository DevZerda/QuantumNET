import os, sys, time

class CRUD:
    def GetUser(Finduser):
        db = open("./assets/db/users.db", "r").read()
        users = db.split("\n")

        user_found = False
        user_line = ""

        for user in users:
            if len(user) > 4:
                if user.startswith("('" + Finduser):
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
        db.write(f"('{user}','{ip}','{password}','{level}','{maxtime}','{admin}')\n")
        db.close()
        return f"[+] User: {user} successfully added!\r\n"
    
    def RemoveUser(user):
        db = open("./assets/db/users.db", "r").read()
        users = db.split("\n")

        new_db = ""

        for u in users:
            if len(u) > 4:
                if user in u:
                    ## Edit user here
                    print("User found and removed!")
                else:
                    new_db += u + "\n"

        w_db = open("./assets/db/users.db", "w")
        w_db.write(new_db)
        w_db.close()
        return f"[x] User: {user} successfully updated!\r\n"

    def updateUser(user, newlvl, newmtime, newadmin):
        db = open("./assets/db/users.db", "r").read()
        users = db.split("\n")

        new_db = ""

        for usr in users:
            if len(usr) > 5:
                if usr.startswith("('" + usr):
                    fix = usr.replace("('", "")
                    fix2 = fix.replace("')", "")
                    userinfo = fix2.split("','")
                    new_db += "('" + userinfo[0] + "','" + userinfo[1] + "','" + userinfo[2] + "','" + newlvl + "','" + newmtime + "','" + newadmin + "')\n"
                else:
                    new_db += usr

        w_db = open("./assets/db/users.db", "w")
        w_db.write(new_db)
        return f"User: {user} successfully updated!\r\n"