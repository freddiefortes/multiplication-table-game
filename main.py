import os
import sys
import time
import datetime
import random

name = ""
level = 1
score_total = 0
save = {}

def color(color):
  if color == "d":
    return "\033[0m"
  elif color == "r":
    return "\033[31m"
  elif color == "g":
    return "\033[32m"
  elif color == "y":
    return "\033[33m"
  elif color == "b":
    return "\033[34m"
  elif color == "p":
    return "\033[35m"
  elif color == "c":
    return "\033[36m"

title = f'\t\t\t{color("p")}MULTIPLICATION TABLE GAME{color("d")}\n\n\n'

bonus_title = f'\t\t\t{color("r")}BONUS ROUND!{color("d")}\n\n'

final_title = f'\t\t\t{color("r")}FINAL ROUND{color("d")}\n\n'

def level_title():
  global level
  print(f'\t\t\t{color("r")}LEVEL {level}{color("d")}\n\n')

menu_main = f"""\t\t{color("c")}MENU

1: NEW GAME
2: LOAD GAME
3: CREDITS
4: EXIT

> {color("d")}"""

menu_lvl = f"""\t\t{color("c")}SELECT

1: NEXT LEVEL
2: RETURN TO MAIN MENU

> {color("d")}"""

menu_retry = f"""\t\t{color("c")}SELECT

1: RESTART LEVEL
2: RETURN TO MAIN MENU

> {color("d")}"""

def pre_load():
  global save
  maindir = os.listdir()
  if "backup" not in maindir:
    os.mkdir("backup")
  if "save.txt" not in maindir:
    f = open("save.txt", "w")
    f.close
  else:
    f = open("save.txt", "r")
    try:
      save = eval(f.read())
      f.close()
    except SyntaxError:
      save = {}

def load():
  global name, level, score_total, save
  if save == {}:
    print("No save file found.\n")
    select_main()
  else:
    list = save.keys()
    for key, row in save.items():
      print(f'{key:<7}.......{row["score"]:>7}')
    user = input("\nLoad game: ").title()
    print()
    if user in list:
      name = user
      level = save[user]["level"]
      score_total = save[user]["score"]
    else:
      print("Game not found.\n")
      select_main()

def top_scores():
  global save
  print(f'\t\t{color("r")}TOP SCORES\n')
  counter = 0
  for key in save.keys():
    print(f'{key:<7}.......{save[key]["score"]:>7}')
    counter += 1
    if counter == 3:
      break
  print(f'\n\n{color("d")}')

def backup():
  file_name = f"backup{datetime.datetime.now()}.txt"
  file_path = os.path.join("backup/", file_name)
  os.rename("save.txt", file_path)

def saving():
  backup()
  global name, level, score_total, save
  save[name] = {"level": level, "score": score_total}
  pre_save = sorted(save.items(), key=lambda x: x[1]["score"], reverse=True)
  new_save = {}
  for key, value in pre_save:
    new_save[key] = value
  f = open("save.txt", "w")
  f.write(str(new_save))
  f.close()

def credits():
  os.system("clear")
  print("""
........................................................

                        CREDITS

........................................................

    Created by Freddie Fortes (@Freddie_Fortes at 𝕏)
........................................................

                                  To my beloved daugther
........................................................
""")
  time.sleep(7)
  os.system("clear")

def select_main():
  while True:
    time.sleep(3)
    os.system("clear")
    global name, level, score_total, save
    pre_load()
    print(title)
    top_scores()
    select = input(menu_main)
    print()
    if select == "1":
      while True:
        name = input("Insert your name: ").title()
        list = save.keys()
        if name in list:
          print("\nName already taken. Chose another one.\n")
        else:
          saving()
          break
      lvl1()
    elif select == "2":
      load()
      select_level()
    elif select == "3":
      credits()
    elif select == "4":
      print("bye!\n")
      exit()
    else:
      print("\nOops. Something went wrong. Please, select a valid option.\n\nTry again:\n")

