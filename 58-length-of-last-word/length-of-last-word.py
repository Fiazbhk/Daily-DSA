class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        a = s.split()
        print(a)
        if a:
            return len(a[-1])
        return 0
        
    # T C = O(n)
    # S C = O(n)