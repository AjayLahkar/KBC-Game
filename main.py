# Create a programme capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers.
# Displaying the final amount the person is taking home after playing the game.

print("  -: Welcome to You in KBC Game :-")
prize = 0
# print(type (prize))
que1 = "Q1.- How many types of Yuga?"
print(que1)
opt1 = 4
print("[A]", + opt1)
opt2 = 11
print("[B]", + opt2)
opt3 = 7
print("[C]", + opt3)
opt4 = 72
print("[D]", + opt4)
ans = input("Please give the answer in A, B, C, D :- ")
# print(type (ans))
if (ans == "A"):
  prize += 10000
  print("Congrates! Your answer is correct and You Win Rs. 10000 for this Quetion.", + prize)
elif(ans != "A"):
  print("Oops..! Wrong Answer, Better Luck Next Time", + prize)


que2 = "Q2.- How many brothers of Pandvas?"
print(que2)
opt1 = 4
print("[A]", + opt1)
opt2 = 100
print("[B]", + opt2)
opt3 = 5
print("[C]", + opt3)
opt4 = 6
print("[D]", + opt4)
ans = input("Please give the answer in A, B, C, D :- ")
# print(type (ans))
if (ans == "C"):
  prize += 20000
  print("Congrates! Your answer is correct and You Win Rs. 20000 for this Quetion.", + prize)
elif(ans != "C"):
  print("Oops..! Wrong Answer, Better Luck Next Time", + prize)


que3 = "Q3.- How many years age of KaliYuga?"
print(que3)
opt1 = 832000
print("[A]", + opt1)
opt2 = 432000
print("[B]", + opt2)
opt3 = 1232000
print("[C]", + opt3)
opt4 = 5000
print("[D]", + opt4)
ans = input("Please give the answer in A, B, C, D :- ")
# print(type (ans))
if (ans == "B"):
  prize += 30000
  print("Congrates! Your answer is correct and You Win Rs. 30000 for this Quetion.", + prize)
elif(ans != "B"):
  print("Oops..! Wrong Answer, Better Luck Next Time", + prize)


que4 = "Q4.- How many types of Vedas?"
print(que4)
opt1 = 5
print("[A]", + opt1)
opt2 = 18
print("[B]", + opt2)
opt3 = 12
print("[C]", + opt3)
opt4 = 4
print("[D]", + opt4)
ans = input("Please give the answer in A, B, C, D :- ")
# print(type (ans))
if (ans == "D"):
  prize += 40000
  print("Congrates! Your answer is correct and You Win Rs. 40000 for this Quetion.", + prize)
elif(ans != "D"):
  print("Oops..! Wrong Answer, Better Luck Next Time", + prize)


que5 = "Q5.- Who are the mother of Karna?"
print(que5)
opt1 = "Radha"
# print(type(opt1))
print("[A]", opt1)
opt2 = "Gandhari"
print("[B]", opt2)
opt3 = "Kunti"
print("[C]", opt3)
opt4 = "Devki"
print("[D]", opt4)
ans = input("Please give the answer in A, B, C, D :- ")
# print(type (ans))
if (ans == "C"):
  prize += 50000
  print("Congrates! Your answer is correct and You Win Rs. 50000 for this Quetion.", + prize)
elif(ans != "C"):
  print("Oops..! Wrong Answer, Better Luck Next Time", + prize)
