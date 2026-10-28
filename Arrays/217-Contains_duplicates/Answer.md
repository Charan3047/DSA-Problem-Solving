# Solution Explanation

## Approach

**Hash Map / Duplicate Detection**

Use a dictionary to track the elements that have already appeared in the array.

If an element is encountered again, a duplicate exists, and we can immediately return `True`.

If the entire array is traversed without finding a duplicate, return `False`.

## Intuition

We do not need to count the frequency of every element. We only need to know whether an element has appeared before.

For example:

```text
nums = [1, 2, 3, 1]
```

Traversal:

1. `1` is new, so store it.
2. `2` is new, so store it.
3. `3` is new, so store it.
4. `1` already exists in the dictionary, so return `True`.

## Algorithm

1. Initialize an empty dictionary named `seen`.
2. Traverse every number in `nums`.
3. If the number is not in `seen`, add it.
4. Otherwise, return `True`.
5. If the loop finishes, return `False`.

## Complexity Analysis

**Time Complexity:** `O(n)` average, where `n` is the length of the array. Dictionary lookups and insertions take expected constant time.

**Auxiliary Space Complexity:** `O(n)` in the worst case, when all elements are distinct and stored in the dictionary.

## Key Learning

A hash map allows us to detect duplicates without comparing every element against every other element.

A **hash set** can solve the same problem more naturally because we only need to track whether an element has been seen, not its frequency.

**Pattern:** Hashing + Duplicate Detection.
