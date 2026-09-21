import time
YES = "y"
NO = "n"
QUIZ_CHOICE_A = "a"
QUIZ_CHOICE_B = "b"
QUIZ_CHOICE_C = "c"
QUIZ_CHOICE_D = "d"
QUIZ_QUESTIONS_MIN = 1
QUIZ_QUESTIONS_MAX = 10
MATHEMATICS = "mathematics"
SCIENCE = "science"
QUIZ_OPTION_1 = "1"
QUIZ_OPTION_2 = "2"
ACHIEVED_PERCENTAGE_MIN = 0.60
ACHIEVED_PERCENTAGE_MAX = 0.74
MERIT_PERCENTAGE_MIN = 0.75
MERIT_PERCENTAGE_MAX = 0.89
EXCELLENCE_PERCENTAGE_MIN = 0.90
EXCELLENCE_PERCENTAGE_MAX = 1

# Mathematics quiz questions
MATHEMATICS_QUESTIONS = [
    "1. Expand: (x - 8)²:   \n \na) x² - 16x + 64   \nb) x³ - 24x + 128   \nc) a² + b² = c²   \nd) (x - 8)(x + 8)",
    "2. Simplify: 7x(y + x):  \n \na) 7xy²   \nb) 7y + 5x   \nc) 7xy + 7x²   \nd) (10y²) + 8y",
    "3. Simplify: 3a(2a-4) - 2(7-a):  \n \na) 4a² - 8a - 12   \nb) 7a - 12a - 14   \nc) 31a² + 12a -11 \nd) 6a² - 10a - 14",
    "4. Solve for x: 5(x - 3) = 25:  \n \na) x = 5   \nb) x = 8   \nc) x = 4   \nd) x = 10",
    "5. Solve for y: 5y + 3 = 4y - 2:  \n \na) y = 10   \nb) y = -5   \nc) y = -8   \nd) y = 8",
    "6. What do the interior angles of a triangle sum to:  \n \na) 120   \nb) 160   \nc) 270   \nd) 180",
    "7. What is equation for the Pythagorean theorem:  \n \na) a² + b² = c2²   \nb) a² - c = b²   \nc) c² * a² = 5²   \nd) a + b = c",
    "8. Simplify: x³ * x⁵:  \n \na) x⁷   \nb) x = 8   \nc) x⁸   \nd) 8x",
    "9. Simplify: 3y(5x + 2x + 4y):  \n \na) 21xy + 12y²   \nb) 14xy + 6x²   \nc) 12x + 12xy   \nd) 9xy + 16³",
    "10. Find the area of the circle to 2 dp: r = 6 cm:  \n \na) a = 37.70 cm²   \nb) a = 113.10 cm²   \nc) a = 18.85 cm²   \nd) a = 150.80 cm²"
]

# Mathematics quiz answers
MATHEMATICS_ANSWERS = [
    "a",
    "c",
    "d",
    "b",
    "b",
    "d",
    "a",
    "c",
    "a",
    "b"
]

# Science quiz questions
SCIENCE_QUESTIONS = [
    "1. How many covalent does Oxygen have?:  \n \na) 1   \nb) 2   \nc) 3   \nd) 4",
    "2. Which factor will increase the rate of a chemical reaction?:  \n \na) Lower temperature \nb) Smaller surface area \nc) Higher concentration of reactants \nd) Removing a catalyst",
    "3. Why does increasing temperature speed up a reaction?:  \n \na) Particles move slower   \nb) Particles have more energy and collide more often   \nc) It reduces the number of collisions   \nd) It removes activation energy",
    "4. What is the role of a catalyst in a reaction?:   \n \na) To increase the mass of products   \nb) To lower activation energy   \nc) To slow down the reaction   \nd) To increase concentration",
    "5. Where does most digestion and absorption occur?:   \n \na) Small intestine    \nb) Large intestine    \nc) Stomach    \nd) Oesophagus",
    "6. What is the main function of the stomach?:   \n \na) Absorb nutrients   \nb) Produce bile   \nc) Mix food with acid and enzymes   \nd) Store waste",
    "7. Which organ produces bile?:   \n \na) Pancreas   \nb) Liver   \nc) Gallbladder   \nd) Small intestine",
    "8. What is the role of enzymes in digestion?:   \n \na) To slow down digestion   \nb) To absorb nutrients   \nc)To move food through the body    \nd) To break down large molecules into smaller ones",
    "9. Which part of the digestive system absorbs most water?:   \n \na) Large intestine   \nb) Stomach   \nc) Oesophagus   \nd) Small intestine",
    "10. Which part of the heart pumps oxygenated blood to the body?:   \n \na) Right atrium   \nb) Right ventricle   \nc) Left atrium   \nd) Left ventricle"
]

# Science quiz answers
SCIENCE_ANSWERS = [
    "b",
    "c",
    "b",
    "b",
    "a",
    "c",
    "b",
    "d",
    "a",
    "d"
]

print("Welcome to the study quiz for year 11 MAGS students")

