Overview

This repository contains a Python implementation of the classic Two Sum problem, commonly asked in coding interviews and competitive programming.

The goal is to find two indices in an array whose values add up to a given target.

The solution uses a hash map (dictionary) to achieve an efficient lookup and reduce time complexity.

Problem Statement

Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.

Constraints:

Each input has exactly one solution

You cannot use the same element twice

Return the indices in any order

Example:

Input

nums = [2,7,11,15]
target = 9

Output

[0,1]

Explanation
nums[0] + nums[1] = 2 + 7 = 9

Approach

The optimized solution uses a Hash Map (Dictionary).

Steps

Create an empty dictionary to store numbers and their indices.

Iterate through the array.

For each element:

Calculate the number needed to reach the target.

Check if the required number exists in the dictionary.

If it exists, return the stored index and the current index.

Otherwise, store the current number and index in the dictionary.

This avoids the O(n²) brute force approach.

Algorithm
Initialize empty hashmap

For each number in array:
    compute required value = target - current number
    
    if required value exists in hashmap:
        return indices
        
    store current number and index in hashmap
Code Implementation
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            num = nums[i]
            need = target - num

            if need in map:
                return [map[need], i]

            map[num] = i
Time and Space Complexity
Complexity	Value
Time Complexity	O(n)
Space Complexity	O(n)

Each element is processed once.

Dictionary lookup is O(1) on average.

Technologies Used

Python

Hash Map (Dictionary)

Algorithmic Problem Solving

Learning Outcome

This project demonstrates:

Efficient use of hash tables

Optimization from O(n²) to O(n)

Common coding interview pattern
