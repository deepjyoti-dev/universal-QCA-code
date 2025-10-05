# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 10:34:36 2025

@author: deepj
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from matplotlib.widgets import Button, RadioButtons
import numpy as np

CELL_UP = 1
CELL_DOWN = -1
CELL_NONE = 0

# Predefined gate templates (relative coordinates)
GATE_TEMPLATES = {
    "AND": [(0,0,CELL_NONE),(1,0,CELL_NONE),(0,1,CELL_NONE),(1,1,CELL_UP)],
    "OR": [(0,0,CELL_NONE),(1,0,CELL_NONE),(0,1,CELL_NONE),(1,1,CELL_UP)],
    "NOT": [(0,0,CELL_NONE),(1,0,CELL_DOWN)],
    "XOR": [(0,0,CELL_NONE),(1,0,CELL_NONE),(0,1,CELL_NONE),(1,1,CELL_UP)]
}

class QCADesigner:
    def __init__(self, width=12, height=8):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)
        self.selected_polarity = CELL_UP
        self.selected_gate = None
        self.fig, self.ax = plt.subplots(figsize=(width, height))
        plt.subplots_adjust(bottom=0.25)
        self.draw_grid()
        self.cid_click = self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.create_buttons()
        plt.show()

    def draw_grid(self):
        self.ax.clear()
        for y in range(self.height):
            for x in range(self.width):
                pol = self.grid[y, x]
                color = 'white'
                if pol == CELL_UP:
                    color = 'red'
                elif pol == CELL_DOWN:
                    color = 'blue'
                circle = Circle((x, -y), 0.3, facecolor=color, edgecolor='black')
                self.ax.add_patch(circle)
        self.ax.set_xlim(-1, self.width)
        self.ax.set_ylim(-self.height, 1)
        self.ax.set_aspect('equal')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_title("Drag-and-Drop QCA CAD Simulator")
        self.fig.canvas.draw()

    def on_click(self, event):
        if event.inaxes != self.ax:
            return
        x = int(round(event.xdata))
        y = int(round(-event.ydata))
        if self.selected_gate:
            self.place_gate(x, y)
        else:
            if 0 <= x < self.width and 0 <= y < self.height:
                self.grid[y, x] = self.selected_polarity
        self.draw_grid()

    def create_buttons(self):
        # Polarity buttons
        ax_up = plt.axes([0.05, 0.1, 0.1, 0.075])
        btn_up = Button(ax_up, 'UP (+1)')
        btn_up.on_clicked(lambda event: self.set_polarity(CELL_UP))
        ax_down = plt.axes([0.05, 0.02, 0.1, 0.075])
        btn_down = Button(ax_down, 'DOWN (-1)')
        btn_down.on_clicked(lambda event: self.set_polarity(CELL_DOWN))
        # Propagate button
        ax_prop = plt.axes([0.2, 0.05, 0.15, 0.075])
        btn_prop = Button(ax_prop, 'Propagate')
        btn_prop.on_clicked(self.propagate)
        # Gate selection radio buttons
        ax_radio = plt.axes([0.4, 0.02, 0.2, 0.15])
        self.radio = RadioButtons(ax_radio, ('None','AND','OR','NOT','XOR'))
        self.radio.on_clicked(self.select_gate)

    def set_polarity(self, pol):
        self.selected_polarity = pol
        self.selected_gate = None
        self.radio.set_active(0)

    def select_gate(self, label):
        self.selected_gate = None if label=='None' else label

    def place_gate(self, x, y):
        template = GATE_TEMPLATES[self.selected_gate]
        for dx, dy, pol in template:
            gx, gy = x+dx, y+dy
            if 0 <= gx < self.width and 0 <= gy < self.height:
                self.grid[gy, gx] = pol

    def propagate(self, event):
        new_grid = self.grid.copy()
        for _ in range(3):
            for y in range(self.height):
                for x in range(self.width):
                    neighbors = self.get_neighbors(x, y)
                    influence = sum(neighbors)
                    if influence > 0:
                        new_grid[y, x] = CELL_UP
                    elif influence < 0:
                        new_grid[y, x] = CELL_DOWN
        self.grid = new_grid.copy()
        self.draw_grid()

    def get_neighbors(self, x, y):
        neighbors = []
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbors.append(self.grid[ny, nx])
        return neighbors

# ===== Run the drag-and-drop QCA CAD tool =====
QCADesigner(width=14, height=10)