#Main loop
while True:
    score = 0
    # User chooses a subject
    while True:
        print()
        print("Your subject options are: ")
        print("Mathematics")
        print("Science")
        subject_chosen = input("Please choose a subject you would like to study: ").lower()

        # Checks if the chosen subejct is valid
        if subject_chosen != MATHEMATICS and subject_chosen != SCIENCE:
            print()
            print("That is not a valid subject. Please try again")
            continue
        else: 
            break
    
    if subject_chosen == MATHEMATICS:
        questions = MATHEMATICS_QUESTIONS
        answers = MATHEMATICS_ANSWERS
    elif subject_chosen == SCIENCE:
        questions = SCIENCE_QUESTIONS
        answers = SCIENCE_ANSWERS

    # Asks user to choose an option and checks if it's valid
    while True:
        print()
        print("What would you like to do?")
        print("Options:")
        print("1. Study the entire quiz")
        print("2. Specific question")
        option = input("Please choose an option: ")
        
        if option != QUIZ_OPTION_1 and option != QUIZ_OPTION_2:
            print()
            print("That isn't an option! Please try again")
            continue
        else:
            break

    # Entire quiz option
    if option == QUIZ_OPTION_1:
        starting_time = time.time()
        question_count = 0
        
        # Loops through for every question in the question list
        for question in questions:
            print()
            print(question)

            # Asks user to chose an answer and checks if it was valid
            while True:
                print()
                user_answer = input("Choose the answer: ").lower()
                if (user_answer != QUIZ_CHOICE_A
                    and user_answer != QUIZ_CHOICE_B
                    and user_answer != QUIZ_CHOICE_C
                    and user_answer != QUIZ_CHOICE_D):
                    print()
                    print("That is not a valid answer! Please try again")
                    continue
                
                else:
                    break

            # Checks if the user entered the incorrect answer
            if user_answer != answers[question_count]:
                print("Incorect")
                print(f"The answer was {answers[question_count]}")

            # Otherwise the user is correct
            else:
                print("Correct!")
                score += 1
                print("Your score increased by 1")
            question_count += 1

        print()
        print(f"You scored {score}/{QUIZ_QUESTIONS_MAX}")
        percentage_correct_decimal = score/QUIZ_QUESTIONS_MAX
        print(f"That is {percentage_correct_decimal * 100}%")

        # Gives the user a specified grade based percentage scored
        if percentage_correct_decimal >= ACHIEVED_PERCENTAGE_MIN and percentage_correct_decimal <= ACHIEVED_PERCENTAGE_MAX:
            print()
            print("You got an achieved!")
            print("Well done!")
        elif percentage_correct_decimal >= MERIT_PERCENTAGE_MIN and percentage_correct_decimal <= MERIT_PERCENTAGE_MAX:
            print()
            print("You got a merit!")
            print("Well done!")
        elif percentage_correct_decimal >= EXCELLENCE_PERCENTAGE_MIN and percentage_correct_decimal <= EXCELLENCE_PERCENTAGE_MAX:
            print()
            print("You got an excellence")
            print("Well done!")
        else:
            print()
            print("You got not achieved")
            print("You should keep studying")

        ending_time = time.time()
        time_taken_float = ending_time - starting_time
        time_taken_rounded = round(time_taken_float, 1)
        print(f"It took you {time_taken_rounded} seconds for you to complete the quiz")
        
    #Choosing specific question
    elif option == QUIZ_OPTION_2:
        #Asks user to choose a question and checks if it is valid
        while True:
            print()
            print("What question do you want to study")
            print(f"Your options range between {QUIZ_QUESTIONS_MIN}-{QUIZ_QUESTIONS_MAX}")
            
            try:
                question_asking = int(input("Please choose a question: "))
            except ValueError:
                print()
                print("That is not a valid question")
                continue
            
            if question_asking < QUIZ_QUESTIONS_MIN or question_asking > QUIZ_QUESTIONS_MAX:
                print()
                print("That is not a valid question")
                continue
            else:
                break

        print()
        print(questions[question_asking - 1])
    
        # Asks user to chose an answer and checks if it was valid
        while True:
            print()
            user_answer = input("Choose the answer: ").lower()
            if (user_answer != QUIZ_CHOICE_A
                and user_answer != QUIZ_CHOICE_B
                and user_answer != QUIZ_CHOICE_C
                and user_answer != QUIZ_CHOICE_D):
                print()
                print("That is not a valid option! Please try again")
                continue
            
            else:
                break

        #Checks if the user entered the correct answer
        if user_answer != answers[question_asking-1]:
                print("Incorect")
                print(f"The answer was {answers[question_asking-1]}")

        else:
            print("Correct!")

    # Asks if the user wants to play again
    while True:
        print()
        replay = input("Do you want to play again (y/n)?: ").lower()
        
        if replay != YES and replay != NO:
            print()
            print("That is not a valid option")
            continue
        
        else:
            break

    if replay == NO:
        print()
        print("Thank you for studying!")
        break