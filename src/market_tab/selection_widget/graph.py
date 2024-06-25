from PySide6.QtWidgets import QWidget, QVBoxLayout
import numpy as np
import pyqtgraph as pg
from pyqtgraph import PlotWidget, ViewBox, AxisItem

from src.backend.graphs_api.definitions import RunnerChartResult

class RunnerChart(QWidget):
    def __init__(self, data, title, parent=None):
        super().__init__(parent)

        # Extracting and processing the data
        self.values = [item['value'] for item in data['points']]
        self.volumes = [item['volume'] for item in data['points']]

        self.setMinimumSize(300, 400)  # Set a minimum size for the widget

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        self.plot_widget = PlotWidget()
        layout.addWidget(self.plot_widget)
        self.plot_widget.setTitle(title)

        # Setting up the left axis for values
        self.plot_widget.setLabel('left', '', color='blue', size=20)
        self.plot_widget.showGrid(x=True, y=True)

        # Plotting the value as a line plot
        x_values = list(range(len(self.values)))
        self.plot_widget.plot(x_values, self.values, pen=pg.mkPen(color='b', width=2), name="")

        # Adding a second y-axis on the right for volumes
        self.volume_axis = ViewBox()
        self.plot_widget.scene().addItem(self.volume_axis)
        
        # Custom Axis for the right side
        self.volume_axis_item = AxisItem('right')
        self.plot_widget.plotItem.layout.addItem(self.volume_axis_item, 2, 3)
        self.volume_axis_item.linkToView(self.volume_axis)
        self.volume_axis_item.setLabel('', color='red', size=20)

        # Linking the right axis with the plot_widget
        self.plot_widget.getPlotItem().getViewBox().sigResized.connect(self.update_views)

        # Plotting the volume as a bar graph
        self.volume_bar_graph_item = pg.BarGraphItem(x=x_values, height=self.volumes, width=0.8, brush='r')
        self.volume_axis.addItem(self.volume_bar_graph_item)

        # Enable zooming and set limits
        self.plot_widget.setLimits(xMin=min(x_values), xMax=max(x_values), yMin=1.00, yMax=max(self.values)*1.2)
        self.plot_widget.getViewBox().setMouseEnabled(x=False, y=True)
        self.plot_widget.getViewBox().setLimits(xMin=min(x_values), xMax=max(x_values), yMin=1.00, yMax=max(self.values)*1.2)
        self.volume_axis.setMouseEnabled(x=False, y=True)
        
        # Set the y-axis range for the volume axis to start from 0
        self.volume_axis.setYRange(1, max(self.volumes) * 1.5, padding=0)

        self.plot_widget.getAxis('bottom').setTicks([])

        # Automatically assign ticks on the left axis
        left_axis = self.plot_widget.getAxis('left')
        left_axis.enableAutoSIPrefix(False)  # Disable auto SI prefix for decimal formatting

        # Zoom to fit the initial view
        self.plot_widget.getViewBox().autoRange()

        layout.addWidget(self.plot_widget)  # Add plot widget to the layout

    def update_views(self):
        self.volume_axis.setGeometry(self.plot_widget.getViewBox().sceneBoundingRect())