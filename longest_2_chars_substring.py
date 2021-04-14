# Find longest substring with at most 2 distinct characters.


def find_substring(s: str) -> str:
    """Function returns a substring of string 's'
    that contains no more than 2 distinct characters.
    """
    # On each iteration take substrings of the original string
    # moving a 'sliding window' of gradually decreasing size
    # from left to right with step=1.
    n_segments = 0
    for i in range(len(s)):
        n_segments += 1  # 1 segment means take whole string
        segment_len = len(s) - i  # window size
        for j in range(n_segments):
            substring = s[j:j + segment_len]
            # We go from largest substrings to smallest.
            # As soon as we found substring with 2 distinct chars,
            # it is the longest possible substring.
            if len(set(substring)) == 2:
                return substring
    # This case would only be possible, if len(s) < 2
    return ''


s = 'aabbbcccd'
print(find_substring(s))
