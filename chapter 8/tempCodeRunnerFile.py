if (score > int(c)):
    f = open("chapter 8/Hi_score.txt", "w") 
    f.write(str(score))
    f.close()
else:
    print(c)