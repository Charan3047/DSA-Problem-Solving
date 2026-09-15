# LeetCode 977 — Squares of a Sorted Array


## Explanation

The input array is already sorted, but squaring the numbers can destroy that ordering.

For example:

```text
[-7, -3, 2, 3, 11]
```

After squaring:

```text
[49, 9, 4, 9, 121]
```

The largest square must come from one of the two ends.

Therefore, use two pointers:

```text
left  → beginning
right → end
```

Compare the absolute values:

```python
abs(nums[left])
```

and:

```python
abs(nums[right])
```

The larger absolute value produces the larger square.

Put that square at the current position from the **right side** of `res`.

### Example

```text
nums = [-7,-3,2,3,11]

         L           R
        -7          11
```

Compare:

```text
|-7| = 7
|11| = 11
```

So:

```text
11² = 121
```

goes at the end.

Then move `right`.

Continue until all elements are processed.

## Complexity

* **Time:** `O(n)`
* **Space:** `O(n)` for the result array.

## Key DSA Pattern

**Sorted Array + Compare Both Ends → Two Pointers**

This is an important variation of the Two Pointer technique because the array does **not** need to be sorted after squaring; instead, we exploit the fact that the largest absolute values are at the ends.
