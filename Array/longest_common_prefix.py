from typing import List

class Solution:
    def longestCommonPrefix(self, words: List[str]) -> str:
        # Handle the case where the input list is empty
        if not words:
            return ""
        
        common_prefix = ""
        
        for i in range(len(words[0])):
            char = words[0][i]
            for word in words:
                if i >= len(word) or word[i] != char:
                    return common_prefix
            common_prefix += char
        
        return common_prefix