def select_level():
  saving()
  while True:
    time.sleep(3)
    select = input(menu_lvl)
    print()
    if select == "1":
      if level == 1:
        lvl1()
      elif level == 2:
        lvl2()
      elif level == 2.5:
        lvl2_bonus()
      elif level == 3:
        lvl3()
      elif level == 4:
        lvl4()
      elif level == 5:
        lvl5()
      elif level == 6:
        lvl6()
      elif level == 7:
        lvl7()
      elif level == 7.5:
        lvl7_bonus()
      elif level == 8:
        lvl8()
      elif level == 9:
        lvl9()
      elif level == 10:
        lvl10()
      elif level == 11:
        final_round()
      elif level == 12:
        final_bonus()
    elif select == "2":
      select_main()
    else:
      print("\nOops. Something went wrong. Please, select a valid option.\n\nTry again:\n")

def retry():
  saving()
  while True:
    time.sleep(3)
    select = input(menu_retry)
    print()
    if select == "1":
      if level == 1:
        lvl1()
      elif level == 2:
        lvl2()
      elif level == 2.5:
        lvl2_bonus()
      elif level == 3:
        lvl3()
      elif level == 4:
        lvl4()
      elif level == 5:
        lvl5()
      elif level == 6:
        lvl6()
      elif level == 7:
        lvl7()
      elif level == 7.5:
        lvl7_bonus()
      elif level == 8:
        lvl8()
      elif level == 9:
        lvl9()
      elif level == 10:
        lvl10()
      elif level == 11:
        final_round()
      elif level == 12:
        final_bonus()
    elif select == "2":
      select_main()
    else:
      print("\nOops. Something went wrong. Please, select a valid option.\n\nTry again:\n")

def the_end():
  saving()
  time.sleep(3)
  os.system("clear")
  print(f'{title}\t\t\t{color("p")}YOU WON!\n\n\t\t\tCONGRATULATIONS!\n\n\t\t\tYOUR FINAL SCORE IS {score_total}!{color("d")}\n')
  time.sleep(7)
  credits()
  select_main()

def random_list():
  list = []
  for index in range(13):
    while True:
      number = random.randint(0, 12)
      if number not in list:
        list.append(number)
        break
  return list

def scramble_list(pre_list):
  list = []
  for index in range(len(pre_list)):
    while True:
      number = random.choice(pre_list)
      if number not in list:
        list.append(number)
        break
  return list

def grade(score, max):
  percentile = int(round(score / max * 100))
  if percentile >= 97:
    return "A+"
  if percentile >= 93:
    return "A"
  if percentile >= 90:
    return "A-"
  elif percentile >= 87:
    return "B+"
  elif percentile >= 83:
    return "B"
  elif percentile >= 80:
    return "B-"
  elif percentile >= 77:
    return "C+"
  elif percentile >= 73:
    return "C"
  elif percentile >= 70:
    return "C-"
  elif percentile >= 67:
    return "D+"
  elif percentile >= 63:
    return "D"
  elif percentile >= 60:
    return "D-"
  else:
    return "F"

def lvl1():
  global level
  global score_total
  score_lvl1 = 0
  max_lvl1 = 2 * 12 * 100
  os.system("clear")
  print(title)
  level_title()
  for multiple in range(2, 4):
    for number in range(1, 13):
      answer = multiple * number
      equation = f"{multiple} x {number} = "
      while True:
        try:
          guess = int(input(equation))
          if guess == answer:
            score_lvl1 += 100
            sys.stdout.write(f'\033[F{equation}{guess} ⭐\n\n')
            break
          else:
            sys.stdout.write(f'\033[F{equation}{guess} ❌ ({equation}{answer})\n\n')
            break
        except ValueError:
          print("\nOops. Something went wrong. Please, select only numbers.\n\nTry again:\n")
  print(f"SCORE: {score_lvl1}!\n")
  print(f"Grade: {grade(score_lvl1, max_lvl1)}\n")
  if (score_lvl1 / max_lvl1) < 0.6:
    print("You failed. Try again.\n")
    retry()
  else:
    score_total += score_lvl1
    level = 2
    select_level()

