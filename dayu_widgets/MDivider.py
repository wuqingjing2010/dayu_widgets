#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from qt import *
from MLabel import MLabel

@property_mixin
class MDivider(QWidget):
    _alignment_map = {
        Qt.AlignCenter: 50,
        Qt.AlignLeft: 20,
        Qt.AlignRight: 80,
    }

    def __init__(self, text='', orientation=Qt.Horizontal, alignment=Qt.AlignCenter, parent=None):
        super(MDivider, self).__init__(parent)
        self._text_label = MLabel(type=MLabel.HelpType)
        self._left_frame = QFrame()
        self._right_frame = QFrame()
        self._main_lay = QHBoxLayout()
        self._main_lay.setContentsMargins(0, 0, 0, 0)
        self._main_lay.setSpacing(0)
        self._main_lay.addWidget(self._left_frame)
        self._main_lay.addWidget(self._text_label)
        self._main_lay.addWidget(self._right_frame)
        self.setLayout(self._main_lay)

        self.setProperty('text', text)
        self.setProperty('orientation', orientation)
        self.setProperty('alignment', alignment)

    def set_text(self, value):
        self._text_label.setProperty('text', value)
        with_text = bool(value)
        if not with_text:
            self._text_label.setStyleSheet('font-size:1px;padding:0')

    def set_orientation(self, value):
        if value == Qt.Horizontal:
            self._left_frame.setVisible(True)
            self._text_label.setVisible(True)
            self._right_frame.setVisible(True)
            self._left_frame.setFrameShape(QFrame.HLine)
            self._left_frame.setFrameShadow(QFrame.Sunken)
            self._right_frame.setFrameShape(QFrame.HLine)
            self._right_frame.setFrameShadow(QFrame.Sunken)
        else:
            self._left_frame.setVisible(True)
            self._text_label.setVisible(False)
            self._right_frame.setVisible(False)
            self._left_frame.setFrameShape(QFrame.VLine)
            self._left_frame.setFrameShadow(QFrame.Plain)
            self.setFixedWidth(2)

    def set_alignment(self, value):
        self._main_lay.setStretchFactor(self._left_frame, self._alignment_map.get(value, 50))
        self._main_lay.setStretchFactor(self._right_frame, 100 - self._alignment_map.get(value, 50))
