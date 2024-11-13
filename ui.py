from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout,
                             QVBoxLayout, QLabel, QComboBox,
                             QSlider, QPushButton)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QPainter, QColor
from algorithms import BubbleSortWidget, QuickSortWidget


class ControlPanel(QWidget):
    start_signal = pyqtSignal()
    pause_signal = pyqtSignal()
    reset_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        # control panel label
        title_label = QLabel('Control Panel')
        title_label.setFont(QFont('Arial', 14, QFont.Bold))
        layout.addWidget(title_label)

        # algorithms list
        algorithm_label = QLabel('Select Algorithm:')
        algorithm_label.setObjectName('algorithm_label')
        self.algorithm_combo = QComboBox()
        self.algorithm_combo.addItems([
            'Bubble Sort',
            'Quick Sort',
            'Merge Sort',
            'Binary Search',
            'DFS',
            'BFS'
        ])

        layout.addWidget(algorithm_label)
        layout.addWidget(self.algorithm_combo)

        # speed slider
        speed_label = QLabel('Animation Speed:')
        speed_slider = QSlider(Qt.Horizontal)
        speed_slider.setMinimum(1)
        speed_slider.setMaximum(100)
        speed_slider.setValue(50)
        layout.addWidget(speed_label)
        layout.addWidget(speed_slider)

        # control buttons
        start_button = QPushButton('Start')
        pause_button = QPushButton('Pause')
        reset_button = QPushButton('Reset')

        # connect signals
        start_button.clicked.connect(self.start_signal.emit)
        pause_button.clicked.connect(self.pause_signal.emit)
        reset_button.clicked.connect(self.reset_signal.emit)

        # adding buttons
        layout.addWidget(start_button)
        layout.addWidget(pause_button)
        layout.addWidget(reset_button)

        # stretched space
        layout.addStretch()

        # styles
        self.setStyleSheet("""
                    QWidget {
                        background-color: #f0f0f0;
                        border-right: 1px solid #cccccc;
                    }
                    QPushButton {
                        background-color: #4CAF50;
                        color: white;
                        border: none;
                        padding: 8px;
                        margin: 5px;
                        border-radius: 4px;
                    }
                    QLabel#algorithm_label {

                    }
                """)


class VisualizationArea(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Python Algorithms Visualizer')
        self.setGeometry(100, 100, 1200, 800)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)

        self.control_panel = ControlPanel()
        self.visualization_area = VisualizationArea()

        # connecting signals
        self.control_panel.start_signal.connect(self.start_visualization)
        self.control_panel.pause_signal.connect(self.pause_visualization)
        self.control_panel.reset_signal.connect(self.reset_visualization)

        main_layout.addWidget(self.control_panel, stretch=1)
        main_layout.addWidget(self.visualization_area, stretch=4)

    def start_visualization(self):
        self.algo_widgets = {
            'Bubble Sort': BubbleSortWidget(),
            'Quick Sort': QuickSortWidget()
        }
        algo = self.control_panel.algorithm_combo.currentText()
        widget = self.algo_widgets[algo]
        layout = self.visualization_area.layout()
        self.clear_layout(layout)
        layout.addWidget(widget)
        widget.start_sorting()

    def clear_layout(self, layout):
        if layout.count() > 0:
            for i in range(layout.count()):
                widget_to_remove = layout.itemAt(i).widget()
                if widget_to_remove is not None:
                    layout.removeWidget(widget_to_remove)
                    widget_to_remove.deleteLater()

    def pause_visualization(self):
        print('pausing')

    def reset_visualization(self):
        print('resetting')
