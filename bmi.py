def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

def display_main_menu():
    print("display_main_menu")

def get_user_input():
    height = input('Enter your Height (m) ')
    weight = input('Enter your Weight (kg) ')
    

def calc_average():
    print("calc_average") 

def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)
    print("BMI = "+str(bmi))
    if (bmi < 18.5):
        print("Under Weight")
    if (bmi < 18.5, bmi > 25.0):
        print("Normal Weight")
    else:
        print("Over Weight")
if __name__=="__main__":
    main()
calculate_bmi(weight=72, height=1.75)