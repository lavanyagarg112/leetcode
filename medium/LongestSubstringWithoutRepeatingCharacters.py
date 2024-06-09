def lengthOfLongestSubstring(s):

    longestSubString = ''
    prev = ''
    flag = True

    for i in s:
        if flag:
            prev = i
            longestSubString = i
            flag = False
            continue
        if i in prev:
            if len(prev) > len(longestSubString):
                longestSubString = prev
        else:
            prev += i

    return max(len(prev),len(longestSubString))

print(lengthOfLongestSubstring("dvdf")) # fails for this