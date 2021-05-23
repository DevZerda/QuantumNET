from .assets.Auth.crud import *

username = input("Username To Search: ")
User_Info = CRUD.GetUser(username)
print("String: " + User_Info)
print("Array: " + str(User_Info.split(",")))
