'''
Longest Repeating Character Replacement

Sliding window problem -

O(n) time
O(1) space

Used for using subarrays mostly

do it then shrink from left/right based on how big or small

'''

'''
My idea -

start with both pointers in the beginning
keep going as long as same char
as soon as encounter a diff char, change it to the same char that was there so far and store length and keep going
(keep track of k for how many times we can change the same stored char)
but once we come to a point where we have k=0 but diff char, shrink the window from left side until we can continue with our k
'''





