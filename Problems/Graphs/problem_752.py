# https://leetcode.com/problems/open-the-lock/
class Solution:
    def Increments(w1, w2, w3, w4):
        yield [(w1 + 1) % 10, w2, w3, w4]
        yield [w1, (w2 + 1) % 10, w3, w4]
        yield [w1, w2, (w3 + 1) % 10, w4]
        yield [w1, w2, w3, (w4 + 1) % 10]

    def decrement(w1, w2, w3, w4):
        yield [(w1 - 1) % 10, w2, w3, w4]
        yield [w1, (w2 - 1) % 10, w3, w4]
        yield [w1, w2, (w3 - 1) % 10, w4]
        yield [w1, w2, w3, (w4 - 1) % 10]

    def isTarget(w1, w2, w3, w4, target):
        if w1 == int(target[0]) and w2 == int(target[1]) and w3 == int(target[2]) and w4 == int(target[3]):
            return True
        else:
            return False

    def openLock(self, deadends, target: str) -> int:
        visited = set()
        for i in deadends:
            visited.add((int(i[0]), int(i[1]), int(i[2]), int(i[3])))
        queue = [[0, 0, 0, 0, 0]]
        while len(queue) > 0:
            # print(queue[0])
            # code,turns = queue.pop(0)
            w1, w2, w3, w4, turns = queue.pop(0)
            if (w1, w2, w3, w4) in visited:
                continue
            # print(w1,w2,w3,w4)
            visited.add((w1, w2, w3, w4))
            # print(visited)
            if Solution.isTarget(w1, w2, w3, w4, target):
                return turns
            # wheel1,wheel2,wheel3,wheel4,turns = queue[0]
            for cells in Solution.Increments(w1, w2, w3, w4):
                # print(cells)
                queue.append(
                    [cells[0], cells[1], cells[2], cells[3], turns + 1])
            for cells in Solution.decrement(w1, w2, w3, w4):
                # print(cells)
                queue.append(
                    [cells[0], cells[1], cells[2], cells[3], turns + 1])
        return -1


obj = Solution()
deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
assert obj.openLock(deadends=deadends, target=target) == 6, "Incorrect"
