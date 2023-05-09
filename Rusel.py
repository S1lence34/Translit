import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog
from PyQt5.QtCore import QTimer

import transliterate

class TransliterationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Транслитерация текста')
        self.setGeometry(100, 100, 600, 400)

        # Создаем виджеты
        self.input_label = QLabel('Введите текст на кириллице:')
        self.input_text = QTextEdit()
        self.output_label = QLabel('Текст на латинице:')
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.transliterate_button = QPushButton('Транслитерировать')
        self.transliterate_button.clicked.connect(self.transliterate)
        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_result)
        self.update_button = QPushButton('Обновить')
        self.update_button.clicked.connect(lambda: QTimer.singleShot(5000, self.transliterate))
        self.clear_button = QPushButton('Очистить')
        self.clear_button.clicked.connect(self.clear_fields)

        # Размещаем виджеты на форме
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.input_label)
        hbox1.addWidget(self.input_text)
        vbox.addLayout(hbox1)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.output_label)
        hbox2.addWidget(self.output_text)
        vbox.addLayout(hbox2)
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.transliterate_button)
        hbox3.addWidget(self.save_button)
        hbox3.addWidget(self.update_button)
        hbox3.addWidget(self.clear_button)
        vbox.addLayout(hbox3)
        self.setLayout(vbox)

    def transliterate(self):
        input_text = self.input_text.toPlainText()
        output_text = transliterate.translit(input_text, 'ru', reversed=True)
        self.output_text.setText(output_text)

    def save_result(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить результат", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'w') as f:
                f.write(self.output_text.toPlainText())

    def clear_fields(self):
        self.input_text.clear()
        self.output_text.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    transliteration_app = TransliterationApp()
    transliteration_app.show()
    sys.exit(app.exec_())




