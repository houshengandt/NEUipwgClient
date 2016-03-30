import sys
from PyQt5.QtWidgets import *
from ui import Ui_Form
from ipwg import PostIt


if __name__ == "__main__":
    post_data = PostIt.info('20131151', 'wsmsdcx', 'connect')
    PostIt.u_operation(post_data)
    app = QApplication(sys.argv)
    widget = QWidget(None)
    Ui_Form().setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
