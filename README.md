# Scientific Computing with SciPy 🔬

Welcome to **Scientific Computing with SciPy** – a collection of Jupyter Notebooks that explore various components of the [SciPy](https://scipy.org/) library. This series is designed to guide learners through key functionalities in scientific and technical computing using Python.

Each section focuses on a different topic, making it easy to learn in small, digestible modules.

---
- A hands-on collection of Jupyter Notebooks exploring key features of the SciPy library – from constants and optimization to sparse data and graph algorithms. Perfect for students, researchers, and anyone diving into scientific computing with Python.

## 📂 Table of Contents

1. [Introduction to SciPy](#1-introduction-to-scipy)
2. [SciPy Constants](#2-scipy-constants)
3. [Optimization in SciPy](#3-optimization-in-scipy)
4. [Sparse Data Handling](#4-sparse-data-handling)
5. [Graph Theory and Spatial Algorithms](#5-graph-theory-and-spatial-algorithms)

---

## 1. Introduction to SciPy

This section provides a foundational overview of the SciPy library. It covers its structure, key submodules, and how it complements NumPy for scientific computing. You'll get hands-on experience with core mathematical operations and special functions.

---

## 2. SciPy Constants

This section introduces the `scipy.constants` module, which provides access to a wide collection of physical constants and unit conversions used in scientific computations.

### 🔹 What You’ll Learn:

- **Accessing standard constants**: Learn how to use predefined constants like:
  - Speed of light (`c`)
  - Planck’s constant (`h`)
  - Gravitational constant (`G`)
  - Avogadro’s number (`N_A`)
  - Boltzmann constant (`k`)
  
- **Working with physical units**: Use helpful unit definitions such as:
  - `minute`, `hour`, `day`, `week`
  - `inch`, `foot`, `mile`
  - `gram`, `pound`, `ton`
  - `atm`, `bar`, `psi`

- **Unit conversions**: Perform unit conversions using tools like:
  - `scipy.constants.convert_temperature(value, original_unit, target_unit)`
  - Converting between Celsius, Fahrenheit, and Kelvin

- **Constants database**: Access a full list of constants using:
  - `scipy.constants.physical_constants`
  - `scipy.constants.codata`
  
  Learn how to extract values, units, and uncertainties from the dictionary.

### 🧪 Example Use Cases:

- Calculate the energy of a photon given its frequency using Planck’s constant.
- Convert inches to meters or psi to pascals.
- Look up the value of the fine-structure constant and its uncertainty.
- Use the Boltzmann constant in thermodynamic equations.

This section makes it easy to incorporate real-world scientific constants into your Python calculations with accuracy and convenience.

---

## 3. Optimization in SciPy

Dive into mathematical optimization using the `optimize` module. This section includes:
- Function minimization techniques
- Solving equations
- Curve fitting with real-world data

Visual examples and plots are included for better understanding.

---

## 4. Sparse Data Handling

Understand how to work efficiently with large datasets that contain mostly zeroes. This topic covers:
- Creating and manipulating sparse matrices
- Storage formats (CSR, CSC, COO)
- Performing matrix operations and comparisons with dense representations

Learn how sparse matrices can greatly optimize memory and computation in scientific applications.

---

## 5. Graph Theory and Spatial Algorithms

Explore graph-based algorithms and spatial data structures. Topics include:
- Representing graphs using sparse adjacency matrices
- Finding shortest paths and minimum spanning trees
- Working with KD-Trees and computing distances in multidimensional space

These tools are especially useful in areas such as network analysis, logistics, and spatial data science.

---

## 🛠️ Requirements

Make sure you have the following Python packages installed:

```bash
pip install numpy scipy matplotlib jupyter


Scipy

git add .

git commit -m "Optimizers file added" 

git push origin main
