#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyvista as pv
from pyvista.core.pointset import PolyData
from pyvistaqt import QtInteractor
from PySide6.QtWidgets import QFrame, QSizePolicy

class Canvas():
	"""The canvas basic class."""
	def __init__(self, frame: QFrame) -> None:
		"""Canvas class initialization."""
		super().__init__()

		self.plotter = QtInteractor(frame)
		self.plotter.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.axis_actors = []

	def draw_capacitor(self, bottom_electrode: PolyData, top_electrode: PolyData) -> None:
		"""
		Draw the capcaitor by PolyData.

		Attributes:
			bottom_electrode(PolyData): points of bottom electrode.
			top_electrode(PolyData): points of top electrode.
		"""

		self.plotter.add_mesh(bottom_electrode, color='blue', opacity=0.7)
		self.plotter.add_mesh(top_electrode, color='red', opacity=0.7)

		self.plotter.camera_position = 'xy'
		self.plotter.reset_camera()
		self.plotter.update()

	def draw_arrow_axis(self, arrow_length: float = 0.1, enable_axis: bool = True) -> None:
		"""Draw an axis arrows."""

		for actor in self.axis_actors:
			self.plotter.remove_actor(actor)
		self.axis_actors = []
		
		if not enable_axis:
			self.plotter.update()
			return

		origin = [0, 0, 0]
		x_axis = pv.Arrow(start=origin, direction=[arrow_length, 0, 0], scale='auto')
		y_axis = pv.Arrow(start=origin, direction=[0, arrow_length, 0], scale='auto')
		z_axis = pv.Arrow(start=origin, direction=[0, 0, arrow_length], scale='auto')

		actor_x = self.plotter.add_mesh(x_axis, color='red')
		actor_y = self.plotter.add_mesh(y_axis, color='green')
		actor_z = self.plotter.add_mesh(z_axis, color='blue')

		text_actor_x = self.plotter.add_point_labels([(arrow_length * 1.1, 0, 0)], ['X'], 
													text_color='red', 
													font_size=10, 
													show_points=False, 
													shape=None)

		text_actor_y = self.plotter.add_point_labels([(0, arrow_length * 1.1, 0)], ['Y'], 
													text_color='green', 
													font_size=10, 
													show_points=False,
													shape=None)

		text_actor_z = self.plotter.add_point_labels([(0, 0, arrow_length * 1.1)], ['Z'], 
													text_color='blue',
													font_size=10, 
													show_points=False,
													shape=None)

		self.axis_actors = [actor_x, actor_y, actor_z, text_actor_x, text_actor_y, text_actor_z]
		self.plotter.update()
