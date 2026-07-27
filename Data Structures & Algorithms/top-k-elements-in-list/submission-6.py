#bucket sort solution

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        #By using an array as your buckets where the index = frequency
        #To get the top $K$ frequent elements, you simply start at the very last index of the array (the highest possible frequency) and walk backward toward 0.
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        #The count variable is a standard dictionary holding your frequencies (e.g., {1: 3, 2: 2, 3: 1}).
        #Calling .items() unpacks that dictionary into a list of pairs (tuples) like this:[(1, 3), (2, 2), (3, 1)]
        for n, cnt in count.items():
            freq[cnt].append(n)

        res = []
        #syntax range(start, stop, step)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res  