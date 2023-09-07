
print("Welcome to the 'Introduction to the Solar System'  quiz! ")
print("This quiz will test your basic knowledge about the celestial bodies in our solar system.")
print("Read each question carefully and select the best answer from the options provided ")
print("Let's get started!")
print("--------------------------")
score=0
print("Question 1: What is the largest planet in our solar system?")
print("\n1.Earth\n2.Jupiter\n3.Mars\n4.Venus")
ans=int(input())
if(ans==2):
    print("CORRECT")
    score=score+1
else:
    print("INCORRECT")
    
print("Question 2: Which planet is known as the ""Red Planet"" due to its reddish appearance?")
print("\n1.Saturn\n2.Neptune\n3.Jupiter\n4.Mars")
ans=int(input())
if(ans==4):
    print("CORRECT")
    score=score+1
else:
    print("INCORRECT")
print("Question 3: What is the closest star to Earth??")
print("\n1. Alpha Centauri\n2.Proxima Centauri\n3.Betelgeuse\n4.Sirius")
ans=int(input())
if(ans==2):
    print("CORRECT")
    score=score+1
else:
    print("INCORRECT")

print("Question 4: Which of these is NOT a type of rock?")
print("\n1.Igneous\n2.Sedimentary\n3.Metamorphic\n4.Liquidous")
ans=int(input())
if(ans==4):
    print("CORRECT")
    score=score+1
else:
    print("INCORRECT")

print("Question 5: What causes the changing phases of the Moon as observed from Earth?")
print("\n1.Earth's shadow\n2.Cloud cover\n3.Tidal forces\n4.Sun's position")
ans=int(input())
if(ans==4):
    print("CORRECT")
    score=score+1
else:
    print("INCORRECT")
print("Question 6:What is the process by which plants make their own food using sunlight?")
print("\n1.Respiration\n2.Photosynthesis\n3.Fermentation\n4.Transpiration")
ans=int(input())
if(ans==2):
    print("CORRECT")
    score=score+1
else:
    print("INCORRECT")
print("Question 7: What holds the planets in orbit around the Sun?")
print("\n1.Gravity\n2.Magnetism\n3.Solar wind\n4.Inertia")
ans=int(input())
if(ans==1):
    print("CORRECT")
    score=score+1
else:
    print("INCORRECT")
    
print("Question 8: What is the outermost layer of the Earth called?")
print("\n1.Mantle\n2.Crust\n3.Core\n4.Asthenosphere")
ans=int(input())
if(ans==2):
    print("CORRECT")
    score=score+1
else:
    print("INCORRECT")
    
print("Question 9: What is the process of a liquid turning into a gas at the surface?")
print("\n1. Melting\n2.Condensation\n3.Evaporation\n4.Sublimation")
ans=int(input())
if(ans==3):
    print("CORRECT")
    score=score+1
else:
    print("INCORRECT")
print("Question 10: What is the name of the brightest star in the night sky, often referred to as the 'Dog Star'?")
print("\n1.Vega\n2.Polaris\n3.Sirius\n4.Betelgeuse")
ans=int(input())
if(ans==3):
    print("CORRECT")
    score=score+1
else:
    print("INCORRECT")

print(f"YOUR SCORE={score}/10")