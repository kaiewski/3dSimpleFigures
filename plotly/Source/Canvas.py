#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import plotly.graph_objects as go

class Canvas():
	"""The canvas basic class."""
	
	def __init__(self) -> None:
		"""Canvas class initialization."""
		self.fig = go.Figure()
		self.draw_arrow_axis()

	def draw_capacitor(self, points: list[list, list, list], electrode_distance: float) -> None:
		"""
		Draw a capacitor by positions.

		Atttributes:
			points(list): the list of lists with start and end points of electrodes.
			electrode_distance(float): the distance between electrodes. 
		"""

		self.fig.add_trace(go.Mesh3d(
			x=points[0],
			y=points[1],
			z=points[2],
			opacity=0.5,
			color='rgba(244,22,100,0.6)',
			name="Bottom electrode"))
		
		self.fig.add_trace(go.Mesh3d(
			x=points[0],
			y=points[1],
			z=[i + electrode_distance for i in points[2]],
			opacity=0.5,
			color='rgba(100,22,244,0.6)',
			name="Top electrode"))

	def draw_arrow_axis(self, arrow_length: float=0.1) -> None:
		"""Draw the axis arrows."""
		self.fig.add_trace(go.Scatter3d(
			x=[0, arrow_length, None, 0, 0, None, 0, 0],
			y=[0, 0, None, 0, arrow_length, None, 0, 0],
			z=[0, 0, None, 0, 0, None, 0, arrow_length],
			mode='lines',
			line=dict(width=5, color='black'),
			showlegend=False))

		self.fig.add_trace(go.Scatter3d(
			x=[arrow_length * 1.1], y=[0], z=[0],
			mode='text',
			text=['X'],
			textfont=dict(size=10, color='red'),
			showlegend=False))
		
		self.fig.add_trace(go.Scatter3d(
			x=[0], y=[arrow_length * 1.1], z=[0],
			mode='text',
			text=['Y'],
			textfont=dict(size=10, color='green'),
			showlegend=False))
		
		self.fig.add_trace(go.Scatter3d(
			x=[0], y=[0], z=[arrow_length * 1.1],
			mode='text',
			text=['Z'],
			textfont=dict(size=10, color='blue'),
			showlegend=False))

	def update_figure_layout(self) -> None:
		"""Update the figure layout."""
		self.fig.update_layout(
			scene=dict(
				xaxis=dict(
					nticks=4, 
					range=[0, 1.3],
					showbackground=False,
					showgrid=False,
					zeroline=False,
					visible=False
				),
				yaxis=dict(
					nticks=4, 
					range=[0, 1.3],
					showbackground=False,
					showgrid=False,
					zeroline=False,
					visible=False
				),
				zaxis=dict(
					nticks=4, 
					range=[0, 1.3],
					showbackground=False,
					showgrid=False,
					zeroline=False,
					visible=False
				),
				bgcolor='white'
			),
			width=490,
			margin=dict(r=20, l=10, b=10, t=10),
			showlegend=True)

	def update_plotly_html(self, file_path: str) -> None:
		"""Save html file with 3d model."""
		html = self.fig.to_html()
		with open(file_path, "w", encoding="utf-8") as f:
			f.write(html)
