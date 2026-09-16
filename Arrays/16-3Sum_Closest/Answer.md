# Solution Explanation

## Approach

**Sorting + Two Pointers**

The array is first sorted.

Then, for every possible first element, two pointers are used:

* `left` starts immediately after the first element.
* `right` starts at the end of the array.

The three elements are:

```text
nums[i] + nums[left] + nums[right]
```

We compare this sum with the target and keep track of the sum with the smallest difference from the target.

## Intuition

Sorting the array allows us to determine which pointer should move.

For each fixed `i`:

### If the current sum is smaller than the target

We need a larger sum, so move the left pointer forward:

```text
left += 1
```

### If the current sum is larger than the target

We need a smaller sum, so move the right pointer backward:

```text
right -= 1
```

### If the current sum equals the target

The exact target has been found, so it is the closest possible sum.

## Algorithm

1. Sort the array.
2. Initialize a variable to store the closest sum.
3. Iterate through the array while leaving two positions for the two pointers.
4. For each `i`:

   * Set `left = i + 1`.
   * Set `right = n - 1`.
5. While `left < right`:

   * Calculate the current three-element sum.
   * Calculate its difference from the target.
   * If this difference is smaller than the previously recorded difference, update the closest sum.
   * If the sum is smaller than the target, move `left` forward.
   * Otherwise, move `right` backward.
6. Return the closest sum.

## Example Walkthrough

For:

```text
nums = [-1,2,1,-4]
target = 1
```

After sorting:

```text
[-4,-1,1,2]
```

Consider:

```text
i = 0
left = 1
right = 3
```

The sum is:

```text
-4 + (-1) + 2 = -3
```

Since `-3 < 1`, move `left` forward.

Eventually:

```text
-1 + 1 + 2 = 2
```

The difference from the target is:

```text
|2 - 1| = 1
```

Therefore, the closest sum is:

```text
2
```

## Complexity Analysis

**Time Complexity:** `O(n²)`

Sorting takes `O(n log n)`, and the two-pointer search for each element takes `O(n)`, resulting in `O(n²)` overall.

**Space Complexity:** `O(log n)` to `O(n)` depending on the sorting implementation.

The two-pointer portion itself uses `O(1)` extra space.

## Key Learning

This problem demonstrates how **sorting combined with two pointers** can reduce a three-element search from a brute-force `O(n³)` approach to `O(n²)`.

An important pattern to remember is:

> Fix one element and use two pointers to efficiently search for the remaining two elements.
