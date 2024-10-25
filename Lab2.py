
def main(temp_list):
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = []
    num_list = get_user_input()
    num_list = temp_list.split(",")
    calc_average_temperature()
    find_min_max_temperature()
    sort_temperature()
    calc_median_temperature()
    
def display_main_menu():
    print("display_main_menu")

def get_user_input():
    temp_list = input('Enter Temperatures: ')

def calc_average_temperature(num_list):
    total_temp = sum(num_list)
    x = len(num_list)
    average_temp = total_temp/x
    print("Average Temperature: " + average_temp)

def find_min_max_temperature(num_list):
    max_temp = max(num_list)
    print("Max temp is : " + max_temp)
    min_temp = min(num_list)
    print("Min temp is : " + min_temp)

def sort_temperature(num_list):
    sorted_num_list = num_list.sort()
    print("Sorted List: "+ sorted_num_list)

def calc_median_temperature(sorted_num_list):
    n1 = len(sorted_num_list)
    if (x%2 == 1):
        median1 = sorted_num_list[n1//2-1]
        median2 = sorted_num_list[n1//2]
        median = (median1 + median2)/2
    else:
        median = sorted_num_list//2
    print("Median is : "+ str(median))

if __name__=="__main__":
    main()
