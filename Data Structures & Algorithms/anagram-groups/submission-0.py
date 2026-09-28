class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = []
        for word in strs:
            arr.append(''.join(sorted(word)))

        dic = {}
        for i in range(len(arr)):
            if arr[i] in dic:
                dic[arr[i]].append(strs[i])
            else:
                dic[arr[i]] = [strs[i]]

        arr2 = []
        for value in dic.values():
            arr2.append(value)

        return arr2