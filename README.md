⚛️ Universal QCA CAD Simulator (Python)

An interactive Quantum-dot Cellular Automata (QCA) CAD tool built in Python using Matplotlib.
Design QCA circuits visually, place logic gates, connect wires, and simulate polarization propagation in real-time.

Ideal for research, learning, and prototyping QCA circuits.

✨ Features
Interactive Cell Placement

Click on the grid to place QCA cells

Red (↑) = +1 polarization

Blue (↓) = -1 polarization

White = empty cell

Drag-and-Drop Logic Gates

Prebuilt gates: AND, OR, NOT, XOR

Select a gate from the radio buttons and click on the grid to place

Wire Connections

Place individual cells as wires

Polarization propagates through wires during simulation

Simulation

Click Propagate to simulate polarization influence across the grid

Real-time visual updates

Selectable Polarity Mode

Switch between UP (+1) and DOWN (-1)

Allows editing individual cells interactively

Scalable Grid

Configurable width and height for designing large QCA circuits

Foundation for Extensions

Can later support:

Automatic wire routing

Multi-layer clocking zones

Truth table simulation per input

Export to graphical diagrams or Python simulation code

🧩 Installation

Python 3.8+ required

Install dependencies:

pip install matplotlib numpy


Clone or download this repository

⚙️ Usage

Run the main script:

python qca_designer.py


The interactive window will open:

Click to place cells

Select polarity: UP (+1) or DOWN (-1)

Select gate: AND, OR, NOT, XOR from radio buttons

Click Propagate to simulate polarization

Observe real-time updates of polarization in the grid

🔹 How it Works
Grid Representation

QCA layout is a 2D NumPy array

Each cell: +1 (UP), -1 (DOWN), 0 (empty)

Polarization Propagation

Each cell is influenced by orthogonal neighbors

If sum(neighbors) > 0 → cell becomes +1

If sum(neighbors) < 0 → cell becomes -1

Gate Templates

Gates defined as relative coordinates with polarizations

Placed onto the grid interactively

🔮 Future Enhancements

Automatic wire routing between gates

Multi-layer clocking zones for real QCA circuits

Truth table simulation for dynamic input/output

Export designs to PDF / image or Python code

Drag-and-drop gate editing with resizing and rotation

🖼️ Example Screenshots

Red Cells → +1 polarization

Blue Cells → -1 polarization

White Cells → Empty / Wire

Place gates, draw wires, propagate, and visualize outputs

👤 Author

Deepjyoti Das
Interactive QCA CAD tool for learning, prototyping, and research

🏷️ Tags

#python #qca #simulation #cad #matplotlib #quantum #interactive #learning #research #visualization
