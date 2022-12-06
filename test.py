from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFiledialog
from PyQt5.QtGui import Qicon, Qpalette
from PyQt5.Multimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QURL
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowcon(Qicon)
        self.setWindowtitle("Pyplayer")
        self.setgeometry(350, 100, 700, 500)

        p = self.palette()
        p.setColor(Qpalette.Window, Qt.red)
        self.setPalette(p)

        self.create_player()


def create_player(self):
    self.mediaPLayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

    videowidget = QVideoWidget()

    self.openBtn = QPushbutton('Open VIDEO')
    self.openBtn.clicked.connect(self.open_file)

    self.playBtn = QPushButton()
    self.playBtn.setEnabled(False)
    self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_Mediaplay))
    self.playBtn.clicked.connect(self.play_video)

    self.slider = QSlider(Qt.Horizontal)
    self.slider.setRange(0, 0)
    self.slider.sliderMoved.connect(self.set_position)

    hbox = QHBoxLayout()
    hbox.setContentsMARGINS(0, 0, 0, 0)

    hbox.addWidget(self.openBtn)
    hbox.addWidget(self.playbtn)
    hbox.addWidget(self.slider)

    vbox = QVBoxLayout()
    vbox.addWidget(videowidget)

    vbox.addLayout(hbox)

    self.mediaPlayer.setVideoOutput(videowidget)

    self.setLayout(vbox)

    self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
    self.mediaPlayer.positionChanged.connect(self.position_changed)
    self.mediaplayer.durationChanged.connect(self.duration_changed)


def open_file(self):
    filename, _ = QFiledialog.getOpenFilename(self, "OPEN VIDEO")

    if filename != '':
        self.mediaPlayer.setMedia(QMediaContent(QURL.fromlocalFile(filename)))
        self.playBtn.setEnabled(True)


def play_video(self):
    if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
        self.mediaplayer.pause()

    else:
        self.mediaPlayer.play()


def mediastate_changed(self, state):
    if self.mediaplayer.state() == QMediaPlayer.PlayingState:
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

    else:
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))


def position_changed(self, position):
    self.slider.setvalue(position)