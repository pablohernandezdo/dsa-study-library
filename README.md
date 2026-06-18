# DSA Learning Library

[![CI](https://github.com/pablohernandezdo/dsa-study-library/actions/workflows/ci.yml/badge.svg)](https://github.com/pablohernandezdo/dsa-study-library/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/dsa-study)](https://pypi.org/project/dsa-study/)
[![Python](https://img.shields.io/pypi/pyversions/dsa-study.svg)](https://pypi.org/project/dsa-study/)
[![License](https://img.shields.io/github/license/pablohernandezdo/dsa-study-library)](https://github.com/pablohernandezdo/dsa-study-library/blob/main/LICENSE)

Educational implementations of common data structures and algorithms written in clean, typed, idiomatic Python.

> ⚠️ This project is currently under active development and is primarily intended for learning and educational purposes.

## Motivation

This project started as part of my journey to build strong software engineering fundamentals.

The goal is not only to study data structures and algorithms, but also to apply software engineering practices such as:

- API design
- Type hints
- Testing
- Documentation
- Packaging
- Versioning

This repository serves both as:

- A learning project
- A reference implementation for my personal knowledge base

## Project Goals

This library aims to be:

1. Easy to use
2. Easy to extend
3. Easy to maintain

The primary objective is clarity and educational value.

Implementations are designed to clearly communicate the underlying ideas behind each data structure and algorithm.

Performance and memory optimizations are considered when they help explain the concepts (for example, path compression in Union-Find), but maximum performance is not the primary goal.

## Design Principles

### Data Structures Own Their Data

Data structures are responsible for storing and managing their internal state.

Examples:

- `LinkedList.append()`
- `BinarySearchTree.insert()`
- `Graph.add_edge()`

### Algorithms Are Standalone

Algorithms operate on data structures but are not part of them.

Examples:

- `breadth_first_search(graph)`
- `depth_first_search(graph)`
- `dijkstra(graph)`
- `topological_sort(graph)`

This separation keeps data structures focused and makes algorithms reusable.

### Explicit and Readable APIs

Public APIs favor clarity over brevity.

Examples:

```python
breadth_first_search(graph)
depth_first_search(graph)
binary_search(array, target)
```

instead of abbreviated names.

### Strong Typing

All public interfaces use Python type hints.

### Pythonic Error Handling

Operations raise exceptions when invalid usage occurs rather than silently returning `None`.

### Educational First

The code prioritizes readability and learning value.

Implementation choices should make the underlying concepts easy to understand.

## Project Structure

```text
src/
└── dsa/
    ├── algorithms/
    ├── data_structures/
    └── graph/
```

## Implemented Data Structures

### Linear Structures

- [X] Linked List
- [X] Doubly Linked List
- [X] Stack
- [X] Queue
- [X] Deque
- [X] Priority Queue

### Hash Based Structures

- [X] Hash Map Chaining
- [ ] Hash Map Open Addressing
- [X] Hash Set

### Tree Structures

- [X] Binary Heap
- [ ] Binary Search Tree

### Advanced Trees

- [ ] Trie

### Graph Structures

- [ ] Graph (Adjacency List)

### Disjoint Sets

- [ ] Union-Find

## Implemented Algorithms

### Graph Algorithms

- [ ] Breadth-First Search (BFS)
- [ ] Depth-First Search (DFS)
- [ ] Topological Sort (Kahn)
- [ ] Topological Sort (DFS)
- [ ] Dijkstra
- [ ] Prim
- [ ] Kruskal

### Sorting Algorithms

- [ ] Bubble Sort
- [ ] Selection Sort
- [ ] Insertion Sort
- [ ] Merge Sort
- [ ] Quick Sort
- [ ] Heap Sort

### Searching Algorithms

- [ ] Binary Search

## Testing Philosophy

Every implementation should include tests covering:

- Happy path scenarios
- Edge cases
- Empty inputs
- Invalid inputs

## Usage

Installation:

```
pip install dsa-study
```

Installation from source:

```bash
git clone https://github.com/pablohernandezdo/dsa-study-library.git
cd dsa-study-library
uv sync
```

Example:

```python
from dsa.data_structures.linked_list import LinkedList

ll = LinkedList([1, 2, 3])

ll.insert_front(0)   # [0, 1, 2, 3]
ll.insert_back(4)    # [0, 1, 2, 3, 4]
ll.find(3)           # 3
ll.delete(2)         # [0, 1, 3, 4]
```

## Future Work

### Type System

- Learn generic types (`TypeVar`, `Generic`)
- Make data structures generic

### Graphs

- Additional graph representations
- Weighted graph abstractions

### Algorithms

- Dynamic Programming
- Greedy Algorithms
- Backtracking
- String Algorithms

### Tooling

- Automated testing with GitHub Actions
- PyPI publication
- API documentation generation

## Versioning

This project follows Semantic Versioning.

Releases are tracked through:

- `pyproject.toml`
- Git tags
- GitHub releases