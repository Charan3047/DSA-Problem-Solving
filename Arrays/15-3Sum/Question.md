# LeetCode 15 — 3Sum

## Problem

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:

* `i != j`
* `i != k`
* `j != k`
* `nums[i] + nums[j] + nums[k] == 0`

The solution set must not contain duplicate triplets.

## Example 1

**Input:**

```text
nums = [-1,0,1,2,-1,-4]
```

**Output:**

```text
[[-1,-1,2],[-1,0,1]]
```

## Example 2

**Input:**

```text
nums = [0,1,1]
```

**Output:**

```text
[]
```

## Example 3

**Input:**

```text
nums = [0,0,0]
```

**Output:**

```text
[[0,0,0]]
```

## Constraints

* `3 <= nums.length <= 3000`
* `-10^5 <= nums[i] <= 10^5`

## Approach

Use the **Two Pointer** technique:

1. Sort the array.
2. Fix one element `nums[i]`.
3. Use two pointers:

   * `left = i + 1`
   * `right = n - 1`
4. Move the pointers based on the current sum.
5. Skip duplicate values to avoid duplicate triplets.

## Complexity

* **Time:** `O(n²)`
* **Space:** `O(n)` due to sorting a copy of the array.
