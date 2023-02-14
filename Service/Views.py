
from Controller import Controller



command_list=["ADD","EXIT","READ","DATE","SELECT","DELETE","EDIT"]

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
                pass
            elif(com == "DATE"):
                pass
            elif(com == "SELECT"):
                pass
            elif(com == "DELETE"):
                pass
            elif(com == "EDIT"):
                pass


