
from PySide import QtCore, QtGui

from publisher.gui.ui.ts_title import Ui_ts_title


class SpinnerOverlay(QtGui.QWidget):

    def __init__(self, parent=None):
        super(SpinnerOverlay, self).__init__(parent)
        self._timer = QtCore.QTimer(self)
        self.box_size = 100
        self.thickness = 6
        self.arc_length = 300
        self._start_angle = 0
        self._timer.timeout.connect(self._on_timer_timeout)

        filter = ResizeEventFilter(parent)
        filter.resized.connect(self._on_parent_resized)
        parent.installEventFilter(filter)

        self.hide()

    def paintEvent(self, event):
        super(SpinnerOverlay, self).paintEvent(event)

        painter = QtGui.QPainter()
        painter.begin(self)
        try:
            painter.setRenderHint(QtGui.QPainter.Antialiasing)

            fg_col = self.palette().color(self.foregroundRole())
            pen = QtGui.QPen(fg_col)
            pen.setWidth(self.thickness)
            painter.setPen(pen)

            width_border = (self.width()-self.box_size)/2
            height_border = (self.height()-self.box_size)/2
            r = QtCore.QRect(0, 0, self.width(), self.height())
            r.adjust(width_border, height_border, -width_border, -height_border)

            # draw the arc:
            painter.drawArc(r, -self._start_angle * 16, self.arc_length * 16)
            r = None

        finally:
            painter.end()
            painter = None

    def showEvent(self, event):
        if not self._timer.isActive():
            self._timer.start(100)
        super(SpinnerOverlay, self).showEvent(event)

    def hideEvent(self, event):
        self._timer.stop()
        super(SpinnerOverlay, self).hideEvent(event)

    def closeEvent(self, event):
        self._timer.stop()
        super(SpinnerOverlay, self).closeEvent(event)

    def _on_timer_timeout(self):
        self._start_angle = (self._start_angle + 10)
        if self._start_angle > 360:
            self._start_angle -= 360
        self.update()

    def _on_parent_resized(self):
        self.resize(self.parentWidget().size())


class TSTitle(QtGui.QWidget, Ui_ts_title):

    def __init__(self, parent=None):
        super(TSTitle, self).__init__(parent)
        self.setupUi(self)

    def setText(self, text):
        self.label.setText(text)


class ResizeEventFilter(QtCore.QObject):
    """
    Event filter which emits a resized signal whenever
    the monitored widget resizes. This is so that the overlay wrapper
    class can be informed whenever the Widget gets a resize event.
    """
    resized = QtCore.Signal()

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.Resize:
            self.resized.emit()
        return False
