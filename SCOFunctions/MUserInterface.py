import os
import sys
import time
import traceback
import subprocess

from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets

from SCOFunctions.MFilePath import innerPath
from SCOFunctions.MLogging import logclass
from SCOFunctions.MainFunctions import show_overlay


logger = logclass('UI','INFO')


def find_file(file):
    new_path = os.path.abspath(file)
    logger.info(f'Finding file {new_path}')
    subprocess.Popen(f'explorer /select,"{new_path}"')


class MapEntry(QtWidgets.QWidget):
    """Custom widget for map entry in stats""" 
    def __init__(self, parent, y, name, time_fastest, time_average, wins, losses, button=True, bold=False):
        super().__init__(parent)

        self.setGeometry(QtCore.QRect(15, y, parent.width()-15, 40))
        if bold:
            self.setStyleSheet('font-weight: bold')
        
        # Button/label
        self.bt_button = QtWidgets.QPushButton(self) if button else QtWidgets.QLabel(self)
        if not button:
            self.bt_button.setAlignment(QtCore.Qt.AlignCenter)
        self.bt_button.setGeometry(QtCore.QRect(0, 0, 150, 25))
        if 'Lock' in name and 'Load' in name:
            name = "Lock and Load"
        self.bt_button.setText(name)

        # Average time
        self.la_average = QtWidgets.QLabel(self)
        self.la_average.setGeometry(QtCore.QRect(155, 0, 70, 20))
        self.la_average.setAlignment(QtCore.Qt.AlignCenter)
        self.la_average.setToolTip('Average victory time')
        time_average = time_average if time_average != 3599 else '–'
        if isinstance(time_average, int) or isinstance(time_average, float):
            if time_average < 3600:
                self.la_average.setText(time.strftime('%M:%S',time.gmtime(time_average)))
            else:
                self.la_average.setText(time.strftime('%H:%M:%S',time.gmtime(time_average)))
        else:
            self.la_average.setText(time_average)

        # Fastest time
        self.la_fastest = QtWidgets.QLabel(self)
        self.la_fastest.setGeometry(QtCore.QRect(218, 0, 70, 20))
        self.la_fastest.setAlignment(QtCore.Qt.AlignCenter)
        self.la_fastest.setToolTip('Fastest victory time')
        time_fastest = time_fastest if time_fastest != 3599 else '–'
        if isinstance(time_fastest, int) or isinstance(time_fastest, float):
            if time_fastest < 3600:
                self.la_fastest.setText(time.strftime('%M:%S',time.gmtime(time_fastest)))
            else:
                self.la_fastest.setText(time.strftime('%H:%M:%S',time.gmtime(time_fastest)))
        else:
            self.la_fastest.setText(time_fastest)
      
        # Wins
        self.la_wins = QtWidgets.QLabel(self)
        self.la_wins.setGeometry(QtCore.QRect(280, 0, 50, 20))
        self.la_wins.setAlignment(QtCore.Qt.AlignCenter)  
        self.la_wins.setText(str(wins))

        # Losses
        self.la_losses = QtWidgets.QLabel(self)
        self.la_losses.setGeometry(QtCore.QRect(325, 0, 50, 20))
        self.la_losses.setAlignment(QtCore.Qt.AlignCenter)  
        self.la_losses.setText(str(losses))

        # Winrate
        self.la_winrate = QtWidgets.QLabel(self)
        self.la_winrate.setGeometry(QtCore.QRect(380, 0, 50, 20))
        self.la_winrate.setAlignment(QtCore.Qt.AlignCenter)  
        if isinstance(wins, str) or isinstance(losses, str):
            winrate = 'Winrate'
        else:
            winrate = '-'
            if wins or losses > 0:
                winrate = f"{100*wins/(wins+losses):.0f}%"
        self.la_winrate.setText(winrate)


