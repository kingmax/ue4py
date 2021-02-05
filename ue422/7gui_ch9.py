# coding:utf-8

import os
import sys
import unreal as u

from PySide import QtCore, QtGui, QtUiTools

_ui = os.path.join(os.path.dirname(__file__), 'basic.ui')
print(_ui)

edLevelLib = u.EditorLevelLibrary()


class Win(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Win, self).__init__(parent)

        self.widget = QtUiTools.QUiLoader().load(_ui)

        # attach the widget to 'self' GUI
        self.widget.setParent(self)

        # set the UI geometry (if UI is not centered/visible)
        self.widget.setGeometry(0, 0, self.widget.width(), self.widget.height())

        # find the interaction elements
        self.txtA = self.widget.findChild(QtGui.QLineEdit, 'txtA')
        self.txtB = self.widget.findChild(QtGui.QLineEdit, 'txtB')

        self.slider = self.widget.findChild(QtGui.QSlider, 'sld')

        self.chkSure = self.widget.findChild(QtGui.QCheckBox, 'chkSure')
        self.btnOK = self.widget.findChild(QtGui.QPushButton, 'btnOK')
        self.btnCancel = self.widget.findChild(QtGui.QPushButton, 'btnCancel')

        self.slider.sliderMoved.connect(self.on_slide)
        self.btnOK.clicked.connect(self.btnOK_click)
        self.btnCancel.clicked.connect(self.btnCancel_click)

    def on_slide(self):
        value = self.slider.value()
        print(value)

        # move the selected actor according to the slider value
        selected_actors = edLevelLib.get_selected_level_actors()
        if selected_actors:
            actor = selected_actors[0]

            transform = actor.get_actor_transform()
            transform.translation.y = value

            actor.set_actor_transform(transform, True, True)

    def btnOK_click(self):
        txtA = self.txtA.text()
        txtB = self.txtB.text()
        checked = self.chkSure.isChecked()

        print('txtA:{}, txtB:{}, checked:{}'.format(txtA, txtB, checked))

    def btnCancel_click(self):
        self.close()


# only create an instance of the GUI when it's not already running
app = None
if not QtGui.QApplication.instance():
    app = QtGui.QApplication(sys.argv)
print('app: {}'.format(app))

win = Win()
u.parent_external_window_to_slate(win.winId())
win.show()
print('win.parent:{}'.format(win.parent()))
# https://forums.unrealengine.com/unreal-engine/unreal-studio/1526501-how-to-get-the-main-window-of-the-editor-to-parent-qt-or-pyside-application-to-it
# u.parent_external_window_to_slate(win.winId())
print('win.parent:{}'.format(win.parent()))
print('the end line for testing')


# refs: https://github.com/AlexQuevillon/UnrealPythonLibrary/blob/master/UnrealProject/UnrealPythonLibrary/Plugins/UnrealPythonLibraryPlugin/Content/Python/PythonLibraries/QtFunctions.py
# This function will receive the tick from Unreal
# def __QtAppTick__(delta_seconds):
#     for window in opened_windows:
#         window.eventTick(delta_seconds)
#
#
# # This function will be called when the application is closing.
# def __QtAppQuit__():
#     u.unregister_slate_post_tick_callback(tick_handle)
#
#
# # This function is called by the windows when they are closing. (Only if the connection is properly made.)
# def __QtWindowClosed__(window=None):
#     if window in opened_windows:
#         opened_windows.remove(window)
#
#
# existing_windows = {}
# opened_windows = []
# # This part is for the initial setup. Need to run once to spawn the application.
# unreal_app = QtGui.QApplication.instance()
# if not unreal_app:
#     unreal_app = QtGui.QApplication(sys.argv)
#     tick_handle = u.register_slate_post_tick_callback(__QtAppTick__)
#     unreal_app.aboutToQuit.connect(__QtAppQuit__)
#     global existing_windows
#     existing_windows = {}
#     global opened_windows
#     opened_windows = []
#
#
# # desired_window_class: class QtGui.QWidget : The window class you want to spawn
# # return: The new or existing window
# def spawnQtWindow(desired_window_class=None):
#     window = existing_windows.get(desired_window_class, None)
#     if not window:
#         window = desired_window_class()
#         existing_windows[desired_window_class] = window
#         window.aboutToClose = __QtWindowClosed__
#     if window not in opened_windows:
#         opened_windows.append(window)
#     window.show()
#     window.activateWindow()
#     return window
#
#
# if __name__ == '__main__':
#     spawnQtWindow(Win)
