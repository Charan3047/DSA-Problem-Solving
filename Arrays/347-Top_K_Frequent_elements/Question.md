# LeetCode 347 — Top K Frequent Elements

## Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

You may return the answer in any order.

## Example 1

### Input

```text
nums = [1,1,1,2,2,3]
k = 2
```

### Output

```text
[1,2]
```

### Explanation

- `1` appears 3 times.
- `2` appears 2 times.
- `3` appears 1 time.

The two most frequent elements are `1` and `2`.

## Example 2

### Input

```text
nums = [1]
k = 1
```

### Output

```text
[1]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `k` is in the range `[1, number of distinct elements in nums]`.
- The answer is guaranteed to be unique.

## Technique

- Hash Map / Frequency Counting
- Sorting by Frequency

## Source

[LeetCode 347 — Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
