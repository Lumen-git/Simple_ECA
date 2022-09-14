def mainMenu():
    rule = -1;
    generation = -1;
    print("███████ ██ ███    ███ ██████  ██      ███████     ███████  ██████  █████")
    print("██      ██ ████  ████ ██   ██ ██      ██          ██      ██      ██   ██")
    print("███████ ██ ██ ████ ██ ██████  ██      █████       █████   ██      ███████") 
    print("     ██ ██ ██  ██  ██ ██      ██      ██          ██      ██      ██   ██") 
    print("███████ ██ ██      ██ ██      ███████ ███████     ███████  ██████ ██   ██")
    print("                    Easy tool for generating Elementary Cellular Automata")
    print("")
    print("")

    while (rule < 0) or (rule > 255):
        try:
            rule = int(input("Enter rule number: "))
        except:
            rule = -1
    while (generation < 0):
        try:
            generation = int(input("Enter generations to run (n rows, 2n columns): "))
        except:
            generation = -1


if __name__ == "__main__":
    mainMenu()