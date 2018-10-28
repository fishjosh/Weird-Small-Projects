from random import *
from math import fabs
def main():
    name_1= input("Please enter your name: ")
    name_2= input("Please enter your name: ")
    print("Pick a number one through ten: ")
    print(name_1, end="")
    name_guess_1 = int(input(", Pick a number 1-10: "))
    while name_guess_1 < 1:
        name_guess_1 = int(input("Please pick another number 1-10 "))
    while name_guess_1 >10:
        name_guess_1 = int(input("Please pick another number 1-10 "))        
    print(name_2, end="")
    name_guess_2 = int(input(", Pick a number 1-10: "))
    while 10 < name_guess_2:
        name_guess_2 = int(input("Please pick another number 1-10 "))
    while 1 > name_guess_2:
        name_guess_2 = int(input("Please pick another number 1-10 "))        
    while name_guess_2 == name_guess_1:
        print(name_2, end="")
        name_guess_2 = int(input (", Please pick another number: "))
    number = randrange(1,11)
        
    if fabs((number - name_guess_1)) < fabs((number - name_guess_2)):
        print("Congrats, ",name_1," your guess, ",name_guess_1, ", is closer to ",number," than ",name_2, sep= "")
    if fabs((number - name_guess_2)) < fabs((number - name_guess_1)):
        print("Congrats, ",name_2," your guess, ", name_guess_2, ", is closer to ",number, " than ", name_1, sep="")    
    if fabs((number - name_guess_1)) == fabs((number - name_guess_2)):
        print(name_2," and ",name_1, ", You are both equally close to the number ",number, sep="")
    

main()