# Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is given as frac{4}{3} πr^3

def vol(rad):
    from math import pi
    return 4/3 * pi * rad**3

# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    return low <= num <= high

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33
# HINT: Two string methods that might prove useful: .isupper() and .islower()
# If you feel ambitious, explore the Collections module to solve this problem!

def up_low(s):
    s = s.split()
    upper = 0
    lower = 0
    for word in s:
        for letter in word:
            if letter.isupper():
                upper += 1
            elif letter.islower():
                lower += 1
    return print("Number of lower is: {0} and number of upper is: {1}".format(lower, upper))

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique_list(lst):
    return list(set(lst))

# Write a Python function to multiply all the numbers in a list.
# Sample List : [1, 2, 3, -4]
# Expected Output : -24

def multiply(numbers):
    res = 1
    for num in numbers:
        res *= num
    return res


# Write a Python function that checks whether a passed in string is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

def palindrome(s):
    s_rev = s[::-1]
    return s == s_rev

# Hard:
# Write a Python function to check whether a string is pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
# Hint: Look at the string module

import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    return set(alphabet) <= set(str1.lower())