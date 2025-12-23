# Interactive Monte Carlo π Approximation

This project is an interactive Python visualization that approximates the value of π (pi) using the **Monte Carlo method**. Random points are generated inside a square, and the fraction that fall inside an inscribed circle is used to estimate π.

The simulation updates dynamically as the number of random points changes, allowing you to visually and numerically observe how the approximation improves with larger sample sizes.

---

## How the Monte Carlo Method Approximates π

A circle of radius 1 is inscribed inside a square of side length 2.

* Area of circle: πr² = π
* Area of square: (2r)² = 4

This gives the relationship:

**π ≈ 4 × (points inside circle / total points)**

As more random points are sampled, the ratio converges toward the true value of π.

---

## Features

* Interactive input to control the number of random points
* Real-time graphical visualization
* Displays:

  * Randomly generated points
  * Inscribed circle and bounding square
  * Current π approximation
* Equation breakdown showing why the method works

---

## How to Run: 2 Ways

### 1: Google Colab (Recommended)

1. Open the notebook in Google Colab
2. Run all cells
3. Enter the desired number of points in the input box

### 2: Local Jupyter Notebook

```bash
pip install numpy matplotlib ipywidgets
jupyter notebook
```

Make sure widgets are enabled:

```bash
jupyter nbextension enable --py widgetsnbextension
```

---

## Output Display

* Scatter plot showing random points
* Numerical π approximation updated each run
* Mathematical explanation displayed below the visualization

---

## Concepts Shown

* Monte Carlo methods
* Random sampling
* Geometric probability
* Numerical approximation
* Visualization with Matplotlib
* Interactivity with ipywidgets

---

## Educational Use

This project is well-suited for:

* High school or introductory college math/physics
* Demonstrating convergence and randomness
* Computational modeling practice
* STEM portfolios and research-style projects

---

## Built With

* Python
* NumPy
* Matplotlib
* ipywidgets
