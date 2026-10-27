# Leaders in an Array

## Problem

Given an array of integers `nums`, find all the leaders in the array.

An element is called a **leader** if it is greater than or equal to every element to its right. The rightmost element is always a leader.

Return the leaders in the same order as they appear in the original array.

## Example 1

### Input
```text
nums = [16, 17, 4, 3, 5, 2]
```

### Output
```text
[17, 5, 2]
```

### Explanation

- `17` is greater than every element to its right.
- `5` is greater than every element to its right.
- `2` is the rightmost element, so it is a leader.

## Example 2

### Input
```text
nums = [1, 2, 3, 4, 0]
```

### Output
```text
[4, 0]
```

## Example 3

### Input
```text
nums = [7, 10, 4, 10, 6, 5, 2]
```

### Output
```text
[10, 10, 6, 5, 2]
```

## Constraints

- The array contains at least one element.
- Array elements may be positive, zero, or negative integers.

## Technique

- Array Traversal
- Right-to-Left Traversal
- Maintaining the Maximum Element

## Source

Practice problem: Leaders in an Array.
