f = open("reflection.txt", "w")
f.write("What do I like about learning Python? \nSometimes, there are more efficient ways of doing things in Python that cannot be done in other programming languages.")

f = open("reflection.txt", "a")
f.write("\nWhat do I plan to do after learning Python? \nEven after I finish this course, I'll keep learning about the way Python works.")
f.write("\nHow do I apply what I've learned? \nWhen I find a job, I can apply the lessons I've learned there.")
f.write("\nWhat are my goals? \nMy main goal is to have a skill level equal to my dad's.")

f = open("reflection.txt", "r")
print(f.read())
f.close()