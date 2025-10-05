# universal-QCA-code
universal QCA generator with python
Drag-and-Drop QCA CAD Simulator
Overview

This project is an interactive Quantum-dot Cellular Automata (QCA) CAD tool built in Python using Matplotlib. It allows users to design QCA circuits visually, place logic gates, connect wires, and simulate polarization propagation in real-time.

It’s ideal for research, learning, and prototyping QCA circuits.

Features

Interactive Cell Placement

Click on the grid to place QCA cells.

Red (↑) = +1 polarization.

Blue (↓) = -1 polarization.

White = empty cell.

Drag-and-Drop Logic Gates

Prebuilt gates: AND, OR, NOT, XOR.

Select a gate from the radio buttons and click on the grid to place it.

Wire Connections

Place individual cells to act as wires.

Polarization propagates through wires during simulation.

Simulation

Click Propagate to simulate polarization influence across the grid.

Real-time visual updates.

Selectable Polarity Mode

Switch between UP (+1) and DOWN (-1) using the buttons.

Allows editing individual cells interactively.

Scalable Grid

Configurable width and height for designing large QCA circuits.

Foundation for Extensions

Can later support:

Automatic wire routing

Multi-layer clocking zones

Truth table simulation per input

Export to graphical diagrams or Python simulation code

Installation

Python 3.8+ is required.

Install dependencies:

pip install matplotlib numpy


Clone or download this repository.

Usage

Run the main script:

python qca_designer.py


The interactive window will open:

Click to place cells.

Select polarity: UP (+1) or DOWN (-1).

Select gate: Use the radio buttons (AND, OR, NOT, XOR) and click on the grid to place.

Propagate: Click Propagate button to simulate polarization influence.

Observe the real-time updates of polarization in the grid.

How it Works

Grid Representation

The QCA layout is represented as a 2D NumPy array.

Each cell can be +1 (UP), -1 (DOWN), or 0 (empty).

Polarization Propagation

For each cell, the orthogonal neighbors influence its polarization.

If sum of neighbors > 0 → cell becomes +1.

If sum of neighbors < 0 → cell becomes -1.

Gate Templates

Gates are defined as relative coordinates with polarizations.

Placed onto the grid interactively.

Future Enhancements

Automatic wire routing between gates.

Multi-layer clocking zones to simulate real QCA circuits.

Truth table simulation for dynamic input/output analysis.

Export designs to:

PDF or image of QCA layout

Python code for automated simulation

Drag-and-drop gate editing with resizing and rotation.

Example Screenshots
[Red Cells]   → +1 polarization
[Blue Cells]  → -1 polarization
[White Cells] → Empty / Wire


Place gates, draw wires, propagate, and see outputs visually.

Author

Deepjyoti Das

Interactive QCA CAD tool for learning, prototyping, and research.
