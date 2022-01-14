class Solution:

    def duplicateZeros(self, arr: List[int]) -> None:
        queue = []

        for i in range(0, len(arr)):
            queue.append(arr[i])

            if arr[i] == 0:
                queue.append(0)

            arr[i] = queue.pop()
