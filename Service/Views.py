
from Controller import Controller

command_list=["ADD","EXIT","READ","DATE","SELECT","DELETE","EDIT","HELP"]

def start():

    contr = Controller()

    while True:
        command = input("Введите команду: ")
        com=command.upper()
        if (com not in command_list):
            print("Unknown command")
            continue
        else:
            if(com == "EXIT"): return
            elif(com == "ADD"):
                contr.add()
            elif(com == "READ"):
                contr.read()
            elif(com == "DATE"):
                contr.date()
            elif(com == "SELECT"):
                contr.select()
            elif(com == "DELETE"):
                contr.delete()
            elif(com == "EDIT"):
                contr.edit()
            elif(com == "HELP"):
                contr.help()