def lvl2():
  global level
  global score_total
  score_lvl2 = 0
  max_lvl2 = 2 * 13 * 200
  multiple_list = [5, 10]
  os.system("clear")
  print(title)
  level_title()
  for multiple in multiple_list:
    for number in range(13):
      answer = multiple * number
      equation = f"{multiple} x {number} = "
      while True:
        try:
          guess = int(input(equation))
          if guess == answer:
            score_lvl2 += 200
            sys.stdout.write(f'\033[F{equation}{guess} ⭐\n\n')
            break
          else:
            sys.stdout.write(f'\033[F{equation}{guess} ❌ ({equation}{answer})\n\n')
            break
        except ValueError:
          print("\nOops. Something went wrong. Please, select only numbers.\n\nTry again:\n")
  print(f"SCORE: {score_lvl2}!\n")
  print(f"Grade: {grade(score_lvl2, max_lvl2)}\n")
  if (score_lvl2 / max_lvl2) < 0.6:
    print("You failed. Try again.\n")
    retry()
  else:
    score_total += score_lvl2
    level = 2.5
    select_level()

def lvl2_bonus():
  global level
  global score_total
  score_lvl2_bonus = 0
  max_lvl2_bonus = 1 * 13 * 100
  os.system("clear")
  print(title)
  print(bonus_title)
  for multiple in range(13):
    number = multiple
    answer = multiple * number
    equation = f"{multiple} x {number} = "
    while True:
      try:
        guess = int(input(equation))
        if guess == answer:
          score_lvl2_bonus += 100
          sys.stdout.write(f'\033[F{equation}{guess} ⭐\n\n')
          break
        else:
          sys.stdout.write(f'\033[F{equation}{guess} ❌ ({equation}{answer})\n\n')
          break
      except ValueError:
        print("\nOops. Something went wrong. Please, select only numbers.\n\nTry again:\n")
  print(f"SCORE: {score_lvl2_bonus}!\n")
  print(f"Grade: {grade(score_lvl2_bonus, max_lvl2_bonus)}\n")
  if (score_lvl2_bonus / max_lvl2_bonus) < 0.6:
    print("You failed the bonus round. No bonus points.\n")
    level = 3
    select_level()
  else:
    score_total += score_lvl2_bonus
    level = 3
    select_level()

def lvl3():
  global level
  global score_total
  score_lvl3 = 0
  max_lvl3 = 3 * 13 * 300
  multiple_list = [4, 6, 7]
  os.system("clear")
  print(title)
  level_title()
  for multiple in multiple_list:
    for number in range(13):
      answer = multiple * number
      equation = f"{multiple} x {number} = "
      while True:
        try:
          guess = int(input(equation))
          if guess == answer:
            score_lvl3 += 300
            sys.stdout.write(f'\033[F{equation}{guess} ⭐\n\n')
            break
          else:
            sys.stdout.write(f'\033[F{equation}{guess} ❌ ({equation}{answer})\n\n')
            break
        except ValueError:
          print("\nOops. Something went wrong. Please, select only numbers.\n\nTry again:\n")
  print(f"SCORE: {score_lvl3}!\n")
  print(f"Grade: {grade(score_lvl3, max_lvl3)}\n")
  if (score_lvl3 / max_lvl3) < 0.6:
    print("You failed. Try again.\n")
    retry()
  else:
    score_total += score_lvl3
    level = 4
    select_level()

