import matplotlib.pyplot as plt
import numpy as np

def generateECA(rule, generation):
    
    #Convert base10 rule to binary
    rule = '{0:08b}'.format(rule)

    #Rules
    a = int(rule[0]) #111
    b = int(rule[1]) #110
    c = int(rule[2]) #101
    d = int(rule[3]) #100
    e = int(rule[4]) #011
    f = int(rule[5]) #010
    g = int(rule[6]) #001
    h = int(rule[7]) #000

    #Initial State
    eca = [0] * generation
    eca = eca + [1]
    eca = eca + ([0] * generation)
    eca = [eca]

    #Make ECA
    row_length = (generation*2)+1
    neighborhood = []
    for i in range(1, generation):
        new_row = [None] * row_length
        eca.append(new_row)
        for j in range(row_length):
            #Get neighborhood
            if (j == 0): 
                neighborhood = [eca[i-1][row_length-1], eca[i-1][j], eca[i-1][j+1]]
            if (j == row_length-1): 
                neighborhood = [eca[i-1][j-1], eca[i-1][j], eca[i-1][0]]
            else: 
                neighborhood = [eca[i-1][j-1], eca[i-1][j], eca[i-1][j+1]]
            #Match to rules
            if (neighborhood ==[1,1,1]):
                eca[i][j] = a
            if (neighborhood ==[1,1,0]):
                eca[i][j] = b
            if (neighborhood ==[1,0,1]):
                eca[i][j] = c
            if (neighborhood ==[1,0,0]):
                eca[i][j] = d
            if (neighborhood ==[0,1,1]):
                eca[i][j] = e
            if (neighborhood ==[0,1,0]):
                eca[i][j] = f
            if (neighborhood ==[0,0,1]):
                eca[i][j] = g
            if (neighborhood ==[0,0,0]):
                eca[i][j] = h
    return eca



def mainMenu():
    rule = -1;
    generation = -1;
    print("███████ ██ ███    ███ ██████  ██      ███████     ███████  ██████  █████")
    print("██      ██ ████  ████ ██   ██ ██      ██          ██      ██      ██   ██")
    print("███████ ██ ██ ████ ██ ██████  ██      █████       █████   ██      ███████") 
    print("     ██ ██ ██  ██  ██ ██      ██      ██          ██      ██      ██   ██") 
    print("███████ ██ ██      ██ ██      ███████ ███████     ███████  ██████ ██   ██")
    print("           Easy tool for generating Elementary Cellular Automata graphics")
    print("")
    print("")

    #Get rules and generations
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
    eca = generateECA(rule, generation)

    eca = np.array(eca)
    #print(eca)
    
    plt.imshow(eca, cmap="gray_r") 
    plt.show()

if __name__ == "__main__":
    mainMenu()