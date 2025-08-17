#Create a function that finds all combinations of numbers
#in a list that add up to the target value.
# The function will receive a list of positive integers
# and a target value.
#To obtain the combinations, each element of the list can only be used
# once (but there may be
#repeated elements in it).
#Example: List = [1, 5, 3, 2],  Target = 6
# Solutions: [1, 5] and [1, 3, 2] (both combinations add up to 6)
#(If there are no combinations, return an empty list)

# Solution method
#x. Define one tunction which is going to return a random numbers list


#a. Define a new function. the inbound's function is gonna be the ramdom list
#b. The argument can be: the list of numbers and the objetive to reach
#c. the outbound's function is going to be solution's list
# We can use a number only once

#Backtracking: Backtracking is an algorithmic technique whose goal is to use brute force
# to find all solutions to a problem. It entails gradually compiling a set of all possible solutions.
# Because a problem will have constraints, solutions that do not meet them will be removed.

#Instead to find which sums are gonna be the solution, we can take our target number 
#and subtract every possible set of numbers from it until we get a cero. 


import random

def ranList() -> list:
    randomList = []
    n = random.randint(0, 20)
    for i in range (n):
        randomList.append(random.randint(1, 50))
    return randomList

def ranTarget() -> int:
    n = random.randint(0, 100)
    return n



def findSum(list0: list, target: int) -> list:
    def backtrack(start: int, target: int, combination: list): #we can define a function within another one. A private function
        #True condition. 
        #solution found
        # the target number is going to change through each iteration
        if target == 0:    
            targetList.append(combination[:]) #shallow copy in python [:]
            return
    
        #solution not found
        if target < 0 or start == len(list0):
            return  
    
        #backtrack. By a given range
        for index in range(start, len(list0)):
            if index > start and list0[index] == list0[index - 1]: #If the current number is equal to the previous number, that iteration is skipped.
                continue  

            combination.append(list0[index])
            backtrack(index + 1, target - list0[index], combination)
            combination.pop()

    list0.sort() #Reorder our list
    targetList = []
    backtrack(0, target, [] ) 
    return targetList

def main():
    x = ranList()
    y = ranTarget()
    print(x, y) 
    print(findSum(x, y))

if __name__ == '__main__':
    main()