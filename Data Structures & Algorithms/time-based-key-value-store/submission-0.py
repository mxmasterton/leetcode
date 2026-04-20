class TimeMap:
    def __init__(self):
        self.key_store = {} # key: list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_store:
            self.key_store[key] = []
        self.key_store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.key_store.get(key, [])

        left_pointer = 0
        right_pointer = len(values) - 1
        while left_pointer <= right_pointer:
            middle = (left_pointer + right_pointer) // 2
            if values[middle][1] <= timestamp:
                result = values[middle][0]
                left_pointer = middle + 1
            else:
                right_pointer = middle - 1

        return result