class DifficultyEntry(QtWidgets.QWidget):
    """Custom widget for difficulty entry in stats"""

    def __init__(self, name, wins, losses, winrate, x, y, bold=False, line=False, bg=False, bgcolor="#f1f1f1", parent=None):
        super().__init__(parent)

        self.setGeometry(QtCore.QRect(x, y, 300, 40))

        self.la_name = QtWidgets.QLabel(self)
        self.la_name.setGeometry(QtCore.QRect(10, 10, 70, 20))
        self.la_name.setText(str(name))

        self.la_wins = QtWidgets.QLabel(self)
        self.la_wins.setGeometry(QtCore.QRect(60, 10, 70, 20))
        self.la_wins.setAlignment(QtCore.Qt.AlignCenter)
        self.la_wins.setText(str(wins))

        self.la_losses = QtWidgets.QLabel(self)
        self.la_losses.setGeometry(QtCore.QRect(110, 10, 70, 20))
        self.la_losses.setAlignment(QtCore.Qt.AlignCenter)
        self.la_losses.setText(str(losses))

        self.la_winrate = QtWidgets.QLabel(self)
        self.la_winrate.setGeometry(QtCore.QRect(180, 10, 50, 20))
        self.la_winrate.setAlignment(QtCore.Qt.AlignCenter)
        self.la_winrate.setText(str(winrate))

        style = ''

        if bold:
            style += 'font-weight: bold;'

        if bg:
            style += f'background-color: {bgcolor}'

        self.setStyleSheet(style)

        if line:
            self.line = QtWidgets.QFrame(self)
            self.line.setGeometry(QtCore.QRect(0, 30, 235, 2))
            self.line.setFrameShape(QtWidgets.QFrame.HLine)
            self.line.setFrameShadow(QtWidgets.QFrame.Sunken)                 


class GameEntry:
    """ 
    Class for UI elements in games tab. 
    It takes `replay_dict` generated by s2parser. 
    """

    def __init__(self, replay_dict, handles, parent):
        self.mapname = replay_dict['map_name']
        self.result = replay_dict['result']
        self.difficulty = replay_dict['ext_difficulty']
        self.enemy = replay_dict['enemy_race']
        self.length = replay_dict['form_alength']
        self.file = replay_dict['file']
        self.date = replay_dict['date'][:10].replace(':','-')

        if replay_dict['players'][1]['handle'] in handles:
            self.p1_name = replay_dict['players'][1]['name']
            self.p1_commander = replay_dict['players'][1]['commander']
            self.p1_handle = replay_dict['players'][1]['handle']
            self.p2_name = replay_dict['players'][2]['name']
            self.p2_commander = replay_dict['players'][2]['commander']
            self.p2_handle = replay_dict['players'][2]['handle']
        else:
            self.p1_name = replay_dict['players'][2]['name']
            self.p1_commander = replay_dict['players'][2]['commander']
            self.p1_handle = replay_dict['players'][2]['handle']
            self.p2_name = replay_dict['players'][1]['name']
            self.p2_commander = replay_dict['players'][1]['commander']
            self.p2_handle = replay_dict['players'][1]['handle']


        height = 30
        line_spacing = 7

        self.widget = QtWidgets.QWidget(parent)
        self.widget.setGeometry(QtCore.QRect(0, 0, 931, height))
        self.widget.setMinimumHeight(height)
        self.widget.setMaximumHeight(height)

        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(10, 0, 921, 2))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)        

        self.la_mapname = QtWidgets.QLabel(self.widget)
        self.la_mapname.setGeometry(QtCore.QRect(20, line_spacing, 120, 21))
        self.la_mapname.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.la_mapname.setText(self.mapname)

        self.la_result = QtWidgets.QLabel(self.widget)
        self.la_result.setGeometry(QtCore.QRect(135, line_spacing, 50, 21))
        self.la_result.setAlignment(QtCore.Qt.AlignCenter)
        self.la_result.setText(self.result)

        self.la_p1 = QtWidgets.QLabel(self.widget)
        self.la_p1.setGeometry(QtCore.QRect(170, line_spacing, 200, 21))
        self.la_p1.setAlignment(QtCore.Qt.AlignCenter)
        self.la_p1.setText(f'{self.p1_name} ({self.p1_commander})')

        self.la_p2 = QtWidgets.QLabel(self.widget)
        self.la_p2.setGeometry(QtCore.QRect(305, line_spacing, 200, 21))
        self.la_p2.setAlignment(QtCore.Qt.AlignCenter)
        self.la_p2.setText(f'{self.p2_name} ({self.p2_commander})')

        self.la_enemy = QtWidgets.QLabel(self.widget)
        self.la_enemy.setGeometry(QtCore.QRect(480, line_spacing, 41, 20))
        self.la_enemy.setAlignment(QtCore.Qt.AlignCenter)
        self.la_enemy.setText(self.enemy)

        self.la_length = QtWidgets.QLabel(self.widget)
        self.la_length.setGeometry(QtCore.QRect(530, line_spacing, 71, 20))
        self.la_length.setAlignment(QtCore.Qt.AlignCenter)
        self.la_length.setText(self.length)

        self.la_difficulty = QtWidgets.QLabel(self.widget)
        self.la_difficulty.setGeometry(QtCore.QRect(590, line_spacing, 81, 20))
        self.la_difficulty.setAlignment(QtCore.Qt.AlignCenter)
        self.la_difficulty.setText(self.difficulty)

        self.la_date = QtWidgets.QLabel(self.widget)
        self.la_date.setGeometry(QtCore.QRect(663, line_spacing, 81, 20))
        self.la_date.setAlignment(QtCore.Qt.AlignCenter)
        self.la_date.setText(self.date)

        self.BT_show = QtWidgets.QPushButton(self.widget)
        self.BT_show.setGeometry(QtCore.QRect(840, line_spacing, 90, 23))
        self.BT_show.setText("Show overlay")
        self.BT_show.clicked.connect(lambda: show_overlay(self.file))

        self.BT_file = QtWidgets.QPushButton(self.widget)
        self.BT_file.setGeometry(QtCore.QRect(760, line_spacing, 75, 23))          
        self.BT_file.setText("Find file")
        self.BT_file.clicked.connect(lambda: find_file(self.file))

        # Red losses
        if self.result == 'Defeat':
            for item in {self.la_mapname, self.la_result, self.la_p1, self.la_p2, self.la_enemy, self.la_length, self.la_difficulty, self.la_date}:
                item.setStyleSheet('color: red')


