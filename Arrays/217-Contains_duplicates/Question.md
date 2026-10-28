# LeetCode 217 — Contains Duplicate

## Problem

Given an integer array `nums`, return `True` if any value appears at least twice in the array. Return `False` if every element is distinct.

## Example 1

### Input
```text
nums = [1, 2, 3, 1]
```

### Output
```text
true
```

### Explanation

The element `1` appears twice in the array.

## Example 2

### Input
```text
nums = [1, 2, 3, 4]
```

### Output
```text
false
```

### Explanation

Every element appears exactly once.

## Example 3

### Input
```text
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
```

### Output
```text
true
```

### Explanation

Multiple elements appear more than once.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Technique

- Hash Map
- Duplicate Detection

## Source

[LeetCode 217 — Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
