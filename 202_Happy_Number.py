

# Problem: Happy Number (LeetCode 202)
# --------------------------------------
# We repeatedly replace n with the sum of squares of its digits.
# If it becomes 1 → happy number; if it loops → not happy.

# Approach1: extract each digit using % and //, sum their squares,
# and use a set to track visited numbers to avoid infinite loops.

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n != 1 and n not in visited:
            visited.add(n)
            total = 0
            num = n
            while num != 0:
                digit = num % 10
                num //= 10
                total += digit * digit
            n = total

        return n == 1

# Approach 2: Convert n to string and directly compute the square of each digit.
# Simpler and shorter than using % and //.
# Use a set to detect loops — if n repeats, we’ll be stuck forever.

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = sum(int(x) ** 2 for x in str(n))
        return n == 1

# Approach 3: Floyd’s Cycle Detection (O(1) space)
# Treat the transformation as a linked list.
# Use two pointers (slow and fast) — if they meet, a cycle exists.
# If any reaches 1, the number is happy.

def next_num(n):
    return sum(int(x) ** 2 for x in str(n))

class Solution:
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while True:
            slow = next_num(slow)
            fast = next_num(next_num(fast))
            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False

sol = Solution()
print(sol.isHappy(19))
print(sol.isHappy(2))

