import os, sys, time, subprocess

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

    def CreateUser(user, password, level, maxtime, admin):
        db = open("./assets/db/users.db", "a")
        db.write(f"('{user}','none','{password}','{level}','{maxtime}','{admin}')\n")
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

    def CreateRegisterToken(level, time, admin):
        tokenDB = open("./assets/db/tokens.db", "a")
        new_token = subprocess.getoutput("tr -dc A-Za-z0-9 </dev/urandom | head -c 45 ; echo ''")
        tokenDB.write(f"token={new_token},level={level},time={time},admin={admin}")
        tokenDB.close()
        return f"Token generated: {new_token}\r\n"

        
    def GetTokenInfo(rtoken):
        tokenDB = open("./assets/db/tokens.db", "r").read()
        tokens = tokenDB.split("\n")

        for token in tokens:
            if len(token) > 4:
                if rtoken in token:
                    return rtoken

        return False
        


    #
    #
    #       Session CRUD
    #
    #

    def LogSession(username, ip):
        currentDB = open("./assets/db/current.db", "a")
        currentDB.write("('{}','{}')\n".format(username, ip))
        currentDB.close()
        
    def removeSession(usernameOrip):
        currentDB = open("./assets/db/current.db", "r").read()
        c_users = currentDB.split("\n")

        new_c_usr = ""

        for usr in c_users:
            if len(usr) > 4:
                if usr.startswith(f"('{usernameOrip}") | usr.startswith(f"{usernameOrip}')"):
                    print("User removed!")
                else:
                    new_c_usr = usr + "\n"

        c_db = open("./assets/db/current.db", "w")
        c_db.write(new_c_usr)
        c_db.close()
        

    def GetSessionInfo(usernameOrip):
        c_users = open("./assets/db/current.db", "r").read()
        users = c_users.split("\n")

        for usr in users:
            if len(usr) > 5:
                if usr.startswith(f"('{usernameOrip}") | usr.startswith(f"{usernameOrip}')"):
                    fix = usr.replace("('", "")
                    fix2 = fix.replace("')", "")
                    return fix2.replace("','", ",")

