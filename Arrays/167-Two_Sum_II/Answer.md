# 2️⃣ `Answer.md`

## Approach

Two Pointer Technique

## Intuition

The array is already sorted, so we can use two pointers:

- `left` starts at the beginning.
- `right` starts at the end.

Calculate the sum of the elements at both pointers.

- If the sum equals the target, we found the answer.
- If the sum is smaller than the target, move `left` forward.
- If the sum is larger than the target, move `right` backward.

Because the array is sorted, each pointer movement eliminates
unnecessary possibilities.

## Algorithm

1. Initialize `left = 0`.
2. Initialize `right = len(numbers) - 1`.
3. While `left < right`:
   - Calculate the current sum.
   - If it equals the target, return the indices.
   - If it is smaller, increment `left`.
   - Otherwise, decrement `right`.
4. Return an empty array if no solution exists.

## Complexity Analysis

- Time Complexity: O(n)
- Space Complexity: O(1)

## Key Learning

A sorted array allows the Two Pointer technique to solve this problem
in linear time without using additional data structures.
