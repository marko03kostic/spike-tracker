from PySide6.QtCharts import QChart, QLineSeries, QValueAxis, QChartView
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtGui import QPainter 

from src.backend.graphs_api.definitions import RunnerChartResult

class RunnerChart(QChart):
    def __init__(self, result: RunnerChartResult):
        super().__init__()
        self.setTitle("Runner Chart")
        self.legend().setVisible(True)
        self.legend().setAlignment(Qt.AlignBottom)

        self.populateChart(result)

    def populateChart(self, result: RunnerChartResult):
        value_series = QLineSeries()
        value_series.setName("Value")
        
        for point in result['points']:
            value_series.append(point['timestamp'], point['value'])

        self.addSeries(value_series)

        # Configure x-axis (timestamp)
        axisX = QValueAxis()
        axisX.setLabelFormat("%i")
        axisX.setTitleText("Time")
        self.addAxis(axisX, Qt.AlignBottom)
        value_series.attachAxis(axisX)

        # Configure left y-axis (value)
        axisY = QValueAxis()
        axisY.setTitleText("Value")
        self.addAxis(axisY, Qt.AlignLeft)
        value_series.attachAxis(axisY)

        # Create series for volume (right y-axis)
        volume_series = QLineSeries()
        volume_series.setName("Volume")
        
        for point in result['points']:
            volume_series.append(point['timestamp'], point['volume'])

        self.addSeries(volume_series)

        # Configure right y-axis (volume)
        axisY_right = QValueAxis()
        axisY_right.setTitleText("Volume")
        axisY_right.setLinePenColor(volume_series.pen().color())  # Match color with volume series
        axisY_right.setGridLineVisible(False)
        self.addAxis(axisY_right, Qt.AlignRight)
        volume_series.attachAxis(axisY_right)

        self.setAnimationOptions(QChart.SeriesAnimations)

class RunnerChartWidget(QWidget):
    def __init__(self, result: RunnerChartResult, parent=None):
        super().__init__(parent)
        
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # Ensure no margins to fully utilize space
        
        self.runner_chart = RunnerChart(result)
        self.runner_chart.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        chart_view = QChartView(self.runner_chart)
        chart_view.setRenderHint(QPainter.Antialiasing)  # Enable antialiasing for smoother chart lines
        chart_view.setMinimumSize(400, 300)  # Set a minimum size for the chart view
        
        layout.addWidget(chart_view)