# Solution Explanation

## Approach

**Hash Map / Frequency Counting**

A dictionary is used to keep track of how many times each number appears in the array.

The dictionary stores:

```text
number → frequency
```

After counting all the elements, we iterate through the dictionary and find the number whose frequency is `1`.

## Intuition

Since every number appears exactly twice except one number, we can count the occurrences of each number.

For example:

```text
nums = [4,1,2,1,2]
```

The frequency dictionary becomes:

```text
4 → 1
1 → 2
2 → 2
```

Only `4` has a frequency of `1`, so `4` is the answer.

## Algorithm

1. Create an empty dictionary called `frequency`.
2. Traverse every number in `nums`.
3. If the number already exists in the dictionary:

   * Increase its frequency by `1`.
4. Otherwise:

   * Add the number to the dictionary with a frequency of `1`.
5. Traverse the dictionary.
6. Find the number whose frequency is `1`.
7. Return that number.

## Example Walkthrough

For:

```text
nums = [4,1,2,1,2]
```

After processing the array:

```text
frequency = {
    4: 1,
    1: 2,
    2: 2
}
```

Now check the frequencies:

```text
4 → 1
1 → 2
2 → 2
```

The number with frequency `1` is:

```text
4
```

Therefore:

```text
Answer = 4
```

## Complexity Analysis

**Time Complexity:** `O(n)`

The array is traversed to build the frequency dictionary, and the dictionary is traversed to find the unique element.

**Space Complexity:** `O(n)`

In the worst case, the dictionary can contain `O(n)` distinct elements.

## Key Learning

A **hash map** can efficiently store and retrieve information associated with each value.

This problem is a good example of using a dictionary for **frequency counting**.

Another important solution to this problem uses the **XOR bitwise operation**, which can achieve `O(n)` time and `O(1)` extra space.

The hash-map approach helped establish the basic frequency-counting pattern before exploring the more space-efficient XOR approach.
