# Solution Explanation

## Approach

**Hash Map + Sorting**

Use a dictionary to count the frequency of each element. Then sort the distinct elements according to their frequencies in descending order and return the first `k` elements.

## Intuition

The dictionary stores each number as a key and its frequency as the value.

For example:

```text
nums = [1,1,1,2,2,3]
```

The frequency dictionary becomes:

```text
1 → 3
2 → 2
3 → 1
```

Sorting the numbers by frequency in descending order gives:

```text
[1,2,3]
```

Since `k = 2`, return the first two elements:

```text
[1,2]
```

## Algorithm

1. Create an empty dictionary named `frequency`.
2. Traverse `nums` and count each element's occurrences.
3. Sort the dictionary's keys by their frequencies in descending order.
4. Return the first `k` elements from the sorted result.

## Complexity Analysis

Let:
- `n` be the length of `nums`.
- `m` be the number of distinct elements.

**Time Complexity:** `O(n + m log m)`

- Counting frequencies takes `O(n)` average time.
- Sorting the distinct elements takes `O(m log m)` time.

**Auxiliary Space Complexity:** `O(m)`

The frequency dictionary and sorted list require space proportional to the number of distinct elements.

## Key Learning

A hash map makes frequency counting efficient. Sorting the distinct elements by their frequencies then allows us to select the `k` most frequent elements.

**Pattern:** Hash Map + Frequency Counting + Sorting.

## Further Optimization

A bucket sort approach can solve this problem in `O(n)` time by grouping elements according to their frequencies, avoiding the need to sort all distinct elements.
