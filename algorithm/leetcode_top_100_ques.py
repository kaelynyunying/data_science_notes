# Ques: https://leetcode.com/problems/two-sum/
# Two Sum 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
		required = {}
		for i in range(len(nums)):
			if target - nums[i] in required:
				return [required[target - nums[i]], i]
			else:
				required[nums[i]] = i

# Binary Search Problem Template

def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left


# Ques: https://leetcode.com/problems/first-bad-version/
# First Bad Version
# Time Complexity : O(log2n)
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

# Ques: https://leetcode.com/problems/sqrtx/submissions/
# Implement int sqrt(int x).
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x + 1
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid
        return left - 1


# Ques: https://leetcode.com/problems/search-insert-position/submissions/
# Search Insert Position
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		left, right = 0, len(nums)
		while left < right:
			mid = left + (right - left) // 2
			if nums[mid] < target:
				left = mid + 1
			else:
				right = mid
		return right
