# Modules
import os, sys, time

# Files
from ..Auth.crud import *
from ..Auth.crudFunc import *
from ..Config.main import *
from ..banner_system.modify import *
from ..utils.main import *

def dashboard_command(socket, argv):
    socket.send(str(Strings.MainColors['Clear'] + CustomBannerMaker.CreateMOTD(utils.GetMOTD()) + BannerModify.GetBannerFromFile("main") + BannerModify.GetBannerFromFile("net_stats")).encode())

