# 8-Puzzle Solver
![puzzle gif](8-puzzle.gif)
## Table of Contents
1. [Introduction](#introduction)
2. [Description](#description)
3. [Usage](#usage)
4. [Supported Algorithms](#supported-algorithms)
5. [Input Format](#input-format)
6. [Output Format](#output-format)
7. [Examples](#examples)
8. [Performance and Memory](#performance-and-memory)
9. [Code File](#code-file)
10. [Report PDF](#report-pdf)

## Introduction
This repository contains a Python program to solve the classic 8-puzzle problem using various search algorithms. The project offers a comprehensive exploration of different search strategies to find the optimal solution for this challenging AI problem.

## Description
The code implements the following search algorithms:
- A* (A-star)
- Breadth-First Search (BFS)
- Iterative Deepening Search (IDS)
- Depth-First Search (DFS)

## Usage
To use this program, provide input puzzle configurations in the specified format (explained below) and run the solver with your chosen algorithm. The program will output the solution path and memory consumption.

## Supported Algorithms
- A* (A-star): `A_star(root, goal)`
- Breadth-First Search (BFS): `bfs(root, goal)`
- Iterative Deepening Search (IDS): `ids(root, goal)`
- Depth-First Search (DFS): `dfs(root, goal)`

## Input Format
Input puzzle configurations should be provided in the following format, where `0` represents the empty space:

```
{1, 4, 2, 6, 5, 8, 7, 3, 0}
```

## Output Format
The program will return a tuple containing the solution path, depth, and execution time. If a solution is not found, it returns `-1`. The output format for each example should be in this format:

```
Solution Path: ['D', 'R', 'U', 'L', 'D', 'R', 'R']
Depth: 7
Execution Time: 0.001394 seconds
Memory Usage: 6.925KB
```

## Examples
Check the "Examples.txt" file for sample input configurations, and the corresponding results are recorded in the "out.txt" file.

## Performance and Memory
The program includes memory tracking to measure memory consumption during execution. Results are displayed in the output file ("out.txt"). Note that long execution times may trigger a timeout mechanism.

## Code File
The Python code for this project can be found in [assignment2-babaahmadiNarges-610398102.py](assignment2-babaahmadiNarges-610398102.py).

## Report PDF
The detailed report for this project is available in [report-hw2-babaahmadi-narges-610398102.pdf](report-hw2-babaahmadi-narges-610398102.pdf).