def lvl4():
  global level
  global score_total
  score_lvl4 = 0
  max_lvl4 = 2 * 13 * 400
  multiple_list = [8, 9]
  os.system("clear")
  print(title)
  level_title()
  for multiple in multiple_list:
    for number in range(13):
      answer = multiple * number
      equation = f"{multiple} x {number} = "
      while True:
        try:
          guess = int(input(equation))
          if guess == answer:
            score_lvl4 += 400
            sys.stdout.write(f'\033[F{equation}{guess} ⭐\n\n')
            break
          else:
            sys.stdout.write(f'\033[F{equation}{guess} ❌ ({equation}{answer})\n\n')
            break
        except ValueError:
          print("\nOops. Something went wrong. Please, select only numbers.\n\nTry again:\n")
  print(f"SCORE: {score_lvl4}!\n")
  print(f"Grade: {grade(score_lvl4, max_lvl4)}\n")
  if (score_lvl4 / max_lvl4) < 0.6:
    print("You failed. Try again.\n")
    retry()
  else:
    score_total += score_lvl4
    level = 5
    select_level()

def lvl5():
  global level
  global score_total
  score_lvl5 = 0
  max_lvl5 = 2 * 13 * 500
  multiple_list = [11, 12]
  os.system("clear")
  print(title)
  level_title()
  for multiple in multiple_list:
    for number in range(13):
      answer = multiple * number
      equation = f"{multiple} x {number} = "
      while True:
        try:
          guess = int(input(equation))
          if guess == answer:
            score_lvl5 += 500
            sys.stdout.write(f'\033[F{equation}{guess} ⭐\n\n')
            break
          else:
            sys.stdout.write(f'\033[F{equation}{guess} ❌ ({equation}{answer})\n\n')
            break
        except ValueError:
          print("\nOops. Something went wrong. Please, select only numbers.\n\nTry again:\n")
  print(f"SCORE: {score_lvl5}!\n")
  print(f"Grade: {grade(score_lvl5, max_lvl5)}\n")
  if (score_lvl5 / max_lvl5) < 0.6:
    print("You failed. Try again.\n")
    retry()
  else:
    score_total += score_lvl5
    level = 6
    select_level()

def lvl6():
  global level
  global score_total
  score_lvl6 = 0
  max_lvl6 = 2 * 13 * 600
  pre_list = [2, 3]
  multiple_list = scramble_list(pre_list)
  number_list = random_list()
  os.system("clear")
  print(title)
  level_title()
  for multiple in multiple_list:
    for number in number_list:
      answer = multiple * number
      equation = f"{multiple} x {number} = "
      while True:
        try:
          guess = int(input(equation))
          if guess == answer:
            score_lvl6 += 600
            sys.stdout.write(f'\033[F{equation}{guess} ⭐\n\n')
            break
          else:
            sys.stdout.write(f'\033[F{equation}{guess} ❌ ({equation}{answer})\n\n')
            break
        except ValueError:
          print("\nOops. Something went wrong. Please, select only numbers.\n\nTry again:\n")
  print(f"SCORE: {score_lvl6}!\n")
  print(f"Grade: {grade(score_lvl6, max_lvl6)}\n")
  if (score_lvl6 / max_lvl6) < 0.6:
    print("You failed. Try again.\n")
    retry()
  else:
    score_total += score_lvl6
    level = 7
    select_level()

def lvl7():
  global level
  global score_total
  score_lvl7 = 0
  max_lvl7 = 2 * 13 * 700
  pre_list = [5, 10]
  multiple_list = scramble_list(pre_list)
  number_list = random_list()
  os.system("clear")
  print(title)
  level_title()
  for multiple in multiple_list:
    for number in number_list:
      answer = multiple * number
      equation = f"{multiple} x {number} = "
      while True:
        try:
          guess = int(input(equation))
          if guess == answer:
            score_lvl7 += 700
            sys.stdout.write(f'\033[F{equation}{guess} ⭐\n\n')
            break
          else:
            sys.stdout.write(f'\033[F{equation}{guess} ❌ ({equation}{answer})\n\n')
            break
        except ValueError:
          print("\nOops. Something went wrong. Please, select only numbers.\n\nTry again:\n")
  print(f"SCORE: {score_lvl7}!\n")
  print(f"Grade: {grade(score_lvl7, max_lvl7)}\n")
  if (score_lvl7 / max_lvl7) < 0.6:
    print("You failed. Try again.\n")
    retry()
  else:
    score_total += score_lvl7
    level = 8
    select_level()

