class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort

        #create hashmap to count the frequency of each number, key is the element, value is the freqe-uency
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        #create an array of empty buckets
        freq = [[] for i in range(len(nums) + 1)]
        #place element n into freq[index] since count[n] = index, index of the bucket represents the frequency
        for n, index in count.items():
            freq[index].append(n)
        
        #collect the top k elements
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



