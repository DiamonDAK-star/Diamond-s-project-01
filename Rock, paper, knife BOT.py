from random import randint

wins = 0
loses = 0
draws = 0
  
name = input("Enter your name: ")
if name == "Dima K":
    print("Hi creator!")
else:
     print(f"Hi {name}")
     
while True:
  print("What you want to do?")
  game_mod = input("Write -play-, -statistic- or -stop-: ")
  if game_mod == "play":
    player = input("Write -rock-, -paper- or -knife-: ")
    if player == "rock" or player == "paper" or player == "knife":
      results = randint(1,3)
      if results == 1:
        print("Draw")
        draws+=1
      elif results == 2:
        print("You lose 😔")
        loses+=1
      elif results == 3:
        print("You win 🎉")
        wins+=1
    elif player == "gun":
      print("You win 🎉")
      wins+=1
    else:
      print("I don't understand you🤔")
  elif game_mod == "statistic":
    print(f"You played {wins + loses + draws} games")
    print(f"You win {wins} games")
    print(f"You lose {loses} games")
  elif game_mod == "stop": 
    break
  else:
    print("I don't understand you🤔")
print("Thank you for playing with me🤠")