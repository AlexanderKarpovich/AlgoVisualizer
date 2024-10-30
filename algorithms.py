from PyQt5 import QtWidgets, QtGui, QtCore
import random


# bubble sort
class BubbleSortWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.data = [random.randint(1, 9999) for _ in range(100)]
        self.current_index = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_animation)

    def bubble_sort(self, data: list):
        for i in range(len(data)):
            for j in range(len(data) - 1 - i):
                yield j
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]

    def start_sorting(self):
        self.generator = self.bubble_sort(self.data)
        self.timer.start()

    def update_animation(self):
        try:
            j = next(self.generator)
            self.current_index = j
            self.update()
        except StopIteration:
            self.timer.stop()
            self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        width = self.width() // len(self.data)
        max_height = int(self.height() * 0.9)

        max_value = max(self.data)

        for i, value in enumerate(self.data):
            height = int((value / max_value) * max_height)

            color = QtGui.QColor(0, 0, 255)
            if i == self.current_index or i == self.current_index + 1:
                color = QtGui.QColor(255, 0, 0)

            painter.setBrush(color)
            painter.drawRect(i * width, self.height() - height, width, height)


# quick sort
def quick_sort(data: list) -> list:
    if len(data) < 2:
        yield data
    pivot = data[len(data) // 2]
    less = [x for x in data if x < pivot]
    equal = [x for x in data if x == pivot]
    greater = [x for x in data if x > pivot]
    yield quick_sort(less) + equal + quick_sort(greater)


# merge sort
def merge_sort(data: list) -> list:
    if len(data) < 2:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
