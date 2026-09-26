class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # M-1 Brute Force
        # sortedS = ''.join(sorted(s))
        # sortedT = ''.join(sorted(t))

        # if sortedS == sortedT:
        #     return True
        # return False

        # M-2
        if len(s) != len(t):
            return False
        freqS = {}
        freqT = {}
        for ch in s:
            if ch in freqS:
                freqS[ch] += 1
            else:
                freqS[ch] = 1
        for ch in t:
            if ch in freqT:
                freqT[ch] += 1
            else:
                freqT[ch] = 1

        return (freqS == freqT)        