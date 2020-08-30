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
# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

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


# Ques: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
# Capacity To Ship Packages Within D Days
# Return the least weight capacity of the ship that will result in all the packages
# on the conveyor belt being shipped within D days.

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def feasible(capacity) -> bool:
            days = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:  # too heavy, wait for the next day
                    total = weight
                    days += 1
                    if days > D:  # cannot ship within D days
                        return False
            return True

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left


# Ques: https://leetcode.com/problems/split-array-largest-sum/
# Split Array Largest Sum
# Given an array nums which consists of non-negative integers and an integer m,
# you can split the array into m non-empty continuous subarrays.
# Write an algorithm to minimize the largest sum among these m subarrays.

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def feasible(threshold) -> bool:
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > threshold:
                    total = num
                    count += 1
                    if count > m:
                        return False
            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left

# Ques: https://leetcode.com/problems/shuffle-the-array/
# Shuffle the Array
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

