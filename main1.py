questions = [
  ["Q1. - Which language was used to create fb ? ", "Python", "French", "JavaScript", "php", 4],
  ["Q2. - How many types of Yuga ? ", "4", "11", "7", "72", 1],
  ["Q3. - How many brothers of Pandvas ? ", "4", "100", "5", "6", 3],
  ["Q4.- How many years age of KaliYuga ? ", "832000 Yrs.", "432000 Yrs.", "1232000 Yrs.", "5000 Yrs.", 2],
  ["Q5.- How many types of Vedas ? ", "5", "18", "12", "4", 4],
  ["Q6.- Who are the mother of Karna ? ", "Radha", "Gandhari", "Kunti", "Devki", 3],
  
]

print("----: Welcome to you in KBC Game :---")

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
  question = questions [i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print({question[0]})
  print(f"a. {question[1]}        b.  {question[2]}")
  print(f"c. {question[3]}        d.  {question[4]}")
  reply = int(input("Enter your answer (1-4) or Press 0(Zero) to Quit :-\n "))
  if(reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won RS. {levels[i]}")
    if(i == 4):
       money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 1000000
  else:
    print("Wrong Answer....!")
    break

print(f"Your Take home money is {money}")