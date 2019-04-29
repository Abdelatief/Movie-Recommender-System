from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QTableView
from pyuic5 import *
from mainwindow import *
import sys
from TableMod import *
import pandas as pd
from MovieRecommender import Graphs
import matplotlib.pyplot as plt
import seaborn as sns
from pprint import pprint
from PyQt5.QtCore import QAbstractTableModel, Qt


class MessageBox(QMessageBox):
    """A class to make showing messages easier"""
    def __init__(self, title: str, text: str, icon: QMessageBox.Icon, buttons: QMessageBox.StandardButtons):
        super().__init__()
        self.setText(text)
        self.setWindowTitle(title)
        self.standardIcon(icon)
        self.setStandardButtons(buttons)

    def show(self):
        self.exec_()


class MainForm(QDialog):
    def __init__(self):
        """The constructor of the main form class, it setup the ui and the signals and slots(events)"""
        super().__init__()
        self.ui = Ui_mainwindow_dialog()
        self.ui.setupUi(self)
        self.show()
        self.g = Graphs()
        self.ui.barchar_show_button.clicked.connect(self.g.barchart)
        self.ui.piechart_show_button.clicked.connect(self.g.piechart)
        self.ui.dotplot_show_button.clicked.connect(self.show_dotplot)
        self.ui.hist_show_button.clicked.connect(self.g.hist)
        self.ui.boxplot_show_button.clicked.connect(self.show_boxplot)
        self.ui.mean_show_button.clicked.connect(self.g.mean_table)
        self.ui.correlation_show_button.clicked.connect(self.show_correlation)

    def load_dataframe(self):
        pass

    def show_barchart(self):
        movie = self.get_movie_name()
        if movie is not None:
            pass
            # Write here the code required to show bar chart

    def show_piechart(self):
        movie = self.get_movie_name()
        if movie is not None:
            pass
            # Write here the code required to show pie chart

    def show_dotplot(self):
        movie = self.get_movie_name()
        if movie is not None:
            pass
            # Write here the code required to show dot plot

    def show_hist(self):
        movie = self.get_movie_name()
        if movie is not None:
            pass
            # Write here the code required to show histogram

    def show_boxplot(self):
        movie = self.get_movie_name()
        if movie is not None:
            pass
            # Write here the code required to show boxplot

    def show_mean(self):
        movie = self.get_movie_name()
        if movie is not None:
            pass
            # Write here the code required to show mean

    def show_correlation(self):
        movie = self.get_movie_name()
        if movie is not None:
            pass
            # Write here the code required to show correlation

    def show_table(self, dataframe: pd.DataFrame):
        """This function takes a dataframe and show it in a table.. hopefully"""
        table = Table(dataframe)
        table.show()

    def get_movie_name(self):
        """Shows a message if the movie text field is empty, else returns the movie name"""
        movie_name = self.ui.movie_name_lineEdit.text().strip()
        print(movie_name)
        if movie_name == '':
            empty_line_message = MessageBox('Empty Field', 'Please Enter Movie Name', QMessageBox.Information,
                                            QMessageBox.Ok)
            empty_line_message.show()
            return None
        else:
            return movie_name

    def update_movies_list(self, movies_list: list):
        """This function takes the list of the similar movies list and shows them in the GUI list widget"""
        self.ui.similar_movies_listWidget.clear()
        self.ui.similar_movies_listWidget.addItems(movies_list)


# This if condition makes this line of code run when this module runs from here as if it was imported it won't run
if __name__ == '__main__':
    convert_ui_to_py('mainwindow.ui')
    app = QApplication(sys.argv)
    form = MainForm()
    # print(type(QMessageBox.Information))
    # print(type(QMessageBox.Ok))
    sys.exit(app.exec_())
