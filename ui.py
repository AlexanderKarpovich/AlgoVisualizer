from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout,
                             QVBoxLayout, QLabel, QComboBox,
                             QSlider, QPushButton)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont


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
        algorithm_combo = QComboBox()
        algorithm_combo.addItems([
            'Bubble Sort',
            'Quick Sort',
            'Merge Sort',
            'Binary Search',
            'DFS',
            'BFS'
        ])
        layout.addWidget(algorithm_label)
        layout.addWidget(algorithm_combo)

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

        # test
        placeholder = QLabel('Visualization Area')
        placeholder.setAlignment(Qt.AlignCenter)

        layout.addWidget(placeholder)

        # styles
        self.setStyleSheet("""
                    QWidget {
                        background-color: white;
                    }
                    QLabel {
                        font-size: 24px;
                        color: #666666;
                    }
                """)


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

        control_panel = ControlPanel()
        visualization_area = VisualizationArea()

        # connecting signals
        control_panel.start_signal.connect(self.start_visualization)
        control_panel.pause_signal.connect(self.pause_visualization)
        control_panel.reset_signal.connect(self.reset_visualization)

        main_layout.addWidget(control_panel, stretch=1)
        main_layout.addWidget(visualization_area, stretch=4)

    def start_visualization(self):
        print('starting')

    def pause_visualization(self):
        print('pausing')

    def reset_visualization(self):
        print('resetting')
