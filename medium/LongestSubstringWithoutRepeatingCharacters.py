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

# 2 pointer solution from leetcode:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_length = 0
        char_set = set()
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length