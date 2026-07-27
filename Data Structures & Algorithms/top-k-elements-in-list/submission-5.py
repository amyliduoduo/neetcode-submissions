class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap number - frequency, create an array and sort by frequency - take the top k
        count = {}

        #count frequencies
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        #create an array to sort the frequency
        arr = []
        for n, freq in count.items(): #.items() allows you to loop through both the key (n) and the value (freq) at the exact same time.
            arr.append([freq, n]) #flips the order to frequency - number
        arr.sort() #sort based on the first element which is frequency here

        #create an empty result list
        res = []
        #repeatedly pop from the end of te sorted list(highest frequency) and append the number to the result.
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
