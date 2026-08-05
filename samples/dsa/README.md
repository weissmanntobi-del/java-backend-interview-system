# DSA sample: solve one problem three ways

## Problem

Given an integer array and a target, return the indices of two distinct values whose sum equals the target.

Example:

```text
Input:  [2, 7, 11, 15], target = 9
Output: [0, 1]
```

## Interview progression

### 1. Brute force

Compare every pair.

- Time: `O(n²)`
- Space: `O(1)`
- Benefit: simple and easy to verify
- Limitation: performs unnecessary comparisons

### 2. Structured improvement

Sort value-index pairs and use two pointers.

- Time: `O(n log n)`
- Space: `O(n)` because original indices must be preserved
- Benefit: demonstrates ordered reasoning
- Limitation: sorting is more work than necessary for this exact lookup problem

### 3. Optimised solution

Use a hash map from value to index while scanning once.

- Expected time: `O(n)`
- Space: `O(n)`
- Benefit: checks for the required complement in one pass
- Trade-off: additional memory and hash-table behaviour

Compile and run:

```bash
javac samples/dsa/TwoSumThreeApproaches.java
java -cp samples/dsa TwoSumThreeApproaches
```

During an interview, explain the progression rather than jumping immediately to the final implementation.
