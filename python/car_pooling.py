import heapq

class Solution:
  def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    trips.sort(key = lambda t: t[1])
    heap = [] # (end, num)
    current_passengers = 0
    for t in trips:
      num, start, end = t
      while heap and heap[0][0] <= start: # number of completed
        current_passengers -= heap[0][1]
        heapq.heappop(heap)

      current_passengers += num # current number of passenger
      if current_passengers > capacity:
        return False
      heapq.heappush(heap, [end, num])
    
    return True

  def fast_car_pooling(self, trips: List[List[int]], capacity: int) -> bool:
    # check 0 - 1000 since that is the boundary
    passenger_changed = [0] * 1001
    
    for t in trips:
      num, start, end = t
      passenger_changed[start] += num
      passenger_changed[end] -= num

    current_passengers = 0
    for i in range(1001):
      current_passengers += passenger_changed[i]
      if current_passengers > capacity:
        return False
    
    return True