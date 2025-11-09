#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import PySide6
from PySide6 import QtCore
from PySide6.QtWidgets import QWidget
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

		self.chart = Canvas()
		self.draw_capacitor()

	def initialize_ui(self) -> None:
		"""Initialize the user interface."""
		self.setWindowTitle('3D plotly model test')
		self.file_path = os.path.join(os.getcwd(), "plot.html")
		self.browser = self.ui.webEngineView

	def update_browser_contents(self) -> None:
		"""Update and load html file with 3d model."""
		self.chart.update_plotly_html(self.file_path)
		url = QtCore.QUrl.fromLocalFile(self.file_path)
		self.browser.load(url)
	
	def draw_capacitor(self) -> None:
		"""Draw the capacitor by position."""
		self.chart.draw_capacitor([[0, 1, 0, 1],[0, 0, 1, 1],[0, 0, 0, 0]], 0.2)
		self.chart.update_figure_layout()	
		self.update_browser_contents()
