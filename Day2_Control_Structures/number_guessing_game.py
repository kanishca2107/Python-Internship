import random
print("welcome to the number guessing game")
while True:
    secret_number = 5
    attempt = 7
    attempt -=1
    print("\choose your levels🔥")
    print("1.easy(1-10)")
    print("2.medium(1-50)")
    print("3.hard(1-100)")
    level = int(input("enter your choice😉: "))
    if level == 1:
        secret_number = random.randint(1,10)
    elif level == 2:
        secret_number = random.randint(1,50)
    elif level == 3:
        secret_number = random.randint(1,100)
    else:
        print("invalid choice try again later")
    guess=int(input("enter your guessed value: "))
    if guess == secret_number:
        print("yes you achieved your target")
    if attempt == 1:
        print("mass performance🔥")
    if attempt <= 3:
        print("excellent👍")
    else:
        print("good try")

    print("THANK YOU VISIT AGAIN😊")

