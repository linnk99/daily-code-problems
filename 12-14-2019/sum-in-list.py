import random

def generate_list(numbers_list, list_length):
    for i in range(list_length):
        numbers_list.append(random.randint(0, list_length))
    
    print(numbers_list)
            
def check_sum(numbers_list, number_to_check):
    for i in range(len(numbers_list)):
        if number_to_check - numbers_list[i] in numbers_list:
            print('The number {} is a sum of two numbers in the list'.format(number_to_check))
            break
        else:
            print('The number {} is NOT a sum of two numbers in the list'.format(number_to_check))
            break
        

def run():
    numbers_list = [] #Empty list of numbers to compare with
    
    print('This program checks if a number is the sum of 2 numbers in a random list.')
    
    list_length = int(input('How long is the list?: '))
    number_to_check = int(input('Which number will be compared to the list?: '))
    
    generate_list(numbers_list, list_length)
    check_sum(numbers_list, number_to_check)
    

if __name__ == "__main__":
    run()