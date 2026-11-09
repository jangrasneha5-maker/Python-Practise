# In Python, when you have a list or a string, you can access parts of it using this format:

# list[start : stop : step]

# The Breakdown of [::-1]
# The first colon : (start): Since nothing is written before it, Python assumes you want to start from the very beginning.

# The second colon : (stop): Since nothing is written after it, Python assumes you want to go all the way to the very end.

# The -1 (step): This is the "jump" size.

# A step of 1 means move forward one by one.

# A step of -1 means move backward one by one.

# Visual Example
# Imagine your words list looks like this:
# ['the', 'sky', 'is', 'blue']

# When you say words[::-1], Python starts at the end and "steps" backward:

# It picks 'blue'

# It steps back to 'is'

# It steps back to 'sky'

# It steps back to 'the'

# The result is a brand new list: ['blue', 'is', 'sky', 'the']


# question
# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# /solution
class Solution:
    def reverseWords(self, s: str) -> str:
        # 1. Split the string into a list of words
        # .split() without arguments handles multiple spaces automatically!
        words = s.split()
        
        # 2. Reverse the list of words
        # [::-1] is a cool Python trick to reverse a list
        reversed_words = words[::-1]
        
        # 3. Join the words with a single space
        return " ".join(reversed_words)