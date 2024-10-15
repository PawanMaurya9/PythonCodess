#Find missing number in an array(using summation and XOR operation)
#numbers are 1 2 4 5 6 7
#in the above numbers we have 3 is missing
#so now will solve it by using the summation method to find the missing number
#so the formula is to find the sum of natural number is = n(n+1)/2  = 7*(7+1)/2 = 28
#sum of numbers 1 + 2 + 4 + 5 + 6 + 7 = 25
#(n(n+1)/2)- sum of numbers

#Now we will try to print  the missiing number using XOR Method

#Now we will try to print  the missiing number using XOR Method

def get_missing_summation(a):
    n = a[-1]
    sum1 = 0
    total = n*(n+1)//2
    sum1 = sum(a)
    print(total - sum1)
a = [1,2,4,5,6,7]
get_missing_summation(a)