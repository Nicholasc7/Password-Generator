import random
import string

#Initialize characters
letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
char_lists = [letters, digits, punctuation]

#Get password length
pwd_len = int(input("Password length: "))


#Produce password
password = ""
for x in range(pwd_len):
    random_char = random.choice(random.choice(char_lists))
    password += random_char
print(password)