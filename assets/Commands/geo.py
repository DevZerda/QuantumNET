import os, sys, time, requests, json

def geo_command(socket, argv):
    jsonResp = (requests.get("http://extreme-ip-lookup.com/json/" + argv[1]).text)
    geo = json.loads(jsonResp) #jsonResp.json()*
    responsee = "             IP: " + geo["query"] + "\r\n"
    responsee += "            IP Type: " + geo['ipType'] + "\r\n"
    responsee += "            Country: " + geo['country'] + "\r\n"
    responsee += "            City: " + geo['city'] + "\r\n"
    responsee += "            Continent: " + geo['continent'] + "\r\n"
    responsee += "            IPName: " + geo['ipName'] + "\r\n"
    responsee += "            ISP: " + geo['isp'] + "\r\n"
    responsee += "            Latitute: " + geo['lat'] + "\r\n"
    responsee += "            Longitude: " + geo['lon'] + "\r\n"
    responsee += "            Org: " + geo['org'] + "\r\n"
    responsee += "            Region: " + geo['region'] + "\r\n"
    responsee += "            Status: " + geo['status'] + "\r\n"
    socket.send(f"{responsee}".encode("utf-8"))
