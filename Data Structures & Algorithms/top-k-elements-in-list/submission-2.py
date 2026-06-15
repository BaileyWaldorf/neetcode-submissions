class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        print(counter)
        bucket = {}
        highest = 0
        most_freq = []

        for num in counter:
            count = counter[num]
            highest = max(highest, count)

            if bucket.get(count):
                bucket[count].append(num)
            else:
                bucket[count] = [num]
        
        print(bucket)

        for i in range(highest):
            freq = highest - i
            if bucket.get(freq) and k > 0:
                print(bucket[freq])
                most_freq.extend(bucket[freq])
                k -= len(bucket[freq])
        
        return most_freq
            

