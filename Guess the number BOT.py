from random import randint

player_record = 100
bot_record = 100

name = input("Enter your name: ")
if name == "Dima K":
    print("Hi creator!")
else:
     print(f"Hi {name}")
     
while True:
  print("Who will guess?")
  game_mod = input("Enter -me-, or -you-, or -stop-: ")
  if game_mod == "me":
    hidden_number = randint(1,100)
    player_attemps = 0 
    print("I thought of a number between 1 and 100")
    while True:
      player_attemps = player_attemps + 1
      player_gues = int(input("Insert the number: "))
      if player_gues > hidden_number:
        print(f"I thought of a number less than {player_gues}")
      elif player_gues < hidden_number:
        print(f"I thought of a number bigger than {player_gues}")
      elif player_gues == hidden_number:
        print("Yes")
        print(f"You guess the number in {player_attemps} attemps")
        if player_attemps < player_record:
          print("It's a new record 🥳")
          break
          player_record = player_attemps 
      else:
        print("I don't understand 🤔")
  elif game_mod == "you":
    print("Guess the number and write -start- when you ready ")
    start_guess = input()
    if(start_guess == "start"):
      player_number_top = 100
      player_number_bottom = 0
      bot_attemps = 0
      while True:
        print(f"The number you thought of is {round((player_number_top + player_number_bottom)/2)}?")
        player_answer = input("Write -yes- or -smaller-, or -bigger- ")
        bot_attemps = bot_attemps + 1
        if player_answer == "yes":
          print("YaaaaY 🥳")
          print(f"I did it in  {bot_attemps} attempts")
          if bot_attemps < bot_record:
            print("It's my new record 🎉")
            break
        elif player_answer == "smaller":
          player_number_top = round((player_number_top + player_number_bottom)/2)
        elif player_answer == "bigger":
          player_number_bottom = round((player_number_top + player_number_bottom)/2)
        else:
          print("I don't understand 🤔")
    else:
      print("I don't understand 🤔")
  elif game_mod == "stop":
    break
  else: 
    print("I don't understand you 🤔")
print("Thank you for playing with me🤠")