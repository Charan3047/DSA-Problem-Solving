# Solution Explanation

## Approach

**Two Pointer Technique**

Since the array is already sorted, duplicate elements are always next to each other.

We can use two pointers:

* `unique_index` → points to the position where the next unique element should be placed.
* `current_index` → scans through the array to find new unique elements.

## Intuition

The first element is always unique, so we start with:

```text
unique_index = 0
current_index = 1
```

For every element:

* If the current element is equal to the previous element, it is a duplicate, so we skip it.
* If it is different, we have found a new unique element.
* Place that element at `unique_index + 1` and move `unique_index` forward.

Because the array is sorted, comparing the current element with the previous element is sufficient to identify duplicates.

## Algorithm

1. Set `unique_index = 0`.
2. Set `current_index = 1`.
3. Traverse the array while `current_index < n`.
4. If `nums[current_index]` is equal to `nums[current_index - 1]`:

   * Move `current_index` forward.
5. Otherwise:

   * Copy `nums[current_index]` to `nums[unique_index + 1]`.
   * Increment `unique_index`.
   * Increment the count of unique elements.
6. Continue until the end of the array.
7. Return the number of unique elements.

## Example Walkthrough

For:

```text
nums = [1,1,2,2,3]
```

Initially:

```text
unique_index = 0
current_index = 1
unique_count = 1
```

### Step 1

`nums[1] = 1` and `nums[0] = 1`

They are equal, so `1` is a duplicate.

Move `current_index`.

### Step 2

`nums[2] = 2` and `nums[1] = 1`

They are different.

Place `2` at the next unique position:

```text
[1,2,2,2,3]
```

### Step 3

`nums[3] = 2` and `nums[2] = 2`

Duplicate → skip.

### Step 4

`nums[4] = 3` and `nums[3] = 2`

They are different.

Place `3` at the next unique position:

```text
[1,2,3,2,3]
```

The first three elements now contain the unique values:

```text
[1,2,3]
```

Therefore, the answer is:

```text
3
```

## Complexity Analysis

**Time Complexity:** `O(n)`

Each element is visited at most once.

**Space Complexity:** `O(1)`

Only a constant number of variables are used, and the array is modified in-place.

## Key Learning

A sorted array provides an important advantage: **duplicates appear consecutively**.

This allows the Two Pointer technique to remove duplicates in-place without using an additional data structure such as a set.

The important pattern to remember is:

> One pointer scans the array while another pointer keeps track of the position for the next valid element.
