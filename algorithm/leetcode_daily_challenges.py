# Ques: https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3412/
# Power of Four
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
class Solution:
    import math
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        else:
            check_value = math.log(num,4)
            return check_value == int(check_value)

# Ques: https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3411/
# Valid Palindrome
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.
class Solution:
	import string
	def isPalindrome(self, s: str) -> bool:

		s_nopunc = s.translate(str.maketrans('', '', string.punctuation))
		normal_phrase = s_nopunc.replace(" ", "").split()
		if len(normal_phrase) == 0:
			return True
		elif len(normal_phrase[0]) == 1:
			return True
		else:
			normal_seq = [char.lower() for char in normal_phrase[0]]
			reverse_seq = normal_seq[::-1]
			if normal_seq == reverse_seq:
				return True
			else:
				return False