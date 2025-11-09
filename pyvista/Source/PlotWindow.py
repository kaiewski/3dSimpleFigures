#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pyvista as pv
import pyvistaqt as pvqt
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout
from Source._windows.plot_window import Ui_Form
from Source.Canvas import Canvas as Canvas

class PlotWindow(QWidget):
	"""Main window of the program."""

	def __init__(self) -> None:
		"""Class initialization."""
		super(PlotWindow, self).__init__()

		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.chart = Canvas(self.ui.framePlot)

		self.initialize_ui()
		self.draw_capacitor()

	def initialize_ui(self) -> None:
		"""Initialize the user interface."""
		self.setWindowTitle('3D pyvista model test')
		self.ui.chkAxis.clicked.connect(self.change_axis_state)

		if self.ui.framePlot.layout() is None:
			self.ui.framePlot.setLayout(QVBoxLayout())

		self.ui.framePlot.layout().addWidget(self.chart.plotter)
		self.ui.framePlot.layout().setContentsMargins(0, 0, 0, 0)
		self.ui.framePlot.layout().setSpacing(0)

	def draw_capacitor(self) -> None:
		"""Draw an capacitor."""
		bottom_electrode = pv.Plane(center=(0.5, 0.5, 0), direction=(0, 0, 1), i_size=1, j_size=1)
		top_electrode = pv.Plane(center=(0.5, 0.5, 0.2), direction=(0, 0, 1), i_size=1, j_size=1)
		self.chart.draw_capacitor(bottom_electrode, top_electrode)

	def change_axis_state(self):
		"""Enable/disable an axis arrows."""
		if self.ui.chkAxis.checkState() == Qt.Checked:
			self.chart.draw_arrow_axis(0.1, True)
			return

		self.chart.draw_arrow_axis(0.1, False)
