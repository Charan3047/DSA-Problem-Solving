# LeetCode 26 — Remove Duplicates from Sorted Array

## Problem

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only once.

The relative order of the elements should be kept the same.

Return the number of unique elements in `nums`.

The first `k` elements of `nums` should contain the unique elements, where `k` is the number of unique elements.

The remaining elements beyond `k` do not matter.

## Example 1

### Input

```text
nums = [1,1,2]
```

### Output

```text
2
```

### Explanation

The first two elements of `nums` should be:

```text
[1,2]
```

The number of unique elements is `2`.

## Example 2

### Input

```text
nums = [0,0,1,1,1,2,2,3,3,4]
```

### Output

```text
5
```

### Explanation

The first five elements of `nums` should be:

```text
[0,1,2,3,4]
```

The number of unique elements is `5`.

## Constraints

* `1 <= nums.length <= 3 * 10⁴`
* `-100 <= nums[i] <= 100`
* `nums` is sorted in non-decreasing order.

## Requirements

* Modify the array **in-place**.
* Preserve the relative order of the unique elements.
* Use constant extra space.

## Source

[LeetCode 26 — Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
