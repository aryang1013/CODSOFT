import random

output=['rock','paper','scissor']
scoreA=0
scoreB=0
c='yes'


while c=='yes':   
 
 A=input("enter rock,paper or scissor\n")
 B=random.choice(output)
 
 print(f"computer={B}")
 if(A=='rock'and B=='paper'):
    scoreB=scoreB+1
    print("you lose")
    print(f"computer={scoreB},A={scoreA}")
 elif(A=='rock'and B=='scissor'):    
     scoreA=scoreA+1
     print("you win")
     print(f"computer={scoreB},A={scoreA}")
           
 elif(A=='rock'and B=='rock'):    
     
     print("tie")
     print(f"computer={scoreB},A={scoreA}")
           
 elif(A=='paper' and B=='rock'):    
     scoreA=scoreA+1
     print("you win")
     print(f"computer={scoreB},A={scoreA}")

 elif(A=='paper' and B=='scissor'):    
     scoreB=scoreB+1
     print("you lose")
     print(f"computer={scoreB},A={scoreA}")
 elif(A=='paper'and B=='paper'):    
     
     print("Tie")
     print(f"computer={scoreB},A={scoreA}")
 elif(A=='scissor'and B=='scissor'):    
     
     print("tie")
     print(f"computer={scoreB},A={scoreA}")
 elif(A=='scissor'and B=='paper'):    
     scoreA=scoreA+1
     print("you win")
     print(f"computer={scoreB},A={scoreA}")
 else:

     scoreB=scoreB+1
     print("you lose")
     print(f"computer={scoreB},A={scoreA}")
 print("do you want to play again yes/no")
 c=input()   


     