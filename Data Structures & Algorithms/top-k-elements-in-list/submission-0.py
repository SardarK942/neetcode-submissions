from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        So what we can do is 
        create a sorted hashmap num -> count 
        or should we create a some type of stack/queue where we are always holding the most frequent with size k """

        # for num in nums:
        #     counts[num] = counts.get(num, 0)+1
        counts = Counter(nums)
        heap = []

        for item, count in counts.items():
            heapq.heappush(heap, (count, item))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        for pair in heap: 
            count = pair[0]
            item = pair[1]
            result.append(item)
        return result