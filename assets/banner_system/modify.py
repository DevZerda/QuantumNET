## Modules
import sys, os, time

## Files
from ..utils.main import *
from assets.Config.main import Strings


class BannerModify:
    def GetBannerFromFile(filee):
        slash = None
        if utils.GetOS() == True:
            slash = "/"
        else:
            slash = "\\"
        
        print(os.getcwd())
        print(os.getcwd() + slash + "assets" + slash + "banner_system" + slash + "banners" + slash + filee + ".txt")
        print("Is File: " + str(os.path.isfile(os.getcwd() + slash + "assets" + slash + "banner_system" + slash + "banners" + slash + filee + ".txt")))
        ## isnt reading file data or character symbols from file [THIS NEEDS TO BE FIXED]
        try:
            BannerFile = open(os.getcwd() + slash + "assets" + slash + "banner_system" + slash + "banners" + slash + filee + ".txt","r")
            BannerFile = BannerFile.read()
        except:
            print("Error")
            BannerFile = "Failed"

        return BannerFunc.ColorBanner(BannerFile)
        

class BannerFunc():
    appOwner = None
    appInstagram = None
    appDiscord = None
    appDiscordServer = None
    appName = None
    appVersion = None
    Username = None
    IPAddr = None

    def ColorBanner(bnnr):
        bnnr = bnnr.replace("{RED}", Strings.MainColors['Red'])
        bnnr = bnnr.replace("{YELLOW}", Strings.MainColors['Yellow'])
        bnnr = bnnr.replace("{BLUE}", Strings.MainColors['Blue'])
        bnnr = bnnr.replace("{PURPLE}", Strings.MainColors['Purple'])
        bnnr = bnnr.replace("{GREEN}", Strings.MainColors['Green'])
        bnnr = bnnr.replace("{BLACK}", Strings.MainColors['Black'])
        bnnr = bnnr.replace("{GREY}", Strings.MainColors['Grey'])
        bnnr = bnnr.replace("{CYAN}", Strings.MainColors['Cyan'])
        bnnr = bnnr.replace("{WHITE}", Strings.MainColors['White'])
        bnnr = bnnr.replace("{BG_GREY}", Strings.MainColors['Background_Red'])
        bnnr = bnnr.replace("{BG_GREEN}", Strings.MainColors['Background_Green'])
        bnnr = bnnr.replace("{BG_YELLOW}", Strings.MainColors['Background_Yellow'])
        bnnr = bnnr.replace("{BG_BLUE}", Strings.MainColors['Background_Blue'])
        bnnr = bnnr.replace("{BG_PURPLE}", Strings.MainColors['Background_Purple'])
        bnnr = bnnr.replace("{BG_CYAN}", Strings.MainColors['Background_Cyan'])
        bnnr = bnnr.replace("{BG_LIGHTGREY}", Strings.MainColors['Background_LightGrey'])
        bnnr = bnnr.replace("{BG_DARKGREY}", Strings.MainColors['Background_DarkGrey'])
        bnnr = bnnr.replace("{BG_LIGHTRED}", Strings.MainColors['Background_LightRed'])
        bnnr = bnnr.replace("{BG_LIGHTGREEN}", Strings.MainColors['Background_LightGreen'])
        bnnr = bnnr.replace("{BG_LIGHTYELLOW}", Strings.MainColors['Background_LightYellow'])
        bnnr = bnnr.replace("{BG_RESET}", Strings.MainColors['Background_Reset'])

    