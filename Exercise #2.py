# Create another function for calculating summary and average and printing it to the screen,
# but it would accept *args instead of a list. Test how this function works by calling it with a list of numbers.

def print_sum_avg(*args):
    sum=0
    for x in args:
        sum+=x
    avg=sum/len(args)
    print("Total: ", sum,"Average: ", avg)

(print_sum_avg(1,3,6,9,4))
