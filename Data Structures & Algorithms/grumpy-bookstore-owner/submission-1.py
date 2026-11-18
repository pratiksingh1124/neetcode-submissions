class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0
        window = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfied += customers[i]

            if i < minutes and grumpy[i] == 1:
                window += customers[i]

        max_extra = window

        for i in range(minutes, len(customers)):
            if grumpy[i - minutes] == 1:
                window -= customers[i - minutes]

            if grumpy[i] == 1:
                window += customers[i]

            max_extra = max(max_extra, window)

        return satisfied + max_extra
   
    
        