class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        # Use the shortest string to avoid index errors
        minimum = min(strs, key=len)
        pref = ""

        for i in range(len(minimum)):
            count = 0
            for j in range(1, len(strs)):
                if strs[j][i] == minimum[i]:
                    count += 1
            if count == len(strs) - 1:
                pref += minimum[i]
            else:
                break  # Stop when mismatch occurs

        return pref