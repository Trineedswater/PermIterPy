# PermIterPy
A small python library used to generate permuations of integers in iterative calls. It uses an implementation of Heap's algorithm to generate each permutation. The aim of this library is to optimize the space and time complexity tradeoff for Heap's algorithm - where a recursive approach is used to generate a stack of swaps and then execute them after each call.

## Table of Contents

- [PermIterPy](#PermIterPy)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)

## Installation

No installation, just download the package into your project and call the function.

## Usage

Initialise the PermIter object and obtain the next permutation by calling next_permutation().

```python
perm = Permutation(10)
a = perm.next_permutation()
b = perm.next_permutation()
print(a, b)
```
