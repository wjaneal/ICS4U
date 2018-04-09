"""
author: Jan Bodnar
website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 150)
    w.move(600, 300)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())