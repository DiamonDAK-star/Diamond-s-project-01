from random import randint
import time

question = 0
dif_1_record = 100
dif_2_record = 100
dif_3_record = 100
dif_4_record = 100
dif_5_record = 100
all_dif_1_record = 1000
all_dif_2_record = 1000
all_dif_3_record = 1000
all_dif_4_record = 1000
all_dif_5_record = 1000

name = input("Enter your name: ")
if name == "Dima K":
    print("Hi creator!")
else:
     print(f"Hi {name}")

while True:
    print("What you want to do?")
    game_mod = input("Write -play-, -statistic- or -stop-: ")
    if game_mod == "play":
        # Выбор сложности
        print(" Game Difficulty 1: Addition and subtraction")
        print("Game Difficulty 2: Multiplying numbers up to 10")
        print("Game Difficulty 3: Dividing numbers up to 10")
        print("Game Difficulty 4: Multiplication, addition, and subtraction")
        print("Game Difficulty 5: All actions")
        difficulty = int(input("Choose difficulty: "))
        # Сложность 1
        if difficulty == 1:
            question = 1
            all_start_time = time.time()
            for question in range (1,16):
                print(f"Question {question}/15")
                what_to_do = randint(1,2)
                rand_number_1 = randint(1,25)
                rand_number_2 = randint(1,25)
                if what_to_do == 1:
                    correct_answer = rand_number_1 + rand_number_2
                    start_time = time.time()
                    answer = int(input(f"What was {rand_number_1} + {rand_number_2}? "))
                    if answer == "stop":
                      print("To ma byc numer")
                    elif answer.isdigit() != True:
                      break
                    else:
                      while answer != correct_answer:
                        print("Wrong!")
                        answer = int(input(f"What was {rand_number_1} + {rand_number_2}? "))

                else:
                    correct_answer = rand_number_1 - rand_number_2
                    start_time = time.time()
                    answer = input(f"What was {rand_number_1} - {rand_number_2}? ")
                    if answer == "stop":
                      break
                    elif answer.isdigit() != True:
                      print("To ma byc numer")
                    else:
                      while answer != correct_answer:
                        print("Wrong!")
                        answer = input(f"What was {rand_number_1} - {rand_number_2}? ")
                end_time = time.time()
                print("Correct!")
                elapsed_time = end_time - start_time
                if elapsed_time < dif_1_record:
                    print("It`s a new speed record!")
                    dif_1_record = elapsed_time
                question += 1
            all_end_time = time.time()
            all_elapsed_time = all_end_time - all_start_time
            if all_elapsed_time < all_dif_1_record:
                    print("It`s a new summmary speed record!")
                    all_dif_1_record = all_elapsed_time
        # Сложность 2
        elif difficulty == 2:
            question = 1
            all_start_time = time.time()
            for question in range (1,16):
                print(f"Question {question}/15")
                rand_number_1 = randint(1,10)
                rand_number_2 = randint(1,10)
                correct_answer = rand_number_1 * rand_number_2
                start_time = time.time()
                answer = int(input(f"What was {rand_number_1} * {rand_number_2}? "))
                if answer == "stop":
                      break
                elif answer.isdigit() != True:
                      print("To ma byc numer")
                else:
                  while answer != correct_answer:
                    print("Wrong!")
                    answer = int(input(f"What was {rand_number_1} * {rand_number_2}? "))
                end_time = time.time()
                print("Correct!")
                elapsed_time = end_time - start_time
                if elapsed_time < dif_2_record:
                    print("It`s a new speed record!")
                    dif_2_record = elapsed_time
                question += 1
            all_end_time = time.time()
            all_elapsed_time = all_end_time - all_start_time
            if all_elapsed_time < all_dif_2_record:
                    print("It`s a new summmary speed record!")
                    all_dif_2_record = all_elapsed_time
        # Сложность 3
        elif difficulty == 3:
            question = 1
            all_start_time = time.time()
            for question in range (1,16):
                rand_number_1 = randint(1,10)
                rand_number_2 = randint(1,10)
                correct_answer = rand_number_1
                start_time = time.time()
                answer = int(input(f"What was {rand_number_1 * rand_number_2} / {rand_number_2}? "))
                if answer == "stop":
                      break
                elif answer.isdigit() != True:
                    print("To ma byc numer")
                else:
                  while answer != correct_answer:
                    print("Wrong!")
                    answer = int(input(f"What was {rand_number_1 * rand_number_2} / {rand_number_2}? "))
                end_time = time.time()
                print("Correct!")
                elapsed_time = end_time - start_time
                if elapsed_time < dif_3_record:
                    print("It`s a new speed record!")
                    dif_3_record = elapsed_time
                question += 1
            all_end_time = time.time()
            all_elapsed_time = all_end_time - all_start_time

            if all_elapsed_time < all_dif_3_record:
                print("It`s a new summmary speed record!")
                all_dif_3_record = all_elapsed_time
        # Сложность 4
        elif difficulty == 4:
            question = 1
            all_start_time = time.time()
            for question in range (1,16):
                print(f"Question {question}/15")
                what_to_do = randint(1,2)
                rand_number_1 = randint(1,25)
                rand_number_2 = randint(1,25)
                if what_to_do == 1:
                    correct_answer = rand_number_1 + rand_number_2
                    start_time = time.time()
                    answer = int(input(f"What was {rand_number_1} + {rand_number_2}? "))
                    if answer == "stop":
                      break
                    elif answer.isdigit() != True:
                      print("To ma byc numer")
                    else:
                      while answer != correct_answer:
                        print("Wrong!")
                        answer = int(input(f"What was {rand_number_1} + {rand_number_2}? "))

                elif what_to_do == 2:
                    correct_answer = rand_number_1 - rand_number_2
                    start_time = time.time()
                    answer = int(input(f"What was {rand_number_1} - {rand_number_2}? "))
                    if answer == "stop":
                      break
                    elif answer.isdigit() != True:
                      print("To ma byc numer")
                    else:
                      while answer != correct_answer:
                        print("Wrong!")
                        answer = int(input(f"What was {rand_number_1} - {rand_number_2}? "))
                else:
                    correct_answer = rand_number_1 * rand_number_2
                    start_time = time.time()
                    answer = int(input(f"What was {rand_number_1} * {rand_number_2}? "))
                    if answer == "stop":
                      break
                    elif answer.isdigit() != True:
                      print("To ma byc numer")
                    else:
                      while answer != correct_answer:
                        print("Wrong!")
                        answer = int(input(f"What was {rand_number_1} * {rand_number_2}? "))

                end_time = time.time()
                print("Correct!")
                elapsed_time = end_time - start_time
                if elapsed_time < dif_1_record:
                    print("It`s a new speed record!")
                    dif_1_record = elapsed_time
                question += 1

            all_end_time = time.time()
            all_elapsed_time = all_end_time - all_start_time
            if all_elapsed_time < all_dif_4_record:
                    print("It`s a new summmary speed record!")
                    all_dif_4_record = all_elapsed_time
        # Сложность 5
        elif difficulty == 5:
            question = 1
            all_start_time = time.time()
            for question in range (1,16):
                print(f"Question {question}/15")
                what_to_do = randint(1,2)
                rand_number_1 = randint(1,25)
                rand_number_2 = randint(1,25)
                if what_to_do == 1:
                    correct_answer = rand_number_1 + rand_number_2
                    start_time = time.time()
                    answer = int(input(f"What was {rand_number_1} + {rand_number_2}? "))
                    if answer == "stop":
                      break
                    elif answer.isdigit() != True:
                      print("To ma byc numer")
                    else:
                        while answer != correct_answer:
                          print("Wrong!")
                          answer = int(input(f"What was {rand_number_1} + {rand_number_2}? "))

                elif what_to_do == 2:
                    correct_answer = rand_number_1 - rand_number_2
                    start_time = time.time()
                    answer = int(input(f"What was {rand_number_1} - {rand_number_2}? "))
                    if answer == "stop":
                      break
                    elif answer.isdigit() != True:
                      print("To ma byc numer")
                    else:
                      while answer != correct_answer:
                          print("Wrong!")
                          answer = int(input(f"What was {rand_number_1} - {rand_number_2}? "))
                elif what_to_do == 3:
                    correct_answer = rand_number_1 * rand_number_2
                    start_time = time.time()
                    answer = int(input(f"What was {rand_number_1} * {rand_number_2}? "))
                    if answer == "stop":
                      break
                    elif answer.isdigit() != True:
                      print("To ma byc numer")
                    else:
                      while answer != correct_answer:
                          print("Wrong!")
                          answer = int(input(f"What was {rand_number_1} * {rand_number_2}? "))
                else:
                    correct_answer = rand_number_1
                    start_time = time.time()
                    answer = int(input(f"What was {rand_number_1 * rand_number_2} / {rand_number_2}? "))
                    if answer == "stop":
                      break
                    elif answer.isdigit() != True:
                      print("To ma byc numer")
                    else:
                      while answer != correct_answer:
                          print("Wrong!")
                          answer = int(input(f"What was {rand_number_1 * rand_number_2} / {rand_number_2}? "))

                end_time = time.time()
                print("Correct!")
                elapsed_time = end_time - start_time
                if elapsed_time < dif_1_record:
                    print("It`s a new speed record!")
                    dif_1_record = elapsed_time
                question += 1

            all_end_time = time.time()
            all_elapsed_time = all_end_time - all_start_time
            if all_elapsed_time < all_dif_5_record:
                    print("It`s a new summmary speed record!")
                    all_dif_5_record = all_elapsed_time
        # Защита от неправильного ввода
        else:
            print("I don't understand you🤔")

    elif game_mod == "statistic":
        print("For difficulty 1:")
        print(f"Your record for 1 question is: {dif_1_record}")
        print(f"Your record for all questions: {all_dif_1_record}")
        print("For difficulty 2:")
        print(f"Your record for 1 question is: {dif_2_record}")
        print(f"Your record for all questions: {all_dif_2_record}")
        print("For difficulty 3:")
        print(f"Your record for 1 question is: {dif_3_record}")
        print(f"Your record for all questions: {all_dif_3_record}")
        print("For difficulty 4:")
        print(f"Your record for 1 question is: {dif_5_record}")
        print(f"Your record for all questions: {all_dif_5_record}")
        print("For difficulty 5:")
        print(f"Your record for 1 question is: {dif_5_record}")
        print(f"Your record for all questions: {all_dif_5_record}")
        print("Greate job!")
    elif game_mod == "stop":
        break
    else:
        print("I don't understand you🤔")
print("Thank you for playing with me🤠")