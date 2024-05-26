print("Welcome to my Computer Quiz!")
playing = input("Do you want to play Game? ")
if playing.lower() != "yes":
    quit()
print("OK! lets paly :)")
score = 0


answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

    
answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("What does ROM stands for? ")
if answer.lower() == "read only memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("What does PSU stands for? ")
if answer.lower() == "power supply unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    
print(f" You got {str(score)} questions correct!")
print(f" You got {str(score/4 * 100)}%.")


























