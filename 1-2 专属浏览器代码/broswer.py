import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QToolBar, QAction, QTabWidget, QMenu, QDialog, QVBoxLayout,QListWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.setCentralWidget(self.browser)

        # 添加搜索栏
        search_bar = QLineEdit()
        search_bar.returnPressed.connect(lambda: self.browser.setUrl(QUrl(search_bar.text())))
        toolbar = QToolBar()
        toolbar.addWidget(search_bar)
        self.addToolBar(toolbar)

        # 添加前进、后退和刷新按钮
        back_button = QAction("Back", self)
        back_button.triggered.connect(self.browser.back)
        forward_button = QAction("Forward", self)
        forward_button.triggered.connect(self.browser.forward)
        refresh_button = QAction("Refresh", self)
        refresh_button.triggered.connect(self.browser.reload)

        # 添加按钮到工具栏
        toolbar.addAction(back_button)
        toolbar.addAction(forward_button)
        toolbar.addAction(refresh_button)

        self.showMaximized()

        # 添加查看历史记录的功能
        history_menu = QMenu("History", self)
        history_action = QAction("View History", self)
        history_action.triggered.connect(self.show_history)
        history_menu.addAction(history_action)
        menu_bar = self.menuBar()
        menu_bar.addMenu(history_menu)

    def show_history(self):
        history = self.browser.history()
        dialog = QDialog(self)
        dialog.setWindowTitle("History")
        dialog.setLayout(QVBoxLayout())

        history_list = QListWidget()
        for i in range(history.count()):
            history_list.addItem(history.itemAt(i).url().toString())

        dialog.layout().addWidget(history_list)
        dialog.exec_()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    sys.exit(app.exec_())
