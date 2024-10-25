
def main(temp_list):
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = []
    num_list = get_user_input()
    num_list = temp_list.split(",")
    
def display_main_menu():
    print("display_main_menu")

def get_user_input():
    temp_list = input('Enter Temperatures: ')

def calc_average_temperature(num_list):
    total_temp = sum(num_list)
    x = len(num_list)
    average_temp = total_temp/x
    print("Average Temperature: " + average_temp)

    
def find_min_max_temperature():

def sort_temperature():

def calc_median_temperature():
