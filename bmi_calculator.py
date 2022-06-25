height = float(input("Enter your height in centimeters: "))
weight =  float(input("Enter your weight in KG: "))
height = height / 100

BMI = weight/(height*height)
print("your Body Mass Index is: ", BMI)
if(BMI > 0):
    if(BMI <= 16):
        print("you're severely underweight ")
    elif(BMI <= 18.5):
        print("you're underweight ")
    elif(BMI <= 25):
        print("You're Healthy")
    elif(BMI <= 30):
        print("You're overweight ")
    else:
        print("you're severely overweight ")
else:
    print("Enter valid Details again")
