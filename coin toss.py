#Remember to use the random module
#Hint: Remember to import the random module first. 🎲
import random	 
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write your code below this line 👇
test_seed = random.randint(0,1)
if test_seed == 1:
    print("Heads")
if test_seed == 0:
    print("Tails")


