class TimeMap:
    '''
    we're implmenting a key value store
    along with the ability to set and get
    values according to a timestamp

    we can initialize a default map
    where each key points to a list
    of (value, timestamp) tuples. we 
    know that the timestamp is always
    increasing so we are guaranteed
    to be in sorted order. when we run 
    get, we run binary search to find which
    timestamp prev was the greatest
    '''

    def __init__(self):
        self.collection = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.collection:
            self.collection[key].append((value, timestamp))
        else:
            self.collection[key] = [(value, timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.collection:
            return ""
        arr = self.collection[key]
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        return arr[left - 1][0] if left > 0 else ""
