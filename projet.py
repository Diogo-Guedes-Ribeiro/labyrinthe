import random

def display_map(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if j != len(M[0]) - 1:
                print(M[i][j], end="")
            else:
                print(M[i][j])
display_map([[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]])

def display_map(M, d):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if j != len(M[0]) - 1:
                print(d[M[i][j]], end="")
            else:
                print(d[M[i][j]])
display_map([[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]], {0:' ', 1:'#'})

def create_perso(départ):
    d = {}
    d["char"] = "o"
    d["x"] = départ[0]
    d["y"] = départ[1]
    print(d)
create_perso((0, 0))

def display_map_and_char(M, d, p):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if (i, j) == (p["x"], p["y"]):
                if j != len(M[0]) - 1:
                    print(p["char"], end="")
                else:
                    print(p["char"])
            else:
                if j != len(M[0]) - 1:
                    print(d[M[i][j]], end="")
                else:
                    print(d[M[i][j]])
display_map_and_char([[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]], {0:' ', 1:'#'}, {"char":"o", "x":0, "y":0})

def update_p(letter, p, m, d):
    if letter == "z":
        if 0 <= p["x"]-1 and d[m[p["x"]-1][p["y"]]] != '#':
            p["x"] -= 1
    elif letter == "q":
        if 0 <= p["y"] - 1 and d[m[p["x"]][p["y"]-1]] != '#':
            p["y"] -= 1
    elif letter == "s":
        if p["x"] + 1 < len(m) and d[m[p["x"]+1][p["y"]]] != '#':
            p["x"] += 1
    elif letter == "d" and d[m[p["x"]][p["y"]+1]] != '#':
        if p["y"] + 1 < len(m[0]):
            p["y"] += 1

m = [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
p = {"char":"o", "x":0, "y":0}
d = {0:' ', 1:'#'}
while True: 
    letter = input("Quel déplacement ?")
    update_p(letter, p, m, d)
    display_map_and_char([[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]], d, p)