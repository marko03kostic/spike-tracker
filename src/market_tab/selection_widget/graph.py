from PySide6.QtCharts import QChart, QLineSeries, QValueAxis, QChartView, QDateTimeAxis, QCategoryAxis
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtGui import QPainter
from PySide6.QtCore import QDateTime, Qt

from src.backend.graphs_api.definitions import RunnerChartResult
from src.backend.betting_api.ticks import BETFAIR_TICKS

class RunnerChart(QChart):

    def __init__(self, result: RunnerChartResult, title: str):
        super().__init__()
        self.points = result
        self.setTitle(title)
        self.legend().setVisible(False)
        self.legend().setAlignment(Qt.AlignBottom)
        self.value_series = QLineSeries()
        self.volume_series = QLineSeries()
        self.max_y_left = None
        self.tick_increment = None
        self.axisX = QCategoryAxis()
        self.axisY = QValueAxis()
        self.axisY_right = QValueAxis()
        self.populateChart()

    def populateChart(self):
        values = [point['value'] for point in self.points['points']]
        volumes = [point['volume'] for point in self.points['points']]

        max_value = max(values)
        i = BETFAIR_TICKS.index(max_value)
        self.max_y_left = BETFAIR_TICKS[i+2] if i + 2 < len(BETFAIR_TICKS) else 1000

        self.tick_increment = (self.max_y_left-1)/8
        if self.tick_increment < 5:
            self.tick_increment = 5
        else:
            self.tick_increment = round(self.tick_increment / 5) * 5

        self.value_series.setName("Value")

        for i, value in enumerate(values):
            self.value_series.append(i, value)

        self.addSeries(self.value_series)

        self.axisX.setLabelsVisible(False)  # Hide x-axis labels
        self.addAxis(self.axisX, Qt.AlignBottom)
        self.value_series.attachAxis(self.axisX)

        self.axisY.setTitleText("Value")
        self.axisY.setLabelFormat("%.2f")  # Format y-axis labels to two decimal places
        self.axisY.setRange(1.00, self.max_y_left)  # Set range from 1.00 to max_y_left
        self.axisY.setMinorTickCount(0)  # No minor ticks
        self.axisY.setTickAnchor(1.00)  # Start ticks from 1.00
        self.axisY.setTickInterval(self.tick_increment)  # Set tick interval
        self.addAxis(self.axisY, Qt.AlignLeft)  # Align axis on the left side
        self.value_series.attachAxis(self.axisY)

        # Creating volume series
        self.volume_series.setName("Volume")

        for i, volume in enumerate(volumes):
            self.volume_series.append(i, volume)

        self.addSeries(self.volume_series)

        self.axisY_right.setTitleText("Volume (thousands)")
        self.axisY_right.setLabelFormat("%'d")  # Format y-axis labels rounded to thousands
        self.axisY_right.setRange(0, max(volumes) + 0.1 * max(volumes))  # Set range from 0 to max_volume with 10% padding above
        self.axisY_right.setLinePenColor(self.volume_series.pen().color())
        self.axisY_right.setGridLineVisible(False)
        self.addAxis(self.axisY_right, Qt.AlignRight)  # Align axis on the right side
        self.volume_series.attachAxis(self.axisY_right)

        self.setAnimationOptions(QChart.SeriesAnimations)

    def add_point(self, value, volume):
        new_index = len(self.value_series.pointsVector())
        self.value_series.append(new_index, value)
        self.volume_series.append(new_index, volume)

        # Update the range of the value axis if the new value exceeds the current range
        if value > self.max_y_left:
            self.max_y_left = value
            i = BETFAIR_TICKS.index(value)
            self.max_y_left = BETFAIR_TICKS[i+2] if i + 2 < len(BETFAIR_TICKS) else 1000
            self.tick_increment = (self.max_y_left-1)/8
            if self.tick_increment < 5:
                self.tick_increment = 5
            else:
                self.tick_increment = round(self.tick_increment / 5) * 5
            self.axisY.setRange(1.00, self.max_y_left)
            self.axisY.setTickInterval(self.tick_increment)

        # Update the range of the volume axis if the new volume exceeds the current range
        max_volume = max([point.y() for point in self.volume_series.pointsVector()])
        self.axisY_right.setRange(0, max_volume + 0.1 * max_volume)

class RunnerChartWidget(QWidget):
    def __init__(self, result: RunnerChartResult, title: str, parent=None):
        super().__init__(parent)
        
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.runner_chart = RunnerChart(result, title)
        self.runner_chart.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        chart_view = QChartView(self.runner_chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        chart_view.setMinimumSize(400, 300)
        
        layout.addWidget(chart_view)