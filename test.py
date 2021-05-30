from tkinter import *

wow = Tk()

def ree(hi):
  print(hi)
  
w = Button ( master=wow, command=ree('hi'), text="hi" )
