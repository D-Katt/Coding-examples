# Given a string s and a dictionary of strings wordDict, return true if s can be segmented
# into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false

# Constraints:
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.

s = 'catsandog'
word_dict = ["cats", "dog", "sand", "and", "cat"]

# Turn the list into a set for faster lookups
word_dict = set(word_dict)


def split_word(s: str) -> bool:
    """Function splits characters sequence into words
    up to 20 letters in length and looks up these words
    in the dictionary. Returns True if the splitting
    is successful, otherwise returns False.
    :argument s: String of words without spaces
    """

    def dfs(remaining_s: str) -> bool:
        # If there are no more letters remaining in the string,
        # it means all previous letters were split into valid words.
        if len(remaining_s) == 0:
            return True
        # Words starting from the beginning of the remaining string
        for i in range(20):
            sub_s = remaining_s[:i]
            # If the word exists, call this function with the remaining part of the string
            if sub_s in word_dict:
                result = dfs(remaining_s[i:])
                if result:
                    # Point of success
                    return True
        # Impossible to split
        return False

    result = dfs(s)
    return result


print(split_word(s))
