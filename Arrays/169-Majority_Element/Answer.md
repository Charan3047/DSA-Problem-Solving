# Solution Explanation

## Approach

**Hash Map / Frequency Counting**

Use a dictionary to count the frequency of each element. Then identify the element with the highest frequency and check whether it appears more than half the size of the array.

## Intuition

The dictionary stores each number as a key and its occurrence count as the value.

For example:

```text
nums = [2, 2, 1, 1, 1, 2, 2]
```

Frequency table:

```text
2 → 4
1 → 3
```

Since `2` appears four times and `4 > 7 // 2`, the majority element is `2`.

## Algorithm

1. Create an empty dictionary named `frequency`.
2. Traverse the array and count each element's occurrences.
3. Initialize the candidate majority element.
4. Find the element with the highest frequency.
5. Check whether its frequency is greater than `len(nums) // 2`.
6. Return the element if the condition is satisfied; otherwise, return `None`.

## Complexity Analysis

- **Time Complexity:** `O(n)` average — one traversal to count frequencies and another traversal over the dictionary.
- **Auxiliary Space Complexity:** `O(n)` — the dictionary may store up to `n` distinct elements.

## Key Learning

A hash map is useful when a problem requires counting occurrences or comparing frequencies.

This approach is straightforward and easy to understand. A more space-efficient alternative is the **Boyer–Moore Voting Algorithm**, which uses `O(1)` auxiliary space.

**Pattern:** Hash Map + Frequency Counting.
