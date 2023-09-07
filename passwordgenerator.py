import random 
import string

CHOICE='Y'
while(CHOICE=='Y'or CHOICE=='y'):
    print("ENTER PASSWORD LENGTH:")
    length=int(input())
    print("CHOOSE CHARACTER SET FOR PASSWORD FROM THESE:\n1.DIGITS\n2.LETTERS\n3.BOTH LETTERS AND DIGITS\n4.EXIT")
    choice=int(input())
    if(choice==1):
        character_list=string.digits
    elif(choice==2):
        character_list=string.ascii_letters
    elif(choice==3):
        character_list=string.hexdigits
    elif(choice==4):
        print("THANK YOU")
        exit()
    else:
        print("ERROR")
        exit()
    password=[]
    for i in range(length):
        character=random.choice(character_list)
        password.append(character)
    print("your pass word is "+"".join( password))        
    print("\n")
    print("DO YOU WANT ANOTHER PASSWORD Y/N")
    CHOICE=input()

print("YOU FINAL PASSWORD IS "+"".join(password))
print("THANK YOU ")