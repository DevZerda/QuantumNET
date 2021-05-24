import os, sys, time, subprocess

class Usage:
    def CPU():
        cnc_pid = subprocess.getoutput("pgrep -f c2.py").split("\n")[0]
        get_usage = subprocess.getoutput(f"ps -p {cnc_pid} -o %cpu,%mem,cmd").split(" ")
        print("CPU: " + get_usage[3] + " | MEM: " + get_usage[5])