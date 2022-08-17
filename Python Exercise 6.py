import os

# Steps 1 and 2
f = open("reflection.txt", "r")
print(f.read())

# Step 3
f = open("reflection.txt", "r")
print(f.readline())

# Step 4
f = open("reflection.txt", "r")
for i in f:
    print(i)

f.close()

# Step 5
if os.path.exists("reflection.txt"):
    os.remove("reflection.txt")
else:
    print("This file does not exist")