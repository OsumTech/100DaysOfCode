height = input("Please Enter your Height in m:   ")
weight = input("Please Enter your Weight in Kgs:   ")

height_int = float(height)
print(round(int(weight) / height_int ** 2))

