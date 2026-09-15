# LeetCode 977 — Squares of a Sorted Array

## Problem

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

## Example 1

**Input:**

```text
nums = [-4,-1,0,3,10]
```

**Output:**

```text
[0,1,9,16,100]
```

## Example 2

**Input:**

```text
nums = [-7,-3,2,3,11]
```

**Output:**

```text
[4,9,9,49,121]
```

## Constraints

* `1 <= nums.length <= 10^4`
* `-10^4 <= nums[i] <= 10^4`
* `nums` is sorted in non-decreasing order.

## Approach

Use the **Two Pointer** technique.

The largest square will always come from either:

* the leftmost negative number, or
* the rightmost positive number.

Use:

```text
left = 0
right = n - 1
```

Compare:

```text
abs(nums[left])
```

with:

```text
abs(nums[right])
```

Place the larger square at the end of the result array and move the corresponding pointer.

## Complexity

* **Time:** `O(n)`
* **Space:** `O(n)` for the result array.