class PlayerEntry:
    """ 
    Class for UI elements in players tab. 

    """

    def __init__(self, name, wins, losses, note, parent):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.winrate = 100*wins/(wins+losses)
        self.note = note

        height = 30
        line_spacing = 7

        self.widget = QtWidgets.QWidget(parent)
        self.widget.setGeometry(QtCore.QRect(0, 0, 931, height))
        self.widget.setMinimumHeight(height)
        self.widget.setMaximumHeight(height)

        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(10, 0, 921, 2))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.la_name = QtWidgets.QLabel(self.widget)
        self.la_name.setGeometry(QtCore.QRect(40, line_spacing, 150, 21))
        self.la_name.setText(self.name)

        self.la_wins = QtWidgets.QLabel(self.widget)
        self.la_wins.setGeometry(QtCore.QRect(270, line_spacing, 31, 21))
        self.la_wins.setAlignment(QtCore.Qt.AlignCenter)
        self.la_wins.setText(str(self.wins))

        self.la_losses = QtWidgets.QLabel(self.widget)
        self.la_losses.setGeometry(QtCore.QRect(330, line_spacing, 41, 21))
        self.la_losses.setAlignment(QtCore.Qt.AlignCenter)
        self.la_losses.setText(str(self.losses))

        self.la_winrate = QtWidgets.QLabel(self.widget)
        self.la_winrate.setGeometry(QtCore.QRect(400, line_spacing, 51, 21))
        self.la_winrate.setAlignment(QtCore.Qt.AlignCenter)
        self.la_winrate.setText(f'{self.winrate:.0f}%')

        self.ed_note = QtWidgets.QLineEdit(self.widget)
        self.ed_note.setGeometry(QtCore.QRect(550, line_spacing, 330, 21))
        self.ed_note.setAlignment(QtCore.Qt.AlignCenter)
        self.ed_note.setStyleSheet('color: #444')
        if not self.note in {None,''}:
            self.ed_note.setText(self.note)

        # This is necessary only sometimes (when the user is looking at the tab while its updating )
        for item in {self.widget, self.line, self.la_name, self.la_wins, self.la_losses, self.la_winrate, self.ed_note}:
            item.show()

    def get_note(self):
        return self.ed_note.text()


    def show(self):
        self.widget.show()


    def hide(self):
        self.widget.hide()


    def update_winrates(self, data):
        """ Updates winrate for the player. """
        self.wins = data[0]
        self.losses = data[1]
        self.winrate = 100*self.wins/(self.wins+self.losses)

        self.la_wins.setText(str(self.wins))
        self.la_losses.setText(str(self.losses))       
        self.la_winrate.setText(f'{self.winrate:.0f}%')


class WorkerSignals(QtCore.QObject):
    '''
    Defines the signals available from a running worker thread.
    Supported signals are:

    finished
        No data
    
    error
        `tuple` (exctype, value, traceback.format_exc() )
    
    result
        `object` data returned from processing, anything

    '''
    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(tuple)
    result = QtCore.pyqtSignal(object)


