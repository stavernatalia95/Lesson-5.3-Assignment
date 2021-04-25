#Create a function that asks the user to enter 3 numbers and then prints on the screen their summary and average.

numbers=[]

for i in range(3):
    numbers.append(int(input("Please enter a number:")))

def print_sum_avg(my_numbers):
    result=0
    for x in my_numbers:
        result +=x
    avg=result/len(my_numbers)
    print("Total: ", result, "Average: ", avg)

total_of_numbers=numbers
(print_sum_avg(total_of_numbers))

