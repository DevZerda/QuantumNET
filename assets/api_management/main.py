# Modules
import os, sys, time, requests

# Files
from ..Config.main import *

class API_Manager:
    def addAPI(apiName, api, methods):
        apiDB = open("./assets/db/apis.db", "a")
        apiDB.write(f"apiName={apiName}\napi={api}\nmethods={methods}\n")
        apiDB.close()

    def removeAPI(apiName):
        apiDB = open("./assets/db/apis.db", "r").read()
        apis = apiDB.split("\n")

        new_apiDB = ""

        for api in apis:
            if len(api) > 5:
                if apiName in api:
                    ##dnt add
                    return ""
                else:
                    new_apiDB += api + "\n"
