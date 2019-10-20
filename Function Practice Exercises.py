# #WARMUP SECTION:
#  LESSER OF TWO EVENS: Write a function that returns the lesser of two
#  given numbers if both numbers are even,
#  but returns the greater if one or both numbers are odd
#  lesser_of_two_evens(2,4) --> 2
#  lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a, b)

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_cracker(s1):
    lst = s1.split()
    return lst[0][0] == lst[1][0]


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False¶
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def makes_twenty(a, b):
    return a == 20 or b == 20 or a + b == 20

# LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald

def old_macdonald(s):
    new_s = ""
    for el in range(0, len(s)):
        if el == 0 or el == 3:
            new_s += s[el].capitalize()
        else:
            new_s += s[el]
    return new_s

# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:
# >>> "--".join(['a','b','c'])
# >>> 'a--b--c'
# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:
# >>> " ".join(['Hello','world'])
# >>> "Hello world"

def master_yoda(s):
    s = s.split()
    new_s = []
    for el in s:
        new_s = [el] + new_s
    return " ".join(new_s)


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
# NOTE: abs(num) returns the absolute value of a number

def almost_there(n):
    if abs(200-n) <= 10 or abs(100-n) <= 10:
        return True
    else:
        return False

# LEVEL 2 PROBLEMS
# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(l):
    res = False
    for el in range(1, len(l)):
        if l[el] == 3 and l[el-1] == 3:
            res = True
    return res

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(s):
    new_s = []
    final_s = []
    for el in s:
        new_s += [el]
    for el in s:
        final_s += el*3
    return "".join(final_s)

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def blackjack(n1, n2, n3):
    total = n1 + n2 + n3
    if total <= 21:
        return total
    else:
        if n1 == 11 or n2 == 11 or n3 == 11:
            total -= 10
            if total <= 21:
                return total
            else:
                return "BUST"
        else:
            return "BUST"

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(l):
    halt = False
    num = 0
    if len(l) == 0:
        return 0
    for el in l:
        if el == 6:
            halt = True
            continue
        if halt == True and el == 9:
            halt = False
            continue
        if halt == False:
            num += el
    return num

# CHALLENGING PROBLEMS
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(l):
    first = False
    second = False
    for el in range(len(l)):
        if l[el] == 0:
            if first == True:
                second = True
            first = True
        if l[el] == 7 and second:
            return True
    return False



# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.
def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

def count_primes(n):
    counter = 0
    for i in range(2, n):
        if is_prime(i):
            counter += 1
    print(counter)