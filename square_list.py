#Author: Sophia Philips
#Github Username: sophiacphilips
#Date: 11/10/22
#This program is designed to take a number from a list and return the squares of the original numbers.

def square_list(nums):
    """this function takes a list of numbers and mutates it to their square values"""
    for n in range(len(nums)): #for all numbers in the list that will be input (during testing)
        nums[n]=nums[n]*nums[n] #square each number in the list

#testing
#nums=[7, -3, 12, 9]
#square_list(nums)
#print(nums)