def lvl7_bonus():
  global level
  global score_total
  score_lvl7_bonus = 0
  max_lvl7_bonus = 1 * 13 * 350
  multiple_list = random_list()
  os.system("clear")
  print(title)
  print(bonus_title)
  for multiple in multiple_list:
    number = multiple
    answer = multiple * number
    equation = f"{multiple} x {number} = "
    while True:
      try:
        guess = int(input(equation))
        if guess == answer:
          score_lvl7_bonus += 350
          sys.stdout.write(f'\033[F{equation}{guess} ⭐\n\n')
          break
        else:
          sys.stdout.write(f'\033[F{equation}{guess} ❌ ({equation}{answer})\n\n')
          break
      except ValueError:
        print("\nOops. Something went wrong. Please, select only numbers.\n\nTry again:\n")
  print(f"SCORE: {score_lvl7_bonus}!\n")
  print(f"Grade: {grade(score_lvl7_bonus, max_lvl7_bonus)}\n")
  if (score_lvl7_bonus / max_lvl7_bonus) < 0.6:
    print("You failed the bonus round. No bonus points.\n")
    level = 8
    select_level()
  else:
    score_total += score_lvl7_bonus
    level = 8
    select_level()

def lvl8():
  global level
  global score_total
  score_lvl8 = 0
  max_lvl8 = 3 * 13 * 800
  pre_list = [4, 6, 7]
  multiple_list = scramble_list(pre_list)
  number_list = random_list()
  os.system("clear")
  print(title)
  level_title()
  for multiple in multiple_list:
    for number in number_list:
      answer = multiple * number
      equation = f"{multiple} x {number} = "
      while True:
        try:
          guess = int(input(equation))
          if guess == answer:
            score_lvl8 += 800
            sys.stdout.write(f'\033[F{equation}{guess} ⭐\n\n')
            break
          else:
            sys.stdout.write(f'\033[F{equation}{guess} ❌ ({equation}{answer})\n\n')
            break
        except ValueError:
          print("\nOops. Something went wrong. Please, select only numbers.\n\nTry again:\n")
  print(f"SCORE: {score_lvl8}!\n")
  print(f"Grade: {grade(score_lvl8, max_lvl8)}\n")
  if (score_lvl8 / max_lvl8) < 0.6:
    print("You failed. Try again.\n")
    retry()
  else:
    score_total += score_lvl8
    level = 9
    select_level()

def lvl9():
  global level
  global score_total
  score_lvl9 = 0
  max_lvl9 = 2 * 13 * 900
  pre_list = [8, 9]
  multiple_list = scramble_list(pre_list)
  number_list = random_list()
  os.system("clear")
  print(title)
  level_title()
  for multiple in multiple_list:
    for number in number_list:
      answer = multiple * number
      equation = f"{multiple} x {number} = "
      while True:
        try:
          guess = int(input(equation))
          if guess == answer:
            score_lvl9 += 900
            sys.stdout.write(f'\033[F{equation}{guess} ⭐\n\n')
            break
          else:
            sys.stdout.write(f'\033[F{equation}{guess} ❌ ({equation}{answer})\n\n')
            break
        except ValueError:
          print("\nOops. Something went wrong. Please, select only numbers.\n\nTry again:\n")
  print(f"SCORE: {score_lvl9}!\n")
  print(f"Grade: {grade(score_lvl9, max_lvl9)}\n")
  if (score_lvl9 / max_lvl9) < 0.6:
    print("You failed. Try again.\n")
    retry()
  else:
    score_total += score_lvl9
    level = 10
    select_level()

