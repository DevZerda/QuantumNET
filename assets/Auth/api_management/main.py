# Modules
import os, sys, time, requests

# Files
from ..Config.main import *

class API_Manager:
    def addAPI(api, methods):
        apiDB = open("./assets/db/apis.db", "r").read()