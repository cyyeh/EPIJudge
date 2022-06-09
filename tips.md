# Top tips

## I. The Interview

### Getting Ready

### Strategies For A Great Interview

### Conducting An Interview

## II. Data Structures and Algorithms

### Primitive Types

### Arrays

1. Array problems often have simple brute-force solutions that use O(n) space, but there are subtler solutions that use the array itself to reduce space complexity to O(1).
2. Filling an array from the front is slow, so see if it's possible to write values from the back
3. Instead of deleting an entry (which requires moving all entries to its left), consider overwriting it.
4. When dealing with integers encoded by an array consider processing the digits from the back of the array. Alternately, reverse the array so the least-significant digit is the first entry.
5. Be comfortable with writing code that operates on subarrays
6. It's incredibly easy to make off-by-l errors when operating on arrays-reading past the last element of an array is a common error which has catastrophic consequences.
7. Don't worry about preserving the integrity of the array (sortedness, keeping equal entries together, etc.) until it is time to return.
8. An array can serve as a good data structure when you know the distribution of the elements in advance. For example, a Boolean array of length W is a good choice for representing a subset of {0,1,...,W-1}. (When using a Boolean array to represent a subset of {1,2,3,...,n}, allocate an array of size n+1 to simplify indexing.).
9. When operating on 2D arrays, use parallel logic for rows and for columns
10. Sometimes it's easier to simulate the specification, than to analytically solve for the result. For example, rather than writing a formula for the i-th entry in the spiral order for an n x n matrix, just compute the output from the beginning.

### Strings

### Linked Lists

### Stacks and Queues

### Binary Trees

### Heaps

### Searching

### Hash Tables

### Sorting

### Binary Search Trees

### Recursion

### Dynamic Programming

### Greedy Algorithms and Invariants

### Graphs

### Parallel Computing

## III. Domain Specific Problems

### Design Problems

### Language Questions

- garbage collection
  - What is garbage collection? Explain it in the context of Python.
- closure
  - What does the following program print, and why?
  ```
  increment_by_i = [lambda x: x + i for i in range(10)]
  print(increment_by_i[3](4))
  ```
- shallow and deep copy
  - Describe the differences between a shallow copy and a deep copy. When is each appropriate, and when is neither appropriate? How is deep copy implemented?
- iterators and generators
  - What is the difference between an iterator and a generator?
- `@decorator`
  - Explain what a decorator is, with an example that shows why its useful.
- list vs tuple
  - In what ways are lists and tuples similar, and in what ways are they different?
- `*args` and `**kwargs`
  - What are `*args` and `**kwargs`? Where are they appropriate?
- python code
  - `zip()`, `functools.reduce()`, `heapq.nlargest()`, `sum`, `collections.defaultdict`
- exception handling
  - `try`, `except`, `else`, `finally`, `raise`
- scoping
  - searching order
    - the current function
    - enclosing scopes
    - the module containing the code(also referred to as the global scope)
    - the built-in scope
    - `NameError` is raised if none of these contain a defined variable with the given name
  - `global`, `nonlocal`
  - resolving local variable referenced before assignment
- function arguments
  - positional, keyword, default arguments

### Object-Oriented Design

### Common Tools

## IV. The Honors Class

### Honors Class