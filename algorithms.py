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
class QuickSortWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.data = [random.randint(1, 9999) for _ in range(100)]
        self.current_indices = []
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_animation)

    def quick_sort(self, data: list, start: int = 0, end: int = None):
        if end is None:
            end = len(data) - 1

        if start >= end:
            return

        pivot = data[(start + end) // 2]
        left = start
        right = end

        while left <= right:
            while data[left] < pivot:
                left += 1
            while data[right] > pivot:
                right -= 1
            if left <= right:
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1
                self.current_indices = list(range(start, end + 1))
                yield data

        yield from self.quick_sort(data, start, right)
        yield from self.quick_sort(data, left, end)

    def start_sorting(self):
        self.generator = self.quick_sort(self.data)
        self.timer.start()

    def update_animation(self):
        try:
            self.data = next(self.generator)
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
            if i in self.current_indices:
                color = QtGui.QColor(255, 0, 0)

            painter.setBrush(color)
            painter.drawRect(i * width, self.height() - height, width, height)


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
