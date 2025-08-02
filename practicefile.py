import random
def game():
    print("Welcome to the game!")
    score=random.randint(1, 62)
    with open("hi-score.txt", "r") as f:
        hiscore = f.read() #string ke form me aata hai
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score is: {score}")
    if(score>hiscore ):
        #write this hi score in hi score.txt
        with open("hi-score.txt", "w") as f:
            f.write(str(score))
        return score
game()               