#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QSizePolicy
from Source._windows.plot_window import Ui_Form
from Source.Canvas import Canvas as Canvas

class PlotWindow(QWidget):
	"""Main window of the program."""

	def __init__(self) -> None:
		"""Class initialization."""
		super(PlotWindow, self).__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)

		self.initialize_ui()
		self.draw_basic_model()

	def initialize_ui(self) -> None:
		"""Initialize the user interface."""
		self.setWindowTitle('3D matplotlib model test')
		self.ui.framePlot.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.chart = Canvas(self.ui.framePlot)
		self.ui.chkAxis.clicked.connect(self.change_axis_state)

	def draw_basic_model(self) -> None:
		"""Draw a model of a capacitor."""
		self.chart.draw_capacitor(2, [0, np.linspace(0, 1, 2), 0], [1, np.linspace(0, 1, 2), 0], 0.2)

	def change_axis_state(self) -> None:
		"""Switch XYZ axis."""
		self.chart.clear_plot()

		if self.ui.chkAxis.checkState() == Qt.Checked:
			self.chart.draw_arrow_axis(0.1, True)
			self.draw_basic_model()
			return

		self.chart.draw_arrow_axis(0.1, False)
		self.draw_basic_model()

