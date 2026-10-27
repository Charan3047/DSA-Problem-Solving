# Solution Explanation

## Approach

**Right-to-Left Traversal**

Traverse the array from right to left while maintaining the maximum element encountered so far.

An element is a leader if it is greater than or equal to every element to its right.

## Intuition

Instead of checking every element against all elements to its right, maintain a running maximum.

- If the current element is greater than the maximum seen so far, it is a leader.
- Update the maximum whenever a new leader is found.
- Since the traversal happens from right to left, reverse the collected leaders before returning them.

## Algorithm

1. Initialize an empty list `leaders`.
2. Initialize `max_so_far` to negative infinity.
3. Traverse the array in reverse.
4. If the current element is greater than `max_so_far`:
   - Add it to `leaders`.
   - Update `max_so_far`.
5. Reverse the `leaders` list.
6. Return the result.

## Example Walkthrough

Input:

```text
nums = [16, 17, 4, 3, 5, 2]
```

Traversal from right to left:

| Current element | Maximum so far | Leader? |
|---:|---:|---|
| 2 | 2 | Yes |
| 5 | 5 | Yes |
| 3 | 5 | No |
| 4 | 5 | No |
| 17 | 17 | Yes |
| 16 | 17 | No |

Collected leaders:

```text
[2, 5, 17]
```

After reversing:

```text
[17, 5, 2]
```

## Complexity Analysis

- **Time Complexity:** `O(n)` — each element is visited once, excluding the linear-time reversal, which keeps the overall complexity `O(n)`.
- **Auxiliary Space Complexity:** `O(n)` — the result list and the reversed-list slice require additional space.

## Key Learning

Maintaining a running maximum allows us to solve the problem in linear time instead of comparing every element with all elements to its right.

**Pattern:** Right-to-left traversal + running maximum.
