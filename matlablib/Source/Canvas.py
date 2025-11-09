#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QFrame
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Canvas(FigureCanvas):
	"""The canvas basic class."""
	def __init__(self, parent: QFrame) -> None:
		"""Canvas class initialization."""
		self.parent_app = parent
		self.dpi = 100
		self.figure = Figure(figsize=(parent.width()/self.dpi, parent.height()/self.dpi), dpi=self.dpi)
		self.figure.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)
		
		self.canvas = FigureCanvas(self.figure)
		self.axis = self.figure.add_subplot(111, projection='3d')
		self.clear_plot()

		super().__init__(self.figure)

	def draw_capacitor(self, point_quanity: int, XYZ_start: list, XYZ_end: list, electrode_distance: float) -> None:
		"""
		Draw a model of capactior by position and distance between electodes.

		Attributes:
			point_quanity(int): usualy 4 point to calculate a capacitor model.
			XYZ_start(list): list of start points of capacitor.
			XYZ_end(list): list of end points of capactior.
			electrode_distance(float): distance between electrodes.
		"""

		[x, y, z] = self.calculate_capacitor_sizes(XYZ_start, XYZ_end, electrode_distance)

		N = point_quanity

		self.axis.fill_between(x[0], y[0], z[0], x[1], y[1], z[1], alpha=0.5, edgecolor='k')
		self.axis.fill_between(x[2], y[2], z[2], x[3], y[3], z[3], alpha=0.5, edgecolor='k')
		self.setParent(self.parent_app)

	def calculate_capacitor_sizes(self, XYZ_start: list, XYZ_end: list, electrode_distance: float) -> list[list, list, list]:
		"""Calculate start and end points of capacitor."""
		x_axis = [XYZ_start[0], XYZ_end[0], XYZ_start[0], XYZ_end[0]]
		y_axis = [XYZ_start[1], XYZ_end[1], XYZ_start[1], XYZ_end[1]]
		z_axis = [XYZ_start[2], XYZ_end[2], XYZ_start[2] + electrode_distance, XYZ_end[2] + electrode_distance]

		return[x_axis, y_axis, z_axis]

	def draw_arrow_axis(self, arrow_length: float=0.1, enable_axis: bool=True) -> None:
		"""Draw an axis arrows if they enabled."""
		if enable_axis:
			origin = [0, 0, 0]
			
			x_axis = [arrow_length, 0, 0]
			y_axis = [0, arrow_length, 0] 
			z_axis = [0, 0, arrow_length]

			colors = ['red', 'green', 'blue']
			
			self.axis.quiver(*origin, *x_axis, color=colors[0], arrow_length_ratio=0.1, linewidth=1)
			self.axis.quiver(*origin, *y_axis, color=colors[1], arrow_length_ratio=0.1, linewidth=1)
			self.axis.quiver(*origin, *z_axis, color=colors[2], arrow_length_ratio=0.1, linewidth=1)
			
			self.axis.text(arrow_length * 1.1, 0, 0, "X", color=colors[0], fontsize=5)
			self.axis.text(0, arrow_length * 1.1, 0, "Y", color=colors[1], fontsize=5)
			self.axis.text(0, 0, arrow_length * 1.1, "Z", color=colors[2], fontsize=5)

	def clear_plot(self) -> None:
		"""Clear an axis and plot."""
		self.axis.cla()
		self.axis.set_axis_off()
		self.axis.set(xlim=(0, 1), ylim=(0, 1), zlim=(0, 1))
		self.axis.set_aspect('equal', 'box')