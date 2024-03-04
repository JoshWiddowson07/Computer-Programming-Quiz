print("Welcome to Josh's Computer programming Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Ok! let's play")
score = 0

answer = input("1. What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("2. What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("3. What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("4. What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("5. What language is primarily used for web development? ")
if answer.lower() == "html":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("6. What does CSS stand for in web development? ")
if answer.lower() == "cascading style sheets":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("7. Which programming language beginning with J is often used for building mobile applications? ")
if answer.lower() == "javascript":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("8. What does SQL stand for? ")
if answer.lower() == "structured suery language":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("9. What does the acronym API stand for? ")
if answer.lower() == "application programming interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("10. What does the acronym IDE stand for in programming? ")
if answer.lower() == "integrated development environment":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")                             
    
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100 ) + "%. ")
