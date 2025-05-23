class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        l = len(self.arr)
        if l % 2 == 0:
            return (self.arr[l // 2 - 1] + self.arr[l // 2]) / 2
        else:
            return self.arr[l // 2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()