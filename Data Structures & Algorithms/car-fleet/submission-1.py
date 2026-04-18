class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        cars = [[position, (target - position) / speed] for position, speed in zip(positions, speeds)]
        # (position, time you get there)
        cars.sort()

        stack = [cars[-1][1]]
        for i in range(len(cars) - 2, -1, -1):
            if cars[i][1] <= stack[-1]:
                continue
            else:
                stack.append(cars[i][1])
        
        return len(stack)

            

            
