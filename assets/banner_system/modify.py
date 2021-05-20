from assets.Config.main import MainColors
import sys, os, time


class BannerModify:
    def GetBannerFromFile(filee):
        BannerFile = open(filee, "r").read()
        return BannerFile
        

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
        bnnr = bnnr.replace("{RED}", MainColors['RED'])

    