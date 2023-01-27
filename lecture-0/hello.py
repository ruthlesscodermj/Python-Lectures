#print ("Hello World <3")

NAME = ""
NUMBERS = ""

def another_Hello_World(string:str):
    argument_passed = string
    NUMBERS = 20
    print(argument_passed, NUMBERS)

if __name__ == "__main__":
    another_Hello_World("Print Me")