import random
actual_number = random.randint(1,100)
while True:
    try:
        guessing_number = int(input("Guess a number "))
          
        if guessing_number > actual_number:
           print("Too High")
        elif guessing_number < actual_number:   
           print("Too Low")
        else:
           print("Invalid")
    except ValueError:
        print("Invalid input")    

    
 