def lvl10():
  global level
  global score_total
  score_lvl10 = 0
  max_lvl10 = 2 * 13 * 1000
  pre_list = [11, 12]
  multiple_list = scramble_list(pre_list)
  number_list = random_list()
  os.system("clear")
  print(title)
  level_title()
  for multiple in multiple_list:
    for number in number_list:
      answer = multiple * number
      equation = f"{multiple} x {number} = "
      while True:
        try:
          guess = int(input(equation))
          if guess == answer:
            score_lvl10 += 1000
            sys.stdout.write(f'\033[F{equation}{guess} ⭐\n\n')
            break
          else:
            sys.stdout.write(f'\033[F{equation}{guess} ❌ ({equation}{answer})\n\n')
            break
        except ValueError:
          print("\nOops. Something went wrong. Please, select only numbers.\n\nTry again:\n")
  print(f"SCORE: {score_lvl10}!\n")
  print(f"Grade: {grade(score_lvl10, max_lvl10)}\n")
  if (score_lvl10 / max_lvl10) < 0.6:
    print("You failed. Try again.\n")
    retry()
  else:
    score_total += score_lvl10
    level = 11
    select_level()

def final_round():
  global level
  global score_total
  score_lvl_final = 0
  max_lvl_final = 66 * 500
  multiple_list = [2,3,4,5,6,7,8,9,10,11,12]
  number_list = [2,3,4,5,6,7,8,9,10,11,12]
  dictionary_final = {}
  os.system("clear")
  print(title)
  print(final_title)
  for index in range(66):
    while True:
      multiple = random.choice(multiple_list)
      number = random.choice(number_list)
      equation = f"{multiple} x {number} = "
      if (number >= multiple) and equation not in dictionary_final.keys():
        answer = multiple * number
        dictionary_final[equation] = {"answer": answer, "multiple": multiple, "number": number}
        break

  for equation, row in dictionary_final.items():
    while True:
      try:
        guess = int(input(equation))
        if guess == row["answer"]:
          score_lvl_final += 500
          sys.stdout.write(f'\033[F{equation}{guess} ⭐\n\n')
          break
        else:
          sys.stdout.write(f'\033[F{equation}{guess} ❌ ({equation}{row["answer"]})\n\n')
          break
      except ValueError:
        print("\nOops. Something went wrong. Please, select only numbers.\n\nTry again:\n")
  print(f"SCORE: {score_lvl_final}!\n")
  print(f"Grade: {grade(score_lvl_final, max_lvl_final)}\n")
  if (score_lvl_final / max_lvl_final) < 0.6:
    print("You failed. Try again.\n")
    retry()
  else:
    score_total += score_lvl_final
    level = 12
    the_end()

def final_bonus():
  global level
  global score_total
  score_lvl_final_bonus = 0
  max_lvl_final_bonus = 25 * 250
  multiple_list_bonus = [0,1,2,3,4,5,6,7,8,9,10,11,12]
  number_list = [0,1,2,3,4,5,6,7,8,9,10,11,12]
  dictionary_final_bonus = {}
  os.system("clear")
  print(title)
  print(bonus_title)
  for index in range(25):
    while True:
      multiple = random.choice(multiple_list_bonus)
      number = random.choice(number_list)
      equation = f"{multiple} x {number} = "
      if equation not in dictionary_final_bonus.keys():
        answer = multiple * number
        dictionary_final_bonus[equation] = {"answer": answer, "multiple": multiple, "number": number}
        break
  for equation, row in dictionary_final_bonus.items():
    while True:
      try:
        guess = int(input(equation))
        if guess == row["answer"]:
          score_lvl_final_bonus += 250
          sys.stdout.write(f'\033[F{equation}{guess} ⭐\n\n')
          break
        else:
          sys.stdout.write(f'\033[F{equation}{guess} ❌ ({equation}{row["answer"]})\n\n')
          break
      except ValueError:
        print("\nOops. Something went wrong. Please, select only numbers.\n\nTry again:\n")
  print(f"PARTIAL SCORE: {score_lvl_final_bonus}!\n")
  print(f"Grade: {grade(score_lvl_final_bonus, max_lvl_final_bonus)}\n")
  if (score_lvl_final_bonus / max_lvl_final_bonus) < 0.6:
    print("You failed. Try again.\n")
    retry()
  else:
    score_total += score_lvl_final_bonus
    select_level()

select_main()