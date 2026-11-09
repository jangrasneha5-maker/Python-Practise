#  Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’.

# f=open("chapter 8/poem.txt")
# c=f.read()

# if("sneha" in c):
#     print("twinkle is present")
# else:
#     print("aap dumb hai")

# f.close()

#  The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi
# score whenever the game() function breaks the Hi-score.

f=open("chapter 8/Hi_score.txt")
c=f.read()
f.close()

def game():
    score=int(input("Enter your score:"))
    return score

score=game()
if (score > int(c)):
    f = open("chapter 8/Hi_score.txt", "w") 
    f.write(str(score))
    f.close()
else:
    print(c)

# if (c == "" or score > int(c)):
#     print("Writing to file...") # Add this to see if the code enters here
#     f = open("chapter 8/Hi_score.txt", "w")
#     f.write(str(score))
#     f.close()
#     print("Done!")
# else:
#     print("Score not high enough.")