class Worker(QtCore.QRunnable):
    """
    Worker thread
    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.
    The function callback to run on this worker thread. Supplied args and kwargs will be passed through to the runner.
    `fn` function
    `arg` Arguments to pass to the callback function
    `kwargs` Keywords to pass to the callback function
    """

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()


    @QtCore.pyqtSlot()
    def run(self):
        """ Runs the function and emits signals (error, result, finished) """
        try:
            try:
                result = self.fn(*self.args, **self.kwargs)
            except:
                logger.error(traceback.format_exc())
                exctype, value = sys.exc_info()[:2]
                self.signals.error.emit((exctype, value, traceback.format_exc()))
            else:
                self.signals.result.emit(result)
            finally:
                self.signals.finished.emit()
        except RuntimeError:
            logger.debug('Error with pyqt thread. The app likely closed.')
        except:
            logger.error(traceback.format_exc())


class CustomKeySequenceEdit(QtWidgets.QKeySequenceEdit):
    def __init__(self, parent=None):
        super(CustomKeySequenceEdit, self).__init__(parent)
 
    def keyPressEvent(self, QKeyEvent):
        super(CustomKeySequenceEdit, self).keyPressEvent(QKeyEvent)
        value = self.keySequence()
        self.setKeySequence(QtGui.QKeySequence(value))


class CustomQTabWidget(QtWidgets.QTabWidget):
    def __init__(self, parent=None, settings=dict()):
        super(CustomQTabWidget, self).__init__(parent)

        # Tray
        self.tray_icon = QtWidgets.QSystemTrayIcon()
        self.tray_icon.setIcon(QtGui.QIcon(innerPath('src/OverlayIcon.ico')))
        self.tray_icon.activated.connect(self.tray_activated)
        self.tray_menu = QtWidgets.QMenu()
        self.tray_menu.setStyleSheet("background-color: #272E3B; color: #fff")

        self.show_action = QtWidgets.QAction("   Show ")
        self.show_action.triggered.connect(self.show)
        self.show_action.setIcon(QtGui.QIcon(innerPath('src/OverlayIcon.ico')))
        self.tray_menu.addAction(self.show_action)

        self.tray_menu.addSeparator()

        self.quit_action = QtWidgets.QAction("   Quit ")
        self.quit_action.setIcon(self.style().standardIcon(getattr(QtWidgets.QStyle, 'SP_DialogCancelButton')))
        self.quit_action.triggered.connect(QtWidgets.qApp.quit)
        self.tray_menu.addAction(self.quit_action)
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.show()

        self.settings = settings


    # @QtCore.pyqtSlot(bool)    
    # def closeEvent(self, event):
    #     """ Overriding close event and minimizing instead """
    #     event.ignore()
    #     self.hide()
    #     self.show_minimize_message()


    def format_close_message(self):
        """ Shows few hotkeys in the notification area"""
        text = ''
        setting_dict = {"hotkey_show/hide":"Show/Hide","hotkey_newer":"Newer replay","hotkey_older":"Older replay"}
        for key in setting_dict:
            if key in self.settings and self.settings[key] != '':
                text += f"\n{self.settings[key]} → {setting_dict[key]}"
        return text


    def show_minimize_message(self, message=''):
        self.tray_icon.showMessage(
                "StarCraft Co-op Overlay",
                f"App was minimized into the tray{self.format_close_message()}",
                QtGui.QIcon(innerPath('src/OverlayIcon.ico')),
                2000
            )


    def tray_activated(self, reason):
        """ Hides/shows main window when the tray icon is double clicked """
        if reason == 2:
            if self.isVisible():
                self.hide()
            else:
                #Change flags briefly to bring to front
                self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                self.show()
                self.setWindowFlags(QtCore.Qt.Window)
                self.show()


class CustomWebView(QtWebEngineWidgets.QWebEngineView):
    """ Expanding this class to add javascript after page is loaded. This is could be used to distinquish main overlay from other overlays (e.g. in OBS)"""
    def __init__(self,  parent=None):
        super().__init__(parent)
        self.loadFinished.connect(self.on_load_finished)


    @QtCore.pyqtSlot(bool)
    def on_load_finished(self,ok):
        if ok:
            self.page().runJavaScript(f"showmutators = false;")
