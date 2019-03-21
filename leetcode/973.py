# K Closest Points to Origin
# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
# (Here, the distance between two points on a plane is the Euclidean distance.)
# You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

import heapq
class Solution:
    def e_distance(self, point):
        return point[0]*point[0] + point[1]*point[1]

    #  344 ms, faster than 80.80%
    def kClosest(self, points: 'List[List[int]]', K: 'int') -> 'List[List[int]]':
        heap = []
        for point in points:
            heapq.heappush(heap, (-self.e_distance(point), point))
            if len(heap) > K:
                heapq.heappop(heap)
        return [b for a,b in heap]

points = [[1,3],[-2,2], [10,10]]
print(Solution().kClosest(points, 1))