f_name = input("Please Enter Your First Name: ")
l_name = input("Please Enter Your Last Name: ")

def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    print(f"Your Name is {f_name} {l_name}")

format_name(f_name, l_name)
