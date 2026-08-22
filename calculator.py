import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel,
    QWidget, QGridLayout, QLineEdit,
    QPushButton
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(1400, 100, 450, 600)
        self.setWindowTitle("Calculator")
        self.setStyleSheet("background-color:#FFFDDO;")
        self.setup()
        self.title()
        self.Display()
        self.button()
        self.connection()

    def setup(self):
        self.central = QWidget()
        self.setCentralWidget(self.central)
        self.grid = QGridLayout()
        self.central.setLayout(self.grid)


    def title(self):
        self.Label = QLabel("Calculator")
        self.Label.setAlignment(Qt.AlignTop)
        self.Label.setAlignment(Qt.AlignLeft)
        self.Label.setFont(QFont("Arial", 15))
        self.Label.setFixedHeight(50)
        self.Label.setStyleSheet("""
            background-color: #FFFDDO;
            color: black;
            border-radius: 10px;
        """)

        self.grid.addWidget(self.Label, 0, 0, 1, 4)


    def Display(self):
        self.display = QLineEdit()
        self.display.setFont(QFont("Arial", 38))
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(90)

        self.display.setStyleSheet("""
            QLineEdit{
                background: white;
                border: none;
                border-radius: 10px;
                padding: 10px;
            }
        """)

        self.grid.addWidget(self.display, 1, 0, 1, 4)
    def button(self):

        # Top row
        self.btnAC = QPushButton("AC")
        self.btnd = QPushButton("Del")
        self.btnper = QPushButton("%")
        self.btndiv = QPushButton("/")

        # Row 2
        self.btn7 = QPushButton("7")
        self.btn8 = QPushButton("8")
        self.btn9 = QPushButton("9")
        self.btnmul = QPushButton("*")

        # Row 3
        self.btn4 = QPushButton("4")
        self.btn5 = QPushButton("5")
        self.btn6 = QPushButton("6")
        self.btnmin = QPushButton("-")

        # Row 4
        self.btn1 = QPushButton("1")
        self.btn2 = QPushButton("2")
        self.btn3 = QPushButton("3")
        self.btnadd = QPushButton("+")

        # Row 5
        self.btn0 = QPushButton("0")
        self.btndot = QPushButton(".")
        self.btnequ = QPushButton("=")

        # ---------- Styles ----------

        number_style = """
        QPushButton{
            background-color:#F5F5F5;
            border:none;
            border-radius:20px;
            font:25px Arial;
        }
        QPushButton:hover{
            background-color:#EAEAEA;
        }
        """

        operator_style = """
        QPushButton{
            background-color:#FF9800;
            color:white;
            border:none;
            border-radius:20px;
            font:bold 24px Arial;
        }
        QPushButton:hover{
            background-color:#FB8C00;
        }
        """

        top_style = """
        QPushButton{
            background-color:#F5F5F5;
            color:#FF9800;
            border:none;
            border-radius:20px;
            font:bold 22px Arial;
        }
        """

        self.btnAC.setStyleSheet(top_style)
        self.btnd.setStyleSheet(top_style)
        self.btnper.setStyleSheet(top_style)

        self.btndiv.setStyleSheet(operator_style)
        self.btnmul.setStyleSheet(operator_style)
        self.btnmin.setStyleSheet(operator_style)
        self.btnadd.setStyleSheet(operator_style)
        self.btnequ.setStyleSheet(operator_style)

        self.btn0.setStyleSheet(number_style)
        self.btn1.setStyleSheet(number_style)
        self.btn2.setStyleSheet(number_style)
        self.btn3.setStyleSheet(number_style)
        self.btn4.setStyleSheet(number_style)
        self.btn5.setStyleSheet(number_style)
        self.btn6.setStyleSheet(number_style)
        self.btn7.setStyleSheet(number_style)
        self.btn8.setStyleSheet(number_style)
        self.btn9.setStyleSheet(number_style)
        self.btndot.setStyleSheet(number_style)

        # Button Size
        buttons = [
            self.btnAC, self.btnd, self.btnper, self.btndiv,
            self.btn7, self.btn8, self.btn9, self.btnmul,
            self.btn4, self.btn5, self.btn6, self.btnmin,
            self.btn1, self.btn2, self.btn3, self.btnadd,
            self.btn0, self.btndot, self.btnequ
        ]

        for button in buttons:
            button.setFixedSize(85, 85)


        self.grid.addWidget(self.btnAC, 2, 0)
        self.grid.addWidget(self.btnd, 2, 1)
        self.grid.addWidget(self.btnper, 2, 2)
        self.grid.addWidget(self.btndiv, 2, 3)

        self.grid.addWidget(self.btn7, 3, 0)
        self.grid.addWidget(self.btn8, 3, 1)
        self.grid.addWidget(self.btn9, 3, 2)
        self.grid.addWidget(self.btnmul, 3, 3)

        self.grid.addWidget(self.btn4, 4, 0)
        self.grid.addWidget(self.btn5, 4, 1)
        self.grid.addWidget(self.btn6, 4, 2)
        self.grid.addWidget(self.btnmin, 4, 3)

        self.grid.addWidget(self.btn1, 5, 0)
        self.grid.addWidget(self.btn2, 5, 1)
        self.grid.addWidget(self.btn3, 5, 2)
        self.grid.addWidget(self.btnadd, 5, 3)

        self.grid.addWidget(self.btn0, 6, 1)
        self.grid.addWidget(self.btndot, 6, 2)
        self.grid.addWidget(self.btnequ, 6, 3)


    def connection(self):
        self.btn0.clicked.connect(lambda:self.textadding("0"))
        self.btn1.clicked.connect(lambda:self.textadding("1"))
        self.btn2.clicked.connect(lambda:self.textadding("2"))
        self.btn3.clicked.connect(lambda:self.textadding("3"))
        self.btn4.clicked.connect(lambda:self.textadding("4"))
        self.btn5.clicked.connect(lambda:self.textadding("5"))
        self.btn6.clicked.connect(lambda:self.textadding("6"))
        self.btn7.clicked.connect(lambda:self.textadding("7"))
        self.btn8.clicked.connect(lambda:self.textadding("8"))
        self.btn9.clicked.connect(lambda:self.textadding("9"))

        self.btnadd.clicked.connect(lambda:self.textadding("+"))
        self.btnmin.clicked.connect(lambda:self.textadding("-"))
        self.btnmul.clicked.connect(lambda:self.textadding("*"))
        self.btndiv.clicked.connect(lambda:self.textadding("/"))
        self.btndot.clicked.connect(lambda:self.textadding("."))
        self.btnper.clicked.connect(lambda:self.textadding("%"))

        self.btnAC.clicked.connect(self.clear)
        self.btnd.clicked.connect(self.delete)
        self.btnequ.clicked.connect(self.equals)


    def textadding(self,x):
        self.display.setText(self.display.text()+x)
        


    def clear(self):
        self.display.clear()

    def delete(self):
        text=self.display.text()
        self.display.setText(text[:-1])

    def equals(self):
        try:
            result = str(eval(self.display.text()))
            self.display.setText(result)
        except:
            self.display.setText("Error")
        
        

app=QApplication(sys.argv)
Window=MainWindow()
Window.show()
sys.exit(app.exec())

        