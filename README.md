# Set Packing Problem

## Problem Description

The **Set Packing Problem** is a combinatorial decision problem where the objective is to determine if there exists a collection of disjoint subsets from a given set of subsets such that the collection contains at least a specified number of subsets.

### Parameters:
- **Universe (U)**: The set of all elements.
- **Subsets (S)**: A collection of subsets of \( U \).
- **Threshold (T)**: The minimum number of disjoint subsets required.

### Constraints:
1. Subsets in the solution must be pairwise disjoint.
2. At least \( T \) subsets must be selected.

---

## CNF Encoding

The Set Packing Problem is encoded into DIMACS CNF format for compatibility with SAT solvers such as Glucose. The encoding involves the following steps:

### Propositional Variables
- Each subset \( S_i \) is represented by a propositional variable `x_i`, where:
  - `x_i = true` indicates that subset \( S_i \) is selected.
  - `x_i = false` indicates that subset \( S_i \) is not selected.
- The total number of variables equals the number of subsets.

### Encoding Constraints
1. **Disjoint Subsets**:
   - If two subsets \( S_i \) and \( S_j \) overlap, they cannot both be selected. This is encoded as:
     ```plaintext
     ¬x_i ∨ ¬x_j
     ```
     or in DIMACS CNF:
     ```plaintext
     -i -j 0
     ```

2. **Threshold Requirement**:
   - To ensure that at least \( T \) subsets are selected, we enforce a cardinality constraint. This is encoded as:
     # Set Packing Problem

## Problem Description

The **Set Packing Problem** is a combinatorial decision problem where the objective is to determine if there exists a collection of disjoint subsets from a given set of subsets such that the collection contains at least a specified number of subsets.

### Parameters:
- **Universe (U)**: The set of all elements.
- **Subsets (S)**: A collection of subsets of \( U \).
- **Threshold (T)**: The minimum number of disjoint subsets required.

### Constraints:
1. Subsets in the solution must be pairwise disjoint.
2. At least \( T \) subsets must be selected.

---

## CNF Encoding

The Set Packing Problem is encoded into DIMACS CNF format for compatibility with SAT solvers such as Glucose. The encoding involves the following steps:

### Propositional Variables
- Each subset \( S_i \) is represented by a propositional variable `x_i`, where:
  - `x_i = true` indicates that subset \( S_i \) is selected.
  - `x_i = false` indicates that subset \( S_i \) is not selected.
- The total number of variables equals the number of subsets.

### Encoding Constraints
1. **Disjoint Subsets**:
   - If two subsets \( S_i \) and \( S_j \) overlap, they cannot both be selected. This is encoded as:
     ```plaintext
     ¬x_i ∨ ¬x_j
     ```
     or in DIMACS CNF:
     ```plaintext
     -i -j 0
     ```

2. **Threshold Requirement**:
   - To ensure that at least \( T \) subsets are selected, we enforce a cardinality constraint. This is encoded as:
     ```plaintext
     x_{i_1} ∨ x_{i_2} ∨ ... ∨ x_{i_{n-T+1}}
     ```
     or in DIMACS CNF:
     ```plaintext
     i_1 i_2 ... i_{n-T+1} 0
     ```

### DIMACS CNF Format
The CNF formula is output in DIMACS format:
- The header specifies the number of variables and clauses:
  ```plaintext
  p cnf <num_variables> <num_clauses>


## User Documentation

### Input Format:
The input consists of:
1. An integer `T`: The threshold number of subsets.
2. A list of subsets, where each subset is represented by space-separated integers.

#### Example:
