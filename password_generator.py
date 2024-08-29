import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
numbers = "0123456789"
symbols = "@!#$%^&*(){}:[]/.,;><?"

upper,lower,nums,syms = True,True,True,True
all = ""
if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += numbers
if syms:
    all += symbols
    

length = int(input("Enter the length of password:"))


password = "".join(random.sample(all,length))
print("Generated password:",password)
