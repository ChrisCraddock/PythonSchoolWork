A_Score = 90
B_Score = 80
C_Score = 70
D_Score = 60

score = int(input("What is your number grade: "))

if score >= A_Score:
     print("Your grade is A")
else:
     if score >= B_Score:
         print("Your grade is B")
     else:
         if score >= C_Score:
             print("Your grade is C")
         else:
             if score >= D_Score:
                 print("Your grade is D")
             else:
                 print("Your grade is a D")

speed = int(input('Enter a speed: '))

if speed >= 24 and speed<= 56:
    print("Speed is normal")
else:
    print("Speed is abnormal")
