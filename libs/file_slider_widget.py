import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class FileSliderWidget(QWidget):
   def __init__(self, max_value: int, cur_img_num: int=0, main_window: QMainWindow=None, parent=None):
      super(FileSliderWidget, self).__init__(parent)

      # Validation of function input
      self.max_value = max(max_value, 0)
      self.file_index = min((max(cur_img_num - 1, 0), self.max_value - 1))

      self.main_window = main_window

      layout = QHBoxLayout()

      self.sl = QSlider(Qt.Horizontal)
      self.sl.setMinimum(0)
      self.sl.setMaximum(max_value - 1)
      self.sl.setValue(self.file_index)
      self.sl.setTickPosition(QSlider.TicksBelow)
      self.sl.setTickInterval(5 if max_value > 10 else 1)

      layout.addWidget(self.sl)
      self.sl.valueChanged.connect(self.slider_change)

      self.l1 = QLineEdit(self)
      self.l1.setFixedSize(QSize(100, 40))
      self.l1.setAlignment(Qt.AlignCenter)
      self.l1.setText(str(self.file_index + 1))
      self.l1.setValidator(QIntValidator(1, max_value, self))
      layout.addWidget(self.l1)
      self.setLayout(layout)

   def set_max_value(self, value):
      self.max_value = max(value, 0)
      self.sl.setMaximum(self.max_value - 1)

   def slider_change(self):
      self.file_index = self.sl.value()
      self.l1.setText(str(self.file_index + 1))
      self.file_index_changed()  # TODO: bad practice, ewww :0

   def keyPressEvent(self, qKeyEvent):
      # TODO: Clear input by double clicking on the input field
      if self.l1.hasFocus() and qKeyEvent.key() == Qt.Key_Return:
         input_text = self.l1.text()
         if not input_text:
            input_text = str(self.file_index + 1)
            self.l1.setText(input_text)
         input = min(self.max_value, int(input_text))
         self.file_index = input - 1
         self.sl.setValue(self.file_index)
         self.l1.setText(str(input))
         self.file_index_changed()
      else:
         super().keyPressEvent(qKeyEvent)


   def file_index_changed(self):
      try:
         self.main_window.import_dir_images(file_path=self.main_window.m_img_list[self.file_index])
      except Exception:
         pass

   def file_changed(self, file_index):
      self.file_index = file_index
      self.l1.setText(str(self.file_index + 1))
      self.sl.setValue(self.file_index)


def main():
   app = QApplication(sys.argv)
   ex = FileSliderWidget(100, 10)
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()