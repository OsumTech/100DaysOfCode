height = input("Please Enter your Height in m:   ")
weight = input("Please Enter your Weight in Kgs:   ")

height_int = float(height)
bmi = round(int(weight) / height_int ** 2)
print(bmi)
if bmi < 18.5:
    print("You are under weight kuch khaya pia kr gareeb insan")
elif bmi<25:
    print("Keep It up You are having a normal weight")
elif bmi <30:
    print("You are a overweight")
elif bmi <35:
    print("You are obese")
else:
    print("you are clinically obese")
