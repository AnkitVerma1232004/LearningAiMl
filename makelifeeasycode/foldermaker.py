import os

path = "C:/Users/anime/OneDrive/Desktop/Apna college Prime 2.0/Assignments"

c = 1

while True:
    f = "Assignment " + str(c)
    p = os.path.join(path, f)
    
    if not os.path.exists(p):
        os.mkdir(p)
        print("Created:", f)
        break
    
    c += 1