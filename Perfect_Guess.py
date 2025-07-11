import random 
 
num = random.randint(1, 100)
guesses = 0

for i in range(1, 100):
    a = int(input("Enter Your Number: "))
    guesses+=1

    if(a<=100):

        if(num<a):
            print("Lower Number Please.......")

        elif(num>a):
            print("Higher Number Please.......")

        else:
            print("--------------------------------------------------------------------")
            print(f"Congratulation, You are guess the Perfect Number {num} in {guesses} Attempts")
            print("--------------------------------------------------------------------")
            break
        
    else:
        print("Please Enter The Number Of Range In 1 To 100 ")

else:
    print("Sorry You are not guess the correct number in 100 attemps, Please Try Again!")