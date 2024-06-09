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
            for j in range(len(prev)):
                if prev[j] == i:
                    break
            prev = prev[j+1:] + i
            
        else:
            prev += i

    return max(len(prev),len(longestSubString))

print(lengthOfLongestSubstring("dvdf"))

# need to figure out how to do better