# Majority Element

## Problem

Given an array of integers `nums` of size `n`, find the majority element.

A **majority element** is an element that appears more than `n // 2` times in the array.

If no majority element exists, return `None` for this implementation.

## Example 1

### Input
```text
nums = [3, 2, 3]
```

### Output
```text
3
```

### Explanation

The element `3` appears twice, which is more than `3 // 2`.

## Example 2

### Input
```text
nums = [2, 2, 1, 1, 1, 2, 2]
```

### Output
```text
2
```

### Explanation

The element `2` appears four times, which is more than `7 // 2`.

## Example 3

### Input
```text
nums = [1, 2, 3]
```

### Output
```text
None
```

### Explanation

No element appears more than half the length of the array.

## Constraints

- The array contains at least one element.
- Array elements are integers.

## Technique

- Hash Map
- Frequency Counting

## Source

Practice problem: Majority Element.
