import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView, QSizePolicy
from PyQt5.QtCore import QAbstractTableModel, Qt


class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


class Table:
    def __init__(self, dataframe: pd.DataFrame):
        model = PandasModel(dataframe)
        self.table = QTableView()
        self.table.setModel(model)
        self.table.resize(800, 600)
        self.table.setAccessibleName('Table')
        self.table.setObjectName('tableView')
        self.table.setWindowTitle('T')
        print(self.table.size())

    def show(self):
        self.table.show()
