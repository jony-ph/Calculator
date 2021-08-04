import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        uic.loadUi('GUI.ui', self)

        self.btn_00.clicked.connect(lambda: self.number('00'))
        self.btn_0.clicked.connect(lambda: self.number('0'))
        self.btn_1.clicked.connect(lambda: self.number('1'))
        self.btn_2.clicked.connect(lambda: self.number('2'))
        self.btn_3.clicked.connect(lambda: self.number('3'))
        self.btn_4.clicked.connect(lambda: self.number('4'))
        self.btn_5.clicked.connect(lambda: self.number('5'))
        self.btn_6.clicked.connect(lambda: self.number('6'))
        self.btn_7.clicked.connect(lambda: self.number('7'))
        self.btn_8.clicked.connect(lambda: self.number('8'))
        self.btn_9.clicked.connect(lambda: self.number('9'))
        self.btn_C.clicked.connect(lambda: self.number('C'))

    def number(self, n):

        if n == 'C':
            self.screen.setText('0')
        else:
            
            if self.screen.text() == '0':

                if n == '0' or n == '00':
                    return
                self.screen.setText('')

            self.screen.setText(self.screen.text() + n)

            
        


if __name__ == '__main__':

    app = QApplication(sys.argv)
    root_frame = Main()
    
    root_frame.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing window...')
