# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".



# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.


from typing import List


class Solution:  # TODO: доделать
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]:
            return ''
        prefix = ''
        last_string = ''
        for string in strs:
            if not prefix:
                prefix = string[0]
                continue
            if string[:len(prefix)] != prefix:
                return ''
            try:
                new_symbol = string[len(prefix)]
            except IndexError:
                last_string = string
                continue
            new_prefix = prefix + new_symbol
            if new_prefix == last_string[:len(new_prefix)]:
                prefix += new_symbol
            last_string = string
        return prefix


sol = Solution()
print(sol.longestCommonPrefix(["flower", "flower", "flower", "flower"]))
