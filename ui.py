from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout,
                             QVBoxLayout, QLabel, QComboBox,
                             QSlider, QPushButton)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


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

        control_panel = self.create_control_panel()

        visualization_area = self.create_visualization_area()

        main_layout.addWidget(control_panel, stretch=1)
        main_layout.addWidget(visualization_area, stretch=4)

    def create_control_panel(self):
        # control panel
        control_widget = QWidget()
        control_layout = QVBoxLayout(control_widget)

        # control panel label
        title_label = QLabel('Control Panel')
        title_label.setFont(QFont('Arial', 14, QFont.Bold))
        control_layout.addWidget(title_label)

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
        control_layout.addWidget(algorithm_label)
        control_layout.addWidget(algorithm_combo)

        # speed slider
        speed_label = QLabel('Animation Speed:')
        speed_slider = QSlider(Qt.Horizontal)
        speed_slider.setMinimum(1)
        speed_slider.setMaximum(100)
        speed_slider.setValue(50)
        control_layout.addWidget(speed_label)
        control_layout.addWidget(speed_slider)

        # control buttons
        start_button = QPushButton('Start')
        pause_button = QPushButton('Pause')
        reset_button = QPushButton('Reset')

        # connect signals
        start_button.clicked.connect(self.start_visualization)
        pause_button.clicked.connect(self.pause_visualization)
        reset_button.clicked.connect(self.reset_visualization)

        # adding buttons
        control_layout.addWidget(start_button)
        control_layout.addWidget(pause_button)
        control_layout.addWidget(reset_button)

        # stretched space
        control_layout.addStretch()

        # styles
        control_widget.setStyleSheet("""
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

        return control_widget

    def create_visualization_area(self):
        # creating visualization area
        visualization_widget = QWidget()
        visualization_layout = QVBoxLayout(visualization_widget)

        # test
        placeholder = QLabel('Visualization Area')
        placeholder.setAlignment(Qt.AlignCenter)

        visualization_layout.addWidget(placeholder)

        # styles
        visualization_widget.setStyleSheet("""
            QWidget {
                background-color: white;
            }
            QLabel {
                font-size: 24px;
                color: #666666;
            }
        """)

        return visualization_widget

    def start_visualization(self):
        print('starting')

    def pause_visualization(self):
        print('pausing')

    def reset_visualization(self):
        print('resetting')
