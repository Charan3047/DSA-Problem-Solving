# LeetCode 15 — 3Sum

## Solution

```python
class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        res = []

        a = sorted(nums)

        for i in range(n - 2):
            if i > 0 and a[i] == a[i - 1]:
                continue

            if a[i] > 0:
                break

            left = i + 1
            right = n - 1
            target = -a[i]

            while left < right:
                s = a[left] + a[right]

                if s == target:
                    res.append([a[i], a[left], a[right]])

                    left += 1
                    right -= 1

                    while left < right and a[left] == a[left - 1]:
                        left += 1

                    while left < right and a[right] == a[right + 1]:
                        right -= 1

                elif s < target:
                    left += 1

                else:
                    right -= 1

        return res
```

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
