# LeetCode 15 — 3Sum

## Explanation

First, sort the array.

For every index `i`, treat `a[i]` as the first number of the triplet. We then need to find two numbers whose sum is:

```text
target = -a[i]
```

Use two pointers:

```text
left  → i + 1
right → n - 1
```

### Pointer movement

If:

```text
a[left] + a[right] < target
```

we need a larger sum, so:

```python
left += 1
```

If:

```text
a[left] + a[right] > target
```

we need a smaller sum, so:

```python
right -= 1
```

If they are equal, we found a valid triplet.

### Duplicate Handling

Skip duplicate values for `i`:

```python
if i > 0 and a[i] == a[i - 1]:
    continue
```

After finding a triplet, skip duplicate `left` and `right` values as well.

### Optimization

If:

```python
a[i] > 0
```

we can stop because the array is sorted and all remaining numbers are positive. Therefore, their sum cannot be `0`.

## Complexity

* **Time:** `O(n²)`
* **Space:** `O(n)` because `sorted(nums)` creates a new sorted list.

## Key DSA Pattern

**Sorted Array + Find Pair → Two Pointers**

3Sum is essentially:

> **Fix one element + solve Two Sum using Two Pointers**
