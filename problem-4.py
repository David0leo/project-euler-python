# Project Euler Problem 4
######################################
# Find largest palindrome number which
# is the  product of two 3 digit nums
######################################

#Takes a positive integer, returns a list of its digits
def list_digits(n):
    assert type(n) is int, "Non-integer value"
    assert n >=0, "Positive n values only"
    
    number_string = str(n)
    number_list = []
    # Cycle through digits, convert to ints and throw in list
    for char in number_string:
        number_list.append(int(char))
    
    return number_list

def test_list_digits():
    print(list_digits(13444))
    print(list_digits(3413155455322521))
    print(list_digits(0))
    #print(list_digits(-1)) #throws up assertion
    print(list_digits(5))
    #print(list_digits()) #gives error, missing argument
    return

#checks if a positive integer is a palindrome
def check_palindrome(n):
    assert type(n) is int, "Non-integer value"
    assert n >=0, "Positive n values only"
    
    digit_list = list_digits(n)
    
    for i in range(0, len(digit_list)//2):
        if digit_list[i] != digit_list[-1-i]:
            return False
    #went through loop, found no mismatches
    return True

def test_check_palindrome():
    #prints T, T, T, F, T, T, F when run
    print(check_palindrome(111))
    print(check_palindrome(0))
    print(check_palindrome(1))
    print(check_palindrome(346))
    print(check_palindrome(909))
    print(check_palindrome(1234567890987654321))
    print(check_palindrome(12349994201))
    return

def main():
    #start by getting two large 3 digit numbers
    #check all 900's first, then 800's and so on
    sup = 999
    largest_pal = 0
    largest_pair = [0, 0]
    for i in range(0, 10):
        for j in range(0, 100):
            num1 = sup - 100*i - j
            for k in range(j, 100):
                num2 =  sup - 100*i - k
                #check if product is palindrome
                #exit function and return true for
                if (check_palindrome(num1*num2)) and (num1*num2 > largest_pal):
                    largest_pair[0] = num1
                    largest_pair[1] = num2
                    largest_pal = num1*num2
        #gone through 100*100 nums, check if found a palindrome
        #return largest if one was found
        if largest_pal != 0:
            print(largest_pair[0], "*", largest_pair[1], "=", largest_pal)
            print("Is the largest palindrome, which is the sum of two 3 digit nums.")
            return
          
    if largest_pal == 0:
        print("No palindrome found as product of two 3 digit numbers")
    return

#test
main()

