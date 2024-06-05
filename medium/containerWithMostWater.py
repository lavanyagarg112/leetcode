# Container with Most Water

# Status: IN PROGRESS

# Understanding the problem:

'''
Given: Integer array named height, whose length is n
there are n vertical lines drawn, which is a line from (i,0) to (i, height[i])

find 2 lines tgt that form a container with the most water along the x axis

Return type: integer - the max amount of water

It is given that the length of the array will be atleast 2
'''

# Understanding the problem with the example:

'''
So for eg if we have [1,8,6,2,5,4,8,3,7]

we start with 1 to 8 -> area is (distance between endpoint and start point)*(smallest height between the start and end point)
prev = 1
max = 1

then 8 -> 6
prev = max(1->6 = 2*1 = 2, 8 -> 6 = 1*6 = 6) = 6
max = max(max, prev) = 6

and so on

But in this case we need to keep track of the prev in terms of the height, as well as the area

'''

# Coding attempt

def maxArea(height):

    prevHeight = 0
    prevLength = 0
    immediatePrevHeight = 0
    maxNum = 0
    flag = True

    for i in height:
        if flag:
            print('NEW')
            flag = False
            prevHeight = i
            prevLength = 0
            immediatePrevHeight = i
            maxNum = 0
            print("prevHeight: ", prevHeight)
            print("prevLength: ", prevLength)
            print("immediatePrevHeight: ", immediatePrevHeight)
            print("maxNum:", maxNum)
            print('***')
            continue

        num1 = (prevLength + 1) * min(prevHeight,i)
        num2 = min(immediatePrevHeight,i)

        print("num1: ", num1)
        print("num2: ", num2)

        if num1 > num2:
            prevLength = prevLength + 1
            maxNum = max(maxNum, num1)
        elif num1 < num2:
            prevLength = 1
            prevHeight = immediatePrevHeight
            maxNum = max(maxNum, num2)
        else:
            if prevHeight >= immediatePrevHeight:
                prevLength = prevLength + 1
            else:
                prevLength = 1
                prevHeight = immediatePrevHeight
            maxNum = max(maxNum, num1)
        
        immediatePrevHeight = i

        print("prevHeight: ", prevHeight)
        print("prevLength: ", prevLength)
        print("immediatePrevHeight: ", immediatePrevHeight)
        print("maxNum:", maxNum)
        print('***')


    return maxNum

# print(maxArea([1,8,6,2,5,4,8,3,7]))
# print(maxArea([2,1]))
# print(maxArea([1,2,4,3]))
print(maxArea([2,3,10,5,7,8,9]))

'''
Core issue identified:
[2,3,10,5,7,8,9]

in subarray [2,3,10,5,7]
the max should be 10 -> 7 = 14
instead as per my algorithm it is 2 -> 7 which is 8
'''