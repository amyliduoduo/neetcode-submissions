class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
       #sort by start time
       #intervals.sort(key=lambda pair:pair[0]) #Sort intervals using the first number of each pair as the sorting key.
       intervals.sort()
       res = [intervals[0]] #Wraps that first interval inside a new list.

       #keep track of previous 
       for start, end in intervals:
            lastEnd = res[-1][1] #end element of the last interval in the result list

            #if current.start <= previous.end:
            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end) #overlap → merge
            else:
                res.append([start, end])#no overlap → add new interval 
       return res