"""
Given a string s, find the length of the longest
substring
 without repeating characters.
"""

def LongestSubstring():
    string = 'abcabcbb'

    uniqueCharacters = set(string) # Used a set as sets require each character inside to be unique, thus removing all duplicates
    print('The longest possible substring of the provided string "' + str(string) + '" is: ' + str(len(uniqueCharacters)))
    print('Unique characters are: ' + ', '.join(uniqueCharacters))
   
LongestSubstring()