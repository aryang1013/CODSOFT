
op='y'
while(op=='y'or op=='Y'):
     print("------------------------------")
     print("ENTER 2 NUMBERS")
     num1=float(input("VALUE 1:"))
     num2=float(input("VALUE 2:"))
     print("------------------------------")
     print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.EXIT")
     choice=int(input())
     print("------------------------------")
     if(choice==1):
        print(f"{num1} + {num2}={num1+num2}")
        print(f"THE ANSWER IS :{num1+num2}")
     elif(choice==2):
        print(f"{num1} - {num2}={num1-num2}")
        print(f"THE ANSWER IS :{num1-num2}") 
     elif(choice==3):
        print(f"{num1} x {num2}={num1*num2}")
        print(f"THE ANSWER IS :{num1*num2}")
     elif(choice==4):
        print(f"{num1} / {num2}={num1/num2}")
        print(f"THE ANSWER IS :{num1/num2}")
     elif(choice==5):
        print("THANK YOU")
        exit()
     else:
        print("INVALID INPUT")
        exit()
     print("------------------------------")
     print("DO WANT TO PERFORM ANOTHER CALULATION Y/N")
     op=input()