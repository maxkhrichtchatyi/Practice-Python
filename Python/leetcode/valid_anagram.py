"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.


Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        number_of_additions = 0
        hash_map = {}  # SC O(n)

        for char in s:  # TC O(n)
            hash_map.setdefault(char, 0)
            hash_map[char] += 1
            number_of_additions += 1

        for char in t:  # TC O(n)
            if hash_map.get(char):
                hash_map[char] -= 1
                number_of_additions -= 1

        return not bool(number_of_additions)

# Total: TC O(s+t), SC O(n)
