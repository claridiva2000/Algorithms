#!/usr/bin/python

import argparse





# What are the inputs your code receives?
#   -an array of integers (floats or ints only?)
#   -since the example is integers, i'll stick with that.
#   -test cases show only positive numbers
#   - the number of items in the array can vary

# What is the range of input?
#   - integers between 0 and infinity, tho reasonably, cap at 1     
#     million

# How big can the input be (how much data)?
#    - infinitely large

# What are the outputs your code produces?
#   - expected output is a positive or negative integer that is the difference between any one of the items and any of the items entered before it. 

# What is the range of output?
#   - if the buy prices are all lower than the last item, it could 
#     potentially be a negative number(lost profits). the output 
#     could be any positive or negative integer.

# How big can the output be (how much data)?
#     - the output should be a positive or negative integer

# How performant must the code be?
#     - initially, just want to get it working, then will refactor. 
#     ideally O(n) or O(n**2) since there can be any number of data
#     inputs and stock prices change constantly. Anything less  
#     performant in a real world situation would be unusable. 

# What is missing from the task description?
#      - are we using floats, since stock prices are in dollars and 
#         cents?

# Are there third-party stakeholders who should be consulted?
#     -nope

# What assumptions are you making?
#     none that i havn't already mentioned. 


# Do these assumptions need to be validated by anyone else on the team?
#   not sure yet. 

#================
#steps to solve
#================

#important info: 
# this sounds like it can be solved with a nested loop. 
# startin from the left going right, if we sort all preceeding numbers smallest to largest, we would just need to subtract the smallest number from the current index.
# - set variable for the current index
# - set a variable for the highest difference
# - if the difference on the current indext is higher than the existing highest_difference, then we update it.  

def find_max_profit(prices):
  
  smallest = min(prices[:-1])
  
  temp = 0
  print(smallest)
    
    for items in prices:
      print(prices[0:prices.index(items)])
      if prices[-1]< smallest and items - smallest > temp:
        temp = items-smallest
  print(temp)

  return temp
    # sorted=compare
    # if temp == None:
    #   temp == sorted[0]
    
 
print(find_max_profit([1050, 1540, 3800, 1540, 270, 200, 2]))
# print(find_max_profit([100, 90, 80, 50, 20, 10]))
# print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]))

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
