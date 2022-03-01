
'''

- LAMBDA EX



multiplay_this = lambda x, y: x*y
print(multiplay_this(4, 5))


my_list = [20, 10, 5, 7, 8]
my_list_even = (filter(lambda x: x%2 == 0, my_list))
print(my_list_even)




'''
from typing import List

'''








'''


def isVowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']

def countVovels(str, n):
    if (n == 1):
        return isVowel(str[n - 1]);

    return (countVovels(str, n - 1) +
            isVowel(str[n - 1]));





# string object
str = "i love python";

# Total numbers of Vowel
print(countVovels(str, len(str)))
