class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_counter = Counter(s1)

        left = 0
        right = len(s1)
        substring_counter = {}

        for i in range(len(s1)):
            print(i)
            substring_counter[s2[i]] = substring_counter.get(s2[i], 0) + 1

        if substring_counter == s1_counter:
            return True

        while right < len(s2):

            # shift window over by 1
            substring_counter[s2[right]] = substring_counter.get(s2[right], 0) + 1
            substring_counter[s2[left]] -= 1
            if substring_counter[s2[left]] == 0:
                del(substring_counter[s2[left]])
            left += 1
            right += 1

            # print("s1 counter = ", s1_counter, "s2 counter = ", substring_counter)
            if substring_counter == s1_counter:
                return True
        
        return False