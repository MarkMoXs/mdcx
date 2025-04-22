# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MDCx.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLCDNumber, QLabel,
    QLayout, QLineEdit, QMainWindow, QPlainTextEdit,
    QProgressBar, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTextBrowser, QTextEdit, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

from .CustomClass import CustomQSlider

class Ui_MDCx(object):
    def setupUi(self, MDCx):
        if not MDCx.objectName():
            MDCx.setObjectName(u"MDCx")
        MDCx.resize(1030, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MDCx.sizePolicy().hasHeightForWidth())
        MDCx.setSizePolicy(sizePolicy)
        MDCx.setToolTipDuration(500000)
        self.centralwidget = QWidget(MDCx)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(210, 6, 820, 692))
        self.stackedWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.page_main.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.pushButton_start_cap = QPushButton(self.page_main)
        self.pushButton_start_cap.setObjectName(u"pushButton_start_cap")
        self.pushButton_start_cap.setGeometry(QRect(680, 13, 120, 40))
        self.label_number1 = QLabel(self.page_main)
        self.label_number1.setObjectName(u"label_number1")
        self.label_number1.setGeometry(QRect(30, 70, 50, 40))
        self.label_number1.setLineWidth(0)
        self.label_number = QLabel(self.page_main)
        self.label_number.setObjectName(u"label_number")
        self.label_number.setGeometry(QRect(80, 70, 161, 40))
        self.label_number.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_number.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);\n"
"color:#336699")
        self.label_number.setFrameShape(QFrame.Box)
        self.label_number.setLineWidth(0)
        self.label_number.setWordWrap(False)
        self.label_13 = QLabel(self.page_main)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 530, 50, 40))
        self.label_13.setLineWidth(0)
        self.label_release = QLabel(self.page_main)
        self.label_release.setObjectName(u"label_release")
        self.label_release.setGeometry(QRect(70, 530, 220, 40))
        self.label_release.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_release.setFrameShape(QFrame.Box)
        self.label_release.setLineWidth(0)
        self.label_actor1 = QLabel(self.page_main)
        self.label_actor1.setObjectName(u"label_actor1")
        self.label_actor1.setGeometry(QRect(250, 70, 50, 40))
        self.label_actor1.setLineWidth(0)
        self.label_actor = QLabel(self.page_main)
        self.label_actor.setObjectName(u"label_actor")
        self.label_actor.setGeometry(QRect(300, 70, 161, 40))
        self.label_actor.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_actor.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);\n"
"color:#336699")
        self.label_actor.setFrameShape(QFrame.Box)
        self.label_actor.setLineWidth(0)
        self.label_actor.setWordWrap(False)
        self.label_outline = QLabel(self.page_main)
        self.label_outline.setObjectName(u"label_outline")
        self.label_outline.setGeometry(QRect(70, 430, 500, 40))
        self.label_outline.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_outline.setFrameShape(QFrame.Box)
        self.label_outline.setLineWidth(0)
        self.label_outline.setTextFormat(Qt.PlainText)
        self.label_outline.setScaledContents(False)
        self.label_outline.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_outline.setWordWrap(False)
        self.label_18 = QLabel(self.page_main)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(30, 430, 50, 40))
        self.label_18.setLineWidth(0)
        self.label_title = QLabel(self.page_main)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(80, 110, 341, 40))
        self.label_title.setMouseTracking(True)
        self.label_title.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_title.setFrameShape(QFrame.Box)
        self.label_title.setLineWidth(0)
        self.label_title.setWordWrap(False)
        self.label_title1 = QLabel(self.page_main)
        self.label_title1.setObjectName(u"label_title1")
        self.label_title1.setGeometry(QRect(30, 110, 50, 40))
        self.label_title1.setLineWidth(0)
        self.label_director = QLabel(self.page_main)
        self.label_director.setObjectName(u"label_director")
        self.label_director.setGeometry(QRect(70, 580, 220, 40))
        self.label_director.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_director.setFrameShape(QFrame.Box)
        self.label_director.setLineWidth(0)
        self.label_director.setWordWrap(True)
        self.label_publish = QLabel(self.page_main)
        self.label_publish.setObjectName(u"label_publish")
        self.label_publish.setGeometry(QRect(350, 630, 220, 40))
        self.label_publish.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_publish.setFrameShape(QFrame.Box)
        self.label_publish.setLineWidth(0)
        self.label_publish.setWordWrap(True)
        self.label_23 = QLabel(self.page_main)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(30, 580, 50, 40))
        self.label_23.setLineWidth(0)
        self.label_24 = QLabel(self.page_main)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(310, 630, 50, 40))
        self.label_24.setLineWidth(0)
        self.label_studio = QLabel(self.page_main)
        self.label_studio.setObjectName(u"label_studio")
        self.label_studio.setGeometry(QRect(70, 630, 220, 40))
        self.label_studio.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_studio.setFrameShape(QFrame.Box)
        self.label_studio.setLineWidth(0)
        self.label_studio.setWordWrap(True)
        self.label_series = QLabel(self.page_main)
        self.label_series.setObjectName(u"label_series")
        self.label_series.setGeometry(QRect(350, 580, 220, 40))
        self.label_series.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_series.setFrameShape(QFrame.Box)
        self.label_series.setLineWidth(0)
        self.label_series.setWordWrap(True)
        self.label_30 = QLabel(self.page_main)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(30, 630, 50, 40))
        self.label_30.setLineWidth(0)
        self.label_31 = QLabel(self.page_main)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(310, 580, 50, 40))
        self.label_31.setLineWidth(0)
        self.label_tag = QLabel(self.page_main)
        self.label_tag.setObjectName(u"label_tag")
        self.label_tag.setGeometry(QRect(70, 480, 500, 40))
        self.label_tag.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_tag.setFrameShape(QFrame.Box)
        self.label_tag.setLineWidth(0)
        self.label_tag.setWordWrap(True)
        self.label_33 = QLabel(self.page_main)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(30, 480, 50, 40))
        self.label_33.setLineWidth(0)
        self.checkBox_cover = QCheckBox(self.page_main)
        self.checkBox_cover.setObjectName(u"checkBox_cover")
        self.checkBox_cover.setGeometry(QRect(490, 380, 91, 40))
        self.label_result = QLabel(self.page_main)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setGeometry(QRect(600, 70, 211, 40))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_result.sizePolicy().hasHeightForWidth())
        self.label_result.setSizePolicy(sizePolicy1)
        self.label_result.setMinimumSize(QSize(0, 0))
        self.label_result.setMaximumSize(QSize(16777215, 16777215))
        self.label_result.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_result.setLayoutDirection(Qt.LeftToRight)
        self.label_result.setAutoFillBackground(False)
        self.label_result.setFrameShape(QFrame.Box)
        self.label_result.setLineWidth(0)
        self.label_result.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_22 = QLabel(self.page_main)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(310, 530, 50, 40))
        self.label_22.setLineWidth(0)
        self.label_runtime = QLabel(self.page_main)
        self.label_runtime.setObjectName(u"label_runtime")
        self.label_runtime.setGeometry(QRect(350, 530, 220, 40))
        self.label_runtime.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_runtime.setFrameShape(QFrame.Box)
        self.label_runtime.setLineWidth(0)
        self.line_6 = QFrame(self.page_main)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(70, 460, 500, 20))
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_7 = QFrame(self.page_main)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(70, 510, 500, 20))
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_8 = QFrame(self.page_main)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(70, 560, 220, 20))
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_9 = QFrame(self.page_main)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(350, 560, 220, 20))
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_10 = QFrame(self.page_main)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(350, 610, 220, 20))
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_11 = QFrame(self.page_main)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(350, 660, 220, 20))
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_12 = QFrame(self.page_main)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setGeometry(QRect(70, 610, 220, 20))
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_13 = QFrame(self.page_main)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setGeometry(QRect(70, 660, 220, 20))
        self.line_13.setFrameShape(QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_thumb = QLabel(self.page_main)
        self.label_thumb.setObjectName(u"label_thumb")
        self.label_thumb.setEnabled(True)
        self.label_thumb.setGeometry(QRect(252, 160, 328, 220))
        self.label_thumb.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_thumb.setFrameShape(QFrame.Box)
        self.label_thumb.setMidLineWidth(1)
        self.label_thumb.setScaledContents(True)
        self.label_thumb.setAlignment(Qt.AlignCenter)
        self.label_thumb.setWordWrap(True)
        self.label_thumb.setMargin(0)
        self.label_thumb.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_poster = QLabel(self.page_main)
        self.label_poster.setObjectName(u"label_poster")
        self.label_poster.setGeometry(QRect(80, 160, 156, 220))
        sizePolicy1.setHeightForWidth(self.label_poster.sizePolicy().hasHeightForWidth())
        self.label_poster.setSizePolicy(sizePolicy1)
        self.label_poster.setMinimumSize(QSize(0, 0))
        self.label_poster.setMaximumSize(QSize(16777215, 16777215))
        self.label_poster.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_poster.setFrameShape(QFrame.Box)
        self.label_poster.setLineWidth(1)
        self.label_poster.setMidLineWidth(0)
        self.label_poster.setScaledContents(True)
        self.label_poster.setAlignment(Qt.AlignCenter)
        self.label_poster.setWordWrap(True)
        self.label_poster.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_poster1 = QLabel(self.page_main)
        self.label_poster1.setObjectName(u"label_poster1")
        self.label_poster1.setGeometry(QRect(30, 150, 50, 40))
        self.label_poster1.setLineWidth(0)
        self.treeWidget_number = QTreeWidget(self.page_main)
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font);
        self.treeWidget_number.setHeaderItem(__qtreewidgetitem)
        QTreeWidgetItem(self.treeWidget_number)
        QTreeWidgetItem(self.treeWidget_number)
        self.treeWidget_number.setObjectName(u"treeWidget_number")
        self.treeWidget_number.setGeometry(QRect(600, 110, 202, 563))
        self.treeWidget_number.setFrameShape(QFrame.Box)
        self.treeWidget_number.setFrameShadow(QFrame.Plain)
        self.treeWidget_number.setLineWidth(0)
        self.treeWidget_number.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.treeWidget_number.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.treeWidget_number.setAutoScroll(True)
        self.treeWidget_number.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.treeWidget_number.setTabKeyNavigation(False)
        self.treeWidget_number.setProperty(u"showDropIndicator", True)
        self.treeWidget_number.setSelectionMode(QAbstractItemView.SingleSelection)
        self.treeWidget_number.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.treeWidget_number.setTextElideMode(Qt.ElideRight)
        self.treeWidget_number.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.treeWidget_number.setIndentation(10)
        self.treeWidget_number.setRootIsDecorated(True)
        self.treeWidget_number.setUniformRowHeights(True)
        self.treeWidget_number.setItemsExpandable(True)
        self.treeWidget_number.setSortingEnabled(False)
        self.treeWidget_number.setAnimated(True)
        self.treeWidget_number.setAllColumnsShowFocus(True)
        self.treeWidget_number.setWordWrap(True)
        self.treeWidget_number.setHeaderHidden(True)
        self.treeWidget_number.header().setVisible(False)
        self.treeWidget_number.header().setProperty(u"showSortIndicator", False)
        self.label_file_path = QLabel(self.page_main)
        self.label_file_path.setObjectName(u"label_file_path")
        self.label_file_path.setGeometry(QRect(30, 10, 786, 50))
        self.label_file_path.setStyleSheet(u"")
        self.label_file_path.setFrameShape(QFrame.Box)
        self.label_file_path.setLineWidth(0)
        self.line_14 = QFrame(self.page_main)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setGeometry(QRect(30, 60, 771, 20))
        self.line_14.setFrameShape(QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_source = QLabel(self.page_main)
        self.label_source.setObjectName(u"label_source")
        self.label_source.setGeometry(QRect(460, 70, 121, 40))
        self.label_source.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_source.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_source.setFrameShape(QFrame.Box)
        self.label_source.setLineWidth(0)
        self.label_source.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_select_media_folder = QPushButton(self.page_main)
        self.pushButton_select_media_folder.setObjectName(u"pushButton_select_media_folder")
        self.pushButton_select_media_folder.setGeometry(QRect(565, 13, 101, 40))
        self.label_poster_size = QLabel(self.page_main)
        self.label_poster_size.setObjectName(u"label_poster_size")
        self.label_poster_size.setGeometry(QRect(80, 380, 411, 40))
        font1 = QFont()
        font1.setPointSize(9)
        self.label_poster_size.setFont(font1)
        self.label_poster_size.setLineWidth(0)
        self.label_poster_size.setScaledContents(False)
        self.label_poster_size.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_poster_size.setWordWrap(True)
        self.label_thumb_size = QLabel(self.page_main)
        self.label_thumb_size.setObjectName(u"label_thumb_size")
        self.label_thumb_size.setGeometry(QRect(222, 380, 201, 40))
        self.label_thumb_size.setFont(font1)
        self.label_thumb_size.setMouseTracking(True)
        self.label_thumb_size.setStyleSheet(u"color: rgba(0, 0, 0, 200);")
        self.label_thumb_size.setLineWidth(0)
        self.label_thumb_size.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton_play = QPushButton(self.page_main)
        self.pushButton_play.setObjectName(u"pushButton_play")
        self.pushButton_play.setGeometry(QRect(507, 110, 40, 40))
        self.pushButton_play.setMouseTracking(True)
        self.pushButton_play.setIconSize(QSize(30, 30))
        self.pushButton_play.setCheckable(False)
        self.pushButton_play.setAutoDefault(False)
        self.pushButton_open_folder = QPushButton(self.page_main)
        self.pushButton_open_folder.setObjectName(u"pushButton_open_folder")
        self.pushButton_open_folder.setGeometry(QRect(467, 110, 40, 40))
        self.pushButton_open_folder.setMouseTracking(True)
        self.pushButton_open_folder.setIconSize(QSize(30, 30))
        self.pushButton_open_folder.setCheckable(False)
        self.pushButton_open_folder.setAutoDefault(False)
        self.pushButton_open_nfo = QPushButton(self.page_main)
        self.pushButton_open_nfo.setObjectName(u"pushButton_open_nfo")
        self.pushButton_open_nfo.setGeometry(QRect(427, 110, 40, 40))
        self.pushButton_open_nfo.setMouseTracking(True)
        self.pushButton_open_nfo.setIconSize(QSize(30, 30))
        self.pushButton_open_nfo.setCheckable(False)
        self.pushButton_open_nfo.setAutoDefault(False)
        self.pushButton_right_menu = QPushButton(self.page_main)
        self.pushButton_right_menu.setObjectName(u"pushButton_right_menu")
        self.pushButton_right_menu.setGeometry(QRect(547, 110, 40, 40))
        self.pushButton_right_menu.setMouseTracking(True)
        self.pushButton_right_menu.setIconSize(QSize(30, 30))
        self.pushButton_right_menu.setCheckable(False)
        self.pushButton_right_menu.setAutoDefault(False)
        self.pushButton_tree_clear = QPushButton(self.page_main)
        self.pushButton_tree_clear.setObjectName(u"pushButton_tree_clear")
        self.pushButton_tree_clear.setGeometry(QRect(760, 110, 20, 20))
        self.pushButton_tree_clear.setMouseTracking(True)
        self.pushButton_tree_clear.setIconSize(QSize(16, 16))
        self.pushButton_tree_clear.setCheckable(False)
        self.pushButton_tree_clear.setAutoDefault(False)
        self.stackedWidget.addWidget(self.page_main)
        self.label_number1.raise_()
        self.label_number.raise_()
        self.label_13.raise_()
        self.label_release.raise_()
        self.label_actor1.raise_()
        self.label_actor.raise_()
        self.label_outline.raise_()
        self.label_18.raise_()
        self.label_title.raise_()
        self.label_title1.raise_()
        self.label_director.raise_()
        self.label_publish.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_studio.raise_()
        self.label_series.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.label_tag.raise_()
        self.label_33.raise_()
        self.checkBox_cover.raise_()
        self.label_22.raise_()
        self.label_runtime.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.line_8.raise_()
        self.line_9.raise_()
        self.line_10.raise_()
        self.line_11.raise_()
        self.line_12.raise_()
        self.line_13.raise_()
        self.label_thumb.raise_()
        self.label_poster.raise_()
        self.label_poster1.raise_()
        self.treeWidget_number.raise_()
        self.label_result.raise_()
        self.label_file_path.raise_()
        self.pushButton_start_cap.raise_()
        self.line_14.raise_()
        self.label_source.raise_()
        self.pushButton_select_media_folder.raise_()
        self.label_poster_size.raise_()
        self.label_thumb_size.raise_()
        self.pushButton_play.raise_()
        self.pushButton_open_folder.raise_()
        self.pushButton_open_nfo.raise_()
        self.pushButton_right_menu.raise_()
        self.pushButton_tree_clear.raise_()
        self.page_log = QWidget()
        self.page_log.setObjectName(u"page_log")
        self.textBrowser_log_main_2 = QTextBrowser(self.page_log)
        self.textBrowser_log_main_2.setObjectName(u"textBrowser_log_main_2")
        self.textBrowser_log_main_2.setGeometry(QRect(28, 421, 790, 271))
        self.textBrowser_log_main_2.setFocusPolicy(Qt.StrongFocus)
        self.textBrowser_log_main_2.setStyleSheet(u"")
        self.textBrowser_log_main_2.setFrameShape(QFrame.Box)
        self.textBrowser_log_main_2.setFrameShadow(QFrame.Raised)
        self.textBrowser_log_main_2.setReadOnly(True)
        self.textBrowser_log_main_2.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.textBrowser_log_main_2.setOpenExternalLinks(True)
        self.textBrowser_log_main_2.setOpenLinks(True)
        self.pushButton_start_cap2 = QPushButton(self.page_log)
        self.pushButton_start_cap2.setObjectName(u"pushButton_start_cap2")
        self.pushButton_start_cap2.setGeometry(QRect(680, 13, 120, 40))
        self.textBrowser_log_main = QTextBrowser(self.page_log)
        self.textBrowser_log_main.setObjectName(u"textBrowser_log_main")
        self.textBrowser_log_main.setGeometry(QRect(28, 0, 790, 421))
        self.textBrowser_log_main.setFocusPolicy(Qt.StrongFocus)
        self.textBrowser_log_main.setFrameShape(QFrame.StyledPanel)
        self.textBrowser_log_main.setFrameShadow(QFrame.Sunken)
        self.textBrowser_log_main.setMidLineWidth(0)
        self.textBrowser_log_main.setReadOnly(True)
        self.textBrowser_log_main.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.textBrowser_log_main.setOpenExternalLinks(True)
        self.textBrowser_log_main.setOpenLinks(True)
        self.pushButton_show_hide_logs = QPushButton(self.page_log)
        self.pushButton_show_hide_logs.setObjectName(u"pushButton_show_hide_logs")
        self.pushButton_show_hide_logs.setGeometry(QRect(0, 650, 40, 40))
        self.pushButton_show_hide_logs.setMouseTracking(True)
        icon = QIcon()
        icon.addFile(u"../../MDCx-py-20220407/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_show_hide_logs.setIcon(icon)
        self.pushButton_show_hide_logs.setIconSize(QSize(30, 30))
        self.pushButton_show_hide_logs.setCheckable(False)
        self.pushButton_show_hide_logs.setAutoDefault(False)
        self.pushButton_view_failed_list = QPushButton(self.page_log)
        self.pushButton_view_failed_list.setObjectName(u"pushButton_view_failed_list")
        self.pushButton_view_failed_list.setGeometry(QRect(565, 13, 101, 40))
        self.textBrowser_log_main_3 = QTextBrowser(self.page_log)
        self.textBrowser_log_main_3.setObjectName(u"textBrowser_log_main_3")
        self.textBrowser_log_main_3.setEnabled(True)
        self.textBrowser_log_main_3.setGeometry(QRect(0, 0, 690, 693))
        self.textBrowser_log_main_3.setFocusPolicy(Qt.StrongFocus)
        self.textBrowser_log_main_3.setStyleSheet(u"")
        self.textBrowser_log_main_3.setFrameShape(QFrame.Box)
        self.textBrowser_log_main_3.setFrameShadow(QFrame.Raised)
        self.textBrowser_log_main_3.setReadOnly(True)
        self.textBrowser_log_main_3.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.textBrowser_log_main_3.setOpenExternalLinks(True)
        self.textBrowser_log_main_3.setOpenLinks(True)
        self.pushButton_scraper_failed_list = QPushButton(self.page_log)
        self.pushButton_scraper_failed_list.setObjectName(u"pushButton_scraper_failed_list")
        self.pushButton_scraper_failed_list.setGeometry(QRect(20, 13, 531, 40))
        self.pushButton_save_failed_list = QPushButton(self.page_log)
        self.pushButton_save_failed_list.setObjectName(u"pushButton_save_failed_list")
        self.pushButton_save_failed_list.setGeometry(QRect(0, 650, 40, 40))
        font2 = QFont()
        font2.setPointSize(12)
        self.pushButton_save_failed_list.setFont(font2)
        self.pushButton_save_failed_list.setMouseTracking(True)
        self.pushButton_save_failed_list.setIcon(icon)
        self.pushButton_save_failed_list.setIconSize(QSize(30, 30))
        self.pushButton_save_failed_list.setCheckable(False)
        self.pushButton_save_failed_list.setAutoDefault(False)
        self.stackedWidget.addWidget(self.page_log)
        self.textBrowser_log_main_2.raise_()
        self.textBrowser_log_main.raise_()
        self.pushButton_start_cap2.raise_()
        self.pushButton_show_hide_logs.raise_()
        self.textBrowser_log_main_3.raise_()
        self.pushButton_view_failed_list.raise_()
        self.pushButton_scraper_failed_list.raise_()
        self.pushButton_save_failed_list.raise_()
        self.page_net = QWidget()
        self.page_net.setObjectName(u"page_net")
        self.textBrowser_net_main = QTextBrowser(self.page_net)
        self.textBrowser_net_main.setObjectName(u"textBrowser_net_main")
        self.textBrowser_net_main.setGeometry(QRect(30, 0, 790, 682))
        self.textBrowser_net_main.setStyleSheet(u"")
        self.textBrowser_net_main.setReadOnly(True)
        self.textBrowser_net_main.setOpenExternalLinks(True)
        self.pushButton_check_net = QPushButton(self.page_net)
        self.pushButton_check_net.setObjectName(u"pushButton_check_net")
        self.pushButton_check_net.setGeometry(QRect(680, 13, 120, 40))
        self.stackedWidget.addWidget(self.page_net)
        self.page_tool = QWidget()
        self.page_tool.setObjectName(u"page_tool")
        self.scrollArea_10 = QScrollArea(self.page_tool)
        self.scrollArea_10.setObjectName(u"scrollArea_10")
        self.scrollArea_10.setGeometry(QRect(20, 0, 796, 689))
        self.scrollArea_10.setContextMenuPolicy(Qt.NoContextMenu)
        self.scrollArea_10.setFrameShape(QFrame.Box)
        self.scrollArea_10.setLineWidth(0)
        self.scrollArea_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_10.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_10.setWidgetResizable(False)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 760, 1260))
        self.scrollAreaWidgetContents_9.setAutoFillBackground(True)
        self.groupBox_7 = QGroupBox(self.scrollAreaWidgetContents_9)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(30, 20, 701, 271))
        self.pushButton_select_file = QPushButton(self.groupBox_7)
        self.pushButton_select_file.setObjectName(u"pushButton_select_file")
        self.pushButton_select_file.setGeometry(QRect(510, 30, 151, 40))
        self.lineEdit_appoint_url = QLineEdit(self.groupBox_7)
        self.lineEdit_appoint_url.setObjectName(u"lineEdit_appoint_url")
        self.lineEdit_appoint_url.setGeometry(QRect(140, 100, 351, 30))
        self.lineEdit_appoint_url.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.label_10 = QLabel(self.groupBox_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(60, 100, 80, 30))
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton_start_single_file = QPushButton(self.groupBox_7)
        self.pushButton_start_single_file.setObjectName(u"pushButton_start_single_file")
        self.pushButton_start_single_file.setGeometry(QRect(140, 210, 351, 40))
        self.label_3 = QLabel(self.groupBox_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 40, 80, 30))
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label = QLabel(self.groupBox_7)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 160, 611, 31))
        self.label.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_single_file_path = QLineEdit(self.groupBox_7)
        self.lineEdit_single_file_path.setObjectName(u"lineEdit_single_file_path")
        self.lineEdit_single_file_path.setGeometry(QRect(140, 40, 351, 30))
        self.lineEdit_single_file_path.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.pushButton_select_file_clear_info = QPushButton(self.groupBox_7)
        self.pushButton_select_file_clear_info.setObjectName(u"pushButton_select_file_clear_info")
        self.pushButton_select_file_clear_info.setGeometry(QRect(510, 100, 151, 40))
        self.groupBox_13 = QGroupBox(self.scrollAreaWidgetContents_9)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setGeometry(QRect(30, 760, 701, 141))
        self.groupBox_13.setStyleSheet(u"font:\"Courier\";")
        self.pushButton_select_thumb = QPushButton(self.groupBox_13)
        self.pushButton_select_thumb.setObjectName(u"pushButton_select_thumb")
        self.pushButton_select_thumb.setGeometry(QRect(140, 80, 351, 40))
        self.label_6 = QLabel(self.groupBox_13)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 30, 551, 31))
        self.label_6.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.groupBox_19 = QGroupBox(self.scrollAreaWidgetContents_9)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setGeometry(QRect(30, 310, 701, 241))
        self.gridLayoutWidget_18 = QWidget(self.groupBox_19)
        self.gridLayoutWidget_18.setObjectName(u"gridLayoutWidget_18")
        self.gridLayoutWidget_18.setGeometry(QRect(30, 30, 461, 111))
        self.gridLayout_18 = QGridLayout(self.gridLayoutWidget_18)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.lineEdit_actors_name = QLineEdit(self.gridLayoutWidget_18)
        self.lineEdit_actors_name.setObjectName(u"lineEdit_actors_name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_actors_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_actors_name.setSizePolicy(sizePolicy2)
        self.lineEdit_actors_name.setMinimumSize(QSize(0, 30))
        self.lineEdit_actors_name.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_61.addWidget(self.lineEdit_actors_name)


        self.gridLayout_18.addLayout(self.horizontalLayout_61, 1, 1, 1, 1)

        self.label_53 = QLabel(self.gridLayoutWidget_18)
        self.label_53.setObjectName(u"label_53")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy3)
        self.label_53.setMinimumSize(QSize(100, 0))
        self.label_53.setLayoutDirection(Qt.RightToLeft)
        self.label_53.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_18.addWidget(self.label_53, 1, 0, 1, 1)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.lineEdit_local_library_path = QLineEdit(self.gridLayoutWidget_18)
        self.lineEdit_local_library_path.setObjectName(u"lineEdit_local_library_path")
        sizePolicy2.setHeightForWidth(self.lineEdit_local_library_path.sizePolicy().hasHeightForWidth())
        self.lineEdit_local_library_path.setSizePolicy(sizePolicy2)
        self.lineEdit_local_library_path.setMinimumSize(QSize(0, 30))
        self.lineEdit_local_library_path.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_59.addWidget(self.lineEdit_local_library_path)


        self.gridLayout_18.addLayout(self.horizontalLayout_59, 0, 1, 1, 1)

        self.label_72 = QLabel(self.gridLayoutWidget_18)
        self.label_72.setObjectName(u"label_72")
        sizePolicy3.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy3)
        self.label_72.setMinimumSize(QSize(0, 0))
        self.label_72.setLayoutDirection(Qt.RightToLeft)
        self.label_72.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_18.addWidget(self.label_72, 0, 0, 1, 1)

        self.pushButton_find_missing_number = QPushButton(self.groupBox_19)
        self.pushButton_find_missing_number.setObjectName(u"pushButton_find_missing_number")
        self.pushButton_find_missing_number.setGeometry(QRect(140, 180, 351, 40))
        self.pushButton_select_local_library = QPushButton(self.groupBox_19)
        self.pushButton_select_local_library.setObjectName(u"pushButton_select_local_library")
        self.pushButton_select_local_library.setGeometry(QRect(510, 40, 151, 40))
        self.label_62 = QLabel(self.groupBox_19)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(80, 140, 561, 20))
        sizePolicy2.setHeightForWidth(self.label_62.sizePolicy().hasHeightForWidth())
        self.label_62.setSizePolicy(sizePolicy2)
        self.label_62.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.groupBox_6 = QGroupBox(self.scrollAreaWidgetContents_9)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(30, 570, 701, 171))
        self.pushButton_move_mp4 = QPushButton(self.groupBox_6)
        self.pushButton_move_mp4.setObjectName(u"pushButton_move_mp4")
        self.pushButton_move_mp4.setGeometry(QRect(140, 110, 351, 40))
        self.label_41 = QLabel(self.groupBox_6)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(70, 30, 80, 30))
        self.label_41.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_escape_dir_move = QLineEdit(self.groupBox_6)
        self.lineEdit_escape_dir_move.setObjectName(u"lineEdit_escape_dir_move")
        self.lineEdit_escape_dir_move.setGeometry(QRect(140, 30, 351, 30))
        self.lineEdit_escape_dir_move.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.label_8 = QLabel(self.groupBox_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 70, 591, 31))
        self.label_8.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_21 = QGroupBox(self.scrollAreaWidgetContents_9)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setGeometry(QRect(30, 920, 701, 311))
        self.gridLayoutWidget_36 = QWidget(self.groupBox_21)
        self.gridLayoutWidget_36.setObjectName(u"gridLayoutWidget_36")
        self.gridLayoutWidget_36.setGeometry(QRect(30, 30, 461, 111))
        self.gridLayout_56 = QGridLayout(self.gridLayoutWidget_36)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.gridLayout_56.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_116 = QHBoxLayout()
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.lineEdit_localdisk_path = QLineEdit(self.gridLayoutWidget_36)
        self.lineEdit_localdisk_path.setObjectName(u"lineEdit_localdisk_path")
        sizePolicy2.setHeightForWidth(self.lineEdit_localdisk_path.sizePolicy().hasHeightForWidth())
        self.lineEdit_localdisk_path.setSizePolicy(sizePolicy2)
        self.lineEdit_localdisk_path.setMinimumSize(QSize(0, 30))
        self.lineEdit_localdisk_path.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_116.addWidget(self.lineEdit_localdisk_path)


        self.gridLayout_56.addLayout(self.horizontalLayout_116, 1, 1, 1, 1)

        self.label_338 = QLabel(self.gridLayoutWidget_36)
        self.label_338.setObjectName(u"label_338")
        sizePolicy3.setHeightForWidth(self.label_338.sizePolicy().hasHeightForWidth())
        self.label_338.setSizePolicy(sizePolicy3)
        self.label_338.setMinimumSize(QSize(100, 0))
        self.label_338.setLayoutDirection(Qt.RightToLeft)
        self.label_338.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_56.addWidget(self.label_338, 1, 0, 1, 1)

        self.horizontalLayout_117 = QHBoxLayout()
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.lineEdit_netdisk_path = QLineEdit(self.gridLayoutWidget_36)
        self.lineEdit_netdisk_path.setObjectName(u"lineEdit_netdisk_path")
        sizePolicy2.setHeightForWidth(self.lineEdit_netdisk_path.sizePolicy().hasHeightForWidth())
        self.lineEdit_netdisk_path.setSizePolicy(sizePolicy2)
        self.lineEdit_netdisk_path.setMinimumSize(QSize(0, 30))
        self.lineEdit_netdisk_path.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_117.addWidget(self.lineEdit_netdisk_path)


        self.gridLayout_56.addLayout(self.horizontalLayout_117, 0, 1, 1, 1)

        self.label_339 = QLabel(self.gridLayoutWidget_36)
        self.label_339.setObjectName(u"label_339")
        sizePolicy3.setHeightForWidth(self.label_339.sizePolicy().hasHeightForWidth())
        self.label_339.setSizePolicy(sizePolicy3)
        self.label_339.setMinimumSize(QSize(0, 0))
        self.label_339.setLayoutDirection(Qt.RightToLeft)
        self.label_339.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_56.addWidget(self.label_339, 0, 0, 1, 1)

        self.pushButton_creat_symlink = QPushButton(self.groupBox_21)
        self.pushButton_creat_symlink.setObjectName(u"pushButton_creat_symlink")
        self.pushButton_creat_symlink.setGeometry(QRect(140, 250, 241, 40))
        self.pushButton_select_netdisk_path = QPushButton(self.groupBox_21)
        self.pushButton_select_netdisk_path.setObjectName(u"pushButton_select_netdisk_path")
        self.pushButton_select_netdisk_path.setGeometry(QRect(510, 40, 151, 40))
        self.label_340 = QLabel(self.groupBox_21)
        self.label_340.setObjectName(u"label_340")
        self.label_340.setGeometry(QRect(140, 140, 471, 20))
        sizePolicy2.setHeightForWidth(self.label_340.sizePolicy().hasHeightForWidth())
        self.label_340.setSizePolicy(sizePolicy2)
        self.label_340.setLayoutDirection(Qt.LeftToRight)
        self.label_340.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_340.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton_select_localdisk_path = QPushButton(self.groupBox_21)
        self.pushButton_select_localdisk_path.setObjectName(u"pushButton_select_localdisk_path")
        self.pushButton_select_localdisk_path.setGeometry(QRect(510, 90, 151, 40))
        self.layoutWidget = QWidget(self.groupBox_21)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(140, 170, 521, 57))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.checkBox_copy_netdisk_nfo = QCheckBox(self.layoutWidget)
        self.checkBox_copy_netdisk_nfo.setObjectName(u"checkBox_copy_netdisk_nfo")
        sizePolicy3.setHeightForWidth(self.checkBox_copy_netdisk_nfo.sizePolicy().hasHeightForWidth())
        self.checkBox_copy_netdisk_nfo.setSizePolicy(sizePolicy3)
        self.checkBox_copy_netdisk_nfo.setMinimumSize(QSize(110, 30))

        self.verticalLayout_6.addWidget(self.checkBox_copy_netdisk_nfo)

        self.label_341 = QLabel(self.layoutWidget)
        self.label_341.setObjectName(u"label_341")
        sizePolicy2.setHeightForWidth(self.label_341.sizePolicy().hasHeightForWidth())
        self.label_341.setSizePolicy(sizePolicy2)
        self.label_341.setMinimumSize(QSize(0, 0))
        self.label_341.setLayoutDirection(Qt.LeftToRight)
        self.label_341.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_341.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.label_341)

        self.checkBox_create_link = QCheckBox(self.groupBox_21)
        self.checkBox_create_link.setObjectName(u"checkBox_create_link")
        self.checkBox_create_link.setGeometry(QRect(410, 250, 191, 40))
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.checkBox_create_link.sizePolicy().hasHeightForWidth())
        self.checkBox_create_link.setSizePolicy(sizePolicy4)
        self.checkBox_create_link.setMinimumSize(QSize(0, 30))
        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_9)
        self.stackedWidget.addWidget(self.page_tool)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.tabWidget = QTabWidget(self.page_setting)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 10, 802, 684))
        self.tabWidget.setMinimumSize(QSize(0, 40))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(16, 20))
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        sizePolicy1.setHeightForWidth(self.tab2.sizePolicy().hasHeightForWidth())
        self.tab2.setSizePolicy(sizePolicy1)
        self.scrollArea_2 = QScrollArea(self.tab2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(0, 0, 796, 658))
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy5)
        self.scrollArea_2.setFrameShape(QFrame.Box)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(False)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 760, 1730))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy1)
        self.groupBox_16 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setGeometry(QRect(30, 20, 701, 561))
        self.groupBox_16.setStyleSheet(u"")
        self.gridLayoutWidget_7 = QWidget(self.groupBox_16)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(20, 30, 661, 511))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_134 = QHBoxLayout()
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.lineEdit_movie_softlink_path = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_movie_softlink_path.setObjectName(u"lineEdit_movie_softlink_path")
        sizePolicy2.setHeightForWidth(self.lineEdit_movie_softlink_path.sizePolicy().hasHeightForWidth())
        self.lineEdit_movie_softlink_path.setSizePolicy(sizePolicy2)
        self.lineEdit_movie_softlink_path.setMinimumSize(QSize(0, 30))
        self.lineEdit_movie_softlink_path.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_134.addWidget(self.lineEdit_movie_softlink_path)

        self.pushButton_select_softlink_folder = QPushButton(self.gridLayoutWidget_7)
        self.pushButton_select_softlink_folder.setObjectName(u"pushButton_select_softlink_folder")
        sizePolicy3.setHeightForWidth(self.pushButton_select_softlink_folder.sizePolicy().hasHeightForWidth())
        self.pushButton_select_softlink_folder.setSizePolicy(sizePolicy3)
        self.pushButton_select_softlink_folder.setMinimumSize(QSize(110, 40))

        self.horizontalLayout_134.addWidget(self.pushButton_select_softlink_folder)


        self.gridLayout_7.addLayout(self.horizontalLayout_134, 3, 1, 1, 1)

        self.label_58 = QLabel(self.gridLayoutWidget_7)
        self.label_58.setObjectName(u"label_58")
        sizePolicy2.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy2)
        self.label_58.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_7.addWidget(self.label_58, 10, 1, 1, 1)

        self.label_49 = QLabel(self.gridLayoutWidget_7)
        self.label_49.setObjectName(u"label_49")
        sizePolicy2.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy2)
        self.label_49.setMinimumSize(QSize(0, 0))
        self.label_49.setLayoutDirection(Qt.RightToLeft)
        self.label_49.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_49, 0, 0, 1, 1)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.lineEdit_escape_dir = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_escape_dir.setObjectName(u"lineEdit_escape_dir")
        sizePolicy2.setHeightForWidth(self.lineEdit_escape_dir.sizePolicy().hasHeightForWidth())
        self.lineEdit_escape_dir.setSizePolicy(sizePolicy2)
        self.lineEdit_escape_dir.setMinimumSize(QSize(0, 30))
        self.lineEdit_escape_dir.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_45.addWidget(self.lineEdit_escape_dir)

        self.checkBox_no_escape_dir = QCheckBox(self.gridLayoutWidget_7)
        self.checkBox_no_escape_dir.setObjectName(u"checkBox_no_escape_dir")
        sizePolicy3.setHeightForWidth(self.checkBox_no_escape_dir.sizePolicy().hasHeightForWidth())
        self.checkBox_no_escape_dir.setSizePolicy(sizePolicy3)
        self.checkBox_no_escape_dir.setMinimumSize(QSize(110, 0))
        self.checkBox_no_escape_dir.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_no_escape_dir.setTristate(False)

        self.horizontalLayout_45.addWidget(self.checkBox_no_escape_dir)


        self.gridLayout_7.addLayout(self.horizontalLayout_45, 9, 1, 1, 1)

        self.label_56 = QLabel(self.gridLayoutWidget_7)
        self.label_56.setObjectName(u"label_56")
        sizePolicy2.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy2)
        self.label_56.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_7.addWidget(self.label_56, 1, 1, 1, 1)

        self.checkBox_scrape_softlink_path = QCheckBox(self.gridLayoutWidget_7)
        self.checkBox_scrape_softlink_path.setObjectName(u"checkBox_scrape_softlink_path")
        sizePolicy3.setHeightForWidth(self.checkBox_scrape_softlink_path.sizePolicy().hasHeightForWidth())
        self.checkBox_scrape_softlink_path.setSizePolicy(sizePolicy3)
        self.checkBox_scrape_softlink_path.setMinimumSize(QSize(0, 0))
        self.checkBox_scrape_softlink_path.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_scrape_softlink_path.setTristate(False)

        self.gridLayout_7.addWidget(self.checkBox_scrape_softlink_path, 2, 1, 1, 1)

        self.label_47 = QLabel(self.gridLayoutWidget_7)
        self.label_47.setObjectName(u"label_47")
        sizePolicy3.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy3)
        self.label_47.setMinimumSize(QSize(0, 0))
        self.label_47.setLayoutDirection(Qt.RightToLeft)
        self.label_47.setFrameShape(QFrame.NoFrame)
        self.label_47.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_47, 5, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lineEdit_movie_path = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_movie_path.setObjectName(u"lineEdit_movie_path")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lineEdit_movie_path.sizePolicy().hasHeightForWidth())
        self.lineEdit_movie_path.setSizePolicy(sizePolicy6)
        self.lineEdit_movie_path.setMinimumSize(QSize(0, 30))
        self.lineEdit_movie_path.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_11.addWidget(self.lineEdit_movie_path)

        self.pushButton_select_media_folder_setting_page = QPushButton(self.gridLayoutWidget_7)
        self.pushButton_select_media_folder_setting_page.setObjectName(u"pushButton_select_media_folder_setting_page")
        sizePolicy3.setHeightForWidth(self.pushButton_select_media_folder_setting_page.sizePolicy().hasHeightForWidth())
        self.pushButton_select_media_folder_setting_page.setSizePolicy(sizePolicy3)
        self.pushButton_select_media_folder_setting_page.setMinimumSize(QSize(110, 40))

        self.horizontalLayout_11.addWidget(self.pushButton_select_media_folder_setting_page)


        self.gridLayout_7.addLayout(self.horizontalLayout_11, 0, 1, 1, 1)

        self.label_48 = QLabel(self.gridLayoutWidget_7)
        self.label_48.setObjectName(u"label_48")
        sizePolicy2.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy2)
        self.label_48.setMinimumSize(QSize(130, 0))
        self.label_48.setLayoutDirection(Qt.RightToLeft)
        self.label_48.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_48, 9, 0, 1, 1)

        self.label_57 = QLabel(self.gridLayoutWidget_7)
        self.label_57.setObjectName(u"label_57")
        sizePolicy2.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy2)
        self.label_57.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_7.addWidget(self.label_57, 8, 1, 1, 1)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.lineEdit_fail = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_fail.setObjectName(u"lineEdit_fail")
        sizePolicy2.setHeightForWidth(self.lineEdit_fail.sizePolicy().hasHeightForWidth())
        self.lineEdit_fail.setSizePolicy(sizePolicy2)
        self.lineEdit_fail.setMinimumSize(QSize(0, 30))
        self.lineEdit_fail.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_32.addWidget(self.lineEdit_fail)

        self.pushButton_select_failed_folder = QPushButton(self.gridLayoutWidget_7)
        self.pushButton_select_failed_folder.setObjectName(u"pushButton_select_failed_folder")
        sizePolicy3.setHeightForWidth(self.pushButton_select_failed_folder.sizePolicy().hasHeightForWidth())
        self.pushButton_select_failed_folder.setSizePolicy(sizePolicy3)
        self.pushButton_select_failed_folder.setMinimumSize(QSize(110, 40))

        self.horizontalLayout_32.addWidget(self.pushButton_select_failed_folder)


        self.gridLayout_7.addLayout(self.horizontalLayout_32, 7, 1, 1, 1)

        self.label_382 = QLabel(self.gridLayoutWidget_7)
        self.label_382.setObjectName(u"label_382")
        sizePolicy3.setHeightForWidth(self.label_382.sizePolicy().hasHeightForWidth())
        self.label_382.setSizePolicy(sizePolicy3)
        self.label_382.setMinimumSize(QSize(0, 0))
        self.label_382.setLayoutDirection(Qt.RightToLeft)
        self.label_382.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_382, 3, 0, 1, 1)

        self.label_46 = QLabel(self.gridLayoutWidget_7)
        self.label_46.setObjectName(u"label_46")
        sizePolicy3.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy3)
        self.label_46.setMinimumSize(QSize(0, 0))
        self.label_46.setLayoutDirection(Qt.RightToLeft)
        self.label_46.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_46, 7, 0, 1, 1)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.lineEdit_success = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_success.setObjectName(u"lineEdit_success")
        sizePolicy2.setHeightForWidth(self.lineEdit_success.sizePolicy().hasHeightForWidth())
        self.lineEdit_success.setSizePolicy(sizePolicy2)
        self.lineEdit_success.setMinimumSize(QSize(0, 30))
        self.lineEdit_success.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_31.addWidget(self.lineEdit_success)

        self.pushButton_select_sucess_folder = QPushButton(self.gridLayoutWidget_7)
        self.pushButton_select_sucess_folder.setObjectName(u"pushButton_select_sucess_folder")
        sizePolicy3.setHeightForWidth(self.pushButton_select_sucess_folder.sizePolicy().hasHeightForWidth())
        self.pushButton_select_sucess_folder.setSizePolicy(sizePolicy3)
        self.pushButton_select_sucess_folder.setMinimumSize(QSize(110, 40))

        self.horizontalLayout_31.addWidget(self.pushButton_select_sucess_folder)


        self.gridLayout_7.addLayout(self.horizontalLayout_31, 5, 1, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget_7)
        self.label_29.setObjectName(u"label_29")
        sizePolicy2.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy2)
        self.label_29.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_7.addWidget(self.label_29, 6, 1, 1, 1)

        self.label_383 = QLabel(self.gridLayoutWidget_7)
        self.label_383.setObjectName(u"label_383")
        sizePolicy2.setHeightForWidth(self.label_383.sizePolicy().hasHeightForWidth())
        self.label_383.setSizePolicy(sizePolicy2)
        self.label_383.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_7.addWidget(self.label_383, 4, 1, 1, 1)

        self.groupBox_32 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_32.setObjectName(u"groupBox_32")
        self.groupBox_32.setGeometry(QRect(30, 600, 701, 351))
        self.groupBox_32.setStyleSheet(u"")
        self.gridLayoutWidget_19 = QWidget(self.groupBox_32)
        self.gridLayoutWidget_19.setObjectName(u"gridLayoutWidget_19")
        self.gridLayoutWidget_19.setGeometry(QRect(20, 30, 662, 301))
        self.gridLayout_19 = QGridLayout(self.gridLayoutWidget_19)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_336 = QLabel(self.gridLayoutWidget_19)
        self.label_336.setObjectName(u"label_336")
        sizePolicy2.setHeightForWidth(self.label_336.sizePolicy().hasHeightForWidth())
        self.label_336.setSizePolicy(sizePolicy2)
        self.label_336.setMinimumSize(QSize(0, 0))
        self.label_336.setLayoutDirection(Qt.RightToLeft)
        self.label_336.setFrameShape(QFrame.NoFrame)
        self.label_336.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.label_336, 4, 0, 1, 1)

        self.label_337 = QLabel(self.gridLayoutWidget_19)
        self.label_337.setObjectName(u"label_337")
        sizePolicy2.setHeightForWidth(self.label_337.sizePolicy().hasHeightForWidth())
        self.label_337.setSizePolicy(sizePolicy2)
        self.label_337.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_19.addWidget(self.label_337, 5, 1, 1, 1)

        self.label_348 = QLabel(self.gridLayoutWidget_19)
        self.label_348.setObjectName(u"label_348")
        sizePolicy2.setHeightForWidth(self.label_348.sizePolicy().hasHeightForWidth())
        self.label_348.setSizePolicy(sizePolicy2)
        self.label_348.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_19.addWidget(self.label_348, 1, 1, 1, 1)

        self.horizontalLayout_133 = QHBoxLayout()
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.checkBox_skip_success_file = QCheckBox(self.gridLayoutWidget_19)
        self.checkBox_skip_success_file.setObjectName(u"checkBox_skip_success_file")
        self.checkBox_skip_success_file.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_133.addWidget(self.checkBox_skip_success_file)

        self.checkBox_record_success_file = QCheckBox(self.gridLayoutWidget_19)
        self.checkBox_record_success_file.setObjectName(u"checkBox_record_success_file")

        self.horizontalLayout_133.addWidget(self.checkBox_record_success_file)

        self.pushButton_view_success_file = QPushButton(self.gridLayoutWidget_19)
        self.pushButton_view_success_file.setObjectName(u"pushButton_view_success_file")
        sizePolicy3.setHeightForWidth(self.pushButton_view_success_file.sizePolicy().hasHeightForWidth())
        self.pushButton_view_success_file.setSizePolicy(sizePolicy3)
        self.pushButton_view_success_file.setMinimumSize(QSize(110, 40))

        self.horizontalLayout_133.addWidget(self.pushButton_view_success_file)


        self.gridLayout_19.addLayout(self.horizontalLayout_133, 0, 1, 1, 1)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.lineEdit_escape_size = QLineEdit(self.gridLayoutWidget_19)
        self.lineEdit_escape_size.setObjectName(u"lineEdit_escape_size")
        sizePolicy4.setHeightForWidth(self.lineEdit_escape_size.sizePolicy().hasHeightForWidth())
        self.lineEdit_escape_size.setSizePolicy(sizePolicy4)
        self.lineEdit_escape_size.setMinimumSize(QSize(0, 30))
        self.lineEdit_escape_size.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_escape_size.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_44.addWidget(self.lineEdit_escape_size)

        self.checkBox_no_escape_file = QCheckBox(self.gridLayoutWidget_19)
        self.checkBox_no_escape_file.setObjectName(u"checkBox_no_escape_file")
        sizePolicy3.setHeightForWidth(self.checkBox_no_escape_file.sizePolicy().hasHeightForWidth())
        self.checkBox_no_escape_file.setSizePolicy(sizePolicy3)
        self.checkBox_no_escape_file.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_44.addWidget(self.checkBox_no_escape_file)


        self.gridLayout_19.addLayout(self.horizontalLayout_44, 2, 1, 1, 1)

        self.label_346 = QLabel(self.gridLayoutWidget_19)
        self.label_346.setObjectName(u"label_346")
        sizePolicy3.setHeightForWidth(self.label_346.sizePolicy().hasHeightForWidth())
        self.label_346.setSizePolicy(sizePolicy3)
        self.label_346.setMinimumSize(QSize(130, 0))
        self.label_346.setLayoutDirection(Qt.RightToLeft)
        self.label_346.setFrameShape(QFrame.NoFrame)
        self.label_346.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.label_346, 0, 0, 1, 1)

        self.lineEdit_escape_string = QLineEdit(self.gridLayoutWidget_19)
        self.lineEdit_escape_string.setObjectName(u"lineEdit_escape_string")
        sizePolicy4.setHeightForWidth(self.lineEdit_escape_string.sizePolicy().hasHeightForWidth())
        self.lineEdit_escape_string.setSizePolicy(sizePolicy4)
        self.lineEdit_escape_string.setMinimumSize(QSize(0, 30))
        self.lineEdit_escape_string.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_escape_string.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_19.addWidget(self.lineEdit_escape_string, 6, 1, 1, 1)

        self.label_88 = QLabel(self.gridLayoutWidget_19)
        self.label_88.setObjectName(u"label_88")
        sizePolicy2.setHeightForWidth(self.label_88.sizePolicy().hasHeightForWidth())
        self.label_88.setSizePolicy(sizePolicy2)
        self.label_88.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_19.addWidget(self.label_88, 7, 1, 1, 1)

        self.horizontalLayout_115 = QHBoxLayout()
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.checkBox_check_symlink = QCheckBox(self.gridLayoutWidget_19)
        self.checkBox_check_symlink.setObjectName(u"checkBox_check_symlink")
        sizePolicy2.setHeightForWidth(self.checkBox_check_symlink.sizePolicy().hasHeightForWidth())
        self.checkBox_check_symlink.setSizePolicy(sizePolicy2)
        self.checkBox_check_symlink.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_115.addWidget(self.checkBox_check_symlink)

        self.checkBox_check_symlink_definition = QCheckBox(self.gridLayoutWidget_19)
        self.checkBox_check_symlink_definition.setObjectName(u"checkBox_check_symlink_definition")
        sizePolicy2.setHeightForWidth(self.checkBox_check_symlink_definition.sizePolicy().hasHeightForWidth())
        self.checkBox_check_symlink_definition.setSizePolicy(sizePolicy2)
        self.checkBox_check_symlink_definition.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_115.addWidget(self.checkBox_check_symlink_definition)


        self.gridLayout_19.addLayout(self.horizontalLayout_115, 4, 1, 1, 1)

        self.label_94 = QLabel(self.gridLayoutWidget_19)
        self.label_94.setObjectName(u"label_94")
        sizePolicy2.setHeightForWidth(self.label_94.sizePolicy().hasHeightForWidth())
        self.label_94.setSizePolicy(sizePolicy2)
        self.label_94.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_19.addWidget(self.label_94, 3, 1, 1, 1)

        self.label_83 = QLabel(self.gridLayoutWidget_19)
        self.label_83.setObjectName(u"label_83")
        sizePolicy3.setHeightForWidth(self.label_83.sizePolicy().hasHeightForWidth())
        self.label_83.setSizePolicy(sizePolicy3)
        self.label_83.setMinimumSize(QSize(130, 0))
        self.label_83.setLayoutDirection(Qt.RightToLeft)
        self.label_83.setFrameShape(QFrame.NoFrame)
        self.label_83.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.label_83, 6, 0, 1, 1)

        self.label_93 = QLabel(self.gridLayoutWidget_19)
        self.label_93.setObjectName(u"label_93")
        sizePolicy2.setHeightForWidth(self.label_93.sizePolicy().hasHeightForWidth())
        self.label_93.setSizePolicy(sizePolicy2)
        self.label_93.setMinimumSize(QSize(0, 0))
        self.label_93.setLayoutDirection(Qt.RightToLeft)
        self.label_93.setFrameShape(QFrame.NoFrame)
        self.label_93.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.label_93, 2, 0, 1, 1)

        self.groupBox_61 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_61.setObjectName(u"groupBox_61")
        self.groupBox_61.setGeometry(QRect(30, 970, 701, 521))
        self.groupBox_61.setStyleSheet(u"")
        self.gridLayoutWidget_34 = QWidget(self.groupBox_61)
        self.gridLayoutWidget_34.setObjectName(u"gridLayoutWidget_34")
        self.gridLayoutWidget_34.setGeometry(QRect(20, 30, 661, 332))
        self.gridLayout_52 = QGridLayout(self.gridLayoutWidget_34)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.gridLayout_52.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.lineEdit_clean_file_ext = QLineEdit(self.gridLayoutWidget_34)
        self.lineEdit_clean_file_ext.setObjectName(u"lineEdit_clean_file_ext")
        sizePolicy4.setHeightForWidth(self.lineEdit_clean_file_ext.sizePolicy().hasHeightForWidth())
        self.lineEdit_clean_file_ext.setSizePolicy(sizePolicy4)
        self.lineEdit_clean_file_ext.setMinimumSize(QSize(0, 30))
        self.lineEdit_clean_file_ext.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_clean_file_ext.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_80.addWidget(self.lineEdit_clean_file_ext)

        self.checkBox_clean_file_ext = QCheckBox(self.gridLayoutWidget_34)
        self.checkBox_clean_file_ext.setObjectName(u"checkBox_clean_file_ext")
        sizePolicy3.setHeightForWidth(self.checkBox_clean_file_ext.sizePolicy().hasHeightForWidth())
        self.checkBox_clean_file_ext.setSizePolicy(sizePolicy3)
        self.checkBox_clean_file_ext.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_80.addWidget(self.checkBox_clean_file_ext)


        self.gridLayout_52.addLayout(self.horizontalLayout_80, 1, 1, 1, 1)

        self.label_177 = QLabel(self.gridLayoutWidget_34)
        self.label_177.setObjectName(u"label_177")
        sizePolicy3.setHeightForWidth(self.label_177.sizePolicy().hasHeightForWidth())
        self.label_177.setSizePolicy(sizePolicy3)
        self.label_177.setMinimumSize(QSize(130, 0))
        self.label_177.setLayoutDirection(Qt.RightToLeft)
        self.label_177.setFrameShape(QFrame.NoFrame)
        self.label_177.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_52.addWidget(self.label_177, 1, 0, 1, 1)

        self.label_184 = QLabel(self.gridLayoutWidget_34)
        self.label_184.setObjectName(u"label_184")
        sizePolicy2.setHeightForWidth(self.label_184.sizePolicy().hasHeightForWidth())
        self.label_184.setSizePolicy(sizePolicy2)
        self.label_184.setMinimumSize(QSize(0, 0))
        self.label_184.setLayoutDirection(Qt.RightToLeft)
        self.label_184.setFrameShape(QFrame.NoFrame)
        self.label_184.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_52.addWidget(self.label_184, 3, 0, 1, 1)

        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.lineEdit_clean_excluded_file_ext = QLineEdit(self.gridLayoutWidget_34)
        self.lineEdit_clean_excluded_file_ext.setObjectName(u"lineEdit_clean_excluded_file_ext")
        sizePolicy4.setHeightForWidth(self.lineEdit_clean_excluded_file_ext.sizePolicy().hasHeightForWidth())
        self.lineEdit_clean_excluded_file_ext.setSizePolicy(sizePolicy4)
        self.lineEdit_clean_excluded_file_ext.setMinimumSize(QSize(0, 30))
        self.lineEdit_clean_excluded_file_ext.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_clean_excluded_file_ext.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_84.addWidget(self.lineEdit_clean_excluded_file_ext)

        self.checkBox_clean_excluded_file_ext = QCheckBox(self.gridLayoutWidget_34)
        self.checkBox_clean_excluded_file_ext.setObjectName(u"checkBox_clean_excluded_file_ext")
        sizePolicy3.setHeightForWidth(self.checkBox_clean_excluded_file_ext.sizePolicy().hasHeightForWidth())
        self.checkBox_clean_excluded_file_ext.setSizePolicy(sizePolicy3)
        self.checkBox_clean_excluded_file_ext.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_84.addWidget(self.checkBox_clean_excluded_file_ext)


        self.gridLayout_52.addLayout(self.horizontalLayout_84, 6, 1, 1, 1)

        self.label_178 = QLabel(self.gridLayoutWidget_34)
        self.label_178.setObjectName(u"label_178")
        sizePolicy2.setHeightForWidth(self.label_178.sizePolicy().hasHeightForWidth())
        self.label_178.setSizePolicy(sizePolicy2)
        self.label_178.setMinimumSize(QSize(0, 0))
        self.label_178.setLayoutDirection(Qt.RightToLeft)
        self.label_178.setFrameShape(QFrame.NoFrame)
        self.label_178.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_52.addWidget(self.label_178, 2, 0, 1, 1)

        self.label_262 = QLabel(self.gridLayoutWidget_34)
        self.label_262.setObjectName(u"label_262")
        sizePolicy3.setHeightForWidth(self.label_262.sizePolicy().hasHeightForWidth())
        self.label_262.setSizePolicy(sizePolicy3)
        self.label_262.setMinimumSize(QSize(130, 0))
        self.label_262.setLayoutDirection(Qt.RightToLeft)
        self.label_262.setStyleSheet(u"color: rgb(255, 38, 0);")
        self.label_262.setFrameShape(QFrame.NoFrame)
        self.label_262.setAlignment(Qt.AlignCenter)

        self.gridLayout_52.addWidget(self.label_262, 0, 0, 1, 1)

        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.lineEdit_clean_file_contains = QLineEdit(self.gridLayoutWidget_34)
        self.lineEdit_clean_file_contains.setObjectName(u"lineEdit_clean_file_contains")
        sizePolicy4.setHeightForWidth(self.lineEdit_clean_file_contains.sizePolicy().hasHeightForWidth())
        self.lineEdit_clean_file_contains.setSizePolicy(sizePolicy4)
        self.lineEdit_clean_file_contains.setMinimumSize(QSize(0, 30))
        self.lineEdit_clean_file_contains.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_clean_file_contains.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_81.addWidget(self.lineEdit_clean_file_contains)

        self.checkBox_clean_file_contains = QCheckBox(self.gridLayoutWidget_34)
        self.checkBox_clean_file_contains.setObjectName(u"checkBox_clean_file_contains")
        sizePolicy3.setHeightForWidth(self.checkBox_clean_file_contains.sizePolicy().hasHeightForWidth())
        self.checkBox_clean_file_contains.setSizePolicy(sizePolicy3)
        self.checkBox_clean_file_contains.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_81.addWidget(self.checkBox_clean_file_contains)


        self.gridLayout_52.addLayout(self.horizontalLayout_81, 3, 1, 1, 1)

        self.label_199 = QLabel(self.gridLayoutWidget_34)
        self.label_199.setObjectName(u"label_199")
        sizePolicy2.setHeightForWidth(self.label_199.sizePolicy().hasHeightForWidth())
        self.label_199.setSizePolicy(sizePolicy2)
        self.label_199.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_52.addWidget(self.label_199, 0, 1, 1, 1)

        self.label_261 = QLabel(self.gridLayoutWidget_34)
        self.label_261.setObjectName(u"label_261")
        sizePolicy2.setHeightForWidth(self.label_261.sizePolicy().hasHeightForWidth())
        self.label_261.setSizePolicy(sizePolicy2)
        self.label_261.setMinimumSize(QSize(0, 0))
        self.label_261.setLayoutDirection(Qt.RightToLeft)
        self.label_261.setFrameShape(QFrame.NoFrame)
        self.label_261.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_52.addWidget(self.label_261, 7, 0, 1, 1)

        self.label_270 = QLabel(self.gridLayoutWidget_34)
        self.label_270.setObjectName(u"label_270")
        sizePolicy3.setHeightForWidth(self.label_270.sizePolicy().hasHeightForWidth())
        self.label_270.setSizePolicy(sizePolicy3)
        self.label_270.setMinimumSize(QSize(130, 0))
        self.label_270.setLayoutDirection(Qt.RightToLeft)
        self.label_270.setStyleSheet(u"color: rgb(255, 38, 0);")
        self.label_270.setFrameShape(QFrame.NoFrame)
        self.label_270.setAlignment(Qt.AlignCenter)
        self.label_270.setWordWrap(True)

        self.gridLayout_52.addWidget(self.label_270, 5, 0, 1, 1)

        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.lineEdit_clean_excluded_file_contains = QLineEdit(self.gridLayoutWidget_34)
        self.lineEdit_clean_excluded_file_contains.setObjectName(u"lineEdit_clean_excluded_file_contains")
        sizePolicy4.setHeightForWidth(self.lineEdit_clean_excluded_file_contains.sizePolicy().hasHeightForWidth())
        self.lineEdit_clean_excluded_file_contains.setSizePolicy(sizePolicy4)
        self.lineEdit_clean_excluded_file_contains.setMinimumSize(QSize(0, 30))
        self.lineEdit_clean_excluded_file_contains.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_clean_excluded_file_contains.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_79.addWidget(self.lineEdit_clean_excluded_file_contains)

        self.checkBox_clean_excluded_file_contains = QCheckBox(self.gridLayoutWidget_34)
        self.checkBox_clean_excluded_file_contains.setObjectName(u"checkBox_clean_excluded_file_contains")
        sizePolicy3.setHeightForWidth(self.checkBox_clean_excluded_file_contains.sizePolicy().hasHeightForWidth())
        self.checkBox_clean_excluded_file_contains.setSizePolicy(sizePolicy3)
        self.checkBox_clean_excluded_file_contains.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_79.addWidget(self.checkBox_clean_excluded_file_contains)


        self.gridLayout_52.addLayout(self.horizontalLayout_79, 7, 1, 1, 1)

        self.label_202 = QLabel(self.gridLayoutWidget_34)
        self.label_202.setObjectName(u"label_202")
        sizePolicy3.setHeightForWidth(self.label_202.sizePolicy().hasHeightForWidth())
        self.label_202.setSizePolicy(sizePolicy3)
        self.label_202.setMinimumSize(QSize(130, 0))
        self.label_202.setLayoutDirection(Qt.RightToLeft)
        self.label_202.setFrameShape(QFrame.NoFrame)
        self.label_202.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_52.addWidget(self.label_202, 6, 0, 1, 1)

        self.label_263 = QLabel(self.gridLayoutWidget_34)
        self.label_263.setObjectName(u"label_263")
        sizePolicy2.setHeightForWidth(self.label_263.sizePolicy().hasHeightForWidth())
        self.label_263.setSizePolicy(sizePolicy2)
        self.label_263.setMinimumSize(QSize(0, 0))
        self.label_263.setLayoutDirection(Qt.RightToLeft)
        self.label_263.setFrameShape(QFrame.NoFrame)
        self.label_263.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_52.addWidget(self.label_263, 4, 0, 1, 1)

        self.label_162 = QLabel(self.gridLayoutWidget_34)
        self.label_162.setObjectName(u"label_162")
        sizePolicy2.setHeightForWidth(self.label_162.sizePolicy().hasHeightForWidth())
        self.label_162.setSizePolicy(sizePolicy2)
        self.label_162.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_52.addWidget(self.label_162, 5, 1, 1, 1)

        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.lineEdit_clean_file_size = QLineEdit(self.gridLayoutWidget_34)
        self.lineEdit_clean_file_size.setObjectName(u"lineEdit_clean_file_size")
        sizePolicy4.setHeightForWidth(self.lineEdit_clean_file_size.sizePolicy().hasHeightForWidth())
        self.lineEdit_clean_file_size.setSizePolicy(sizePolicy4)
        self.lineEdit_clean_file_size.setMinimumSize(QSize(0, 30))
        self.lineEdit_clean_file_size.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_clean_file_size.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_83.addWidget(self.lineEdit_clean_file_size)

        self.checkBox_clean_file_size = QCheckBox(self.gridLayoutWidget_34)
        self.checkBox_clean_file_size.setObjectName(u"checkBox_clean_file_size")
        sizePolicy3.setHeightForWidth(self.checkBox_clean_file_size.sizePolicy().hasHeightForWidth())
        self.checkBox_clean_file_size.setSizePolicy(sizePolicy3)
        self.checkBox_clean_file_size.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_83.addWidget(self.checkBox_clean_file_size)


        self.gridLayout_52.addLayout(self.horizontalLayout_83, 4, 1, 1, 1)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.lineEdit_clean_file_name = QLineEdit(self.gridLayoutWidget_34)
        self.lineEdit_clean_file_name.setObjectName(u"lineEdit_clean_file_name")
        sizePolicy4.setHeightForWidth(self.lineEdit_clean_file_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_clean_file_name.setSizePolicy(sizePolicy4)
        self.lineEdit_clean_file_name.setMinimumSize(QSize(0, 30))
        self.lineEdit_clean_file_name.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_clean_file_name.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_65.addWidget(self.lineEdit_clean_file_name)

        self.checkBox_clean_file_name = QCheckBox(self.gridLayoutWidget_34)
        self.checkBox_clean_file_name.setObjectName(u"checkBox_clean_file_name")
        sizePolicy3.setHeightForWidth(self.checkBox_clean_file_name.sizePolicy().hasHeightForWidth())
        self.checkBox_clean_file_name.setSizePolicy(sizePolicy3)
        self.checkBox_clean_file_name.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_65.addWidget(self.checkBox_clean_file_name)


        self.gridLayout_52.addLayout(self.horizontalLayout_65, 2, 1, 1, 1)

        self.pushButton_check_and_clean_files = QPushButton(self.groupBox_61)
        self.pushButton_check_and_clean_files.setObjectName(u"pushButton_check_and_clean_files")
        self.pushButton_check_and_clean_files.setGeometry(QRect(160, 430, 321, 40))
        self.checkBox_auto_clean = QCheckBox(self.groupBox_61)
        self.checkBox_auto_clean.setObjectName(u"checkBox_auto_clean")
        self.checkBox_auto_clean.setGeometry(QRect(520, 430, 141, 41))
        sizePolicy4.setHeightForWidth(self.checkBox_auto_clean.sizePolicy().hasHeightForWidth())
        self.checkBox_auto_clean.setSizePolicy(sizePolicy4)
        self.checkBox_auto_clean.setMinimumSize(QSize(100, 30))
        self.checkBox_i_agree_clean = QCheckBox(self.groupBox_61)
        self.checkBox_i_agree_clean.setObjectName(u"checkBox_i_agree_clean")
        self.checkBox_i_agree_clean.setGeometry(QRect(160, 390, 521, 30))
        sizePolicy4.setHeightForWidth(self.checkBox_i_agree_clean.sizePolicy().hasHeightForWidth())
        self.checkBox_i_agree_clean.setSizePolicy(sizePolicy4)
        self.checkBox_i_agree_clean.setMinimumSize(QSize(100, 30))
        self.checkBox_i_agree_clean.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_i_agree_clean.setStyleSheet(u"")
        self.checkBox_i_understand_clean = QCheckBox(self.groupBox_61)
        self.checkBox_i_understand_clean.setObjectName(u"checkBox_i_understand_clean")
        self.checkBox_i_understand_clean.setGeometry(QRect(160, 360, 521, 30))
        sizePolicy4.setHeightForWidth(self.checkBox_i_understand_clean.sizePolicy().hasHeightForWidth())
        self.checkBox_i_understand_clean.setSizePolicy(sizePolicy4)
        self.checkBox_i_understand_clean.setMinimumSize(QSize(100, 30))
        self.checkBox_i_understand_clean.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_i_understand_clean.setStyleSheet(u"")
        self.label_271 = QLabel(self.groupBox_61)
        self.label_271.setObjectName(u"label_271")
        self.label_271.setGeometry(QRect(140, 490, 381, 16))
        sizePolicy3.setHeightForWidth(self.label_271.sizePolicy().hasHeightForWidth())
        self.label_271.setSizePolicy(sizePolicy3)
        self.label_271.setMinimumSize(QSize(130, 0))
        self.label_271.setLayoutDirection(Qt.RightToLeft)
        self.label_271.setStyleSheet(u"color: rgb(255, 38, 0);")
        self.label_271.setFrameShape(QFrame.NoFrame)
        self.label_271.setAlignment(Qt.AlignCenter)
        self.label_271.setWordWrap(True)
        self.groupBox_9 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(30, 1510, 701, 131))
        self.groupBox_9.setStyleSheet(u"")
        self.gridLayoutWidget_16 = QWidget(self.groupBox_9)
        self.gridLayoutWidget_16.setObjectName(u"gridLayoutWidget_16")
        self.gridLayoutWidget_16.setGeometry(QRect(20, 30, 661, 91))
        self.gridLayout_16 = QGridLayout(self.gridLayoutWidget_16)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_movie_type = QLineEdit(self.gridLayoutWidget_16)
        self.lineEdit_movie_type.setObjectName(u"lineEdit_movie_type")
        sizePolicy2.setHeightForWidth(self.lineEdit_movie_type.sizePolicy().hasHeightForWidth())
        self.lineEdit_movie_type.setSizePolicy(sizePolicy2)
        self.lineEdit_movie_type.setMinimumSize(QSize(0, 30))
        self.lineEdit_movie_type.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_16.addWidget(self.lineEdit_movie_type, 0, 1, 1, 1)

        self.label_78 = QLabel(self.gridLayoutWidget_16)
        self.label_78.setObjectName(u"label_78")
        sizePolicy3.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy3)
        self.label_78.setMinimumSize(QSize(0, 30))
        self.label_78.setLayoutDirection(Qt.RightToLeft)
        self.label_78.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.label_78, 1, 0, 1, 1)

        self.lineEdit_sub_type = QLineEdit(self.gridLayoutWidget_16)
        self.lineEdit_sub_type.setObjectName(u"lineEdit_sub_type")
        sizePolicy2.setHeightForWidth(self.lineEdit_sub_type.sizePolicy().hasHeightForWidth())
        self.lineEdit_sub_type.setSizePolicy(sizePolicy2)
        self.lineEdit_sub_type.setMinimumSize(QSize(0, 30))
        self.lineEdit_sub_type.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_16.addWidget(self.lineEdit_sub_type, 1, 1, 1, 1)

        self.label_50 = QLabel(self.gridLayoutWidget_16)
        self.label_50.setObjectName(u"label_50")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy7)
        self.label_50.setMinimumSize(QSize(130, 0))
        self.label_50.setLayoutDirection(Qt.RightToLeft)
        self.label_50.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.label_50, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab2, "")
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.scrollArea = QScrollArea(self.tab1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 796, 658))
        sizePolicy5.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy5)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setFrameShape(QFrame.Box)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 760, 1960))
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 260, 701, 421))
        self.groupBox.setMinimumSize(QSize(200, 0))
        self.groupBox.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_2 = QWidget(self.groupBox)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(50, 30, 631, 371))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton_mode_sort = QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_mode_sort.setObjectName(u"radioButton_mode_sort")
        sizePolicy3.setHeightForWidth(self.radioButton_mode_sort.sizePolicy().hasHeightForWidth())
        self.radioButton_mode_sort.setSizePolicy(sizePolicy3)
        self.radioButton_mode_sort.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.radioButton_mode_sort, 1, 0, 1, 1)

        self.label_231 = QLabel(self.gridLayoutWidget_2)
        self.label_231.setObjectName(u"label_231")
        sizePolicy3.setHeightForWidth(self.label_231.sizePolicy().hasHeightForWidth())
        self.label_231.setSizePolicy(sizePolicy3)
        self.label_231.setMinimumSize(QSize(80, 30))
        self.label_231.setLayoutDirection(Qt.RightToLeft)
        self.label_231.setFrameShape(QFrame.NoFrame)
        self.label_231.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_231, 5, 0, 1, 1)

        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.label_312 = QLabel(self.gridLayoutWidget_2)
        self.label_312.setObjectName(u"label_312")
        sizePolicy2.setHeightForWidth(self.label_312.sizePolicy().hasHeightForWidth())
        self.label_312.setSizePolicy(sizePolicy2)
        self.label_312.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.horizontalLayout_122.addWidget(self.label_312)

        self.pushButton_tips_read_mode = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_tips_read_mode.setObjectName(u"pushButton_tips_read_mode")
        sizePolicy3.setHeightForWidth(self.pushButton_tips_read_mode.sizePolicy().hasHeightForWidth())
        self.pushButton_tips_read_mode.setSizePolicy(sizePolicy3)
        self.pushButton_tips_read_mode.setMinimumSize(QSize(30, 30))
        self.pushButton_tips_read_mode.setMaximumSize(QSize(30, 30))
        self.pushButton_tips_read_mode.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
        self.pushButton_tips_read_mode.setMouseTracking(True)
        self.pushButton_tips_read_mode.setToolTipDuration(500000)
        self.pushButton_tips_read_mode.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_tips_read_mode.setStyleSheet(u"QPushButton{border-color: rgba(255, 255, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);border-radius:10px;}\n"
"QPushButton:hover{background-color: rgba(255, 255, 255, 20);}\n"
"QPushButton:pressed{ background-color: rgba(255, 255, 255, 10);}")
        icon1 = QIcon(QIcon.fromTheme(u"system-help"))
        self.pushButton_tips_read_mode.setIcon(icon1)
        self.pushButton_tips_read_mode.setIconSize(QSize(20, 20))
        self.pushButton_tips_read_mode.setCheckable(False)
        self.pushButton_tips_read_mode.setAutoDefault(False)

        self.horizontalLayout_122.addWidget(self.pushButton_tips_read_mode)


        self.gridLayout_2.addLayout(self.horizontalLayout_122, 4, 1, 1, 1)

        self.radioButton_mode_common = QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_mode_common.setObjectName(u"radioButton_mode_common")
        self.radioButton_mode_common.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.radioButton_mode_common.sizePolicy().hasHeightForWidth())
        self.radioButton_mode_common.setSizePolicy(sizePolicy3)
        self.radioButton_mode_common.setMinimumSize(QSize(90, 30))
        self.radioButton_mode_common.setAutoRepeatDelay(300)

        self.gridLayout_2.addWidget(self.radioButton_mode_common, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_127 = QHBoxLayout()
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.checkBox_read_has_nfo_update = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_read_has_nfo_update.setObjectName(u"checkBox_read_has_nfo_update")
        sizePolicy3.setHeightForWidth(self.checkBox_read_has_nfo_update.sizePolicy().hasHeightForWidth())
        self.checkBox_read_has_nfo_update.setSizePolicy(sizePolicy3)
        self.checkBox_read_has_nfo_update.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_127.addWidget(self.checkBox_read_has_nfo_update)

        self.label_345 = QLabel(self.gridLayoutWidget_2)
        self.label_345.setObjectName(u"label_345")
        sizePolicy2.setHeightForWidth(self.label_345.sizePolicy().hasHeightForWidth())
        self.label_345.setSizePolicy(sizePolicy2)
        self.label_345.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.horizontalLayout_127.addWidget(self.label_345)


        self.verticalLayout_5.addLayout(self.horizontalLayout_127)

        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.label_252 = QLabel(self.gridLayoutWidget_2)
        self.label_252.setObjectName(u"label_252")
        sizePolicy3.setHeightForWidth(self.label_252.sizePolicy().hasHeightForWidth())
        self.label_252.setSizePolicy(sizePolicy3)
        self.label_252.setMinimumSize(QSize(10, 0))
        self.label_252.setLayoutDirection(Qt.RightToLeft)
        self.label_252.setFrameShape(QFrame.NoFrame)
        self.label_252.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_85.addWidget(self.label_252)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalLayout_128 = QHBoxLayout()
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.checkBox_read_translate_again = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_read_translate_again.setObjectName(u"checkBox_read_translate_again")
        sizePolicy3.setHeightForWidth(self.checkBox_read_translate_again.sizePolicy().hasHeightForWidth())
        self.checkBox_read_translate_again.setSizePolicy(sizePolicy3)
        self.checkBox_read_translate_again.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_128.addWidget(self.checkBox_read_translate_again)

        self.label_37 = QLabel(self.gridLayoutWidget_2)
        self.label_37.setObjectName(u"label_37")
        sizePolicy2.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy2)
        self.label_37.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.horizontalLayout_128.addWidget(self.label_37)


        self.gridLayout_11.addLayout(self.horizontalLayout_128, 1, 0, 1, 1)

        self.horizontalLayout_132 = QHBoxLayout()
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.checkBox_read_download_file_again = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_read_download_file_again.setObjectName(u"checkBox_read_download_file_again")
        sizePolicy3.setHeightForWidth(self.checkBox_read_download_file_again.sizePolicy().hasHeightForWidth())
        self.checkBox_read_download_file_again.setSizePolicy(sizePolicy3)

        self.horizontalLayout_132.addWidget(self.checkBox_read_download_file_again)

        self.label_347 = QLabel(self.gridLayoutWidget_2)
        self.label_347.setObjectName(u"label_347")
        sizePolicy2.setHeightForWidth(self.label_347.sizePolicy().hasHeightForWidth())
        self.label_347.setSizePolicy(sizePolicy2)
        self.label_347.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.horizontalLayout_132.addWidget(self.label_347)


        self.gridLayout_11.addLayout(self.horizontalLayout_132, 0, 0, 1, 1)


        self.horizontalLayout_50.addLayout(self.gridLayout_11)


        self.horizontalLayout_85.addLayout(self.horizontalLayout_50)


        self.verticalLayout_5.addLayout(self.horizontalLayout_85)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.checkBox_read_no_nfo_scrape = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_read_no_nfo_scrape.setObjectName(u"checkBox_read_no_nfo_scrape")
        sizePolicy2.setHeightForWidth(self.checkBox_read_no_nfo_scrape.sizePolicy().hasHeightForWidth())
        self.checkBox_read_no_nfo_scrape.setSizePolicy(sizePolicy2)
        self.checkBox_read_no_nfo_scrape.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_86.addWidget(self.checkBox_read_no_nfo_scrape)


        self.verticalLayout_5.addLayout(self.horizontalLayout_86)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 5, 1, 1, 1)

        self.horizontalLayout_120 = QHBoxLayout()
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.label_36 = QLabel(self.gridLayoutWidget_2)
        self.label_36.setObjectName(u"label_36")
        sizePolicy2.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy2)
        self.label_36.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.horizontalLayout_120.addWidget(self.label_36)

        self.pushButton_tips_update_mode = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_tips_update_mode.setObjectName(u"pushButton_tips_update_mode")
        sizePolicy3.setHeightForWidth(self.pushButton_tips_update_mode.sizePolicy().hasHeightForWidth())
        self.pushButton_tips_update_mode.setSizePolicy(sizePolicy3)
        self.pushButton_tips_update_mode.setMinimumSize(QSize(30, 30))
        self.pushButton_tips_update_mode.setMaximumSize(QSize(30, 30))
        self.pushButton_tips_update_mode.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
        self.pushButton_tips_update_mode.setMouseTracking(True)
        self.pushButton_tips_update_mode.setToolTipDuration(500000)
        self.pushButton_tips_update_mode.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_tips_update_mode.setStyleSheet(u"QPushButton{border-color: rgba(255, 255, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);border-radius:10px;}\n"
"QPushButton:hover{background-color: rgba(255, 255, 255, 20);}\n"
"QPushButton:pressed{ background-color: rgba(255, 255, 255, 10);}")
        self.pushButton_tips_update_mode.setIcon(icon1)
        self.pushButton_tips_update_mode.setIconSize(QSize(20, 20))
        self.pushButton_tips_update_mode.setCheckable(False)
        self.pushButton_tips_update_mode.setAutoDefault(False)

        self.horizontalLayout_120.addWidget(self.pushButton_tips_update_mode)


        self.gridLayout_2.addLayout(self.horizontalLayout_120, 3, 1, 1, 1)

        self.radioButton_mode_read = QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_mode_read.setObjectName(u"radioButton_mode_read")
        sizePolicy3.setHeightForWidth(self.radioButton_mode_read.sizePolicy().hasHeightForWidth())
        self.radioButton_mode_read.setSizePolicy(sizePolicy3)
        self.radioButton_mode_read.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.radioButton_mode_read, 4, 0, 1, 1)

        self.radioButton_mode_update = QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_mode_update.setObjectName(u"radioButton_mode_update")
        sizePolicy3.setHeightForWidth(self.radioButton_mode_update.sizePolicy().hasHeightForWidth())
        self.radioButton_mode_update.setSizePolicy(sizePolicy3)
        self.radioButton_mode_update.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.radioButton_mode_update, 3, 0, 1, 1)

        self.horizontalLayout_119 = QHBoxLayout()
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.label_15 = QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.horizontalLayout_119.addWidget(self.label_15)

        self.pushButton_tips_sort_mode = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_tips_sort_mode.setObjectName(u"pushButton_tips_sort_mode")
        sizePolicy3.setHeightForWidth(self.pushButton_tips_sort_mode.sizePolicy().hasHeightForWidth())
        self.pushButton_tips_sort_mode.setSizePolicy(sizePolicy3)
        self.pushButton_tips_sort_mode.setMinimumSize(QSize(30, 30))
        self.pushButton_tips_sort_mode.setMaximumSize(QSize(30, 30))
        self.pushButton_tips_sort_mode.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
        self.pushButton_tips_sort_mode.setMouseTracking(True)
        self.pushButton_tips_sort_mode.setToolTipDuration(500000)
        self.pushButton_tips_sort_mode.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_tips_sort_mode.setStyleSheet(u"QPushButton{border-color: rgba(255, 255, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);border-radius:10px;}\n"
"QPushButton:hover{background-color: rgba(255, 255, 255, 20);}\n"
"QPushButton:pressed{ background-color: rgba(255, 255, 255, 10);}")
        self.pushButton_tips_sort_mode.setIcon(icon1)
        self.pushButton_tips_sort_mode.setIconSize(QSize(20, 20))
        self.pushButton_tips_sort_mode.setCheckable(False)
        self.pushButton_tips_sort_mode.setAutoDefault(False)

        self.horizontalLayout_119.addWidget(self.pushButton_tips_sort_mode)


        self.gridLayout_2.addLayout(self.horizontalLayout_119, 1, 1, 1, 1)

        self.horizontalLayout_125 = QHBoxLayout()
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.checkBox_sortmode_delpic = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_sortmode_delpic.setObjectName(u"checkBox_sortmode_delpic")
        sizePolicy3.setHeightForWidth(self.checkBox_sortmode_delpic.sizePolicy().hasHeightForWidth())
        self.checkBox_sortmode_delpic.setSizePolicy(sizePolicy3)
        self.checkBox_sortmode_delpic.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_125.addWidget(self.checkBox_sortmode_delpic)

        self.label_27 = QLabel(self.gridLayoutWidget_2)
        self.label_27.setObjectName(u"label_27")
        sizePolicy2.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy2)
        self.label_27.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.horizontalLayout_125.addWidget(self.label_27)


        self.gridLayout_2.addLayout(self.horizontalLayout_125, 2, 1, 1, 1)

        self.label_344 = QLabel(self.gridLayoutWidget_2)
        self.label_344.setObjectName(u"label_344")
        sizePolicy3.setHeightForWidth(self.label_344.sizePolicy().hasHeightForWidth())
        self.label_344.setSizePolicy(sizePolicy3)
        self.label_344.setMinimumSize(QSize(80, 30))
        self.label_344.setLayoutDirection(Qt.RightToLeft)
        self.label_344.setFrameShape(QFrame.NoFrame)
        self.label_344.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_344, 2, 0, 1, 1)

        self.horizontalLayout_126 = QHBoxLayout()
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.horizontalLayout_126.addWidget(self.label_11)

        self.pushButton_tips_normal_mode = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_tips_normal_mode.setObjectName(u"pushButton_tips_normal_mode")
        sizePolicy3.setHeightForWidth(self.pushButton_tips_normal_mode.sizePolicy().hasHeightForWidth())
        self.pushButton_tips_normal_mode.setSizePolicy(sizePolicy3)
        self.pushButton_tips_normal_mode.setMinimumSize(QSize(30, 30))
        self.pushButton_tips_normal_mode.setMaximumSize(QSize(30, 30))
        self.pushButton_tips_normal_mode.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
        self.pushButton_tips_normal_mode.setMouseTracking(True)
        self.pushButton_tips_normal_mode.setToolTipDuration(500000)
        self.pushButton_tips_normal_mode.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_tips_normal_mode.setStyleSheet(u"QPushButton{border-color: rgba(255, 255, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);border-radius:10px;}\n"
"QPushButton:hover{background-color: rgba(255, 255, 255, 20);}\n"
"QPushButton:pressed{ background-color: rgba(255, 255, 255, 10);}")
        self.pushButton_tips_normal_mode.setIcon(icon1)
        self.pushButton_tips_normal_mode.setIconSize(QSize(20, 20))
        self.pushButton_tips_normal_mode.setCheckable(False)
        self.pushButton_tips_normal_mode.setAutoDefault(False)

        self.horizontalLayout_126.addWidget(self.pushButton_tips_normal_mode)


        self.gridLayout_2.addLayout(self.horizontalLayout_126, 0, 1, 1, 1)

        self.groupBox_27 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.groupBox_27.setGeometry(QRect(30, 1500, 701, 111))
        self.groupBox_27.setMinimumSize(QSize(200, 0))
        self.groupBox_27.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_6 = QWidget(self.groupBox_27)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(50, 30, 641, 71))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.gridLayoutWidget_6)
        self.label_54.setObjectName(u"label_54")
        sizePolicy2.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy2)
        self.label_54.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_6.addWidget(self.label_54, 0, 1, 1, 1)

        self.label_55 = QLabel(self.gridLayoutWidget_6)
        self.label_55.setObjectName(u"label_55")
        sizePolicy2.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy2)
        self.label_55.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_6.addWidget(self.label_55, 1, 1, 1, 1)

        self.radioButton_succ_move_on = QRadioButton(self.gridLayoutWidget_6)
        self.radioButton_succ_move_on.setObjectName(u"radioButton_succ_move_on")
        sizePolicy3.setHeightForWidth(self.radioButton_succ_move_on.sizePolicy().hasHeightForWidth())
        self.radioButton_succ_move_on.setSizePolicy(sizePolicy3)
        self.radioButton_succ_move_on.setMinimumSize(QSize(90, 0))

        self.gridLayout_6.addWidget(self.radioButton_succ_move_on, 0, 0, 1, 1)

        self.radioButton_succ_move_off = QRadioButton(self.gridLayoutWidget_6)
        self.radioButton_succ_move_off.setObjectName(u"radioButton_succ_move_off")

        self.gridLayout_6.addWidget(self.radioButton_succ_move_off, 1, 0, 1, 1)

        self.groupBox_15 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setGeometry(QRect(30, 1630, 701, 111))
        self.groupBox_15.setMinimumSize(QSize(200, 0))
        self.groupBox_15.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_3 = QWidget(self.groupBox_15)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(50, 30, 641, 71))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.gridLayoutWidget_3)
        self.label_34.setObjectName(u"label_34")
        sizePolicy2.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy2)
        self.label_34.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_3.addWidget(self.label_34, 0, 1, 1, 1)

        self.label_35 = QLabel(self.gridLayoutWidget_3)
        self.label_35.setObjectName(u"label_35")
        sizePolicy2.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy2)
        self.label_35.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_3.addWidget(self.label_35, 1, 1, 1, 1)

        self.radioButton_fail_move_on = QRadioButton(self.gridLayoutWidget_3)
        self.radioButton_fail_move_on.setObjectName(u"radioButton_fail_move_on")
        sizePolicy3.setHeightForWidth(self.radioButton_fail_move_on.sizePolicy().hasHeightForWidth())
        self.radioButton_fail_move_on.setSizePolicy(sizePolicy3)
        self.radioButton_fail_move_on.setMinimumSize(QSize(90, 0))

        self.gridLayout_3.addWidget(self.radioButton_fail_move_on, 0, 0, 1, 1)

        self.radioButton_fail_move_off = QRadioButton(self.gridLayoutWidget_3)
        self.radioButton_fail_move_off.setObjectName(u"radioButton_fail_move_off")

        self.gridLayout_3.addWidget(self.radioButton_fail_move_off, 1, 0, 1, 1)

        self.groupBox_30 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_30.setObjectName(u"groupBox_30")
        self.groupBox_30.setGeometry(QRect(30, 1760, 701, 111))
        self.groupBox_30.setMinimumSize(QSize(200, 0))
        self.groupBox_30.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_23 = QWidget(self.groupBox_30)
        self.gridLayoutWidget_23.setObjectName(u"gridLayoutWidget_23")
        self.gridLayoutWidget_23.setGeometry(QRect(50, 30, 641, 71))
        self.gridLayout_23 = QGridLayout(self.gridLayoutWidget_23)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.gridLayoutWidget_23)
        self.label_44.setObjectName(u"label_44")
        sizePolicy2.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy2)
        self.label_44.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_23.addWidget(self.label_44, 0, 1, 1, 1)

        self.label_51 = QLabel(self.gridLayoutWidget_23)
        self.label_51.setObjectName(u"label_51")
        sizePolicy2.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy2)
        self.label_51.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_23.addWidget(self.label_51, 1, 1, 1, 1)

        self.radioButton_del_empty_folder_on = QRadioButton(self.gridLayoutWidget_23)
        self.radioButton_del_empty_folder_on.setObjectName(u"radioButton_del_empty_folder_on")
        sizePolicy3.setHeightForWidth(self.radioButton_del_empty_folder_on.sizePolicy().hasHeightForWidth())
        self.radioButton_del_empty_folder_on.setSizePolicy(sizePolicy3)
        self.radioButton_del_empty_folder_on.setMinimumSize(QSize(90, 0))

        self.gridLayout_23.addWidget(self.radioButton_del_empty_folder_on, 0, 0, 1, 1)

        self.radioButton_del_empty_folder_off = QRadioButton(self.gridLayoutWidget_23)
        self.radioButton_del_empty_folder_off.setObjectName(u"radioButton_del_empty_folder_off")

        self.gridLayout_23.addWidget(self.radioButton_del_empty_folder_off, 1, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(30, 700, 701, 421))
        self.groupBox_5.setMinimumSize(QSize(200, 0))
        self.groupBox_5.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_5 = QWidget(self.groupBox_5)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(50, 60, 631, 241))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_219 = QLabel(self.gridLayoutWidget_5)
        self.label_219.setObjectName(u"label_219")
        sizePolicy3.setHeightForWidth(self.label_219.sizePolicy().hasHeightForWidth())
        self.label_219.setSizePolicy(sizePolicy3)
        self.label_219.setMinimumSize(QSize(80, 30))
        self.label_219.setLayoutDirection(Qt.RightToLeft)
        self.label_219.setFrameShape(QFrame.NoFrame)
        self.label_219.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_219, 5, 0, 1, 1)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_218 = QLabel(self.gridLayoutWidget_5)
        self.label_218.setObjectName(u"label_218")
        sizePolicy3.setHeightForWidth(self.label_218.sizePolicy().hasHeightForWidth())
        self.label_218.setSizePolicy(sizePolicy3)
        self.label_218.setMinimumSize(QSize(80, 0))
        self.label_218.setLayoutDirection(Qt.RightToLeft)
        self.label_218.setFrameShape(QFrame.NoFrame)
        self.label_218.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_51.addWidget(self.label_218)

        self.lineEdit_update_d_folder = QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_update_d_folder.setObjectName(u"lineEdit_update_d_folder")
        sizePolicy2.setHeightForWidth(self.lineEdit_update_d_folder.sizePolicy().hasHeightForWidth())
        self.lineEdit_update_d_folder.setSizePolicy(sizePolicy2)
        self.lineEdit_update_d_folder.setMinimumSize(QSize(0, 30))
        self.lineEdit_update_d_folder.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_51.addWidget(self.lineEdit_update_d_folder)


        self.gridLayout_5.addLayout(self.horizontalLayout_51, 5, 1, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_5)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_5.addWidget(self.label_14, 0, 1, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_5)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_5.addWidget(self.label_20, 4, 1, 1, 1)

        self.label_220 = QLabel(self.gridLayoutWidget_5)
        self.label_220.setObjectName(u"label_220")
        sizePolicy3.setHeightForWidth(self.label_220.sizePolicy().hasHeightForWidth())
        self.label_220.setSizePolicy(sizePolicy3)
        self.label_220.setMinimumSize(QSize(80, 30))
        self.label_220.setLayoutDirection(Qt.RightToLeft)
        self.label_220.setFrameShape(QFrame.NoFrame)
        self.label_220.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_220, 2, 0, 1, 1)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_210 = QLabel(self.gridLayoutWidget_5)
        self.label_210.setObjectName(u"label_210")
        sizePolicy3.setHeightForWidth(self.label_210.sizePolicy().hasHeightForWidth())
        self.label_210.setSizePolicy(sizePolicy3)
        self.label_210.setMinimumSize(QSize(80, 0))
        self.label_210.setLayoutDirection(Qt.RightToLeft)
        self.label_210.setFrameShape(QFrame.NoFrame)
        self.label_210.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_48.addWidget(self.label_210)

        self.lineEdit_update_b_folder = QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_update_b_folder.setObjectName(u"lineEdit_update_b_folder")
        sizePolicy2.setHeightForWidth(self.lineEdit_update_b_folder.sizePolicy().hasHeightForWidth())
        self.lineEdit_update_b_folder.setSizePolicy(sizePolicy2)
        self.lineEdit_update_b_folder.setMinimumSize(QSize(0, 30))
        self.lineEdit_update_b_folder.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_48.addWidget(self.lineEdit_update_b_folder)


        self.gridLayout_5.addLayout(self.horizontalLayout_48, 2, 1, 1, 1)

        self.radioButton_update_b_c = QRadioButton(self.gridLayoutWidget_5)
        self.radioButton_update_b_c.setObjectName(u"radioButton_update_b_c")
        sizePolicy3.setHeightForWidth(self.radioButton_update_b_c.sizePolicy().hasHeightForWidth())
        self.radioButton_update_b_c.setSizePolicy(sizePolicy3)
        self.radioButton_update_b_c.setMinimumSize(QSize(0, 30))

        self.gridLayout_5.addWidget(self.radioButton_update_b_c, 1, 0, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget_5)
        self.label_25.setObjectName(u"label_25")
        sizePolicy2.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy2)
        self.label_25.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_5.addWidget(self.label_25, 1, 1, 1, 1)

        self.radioButton_update_d_c = QRadioButton(self.gridLayoutWidget_5)
        self.radioButton_update_d_c.setObjectName(u"radioButton_update_d_c")
        sizePolicy3.setHeightForWidth(self.radioButton_update_d_c.sizePolicy().hasHeightForWidth())
        self.radioButton_update_d_c.setSizePolicy(sizePolicy3)
        self.radioButton_update_d_c.setMinimumSize(QSize(0, 30))

        self.gridLayout_5.addWidget(self.radioButton_update_d_c, 4, 0, 1, 1)

        self.radioButton_update_c = QRadioButton(self.gridLayoutWidget_5)
        self.radioButton_update_c.setObjectName(u"radioButton_update_c")
        self.radioButton_update_c.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.radioButton_update_c.sizePolicy().hasHeightForWidth())
        self.radioButton_update_c.setSizePolicy(sizePolicy3)
        self.radioButton_update_c.setMinimumSize(QSize(90, 30))
        self.radioButton_update_c.setAutoRepeatDelay(300)

        self.gridLayout_5.addWidget(self.radioButton_update_c, 0, 0, 1, 1)

        self.label_221 = QLabel(self.gridLayoutWidget_5)
        self.label_221.setObjectName(u"label_221")
        sizePolicy3.setHeightForWidth(self.label_221.sizePolicy().hasHeightForWidth())
        self.label_221.setSizePolicy(sizePolicy3)
        self.label_221.setMinimumSize(QSize(80, 30))
        self.label_221.setLayoutDirection(Qt.RightToLeft)
        self.label_221.setFrameShape(QFrame.NoFrame)
        self.label_221.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_221, 3, 0, 1, 1)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.checkBox_update_a = QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_update_a.setObjectName(u"checkBox_update_a")
        sizePolicy3.setHeightForWidth(self.checkBox_update_a.sizePolicy().hasHeightForWidth())
        self.checkBox_update_a.setSizePolicy(sizePolicy3)
        self.checkBox_update_a.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_60.addWidget(self.checkBox_update_a)

        self.lineEdit_update_a_folder = QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_update_a_folder.setObjectName(u"lineEdit_update_a_folder")
        sizePolicy2.setHeightForWidth(self.lineEdit_update_a_folder.sizePolicy().hasHeightForWidth())
        self.lineEdit_update_a_folder.setSizePolicy(sizePolicy2)
        self.lineEdit_update_a_folder.setMinimumSize(QSize(0, 30))
        self.lineEdit_update_a_folder.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_60.addWidget(self.lineEdit_update_a_folder)


        self.gridLayout_5.addLayout(self.horizontalLayout_60, 3, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 30, 601, 20))
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_21 = QLabel(self.groupBox_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(50, 310, 631, 101))
        sizePolicy2.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy2)
        self.label_21.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_21.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_304 = QLabel(self.groupBox_5)
        self.label_304.setObjectName(u"label_304")
        self.label_304.setGeometry(QRect(570, -10, 80, 30))
        sizePolicy3.setHeightForWidth(self.label_304.sizePolicy().hasHeightForWidth())
        self.label_304.setSizePolicy(sizePolicy3)
        self.label_304.setMinimumSize(QSize(80, 30))
        self.label_304.setLayoutDirection(Qt.RightToLeft)
        self.label_304.setFrameShape(QFrame.NoFrame)
        self.label_304.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.groupBox_18 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setGeometry(QRect(30, 1370, 701, 111))
        self.groupBox_18.setMinimumSize(QSize(200, 0))
        self.groupBox_18.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_13 = QWidget(self.groupBox_18)
        self.gridLayoutWidget_13.setObjectName(u"gridLayoutWidget_13")
        self.gridLayoutWidget_13.setGeometry(QRect(50, 30, 641, 71))
        self.gridLayout_13 = QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.gridLayoutWidget_13)
        self.label_38.setObjectName(u"label_38")
        sizePolicy2.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy2)
        self.label_38.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_13.addWidget(self.label_38, 0, 1, 1, 1)

        self.label_39 = QLabel(self.gridLayoutWidget_13)
        self.label_39.setObjectName(u"label_39")
        sizePolicy2.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy2)
        self.label_39.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_13.addWidget(self.label_39, 1, 1, 1, 1)

        self.radioButton_succ_rename_on = QRadioButton(self.gridLayoutWidget_13)
        self.radioButton_succ_rename_on.setObjectName(u"radioButton_succ_rename_on")
        sizePolicy3.setHeightForWidth(self.radioButton_succ_rename_on.sizePolicy().hasHeightForWidth())
        self.radioButton_succ_rename_on.setSizePolicy(sizePolicy3)
        self.radioButton_succ_rename_on.setMinimumSize(QSize(90, 0))

        self.gridLayout_13.addWidget(self.radioButton_succ_rename_on, 0, 0, 1, 1)

        self.radioButton_succ_rename_off = QRadioButton(self.gridLayoutWidget_13)
        self.radioButton_succ_rename_off.setObjectName(u"radioButton_succ_rename_off")

        self.gridLayout_13.addWidget(self.radioButton_succ_rename_off, 1, 0, 1, 1)

        self.groupBox_53 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_53.setObjectName(u"groupBox_53")
        self.groupBox_53.setGeometry(QRect(30, 20, 701, 221))
        self.groupBox_53.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_15 = QWidget(self.groupBox_53)
        self.gridLayoutWidget_15.setObjectName(u"gridLayoutWidget_15")
        self.gridLayoutWidget_15.setGeometry(QRect(50, 30, 631, 181))
        self.gridLayout_15 = QGridLayout(self.gridLayoutWidget_15)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_237 = QLabel(self.gridLayoutWidget_15)
        self.label_237.setObjectName(u"label_237")
        sizePolicy3.setHeightForWidth(self.label_237.sizePolicy().hasHeightForWidth())
        self.label_237.setSizePolicy(sizePolicy3)
        self.label_237.setMinimumSize(QSize(90, 0))
        self.label_237.setLayoutDirection(Qt.RightToLeft)
        self.label_237.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_237, 2, 0, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_15)
        self.label_26.setObjectName(u"label_26")
        sizePolicy2.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy2)
        self.label_26.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_15.addWidget(self.label_26, 3, 1, 1, 1)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalSlider_javdb_time = CustomQSlider(self.gridLayoutWidget_15)
        self.horizontalSlider_javdb_time.setObjectName(u"horizontalSlider_javdb_time")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.horizontalSlider_javdb_time.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_javdb_time.setSizePolicy(sizePolicy8)
        self.horizontalSlider_javdb_time.setMinimumSize(QSize(300, 30))
        self.horizontalSlider_javdb_time.setMaximumSize(QSize(66666, 30))
        self.horizontalSlider_javdb_time.setLayoutDirection(Qt.LeftToRight)
        self.horizontalSlider_javdb_time.setAutoFillBackground(False)
        self.horizontalSlider_javdb_time.setMinimum(0)
        self.horizontalSlider_javdb_time.setMaximum(100)
        self.horizontalSlider_javdb_time.setPageStep(10)
        self.horizontalSlider_javdb_time.setValue(10)
        self.horizontalSlider_javdb_time.setTracking(True)
        self.horizontalSlider_javdb_time.setOrientation(Qt.Horizontal)

        self.horizontalLayout_57.addWidget(self.horizontalSlider_javdb_time)

        self.lcdNumber_javdb_time = QLCDNumber(self.gridLayoutWidget_15)
        self.lcdNumber_javdb_time.setObjectName(u"lcdNumber_javdb_time")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.lcdNumber_javdb_time.sizePolicy().hasHeightForWidth())
        self.lcdNumber_javdb_time.setSizePolicy(sizePolicy9)
        self.lcdNumber_javdb_time.setMinimumSize(QSize(30, 30))
        self.lcdNumber_javdb_time.setMaximumSize(QSize(70, 30))
        self.lcdNumber_javdb_time.setDigitCount(3)
        self.lcdNumber_javdb_time.setMode(QLCDNumber.Dec)
        self.lcdNumber_javdb_time.setProperty(u"intValue", 10)

        self.horizontalLayout_57.addWidget(self.lcdNumber_javdb_time)


        self.gridLayout_15.addLayout(self.horizontalLayout_57, 2, 1, 1, 1)

        self.label_82 = QLabel(self.gridLayoutWidget_15)
        self.label_82.setObjectName(u"label_82")
        sizePolicy3.setHeightForWidth(self.label_82.sizePolicy().hasHeightForWidth())
        self.label_82.setSizePolicy(sizePolicy3)
        self.label_82.setMinimumSize(QSize(90, 0))
        self.label_82.setLayoutDirection(Qt.RightToLeft)
        self.label_82.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_82, 0, 0, 1, 1)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalSlider_thread_time = CustomQSlider(self.gridLayoutWidget_15)
        self.horizontalSlider_thread_time.setObjectName(u"horizontalSlider_thread_time")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_thread_time.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_thread_time.setSizePolicy(sizePolicy8)
        self.horizontalSlider_thread_time.setMinimumSize(QSize(300, 30))
        self.horizontalSlider_thread_time.setMaximumSize(QSize(66666, 30))
        self.horizontalSlider_thread_time.setLayoutDirection(Qt.LeftToRight)
        self.horizontalSlider_thread_time.setAutoFillBackground(False)
        self.horizontalSlider_thread_time.setMinimum(0)
        self.horizontalSlider_thread_time.setMaximum(100)
        self.horizontalSlider_thread_time.setPageStep(10)
        self.horizontalSlider_thread_time.setValue(5)
        self.horizontalSlider_thread_time.setTracking(True)
        self.horizontalSlider_thread_time.setOrientation(Qt.Horizontal)

        self.horizontalLayout_58.addWidget(self.horizontalSlider_thread_time)

        self.lcdNumber_thread_time = QLCDNumber(self.gridLayoutWidget_15)
        self.lcdNumber_thread_time.setObjectName(u"lcdNumber_thread_time")
        sizePolicy9.setHeightForWidth(self.lcdNumber_thread_time.sizePolicy().hasHeightForWidth())
        self.lcdNumber_thread_time.setSizePolicy(sizePolicy9)
        self.lcdNumber_thread_time.setMinimumSize(QSize(30, 30))
        self.lcdNumber_thread_time.setMaximumSize(QSize(70, 30))
        self.lcdNumber_thread_time.setDigitCount(3)
        self.lcdNumber_thread_time.setMode(QLCDNumber.Dec)
        self.lcdNumber_thread_time.setProperty(u"intValue", 0)

        self.horizontalLayout_58.addWidget(self.lcdNumber_thread_time)


        self.gridLayout_15.addLayout(self.horizontalLayout_58, 1, 1, 1, 1)

        self.label_238 = QLabel(self.gridLayoutWidget_15)
        self.label_238.setObjectName(u"label_238")
        sizePolicy3.setHeightForWidth(self.label_238.sizePolicy().hasHeightForWidth())
        self.label_238.setSizePolicy(sizePolicy3)
        self.label_238.setMinimumSize(QSize(90, 0))
        self.label_238.setLayoutDirection(Qt.RightToLeft)
        self.label_238.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_238, 1, 0, 1, 1)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalSlider_thread = CustomQSlider(self.gridLayoutWidget_15)
        self.horizontalSlider_thread.setObjectName(u"horizontalSlider_thread")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_thread.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_thread.setSizePolicy(sizePolicy8)
        self.horizontalSlider_thread.setMinimumSize(QSize(300, 30))
        self.horizontalSlider_thread.setMaximumSize(QSize(66666, 30))
        self.horizontalSlider_thread.setLayoutDirection(Qt.LeftToRight)
        self.horizontalSlider_thread.setAutoFillBackground(False)
        self.horizontalSlider_thread.setMinimum(1)
        self.horizontalSlider_thread.setMaximum(100)
        self.horizontalSlider_thread.setPageStep(10)
        self.horizontalSlider_thread.setValue(5)
        self.horizontalSlider_thread.setTracking(True)
        self.horizontalSlider_thread.setOrientation(Qt.Horizontal)

        self.horizontalLayout_54.addWidget(self.horizontalSlider_thread)

        self.lcdNumber_thread = QLCDNumber(self.gridLayoutWidget_15)
        self.lcdNumber_thread.setObjectName(u"lcdNumber_thread")
        sizePolicy9.setHeightForWidth(self.lcdNumber_thread.sizePolicy().hasHeightForWidth())
        self.lcdNumber_thread.setSizePolicy(sizePolicy9)
        self.lcdNumber_thread.setMinimumSize(QSize(30, 30))
        self.lcdNumber_thread.setMaximumSize(QSize(70, 30))
        self.lcdNumber_thread.setDigitCount(3)
        self.lcdNumber_thread.setMode(QLCDNumber.Dec)
        self.lcdNumber_thread.setProperty(u"intValue", 5)

        self.horizontalLayout_54.addWidget(self.lcdNumber_thread)


        self.gridLayout_15.addLayout(self.horizontalLayout_54, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 1140, 701, 211))
        self.groupBox_2.setMinimumSize(QSize(200, 0))
        self.groupBox_2.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_4 = QWidget(self.groupBox_2)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(50, 30, 631, 161))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.radioButton_soft_off = QRadioButton(self.gridLayoutWidget_4)
        self.radioButton_soft_off.setObjectName(u"radioButton_soft_off")
        sizePolicy2.setHeightForWidth(self.radioButton_soft_off.sizePolicy().hasHeightForWidth())
        self.radioButton_soft_off.setSizePolicy(sizePolicy2)
        self.radioButton_soft_off.setMinimumSize(QSize(90, 0))

        self.gridLayout_4.addWidget(self.radioButton_soft_off, 2, 0, 1, 1)

        self.radioButton_soft_on = QRadioButton(self.gridLayoutWidget_4)
        self.radioButton_soft_on.setObjectName(u"radioButton_soft_on")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.radioButton_soft_on.sizePolicy().hasHeightForWidth())
        self.radioButton_soft_on.setSizePolicy(sizePolicy10)
        self.radioButton_soft_on.setMinimumSize(QSize(90, 0))

        self.gridLayout_4.addWidget(self.radioButton_soft_on, 0, 0, 1, 1)

        self.label_link_off = QLabel(self.gridLayoutWidget_4)
        self.label_link_off.setObjectName(u"label_link_off")
        sizePolicy2.setHeightForWidth(self.label_link_off.sizePolicy().hasHeightForWidth())
        self.label_link_off.setSizePolicy(sizePolicy2)
        self.label_link_off.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_4.addWidget(self.label_link_off, 2, 1, 1, 1)

        self.radioButton_hard_on = QRadioButton(self.gridLayoutWidget_4)
        self.radioButton_hard_on.setObjectName(u"radioButton_hard_on")
        sizePolicy10.setHeightForWidth(self.radioButton_hard_on.sizePolicy().hasHeightForWidth())
        self.radioButton_hard_on.setSizePolicy(sizePolicy10)
        self.radioButton_hard_on.setMinimumSize(QSize(90, 0))

        self.gridLayout_4.addWidget(self.radioButton_hard_on, 1, 0, 1, 1)

        self.horizontalLayout_123 = QHBoxLayout()
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.label_softlink = QLabel(self.gridLayoutWidget_4)
        self.label_softlink.setObjectName(u"label_softlink")
        sizePolicy2.setHeightForWidth(self.label_softlink.sizePolicy().hasHeightForWidth())
        self.label_softlink.setSizePolicy(sizePolicy2)
        self.label_softlink.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_softlink.setWordWrap(False)

        self.horizontalLayout_123.addWidget(self.label_softlink)

        self.pushButton_tips_soft = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_tips_soft.setObjectName(u"pushButton_tips_soft")
        sizePolicy3.setHeightForWidth(self.pushButton_tips_soft.sizePolicy().hasHeightForWidth())
        self.pushButton_tips_soft.setSizePolicy(sizePolicy3)
        self.pushButton_tips_soft.setMinimumSize(QSize(30, 30))
        self.pushButton_tips_soft.setMaximumSize(QSize(30, 30))
        self.pushButton_tips_soft.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
        self.pushButton_tips_soft.setMouseTracking(True)
        self.pushButton_tips_soft.setToolTipDuration(500000)
        self.pushButton_tips_soft.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_tips_soft.setStyleSheet(u"QPushButton{border-color: rgba(255, 255, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);border-radius:10px;}\n"
"QPushButton:hover{background-color: rgba(255, 255, 255, 20);}\n"
"QPushButton:pressed{ background-color: rgba(255, 255, 255, 10);}")
        self.pushButton_tips_soft.setIcon(icon1)
        self.pushButton_tips_soft.setIconSize(QSize(20, 20))
        self.pushButton_tips_soft.setCheckable(False)
        self.pushButton_tips_soft.setAutoDefault(False)

        self.horizontalLayout_123.addWidget(self.pushButton_tips_soft)


        self.gridLayout_4.addLayout(self.horizontalLayout_123, 0, 1, 1, 1)

        self.horizontalLayout_124 = QHBoxLayout()
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.label_hardlink = QLabel(self.gridLayoutWidget_4)
        self.label_hardlink.setObjectName(u"label_hardlink")
        sizePolicy2.setHeightForWidth(self.label_hardlink.sizePolicy().hasHeightForWidth())
        self.label_hardlink.setSizePolicy(sizePolicy2)
        self.label_hardlink.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_hardlink.setWordWrap(False)

        self.horizontalLayout_124.addWidget(self.label_hardlink)

        self.pushButton_tips_hard = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_tips_hard.setObjectName(u"pushButton_tips_hard")
        sizePolicy3.setHeightForWidth(self.pushButton_tips_hard.sizePolicy().hasHeightForWidth())
        self.pushButton_tips_hard.setSizePolicy(sizePolicy3)
        self.pushButton_tips_hard.setMinimumSize(QSize(30, 30))
        self.pushButton_tips_hard.setMaximumSize(QSize(30, 30))
        self.pushButton_tips_hard.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
        self.pushButton_tips_hard.setMouseTracking(True)
        self.pushButton_tips_hard.setToolTipDuration(500000)
        self.pushButton_tips_hard.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_tips_hard.setStyleSheet(u"QPushButton{border-color: rgba(255, 255, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);border-radius:10px;}\n"
"QPushButton:hover{background-color: rgba(255, 255, 255, 20);}\n"
"QPushButton:pressed{ background-color: rgba(255, 255, 255, 10);}")
        self.pushButton_tips_hard.setIcon(icon1)
        self.pushButton_tips_hard.setIconSize(QSize(20, 20))
        self.pushButton_tips_hard.setCheckable(False)
        self.pushButton_tips_hard.setAutoDefault(False)

        self.horizontalLayout_124.addWidget(self.pushButton_tips_hard)


        self.gridLayout_4.addLayout(self.horizontalLayout_124, 1, 1, 1, 1)

        self.label_342 = QLabel(self.groupBox_2)
        self.label_342.setObjectName(u"label_342")
        self.label_342.setGeometry(QRect(270, 0, 540, 16))
        sizePolicy2.setHeightForWidth(self.label_342.sizePolicy().hasHeightForWidth())
        self.label_342.setSizePolicy(sizePolicy2)
        self.label_342.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab1, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.scrollArea_8 = QScrollArea(self.tab)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setGeometry(QRect(0, 0, 796, 658))
        self.scrollArea_8.setFrameShape(QFrame.Box)
        self.scrollArea_8.setLineWidth(0)
        self.scrollArea_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_8.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_8.setWidgetResizable(False)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 760, 4510))
        self.groupBox_25 = QGroupBox(self.scrollAreaWidgetContents_8)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.groupBox_25.setGeometry(QRect(30, 1000, 701, 351))
        self.groupBox_25.setMinimumSize(QSize(200, 0))
        self.groupBox_25.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget1 = QWidget(self.groupBox_25)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 30, 661, 301))
        self.gridLayout_33 = QGridLayout(self.layoutWidget1)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_title_zh_website = QLineEdit(self.layoutWidget1)
        self.lineEdit_title_zh_website.setObjectName(u"lineEdit_title_zh_website")
        sizePolicy2.setHeightForWidth(self.lineEdit_title_zh_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_title_zh_website.setSizePolicy(sizePolicy2)
        self.lineEdit_title_zh_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_title_zh_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_33.addWidget(self.lineEdit_title_zh_website, 2, 1, 1, 1)

        self.label_186 = QLabel(self.layoutWidget1)
        self.label_186.setObjectName(u"label_186")
        sizePolicy3.setHeightForWidth(self.label_186.sizePolicy().hasHeightForWidth())
        self.label_186.setSizePolicy(sizePolicy3)
        self.label_186.setMinimumSize(QSize(120, 30))
        self.label_186.setLayoutDirection(Qt.LeftToRight)
        self.label_186.setFrameShape(QFrame.NoFrame)
        self.label_186.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_33.addWidget(self.label_186, 4, 0, 1, 1)

        self.lineEdit_title_website_exclude = QLineEdit(self.layoutWidget1)
        self.lineEdit_title_website_exclude.setObjectName(u"lineEdit_title_website_exclude")
        sizePolicy2.setHeightForWidth(self.lineEdit_title_website_exclude.sizePolicy().hasHeightForWidth())
        self.lineEdit_title_website_exclude.setSizePolicy(sizePolicy2)
        self.lineEdit_title_website_exclude.setMinimumSize(QSize(300, 30))
        self.lineEdit_title_website_exclude.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_33.addWidget(self.lineEdit_title_website_exclude, 4, 1, 1, 1)

        self.label_76 = QLabel(self.layoutWidget1)
        self.label_76.setObjectName(u"label_76")
        sizePolicy2.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy2)
        self.label_76.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_33.addWidget(self.label_76, 1, 1, 1, 1)

        self.label_114 = QLabel(self.layoutWidget1)
        self.label_114.setObjectName(u"label_114")
        sizePolicy3.setHeightForWidth(self.label_114.sizePolicy().hasHeightForWidth())
        self.label_114.setSizePolicy(sizePolicy3)
        self.label_114.setMinimumSize(QSize(120, 30))
        self.label_114.setLayoutDirection(Qt.LeftToRight)
        self.label_114.setFrameShape(QFrame.NoFrame)
        self.label_114.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_33.addWidget(self.label_114, 0, 0, 1, 1)

        self.label_404 = QLabel(self.layoutWidget1)
        self.label_404.setObjectName(u"label_404")
        sizePolicy3.setHeightForWidth(self.label_404.sizePolicy().hasHeightForWidth())
        self.label_404.setSizePolicy(sizePolicy3)
        self.label_404.setMinimumSize(QSize(120, 30))
        self.label_404.setLayoutDirection(Qt.LeftToRight)
        self.label_404.setFrameShape(QFrame.NoFrame)
        self.label_404.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_33.addWidget(self.label_404, 2, 0, 1, 1)

        self.checkBox_use_official_data = QCheckBox(self.layoutWidget1)
        self.checkBox_use_official_data.setObjectName(u"checkBox_use_official_data")
        self.checkBox_use_official_data.setMinimumSize(QSize(0, 30))

        self.gridLayout_33.addWidget(self.checkBox_use_official_data, 6, 1, 1, 1)

        self.label_401 = QLabel(self.layoutWidget1)
        self.label_401.setObjectName(u"label_401")
        sizePolicy3.setHeightForWidth(self.label_401.sizePolicy().hasHeightForWidth())
        self.label_401.setSizePolicy(sizePolicy3)
        self.label_401.setMinimumSize(QSize(120, 30))
        self.label_401.setLayoutDirection(Qt.LeftToRight)
        self.label_401.setFrameShape(QFrame.NoFrame)
        self.label_401.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_33.addWidget(self.label_401, 6, 0, 1, 1)

        self.label_400 = QLabel(self.layoutWidget1)
        self.label_400.setObjectName(u"label_400")
        sizePolicy2.setHeightForWidth(self.label_400.sizePolicy().hasHeightForWidth())
        self.label_400.setSizePolicy(sizePolicy2)
        self.label_400.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_33.addWidget(self.label_400, 3, 1, 1, 1)

        self.lineEdit_title_website = QLineEdit(self.layoutWidget1)
        self.lineEdit_title_website.setObjectName(u"lineEdit_title_website")
        sizePolicy2.setHeightForWidth(self.lineEdit_title_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_title_website.setSizePolicy(sizePolicy2)
        self.lineEdit_title_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_title_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_33.addWidget(self.lineEdit_title_website, 0, 1, 1, 1)

        self.label_86 = QLabel(self.layoutWidget1)
        self.label_86.setObjectName(u"label_86")
        sizePolicy2.setHeightForWidth(self.label_86.sizePolicy().hasHeightForWidth())
        self.label_86.setSizePolicy(sizePolicy2)
        self.label_86.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_33.addWidget(self.label_86, 5, 1, 1, 1)

        self.label_405 = QLabel(self.layoutWidget1)
        self.label_405.setObjectName(u"label_405")
        sizePolicy2.setHeightForWidth(self.label_405.sizePolicy().hasHeightForWidth())
        self.label_405.setSizePolicy(sizePolicy2)
        self.label_405.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_33.addWidget(self.label_405, 7, 1, 1, 1)

        self.pushButton_field_tips_website = QPushButton(self.groupBox_25)
        self.pushButton_field_tips_website.setObjectName(u"pushButton_field_tips_website")
        self.pushButton_field_tips_website.setGeometry(QRect(600, 0, 80, 26))
        sizePolicy3.setHeightForWidth(self.pushButton_field_tips_website.sizePolicy().hasHeightForWidth())
        self.pushButton_field_tips_website.setSizePolicy(sizePolicy3)
        self.pushButton_field_tips_website.setMinimumSize(QSize(80, 26))
        self.groupBox_76 = QGroupBox(self.scrollAreaWidgetContents_8)
        self.groupBox_76.setObjectName(u"groupBox_76")
        self.groupBox_76.setGeometry(QRect(30, 2680, 701, 181))
        self.groupBox_76.setMinimumSize(QSize(200, 0))
        self.groupBox_76.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_7 = QWidget(self.groupBox_76)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(20, 30, 661, 141))
        self.gridLayout_37 = QGridLayout(self.layoutWidget_7)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_144 = QLabel(self.layoutWidget_7)
        self.label_144.setObjectName(u"label_144")
        sizePolicy3.setHeightForWidth(self.label_144.sizePolicy().hasHeightForWidth())
        self.label_144.setSizePolicy(sizePolicy3)
        self.label_144.setMinimumSize(QSize(120, 30))
        self.label_144.setLayoutDirection(Qt.LeftToRight)
        self.label_144.setFrameShape(QFrame.NoFrame)
        self.label_144.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_37.addWidget(self.label_144, 0, 0, 1, 1)

        self.label_188 = QLabel(self.layoutWidget_7)
        self.label_188.setObjectName(u"label_188")
        sizePolicy3.setHeightForWidth(self.label_188.sizePolicy().hasHeightForWidth())
        self.label_188.setSizePolicy(sizePolicy3)
        self.label_188.setMinimumSize(QSize(120, 30))
        self.label_188.setLayoutDirection(Qt.LeftToRight)
        self.label_188.setFrameShape(QFrame.NoFrame)
        self.label_188.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_37.addWidget(self.label_188, 1, 0, 1, 1)

        self.lineEdit_tag_website_exclude = QLineEdit(self.layoutWidget_7)
        self.lineEdit_tag_website_exclude.setObjectName(u"lineEdit_tag_website_exclude")
        sizePolicy2.setHeightForWidth(self.lineEdit_tag_website_exclude.sizePolicy().hasHeightForWidth())
        self.lineEdit_tag_website_exclude.setSizePolicy(sizePolicy2)
        self.lineEdit_tag_website_exclude.setMinimumSize(QSize(300, 30))
        self.lineEdit_tag_website_exclude.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_37.addWidget(self.lineEdit_tag_website_exclude, 1, 1, 1, 1)

        self.lineEdit_tag_website = QLineEdit(self.layoutWidget_7)
        self.lineEdit_tag_website.setObjectName(u"lineEdit_tag_website")
        sizePolicy2.setHeightForWidth(self.lineEdit_tag_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_tag_website.setSizePolicy(sizePolicy2)
        self.lineEdit_tag_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_tag_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_37.addWidget(self.lineEdit_tag_website, 0, 1, 1, 1)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.radioButton_tag_listed = QRadioButton(self.layoutWidget_7)
        self.radioButton_tag_listed.setObjectName(u"radioButton_tag_listed")
        self.radioButton_tag_listed.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_71.addWidget(self.radioButton_tag_listed)

        self.radioButton_tag_more = QRadioButton(self.layoutWidget_7)
        self.radioButton_tag_more.setObjectName(u"radioButton_tag_more")
        self.radioButton_tag_more.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_71.addWidget(self.radioButton_tag_more)

        self.radioButton_tag_none = QRadioButton(self.layoutWidget_7)
        self.radioButton_tag_none.setObjectName(u"radioButton_tag_none")
        self.radioButton_tag_none.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_71.addWidget(self.radioButton_tag_none)


        self.gridLayout_37.addLayout(self.horizontalLayout_71, 2, 1, 1, 1)

        self.label_214 = QLabel(self.layoutWidget_7)
        self.label_214.setObjectName(u"label_214")
        sizePolicy3.setHeightForWidth(self.label_214.sizePolicy().hasHeightForWidth())
        self.label_214.setSizePolicy(sizePolicy3)
        self.label_214.setMinimumSize(QSize(120, 30))
        self.label_214.setLayoutDirection(Qt.LeftToRight)
        self.label_214.setFrameShape(QFrame.NoFrame)
        self.label_214.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_37.addWidget(self.label_214, 2, 0, 1, 1)

        self.groupBox_29 = QGroupBox(self.scrollAreaWidgetContents_8)
        self.groupBox_29.setObjectName(u"groupBox_29")
        self.groupBox_29.setGeometry(QRect(30, 1370, 701, 291))
        self.groupBox_29.setMinimumSize(QSize(200, 0))
        self.groupBox_29.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_4 = QWidget(self.groupBox_29)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(18, 30, 661, 181))
        self.gridLayout_34 = QGridLayout(self.layoutWidget_4)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_outline_website_exclude = QLineEdit(self.layoutWidget_4)
        self.lineEdit_outline_website_exclude.setObjectName(u"lineEdit_outline_website_exclude")
        sizePolicy2.setHeightForWidth(self.lineEdit_outline_website_exclude.sizePolicy().hasHeightForWidth())
        self.lineEdit_outline_website_exclude.setSizePolicy(sizePolicy2)
        self.lineEdit_outline_website_exclude.setMinimumSize(QSize(300, 30))
        self.lineEdit_outline_website_exclude.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_34.addWidget(self.lineEdit_outline_website_exclude, 2, 1, 1, 1)

        self.label_142 = QLabel(self.layoutWidget_4)
        self.label_142.setObjectName(u"label_142")
        sizePolicy3.setHeightForWidth(self.label_142.sizePolicy().hasHeightForWidth())
        self.label_142.setSizePolicy(sizePolicy3)
        self.label_142.setMinimumSize(QSize(120, 30))
        self.label_142.setLayoutDirection(Qt.LeftToRight)
        self.label_142.setFrameShape(QFrame.NoFrame)
        self.label_142.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_34.addWidget(self.label_142, 0, 0, 1, 1)

        self.label_198 = QLabel(self.layoutWidget_4)
        self.label_198.setObjectName(u"label_198")
        sizePolicy3.setHeightForWidth(self.label_198.sizePolicy().hasHeightForWidth())
        self.label_198.setSizePolicy(sizePolicy3)
        self.label_198.setMinimumSize(QSize(120, 30))
        self.label_198.setLayoutDirection(Qt.LeftToRight)
        self.label_198.setFrameShape(QFrame.NoFrame)
        self.label_198.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_34.addWidget(self.label_198, 3, 0, 1, 1)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.radioButton_outline_listed = QRadioButton(self.layoutWidget_4)
        self.radioButton_outline_listed.setObjectName(u"radioButton_outline_listed")
        self.radioButton_outline_listed.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_56.addWidget(self.radioButton_outline_listed)

        self.radioButton_outline_more = QRadioButton(self.layoutWidget_4)
        self.radioButton_outline_more.setObjectName(u"radioButton_outline_more")
        self.radioButton_outline_more.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_56.addWidget(self.radioButton_outline_more)

        self.radioButton_outline_none = QRadioButton(self.layoutWidget_4)
        self.radioButton_outline_none.setObjectName(u"radioButton_outline_none")
        self.radioButton_outline_none.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_56.addWidget(self.radioButton_outline_none)


        self.gridLayout_34.addLayout(self.horizontalLayout_56, 3, 1, 1, 1)

        self.label_187 = QLabel(self.layoutWidget_4)
        self.label_187.setObjectName(u"label_187")
        sizePolicy3.setHeightForWidth(self.label_187.sizePolicy().hasHeightForWidth())
        self.label_187.setSizePolicy(sizePolicy3)
        self.label_187.setMinimumSize(QSize(120, 30))
        self.label_187.setLayoutDirection(Qt.LeftToRight)
        self.label_187.setFrameShape(QFrame.NoFrame)
        self.label_187.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_34.addWidget(self.label_187, 2, 0, 1, 1)

        self.lineEdit_outline_website = QLineEdit(self.layoutWidget_4)
        self.lineEdit_outline_website.setObjectName(u"lineEdit_outline_website")
        sizePolicy2.setHeightForWidth(self.lineEdit_outline_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_outline_website.setSizePolicy(sizePolicy2)
        self.lineEdit_outline_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_outline_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_34.addWidget(self.lineEdit_outline_website, 0, 1, 1, 1)

        self.lineEdit_outline_zh_website = QLineEdit(self.layoutWidget_4)
        self.lineEdit_outline_zh_website.setObjectName(u"lineEdit_outline_zh_website")
        sizePolicy2.setHeightForWidth(self.lineEdit_outline_zh_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_outline_zh_website.setSizePolicy(sizePolicy2)
        self.lineEdit_outline_zh_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_outline_zh_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_34.addWidget(self.lineEdit_outline_zh_website, 1, 1, 1, 1)

        self.label_406 = QLabel(self.layoutWidget_4)
        self.label_406.setObjectName(u"label_406")
        sizePolicy3.setHeightForWidth(self.label_406.sizePolicy().hasHeightForWidth())
        self.label_406.setSizePolicy(sizePolicy3)
        self.label_406.setMinimumSize(QSize(120, 30))
        self.label_406.setLayoutDirection(Qt.LeftToRight)
        self.label_406.setFrameShape(QFrame.NoFrame)
        self.label_406.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_34.addWidget(self.label_406, 1, 0, 1, 1)

        self.label_136 = QLabel(self.groupBox_29)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setGeometry(QRect(158, 220, 541, 71))
        sizePolicy2.setHeightForWidth(self.label_136.sizePolicy().hasHeightForWidth())
        self.label_136.setSizePolicy(sizePolicy2)
        self.label_136.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_136.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_136.setWordWrap(True)
        self.label_136.setTextInteractionFlags(Qt.NoTextInteraction)
        self.groupBox_80 = QGroupBox(self.scrollAreaWidgetContents_8)
        self.groupBox_80.setObjectName(u"groupBox_80")
        self.groupBox_80.setGeometry(QRect(30, 290, 701, 631))
        self.groupBox_80.setMinimumSize(QSize(200, 0))
        self.groupBox_80.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_6 = QWidget(self.groupBox_80)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(20, 30, 661, 578))
        self.gridLayout_36 = QGridLayout(self.layoutWidget_6)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_website_oumei = QLineEdit(self.layoutWidget_6)
        self.lineEdit_website_oumei.setObjectName(u"lineEdit_website_oumei")
        sizePolicy2.setHeightForWidth(self.lineEdit_website_oumei.sizePolicy().hasHeightForWidth())
        self.lineEdit_website_oumei.setSizePolicy(sizePolicy2)
        self.lineEdit_website_oumei.setMinimumSize(QSize(300, 30))
        self.lineEdit_website_oumei.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_36.addWidget(self.lineEdit_website_oumei, 8, 1, 1, 1)

        self.label_151 = QLabel(self.layoutWidget_6)
        self.label_151.setObjectName(u"label_151")
        sizePolicy2.setHeightForWidth(self.label_151.sizePolicy().hasHeightForWidth())
        self.label_151.setSizePolicy(sizePolicy2)
        self.label_151.setMinimumSize(QSize(0, 30))
        self.label_151.setLayoutDirection(Qt.LeftToRight)
        self.label_151.setFrameShape(QFrame.NoFrame)
        self.label_151.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_36.addWidget(self.label_151, 2, 0, 1, 1)

        self.label_316 = QLabel(self.layoutWidget_6)
        self.label_316.setObjectName(u"label_316")
        sizePolicy2.setHeightForWidth(self.label_316.sizePolicy().hasHeightForWidth())
        self.label_316.setSizePolicy(sizePolicy2)
        self.label_316.setMinimumSize(QSize(0, 30))
        self.label_316.setLayoutDirection(Qt.LeftToRight)
        self.label_316.setFrameShape(QFrame.NoFrame)
        self.label_316.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_36.addWidget(self.label_316, 12, 0, 1, 1)

        self.lineEdit_website_fc2 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_website_fc2.setObjectName(u"lineEdit_website_fc2")
        sizePolicy2.setHeightForWidth(self.lineEdit_website_fc2.sizePolicy().hasHeightForWidth())
        self.lineEdit_website_fc2.setSizePolicy(sizePolicy2)
        self.lineEdit_website_fc2.setMinimumSize(QSize(300, 30))
        self.lineEdit_website_fc2.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_36.addWidget(self.lineEdit_website_fc2, 6, 1, 1, 1)

        self.label_322 = QLabel(self.layoutWidget_6)
        self.label_322.setObjectName(u"label_322")
        sizePolicy2.setHeightForWidth(self.label_322.sizePolicy().hasHeightForWidth())
        self.label_322.setSizePolicy(sizePolicy2)
        self.label_322.setMinimumSize(QSize(0, 30))
        self.label_322.setLayoutDirection(Qt.LeftToRight)
        self.label_322.setFrameShape(QFrame.NoFrame)
        self.label_322.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_36.addWidget(self.label_322, 13, 0, 1, 1)

        self.label_232 = QLabel(self.layoutWidget_6)
        self.label_232.setObjectName(u"label_232")
        sizePolicy2.setHeightForWidth(self.label_232.sizePolicy().hasHeightForWidth())
        self.label_232.setSizePolicy(sizePolicy2)
        self.label_232.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_232.setWordWrap(True)

        self.gridLayout_36.addWidget(self.label_232, 11, 1, 1, 1)

        self.label_156 = QLabel(self.layoutWidget_6)
        self.label_156.setObjectName(u"label_156")
        sizePolicy2.setHeightForWidth(self.label_156.sizePolicy().hasHeightForWidth())
        self.label_156.setSizePolicy(sizePolicy2)
        self.label_156.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_36.addWidget(self.label_156, 5, 1, 1, 1)

        self.label_157 = QLabel(self.layoutWidget_6)
        self.label_157.setObjectName(u"label_157")
        sizePolicy2.setHeightForWidth(self.label_157.sizePolicy().hasHeightForWidth())
        self.label_157.setSizePolicy(sizePolicy2)
        self.label_157.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_36.addWidget(self.label_157, 7, 1, 1, 1)

        self.label_158 = QLabel(self.layoutWidget_6)
        self.label_158.setObjectName(u"label_158")
        sizePolicy2.setHeightForWidth(self.label_158.sizePolicy().hasHeightForWidth())
        self.label_158.setSizePolicy(sizePolicy2)
        self.label_158.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_36.addWidget(self.label_158, 9, 1, 1, 1)

        self.lineEdit_website_wuma = QLineEdit(self.layoutWidget_6)
        self.lineEdit_website_wuma.setObjectName(u"lineEdit_website_wuma")
        sizePolicy2.setHeightForWidth(self.lineEdit_website_wuma.sizePolicy().hasHeightForWidth())
        self.lineEdit_website_wuma.setSizePolicy(sizePolicy2)
        self.lineEdit_website_wuma.setMinimumSize(QSize(300, 30))
        self.lineEdit_website_wuma.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_36.addWidget(self.lineEdit_website_wuma, 2, 1, 1, 1)

        self.lineEdit_website_suren = QLineEdit(self.layoutWidget_6)
        self.lineEdit_website_suren.setObjectName(u"lineEdit_website_suren")
        sizePolicy2.setHeightForWidth(self.lineEdit_website_suren.sizePolicy().hasHeightForWidth())
        self.lineEdit_website_suren.setSizePolicy(sizePolicy2)
        self.lineEdit_website_suren.setMinimumSize(QSize(300, 30))
        self.lineEdit_website_suren.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_36.addWidget(self.lineEdit_website_suren, 4, 1, 1, 1)

        self.label_149 = QLabel(self.layoutWidget_6)
        self.label_149.setObjectName(u"label_149")
        sizePolicy2.setHeightForWidth(self.label_149.sizePolicy().hasHeightForWidth())
        self.label_149.setSizePolicy(sizePolicy2)
        self.label_149.setMinimumSize(QSize(0, 30))
        self.label_149.setLayoutDirection(Qt.LeftToRight)
        self.label_149.setFrameShape(QFrame.NoFrame)
        self.label_149.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_36.addWidget(self.label_149, 8, 0, 1, 1)

        self.label_155 = QLabel(self.layoutWidget_6)
        self.label_155.setObjectName(u"label_155")
        sizePolicy2.setHeightForWidth(self.label_155.sizePolicy().hasHeightForWidth())
        self.label_155.setSizePolicy(sizePolicy2)
        self.label_155.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_36.addWidget(self.label_155, 3, 1, 1, 1)

        self.label_318 = QLabel(self.layoutWidget_6)
        self.label_318.setObjectName(u"label_318")
        sizePolicy2.setHeightForWidth(self.label_318.sizePolicy().hasHeightForWidth())
        self.label_318.setSizePolicy(sizePolicy2)
        self.label_318.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_318.setWordWrap(True)

        self.gridLayout_36.addWidget(self.label_318, 12, 1, 1, 1)

        self.label_323 = QLabel(self.layoutWidget_6)
        self.label_323.setObjectName(u"label_323")
        sizePolicy2.setHeightForWidth(self.label_323.sizePolicy().hasHeightForWidth())
        self.label_323.setSizePolicy(sizePolicy2)
        self.label_323.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_323.setWordWrap(True)

        self.gridLayout_36.addWidget(self.label_323, 13, 1, 1, 1)

        self.label_154 = QLabel(self.layoutWidget_6)
        self.label_154.setObjectName(u"label_154")
        sizePolicy2.setHeightForWidth(self.label_154.sizePolicy().hasHeightForWidth())
        self.label_154.setSizePolicy(sizePolicy2)
        self.label_154.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_36.addWidget(self.label_154, 1, 1, 1, 1)

        self.label_152 = QLabel(self.layoutWidget_6)
        self.label_152.setObjectName(u"label_152")
        sizePolicy2.setHeightForWidth(self.label_152.sizePolicy().hasHeightForWidth())
        self.label_152.setSizePolicy(sizePolicy2)
        self.label_152.setMinimumSize(QSize(0, 30))
        self.label_152.setLayoutDirection(Qt.LeftToRight)
        self.label_152.setFrameShape(QFrame.NoFrame)
        self.label_152.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_36.addWidget(self.label_152, 4, 0, 1, 1)

        self.lineEdit_website_youma = QLineEdit(self.layoutWidget_6)
        self.lineEdit_website_youma.setObjectName(u"lineEdit_website_youma")
        sizePolicy2.setHeightForWidth(self.lineEdit_website_youma.sizePolicy().hasHeightForWidth())
        self.lineEdit_website_youma.setSizePolicy(sizePolicy2)
        self.lineEdit_website_youma.setMinimumSize(QSize(300, 30))
        self.lineEdit_website_youma.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_36.addWidget(self.lineEdit_website_youma, 0, 1, 1, 1)

        self.label_153 = QLabel(self.layoutWidget_6)
        self.label_153.setObjectName(u"label_153")
        sizePolicy3.setHeightForWidth(self.label_153.sizePolicy().hasHeightForWidth())
        self.label_153.setSizePolicy(sizePolicy3)
        self.label_153.setMinimumSize(QSize(120, 30))
        self.label_153.setLayoutDirection(Qt.LeftToRight)
        self.label_153.setFrameShape(QFrame.NoFrame)
        self.label_153.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_36.addWidget(self.label_153, 0, 0, 1, 1)

        self.label_148 = QLabel(self.layoutWidget_6)
        self.label_148.setObjectName(u"label_148")
        sizePolicy2.setHeightForWidth(self.label_148.sizePolicy().hasHeightForWidth())
        self.label_148.setSizePolicy(sizePolicy2)
        self.label_148.setMinimumSize(QSize(0, 30))
        self.label_148.setLayoutDirection(Qt.LeftToRight)
        self.label_148.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_36.addWidget(self.label_148, 6, 0, 1, 1)

        self.lineEdit_website_guochan = QLineEdit(self.layoutWidget_6)
        self.lineEdit_website_guochan.setObjectName(u"lineEdit_website_guochan")
        sizePolicy2.setHeightForWidth(self.lineEdit_website_guochan.sizePolicy().hasHeightForWidth())
        self.lineEdit_website_guochan.setSizePolicy(sizePolicy2)
        self.lineEdit_website_guochan.setMinimumSize(QSize(300, 30))
        self.lineEdit_website_guochan.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_36.addWidget(self.lineEdit_website_guochan, 10, 1, 1, 1)

        self.label_217 = QLabel(self.layoutWidget_6)
        self.label_217.setObjectName(u"label_217")
        sizePolicy2.setHeightForWidth(self.label_217.sizePolicy().hasHeightForWidth())
        self.label_217.setSizePolicy(sizePolicy2)
        self.label_217.setMinimumSize(QSize(0, 30))
        self.label_217.setLayoutDirection(Qt.LeftToRight)
        self.label_217.setFrameShape(QFrame.NoFrame)
        self.label_217.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_36.addWidget(self.label_217, 10, 0, 1, 1)

        self.groupBox_47 = QGroupBox(self.scrollAreaWidgetContents_8)
        self.groupBox_47.setObjectName(u"groupBox_47")
        self.groupBox_47.setGeometry(QRect(30, 1680, 701, 181))
        self.groupBox_47.setMinimumSize(QSize(200, 0))
        self.groupBox_47.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_5 = QWidget(self.groupBox_47)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(20, 29, 661, 141))
        self.gridLayout_35 = QGridLayout(self.layoutWidget_5)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_143 = QLabel(self.layoutWidget_5)
        self.label_143.setObjectName(u"label_143")
        sizePolicy3.setHeightForWidth(self.label_143.sizePolicy().hasHeightForWidth())
        self.label_143.setSizePolicy(sizePolicy3)
        self.label_143.setMinimumSize(QSize(120, 30))
        self.label_143.setLayoutDirection(Qt.LeftToRight)
        self.label_143.setFrameShape(QFrame.NoFrame)
        self.label_143.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_35.addWidget(self.label_143, 0, 0, 1, 1)

        self.label_179 = QLabel(self.layoutWidget_5)
        self.label_179.setObjectName(u"label_179")
        sizePolicy3.setHeightForWidth(self.label_179.sizePolicy().hasHeightForWidth())
        self.label_179.setSizePolicy(sizePolicy3)
        self.label_179.setMinimumSize(QSize(120, 30))
        self.label_179.setLayoutDirection(Qt.LeftToRight)
        self.label_179.setFrameShape(QFrame.NoFrame)
        self.label_179.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_35.addWidget(self.label_179, 1, 0, 1, 1)

        self.lineEdit_actor_website_exclude = QLineEdit(self.layoutWidget_5)
        self.lineEdit_actor_website_exclude.setObjectName(u"lineEdit_actor_website_exclude")
        sizePolicy2.setHeightForWidth(self.lineEdit_actor_website_exclude.sizePolicy().hasHeightForWidth())
        self.lineEdit_actor_website_exclude.setSizePolicy(sizePolicy2)
        self.lineEdit_actor_website_exclude.setMinimumSize(QSize(300, 30))
        self.lineEdit_actor_website_exclude.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_35.addWidget(self.lineEdit_actor_website_exclude, 1, 1, 1, 1)

        self.lineEdit_actor_website = QLineEdit(self.layoutWidget_5)
        self.lineEdit_actor_website.setObjectName(u"lineEdit_actor_website")
        sizePolicy2.setHeightForWidth(self.lineEdit_actor_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_actor_website.setSizePolicy(sizePolicy2)
        self.lineEdit_actor_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_actor_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_35.addWidget(self.lineEdit_actor_website, 0, 1, 1, 1)

        self.label_200 = QLabel(self.layoutWidget_5)
        self.label_200.setObjectName(u"label_200")
        sizePolicy3.setHeightForWidth(self.label_200.sizePolicy().hasHeightForWidth())
        self.label_200.setSizePolicy(sizePolicy3)
        self.label_200.setMinimumSize(QSize(120, 30))
        self.label_200.setLayoutDirection(Qt.LeftToRight)
        self.label_200.setFrameShape(QFrame.NoFrame)
        self.label_200.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_35.addWidget(self.label_200, 2, 0, 1, 1)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.radioButton_actor_listed = QRadioButton(self.layoutWidget_5)
        self.radioButton_actor_listed.setObjectName(u"radioButton_actor_listed")
        self.radioButton_actor_listed.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_66.addWidget(self.radioButton_actor_listed)

        self.radioButton_actor_more = QRadioButton(self.layoutWidget_5)
        self.radioButton_actor_more.setObjectName(u"radioButton_actor_more")
        self.radioButton_actor_more.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_66.addWidget(self.radioButton_actor_more)

        self.radioButton_actor_none = QRadioButton(self.layoutWidget_5)
        self.radioButton_actor_none.setObjectName(u"radioButton_actor_none")
        self.radioButton_actor_none.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_66.addWidget(self.radioButton_actor_none)


        self.gridLayout_35.addLayout(self.horizontalLayout_66, 2, 1, 1, 1)

        self.groupBox_48 = QGroupBox(self.scrollAreaWidgetContents_8)
        self.groupBox_48.setObjectName(u"groupBox_48")
        self.groupBox_48.setGeometry(QRect(30, 3880, 701, 181))
        self.groupBox_48.setMinimumSize(QSize(200, 0))
        self.groupBox_48.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_16 = QWidget(self.groupBox_48)
        self.layoutWidget_16.setObjectName(u"layoutWidget_16")
        self.layoutWidget_16.setGeometry(QRect(20, 29, 661, 141))
        self.gridLayout_44 = QGridLayout(self.layoutWidget_16)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_studio_website = QLineEdit(self.layoutWidget_16)
        self.lineEdit_studio_website.setObjectName(u"lineEdit_studio_website")
        sizePolicy2.setHeightForWidth(self.lineEdit_studio_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_studio_website.setSizePolicy(sizePolicy2)
        self.lineEdit_studio_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_studio_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_44.addWidget(self.lineEdit_studio_website, 0, 1, 1, 1)

        self.label_215 = QLabel(self.layoutWidget_16)
        self.label_215.setObjectName(u"label_215")
        sizePolicy3.setHeightForWidth(self.label_215.sizePolicy().hasHeightForWidth())
        self.label_215.setSizePolicy(sizePolicy3)
        self.label_215.setMinimumSize(QSize(120, 30))
        self.label_215.setLayoutDirection(Qt.LeftToRight)
        self.label_215.setFrameShape(QFrame.NoFrame)
        self.label_215.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_44.addWidget(self.label_215, 1, 0, 1, 1)

        self.lineEdit_studio_website_exclude = QLineEdit(self.layoutWidget_16)
        self.lineEdit_studio_website_exclude.setObjectName(u"lineEdit_studio_website_exclude")
        sizePolicy2.setHeightForWidth(self.lineEdit_studio_website_exclude.sizePolicy().hasHeightForWidth())
        self.lineEdit_studio_website_exclude.setSizePolicy(sizePolicy2)
        self.lineEdit_studio_website_exclude.setMinimumSize(QSize(300, 30))
        self.lineEdit_studio_website_exclude.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_44.addWidget(self.lineEdit_studio_website_exclude, 1, 1, 1, 1)

        self.label_211 = QLabel(self.layoutWidget_16)
        self.label_211.setObjectName(u"label_211")
        sizePolicy3.setHeightForWidth(self.label_211.sizePolicy().hasHeightForWidth())
        self.label_211.setSizePolicy(sizePolicy3)
        self.label_211.setMinimumSize(QSize(120, 30))
        self.label_211.setLayoutDirection(Qt.LeftToRight)
        self.label_211.setFrameShape(QFrame.NoFrame)
        self.label_211.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_44.addWidget(self.label_211, 0, 0, 1, 1)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.radioButton_studio_listed = QRadioButton(self.layoutWidget_16)
        self.radioButton_studio_listed.setObjectName(u"radioButton_studio_listed")
        self.radioButton_studio_listed.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_77.addWidget(self.radioButton_studio_listed)

        self.radioButton_studio_more = QRadioButton(self.layoutWidget_16)
        self.radioButton_studio_more.setObjectName(u"radioButton_studio_more")
        self.radioButton_studio_more.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_77.addWidget(self.radioButton_studio_more)

        self.radioButton_studio_none = QRadioButton(self.layoutWidget_16)
        self.radioButton_studio_none.setObjectName(u"radioButton_studio_none")
        self.radioButton_studio_none.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_77.addWidget(self.radioButton_studio_none)


        self.gridLayout_44.addLayout(self.horizontalLayout_77, 2, 1, 1, 1)

        self.label_257 = QLabel(self.layoutWidget_16)
        self.label_257.setObjectName(u"label_257")
        sizePolicy3.setHeightForWidth(self.label_257.sizePolicy().hasHeightForWidth())
        self.label_257.setSizePolicy(sizePolicy3)
        self.label_257.setMinimumSize(QSize(120, 30))
        self.label_257.setLayoutDirection(Qt.LeftToRight)
        self.label_257.setFrameShape(QFrame.NoFrame)
        self.label_257.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_44.addWidget(self.label_257, 2, 0, 1, 1)

        self.groupBox_35 = QGroupBox(self.scrollAreaWidgetContents_8)
        self.groupBox_35.setObjectName(u"groupBox_35")
        self.groupBox_35.setGeometry(QRect(30, 3680, 701, 181))
        self.groupBox_35.setMinimumSize(QSize(200, 0))
        self.groupBox_35.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_14 = QWidget(self.groupBox_35)
        self.layoutWidget_14.setObjectName(u"layoutWidget_14")
        self.layoutWidget_14.setGeometry(QRect(20, 29, 661, 141))
        self.gridLayout_41 = QGridLayout(self.layoutWidget_14)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_201 = QLabel(self.layoutWidget_14)
        self.label_201.setObjectName(u"label_201")
        sizePolicy3.setHeightForWidth(self.label_201.sizePolicy().hasHeightForWidth())
        self.label_201.setSizePolicy(sizePolicy3)
        self.label_201.setMinimumSize(QSize(120, 30))
        self.label_201.setLayoutDirection(Qt.LeftToRight)
        self.label_201.setFrameShape(QFrame.NoFrame)
        self.label_201.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_41.addWidget(self.label_201, 0, 0, 1, 1)

        self.lineEdit_series_website_exclude = QLineEdit(self.layoutWidget_14)
        self.lineEdit_series_website_exclude.setObjectName(u"lineEdit_series_website_exclude")
        sizePolicy2.setHeightForWidth(self.lineEdit_series_website_exclude.sizePolicy().hasHeightForWidth())
        self.lineEdit_series_website_exclude.setSizePolicy(sizePolicy2)
        self.lineEdit_series_website_exclude.setMinimumSize(QSize(300, 30))
        self.lineEdit_series_website_exclude.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_41.addWidget(self.lineEdit_series_website_exclude, 1, 1, 1, 1)

        self.label_205 = QLabel(self.layoutWidget_14)
        self.label_205.setObjectName(u"label_205")
        sizePolicy3.setHeightForWidth(self.label_205.sizePolicy().hasHeightForWidth())
        self.label_205.setSizePolicy(sizePolicy3)
        self.label_205.setMinimumSize(QSize(120, 30))
        self.label_205.setLayoutDirection(Qt.LeftToRight)
        self.label_205.setFrameShape(QFrame.NoFrame)
        self.label_205.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_41.addWidget(self.label_205, 1, 0, 1, 1)

        self.lineEdit_series_website = QLineEdit(self.layoutWidget_14)
        self.lineEdit_series_website.setObjectName(u"lineEdit_series_website")
        sizePolicy2.setHeightForWidth(self.lineEdit_series_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_series_website.setSizePolicy(sizePolicy2)
        self.lineEdit_series_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_series_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_41.addWidget(self.lineEdit_series_website, 0, 1, 1, 1)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.radioButton_series_listed = QRadioButton(self.layoutWidget_14)
        self.radioButton_series_listed.setObjectName(u"radioButton_series_listed")
        self.radioButton_series_listed.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_76.addWidget(self.radioButton_series_listed)

        self.radioButton_series_more = QRadioButton(self.layoutWidget_14)
        self.radioButton_series_more.setObjectName(u"radioButton_series_more")
        self.radioButton_series_more.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_76.addWidget(self.radioButton_series_more)

        self.radioButton_series_none = QRadioButton(self.layoutWidget_14)
        self.radioButton_series_none.setObjectName(u"radioButton_series_none")
        self.radioButton_series_none.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_76.addWidget(self.radioButton_series_none)


        self.gridLayout_41.addLayout(self.horizontalLayout_76, 2, 1, 1, 1)

        self.label_254 = QLabel(self.layoutWidget_14)
        self.label_254.setObjectName(u"label_254")
        sizePolicy3.setHeightForWidth(self.label_254.sizePolicy().hasHeightForWidth())
        self.label_254.setSizePolicy(sizePolicy3)
        self.label_254.setMinimumSize(QSize(120, 30))
        self.label_254.setLayoutDirection(Qt.LeftToRight)
        self.label_254.setFrameShape(QFrame.NoFrame)
        self.label_254.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_41.addWidget(self.label_254, 2, 0, 1, 1)

        self.groupBox_49 = QGroupBox(self.scrollAreaWidgetContents_8)
        self.groupBox_49.setObjectName(u"groupBox_49")
        self.groupBox_49.setGeometry(QRect(30, 4080, 701, 181))
        self.groupBox_49.setMinimumSize(QSize(200, 0))
        self.groupBox_49.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_18 = QWidget(self.groupBox_49)
        self.layoutWidget_18.setObjectName(u"layoutWidget_18")
        self.layoutWidget_18.setGeometry(QRect(20, 29, 661, 141))
        self.gridLayout_46 = QGridLayout(self.layoutWidget_18)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_223 = QLabel(self.layoutWidget_18)
        self.label_223.setObjectName(u"label_223")
        sizePolicy3.setHeightForWidth(self.label_223.sizePolicy().hasHeightForWidth())
        self.label_223.setSizePolicy(sizePolicy3)
        self.label_223.setMinimumSize(QSize(120, 30))
        self.label_223.setLayoutDirection(Qt.LeftToRight)
        self.label_223.setFrameShape(QFrame.NoFrame)
        self.label_223.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_46.addWidget(self.label_223, 1, 0, 1, 1)

        self.label_222 = QLabel(self.layoutWidget_18)
        self.label_222.setObjectName(u"label_222")
        sizePolicy3.setHeightForWidth(self.label_222.sizePolicy().hasHeightForWidth())
        self.label_222.setSizePolicy(sizePolicy3)
        self.label_222.setMinimumSize(QSize(120, 30))
        self.label_222.setLayoutDirection(Qt.LeftToRight)
        self.label_222.setFrameShape(QFrame.NoFrame)
        self.label_222.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_46.addWidget(self.label_222, 0, 0, 1, 1)

        self.lineEdit_publisher_website = QLineEdit(self.layoutWidget_18)
        self.lineEdit_publisher_website.setObjectName(u"lineEdit_publisher_website")
        sizePolicy2.setHeightForWidth(self.lineEdit_publisher_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_publisher_website.setSizePolicy(sizePolicy2)
        self.lineEdit_publisher_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_publisher_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_46.addWidget(self.lineEdit_publisher_website, 0, 1, 1, 1)

        self.lineEdit_publisher_website_exclude = QLineEdit(self.layoutWidget_18)
        self.lineEdit_publisher_website_exclude.setObjectName(u"lineEdit_publisher_website_exclude")
        sizePolicy2.setHeightForWidth(self.lineEdit_publisher_website_exclude.sizePolicy().hasHeightForWidth())
        self.lineEdit_publisher_website_exclude.setSizePolicy(sizePolicy2)
        self.lineEdit_publisher_website_exclude.setMinimumSize(QSize(300, 30))
        self.lineEdit_publisher_website_exclude.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_46.addWidget(self.lineEdit_publisher_website_exclude, 1, 1, 1, 1)

        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.radioButton_publisher_listed = QRadioButton(self.layoutWidget_18)
        self.radioButton_publisher_listed.setObjectName(u"radioButton_publisher_listed")
        self.radioButton_publisher_listed.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_78.addWidget(self.radioButton_publisher_listed)

        self.radioButton_publisher_more = QRadioButton(self.layoutWidget_18)
        self.radioButton_publisher_more.setObjectName(u"radioButton_publisher_more")
        self.radioButton_publisher_more.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_78.addWidget(self.radioButton_publisher_more)

        self.radioButton_publisher_none = QRadioButton(self.layoutWidget_18)
        self.radioButton_publisher_none.setObjectName(u"radioButton_publisher_none")
        self.radioButton_publisher_none.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_78.addWidget(self.radioButton_publisher_none)


        self.gridLayout_46.addLayout(self.horizontalLayout_78, 2, 1, 1, 1)

        self.label_258 = QLabel(self.layoutWidget_18)
        self.label_258.setObjectName(u"label_258")
        sizePolicy3.setHeightForWidth(self.label_258.sizePolicy().hasHeightForWidth())
        self.label_258.setSizePolicy(sizePolicy3)
        self.label_258.setMinimumSize(QSize(120, 30))
        self.label_258.setLayoutDirection(Qt.LeftToRight)
        self.label_258.setFrameShape(QFrame.NoFrame)
        self.label_258.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_46.addWidget(self.label_258, 2, 0, 1, 1)

        self.groupBox_11 = QGroupBox(self.scrollAreaWidgetContents_8)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(30, 20, 701, 251))
        self.groupBox_11.setMinimumSize(QSize(200, 0))
        self.groupBox_11.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget2 = QWidget(self.groupBox_11)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(50, 28, 631, 204))
        self.gridLayout_28 = QGridLayout(self.layoutWidget2)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.radioButton_scrape_single = QRadioButton(self.layoutWidget2)
        self.radioButton_scrape_single.setObjectName(u"radioButton_scrape_single")
        sizePolicy3.setHeightForWidth(self.radioButton_scrape_single.sizePolicy().hasHeightForWidth())
        self.radioButton_scrape_single.setSizePolicy(sizePolicy3)
        self.radioButton_scrape_single.setMinimumSize(QSize(0, 30))

        self.gridLayout_28.addWidget(self.radioButton_scrape_single, 3, 0, 1, 1)

        self.label_32 = QLabel(self.layoutWidget2)
        self.label_32.setObjectName(u"label_32")
        sizePolicy2.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy2)
        self.label_32.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_32.setWordWrap(True)
        self.label_32.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_28.addWidget(self.label_32, 1, 1, 1, 1)

        self.label_317 = QLabel(self.layoutWidget2)
        self.label_317.setObjectName(u"label_317")
        sizePolicy2.setHeightForWidth(self.label_317.sizePolicy().hasHeightForWidth())
        self.label_317.setSizePolicy(sizePolicy2)
        self.label_317.setMinimumSize(QSize(0, 20))
        self.label_317.setLayoutDirection(Qt.RightToLeft)
        self.label_317.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_317.setFrameShape(QFrame.NoFrame)
        self.label_317.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_317.setWordWrap(False)

        self.gridLayout_28.addWidget(self.label_317, 4, 1, 1, 1)

        self.radioButton_scrape_info = QRadioButton(self.layoutWidget2)
        self.radioButton_scrape_info.setObjectName(u"radioButton_scrape_info")
        sizePolicy3.setHeightForWidth(self.radioButton_scrape_info.sizePolicy().hasHeightForWidth())
        self.radioButton_scrape_info.setSizePolicy(sizePolicy3)
        self.radioButton_scrape_info.setMinimumSize(QSize(0, 30))

        self.gridLayout_28.addWidget(self.radioButton_scrape_info, 1, 0, 1, 1)

        self.label_28 = QLabel(self.layoutWidget2)
        self.label_28.setObjectName(u"label_28")
        sizePolicy2.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy2)
        self.label_28.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_28.setWordWrap(True)
        self.label_28.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_28.addWidget(self.label_28, 0, 1, 1, 1)

        self.radioButton_scrape_speed = QRadioButton(self.layoutWidget2)
        self.radioButton_scrape_speed.setObjectName(u"radioButton_scrape_speed")
        self.radioButton_scrape_speed.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.radioButton_scrape_speed.sizePolicy().hasHeightForWidth())
        self.radioButton_scrape_speed.setSizePolicy(sizePolicy3)
        self.radioButton_scrape_speed.setMinimumSize(QSize(90, 30))
        self.radioButton_scrape_speed.setLayoutDirection(Qt.LeftToRight)
        self.radioButton_scrape_speed.setAutoFillBackground(False)
        self.radioButton_scrape_speed.setAutoRepeatDelay(300)

        self.gridLayout_28.addWidget(self.radioButton_scrape_speed, 0, 0, 1, 1)

        self.comboBox_website_all = QComboBox(self.layoutWidget2)
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.addItem("")
        self.comboBox_website_all.setObjectName(u"comboBox_website_all")
        sizePolicy4.setHeightForWidth(self.comboBox_website_all.sizePolicy().hasHeightForWidth())
        self.comboBox_website_all.setSizePolicy(sizePolicy4)
        self.comboBox_website_all.setMinimumSize(QSize(0, 30))
        self.comboBox_website_all.setMaximumSize(QSize(16000, 30))
        self.comboBox_website_all.setSizeIncrement(QSize(0, 0))
        self.comboBox_website_all.setFocusPolicy(Qt.NoFocus)
        self.comboBox_website_all.setStyleSheet(u"")
        self.comboBox_website_all.setMaxVisibleItems(30)
        self.comboBox_website_all.setFrame(False)

        self.gridLayout_28.addWidget(self.comboBox_website_all, 3, 1, 1, 1)

        self.label_315 = QLabel(self.layoutWidget2)
        self.label_315.setObjectName(u"label_315")
        sizePolicy2.setHeightForWidth(self.label_315.sizePolicy().hasHeightForWidth())
        self.label_315.setSizePolicy(sizePolicy2)
        self.label_315.setMinimumSize(QSize(0, 20))
        self.label_315.setLayoutDirection(Qt.RightToLeft)
        self.label_315.setStyleSheet(u"color: rgb(255, 38, 0);\n"
"")
        self.label_315.setFrameShape(QFrame.NoFrame)
        self.label_315.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_315.setWordWrap(False)

        self.gridLayout_28.addWidget(self.label_315, 2, 1, 1, 1)

        self.pushButton_scrape_note = QPushButton(self.groupBox_11)
        self.pushButton_scrape_note.setObjectName(u"pushButton_scrape_note")
        self.pushButton_scrape_note.setGeometry(QRect(529, 200, 151, 26))
        sizePolicy3.setHeightForWidth(self.pushButton_scrape_note.sizePolicy().hasHeightForWidth())
        self.pushButton_scrape_note.setSizePolicy(sizePolicy3)
        self.pushButton_scrape_note.setMinimumSize(QSize(80, 26))
        self.groupBox_54 = QGroupBox(self.scrollAreaWidgetContents_8)
        self.groupBox_54.setObjectName(u"groupBox_54")
        self.groupBox_54.setGeometry(QRect(30, 2080, 701, 181))
        self.groupBox_54.setMinimumSize(QSize(200, 0))
        self.groupBox_54.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_31 = QWidget(self.groupBox_54)
        self.layoutWidget_31.setObjectName(u"layoutWidget_31")
        self.layoutWidget_31.setGeometry(QRect(20, 29, 661, 141))
        self.gridLayout_49 = QGridLayout(self.layoutWidget_31)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.gridLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_229 = QLabel(self.layoutWidget_31)
        self.label_229.setObjectName(u"label_229")
        sizePolicy3.setHeightForWidth(self.label_229.sizePolicy().hasHeightForWidth())
        self.label_229.setSizePolicy(sizePolicy3)
        self.label_229.setMinimumSize(QSize(120, 30))
        self.label_229.setLayoutDirection(Qt.LeftToRight)
        self.label_229.setFrameShape(QFrame.NoFrame)
        self.label_229.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_49.addWidget(self.label_229, 0, 0, 1, 1)

        self.lineEdit_poster_website = QLineEdit(self.layoutWidget_31)
        self.lineEdit_poster_website.setObjectName(u"lineEdit_poster_website")
        sizePolicy2.setHeightForWidth(self.lineEdit_poster_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_poster_website.setSizePolicy(sizePolicy2)
        self.lineEdit_poster_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_poster_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_49.addWidget(self.lineEdit_poster_website, 0, 1, 1, 1)

        self.label_191 = QLabel(self.layoutWidget_31)
        self.label_191.setObjectName(u"label_191")
        sizePolicy3.setHeightForWidth(self.label_191.sizePolicy().hasHeightForWidth())
        self.label_191.setSizePolicy(sizePolicy3)
        self.label_191.setMinimumSize(QSize(120, 30))
        self.label_191.setLayoutDirection(Qt.LeftToRight)
        self.label_191.setFrameShape(QFrame.NoFrame)
        self.label_191.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_49.addWidget(self.label_191, 1, 0, 1, 1)

        self.lineEdit_poster_website_exclude = QLineEdit(self.layoutWidget_31)
        self.lineEdit_poster_website_exclude.setObjectName(u"lineEdit_poster_website_exclude")
        sizePolicy2.setHeightForWidth(self.lineEdit_poster_website_exclude.sizePolicy().hasHeightForWidth())
        self.lineEdit_poster_website_exclude.setSizePolicy(sizePolicy2)
        self.lineEdit_poster_website_exclude.setMinimumSize(QSize(300, 30))
        self.lineEdit_poster_website_exclude.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_49.addWidget(self.lineEdit_poster_website_exclude, 1, 1, 1, 1)

        self.label_204 = QLabel(self.layoutWidget_31)
        self.label_204.setObjectName(u"label_204")
        sizePolicy3.setHeightForWidth(self.label_204.sizePolicy().hasHeightForWidth())
        self.label_204.setSizePolicy(sizePolicy3)
        self.label_204.setMinimumSize(QSize(120, 30))
        self.label_204.setLayoutDirection(Qt.LeftToRight)
        self.label_204.setFrameShape(QFrame.NoFrame)
        self.label_204.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_49.addWidget(self.label_204, 2, 0, 1, 1)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.radioButton_poster_listed = QRadioButton(self.layoutWidget_31)
        self.radioButton_poster_listed.setObjectName(u"radioButton_poster_listed")
        self.radioButton_poster_listed.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_68.addWidget(self.radioButton_poster_listed)

        self.radioButton_poster_more = QRadioButton(self.layoutWidget_31)
        self.radioButton_poster_more.setObjectName(u"radioButton_poster_more")
        self.radioButton_poster_more.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_68.addWidget(self.radioButton_poster_more)

        self.radioButton_poster_none = QRadioButton(self.layoutWidget_31)
        self.radioButton_poster_none.setObjectName(u"radioButton_poster_none")
        self.radioButton_poster_none.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_68.addWidget(self.radioButton_poster_none)


        self.gridLayout_49.addLayout(self.horizontalLayout_68, 2, 1, 1, 1)

        self.groupBox_60 = QGroupBox(self.scrollAreaWidgetContents_8)
        self.groupBox_60.setObjectName(u"groupBox_60")
        self.groupBox_60.setGeometry(QRect(30, 2480, 701, 181))
        self.groupBox_60.setMinimumSize(QSize(200, 0))
        self.groupBox_60.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_37 = QWidget(self.groupBox_60)
        self.layoutWidget_37.setObjectName(u"layoutWidget_37")
        self.layoutWidget_37.setGeometry(QRect(20, 29, 661, 141))
        self.gridLayout_64 = QGridLayout(self.layoutWidget_37)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.gridLayout_64.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_trailer_website_exclude = QLineEdit(self.layoutWidget_37)
        self.lineEdit_trailer_website_exclude.setObjectName(u"lineEdit_trailer_website_exclude")
        sizePolicy2.setHeightForWidth(self.lineEdit_trailer_website_exclude.sizePolicy().hasHeightForWidth())
        self.lineEdit_trailer_website_exclude.setSizePolicy(sizePolicy2)
        self.lineEdit_trailer_website_exclude.setMinimumSize(QSize(300, 30))
        self.lineEdit_trailer_website_exclude.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_64.addWidget(self.lineEdit_trailer_website_exclude, 1, 1, 1, 1)

        self.lineEdit_trailer_website = QLineEdit(self.layoutWidget_37)
        self.lineEdit_trailer_website.setObjectName(u"lineEdit_trailer_website")
        sizePolicy2.setHeightForWidth(self.lineEdit_trailer_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_trailer_website.setSizePolicy(sizePolicy2)
        self.lineEdit_trailer_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_trailer_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_64.addWidget(self.lineEdit_trailer_website, 0, 1, 1, 1)

        self.label_207 = QLabel(self.layoutWidget_37)
        self.label_207.setObjectName(u"label_207")
        sizePolicy3.setHeightForWidth(self.label_207.sizePolicy().hasHeightForWidth())
        self.label_207.setSizePolicy(sizePolicy3)
        self.label_207.setMinimumSize(QSize(120, 30))
        self.label_207.setLayoutDirection(Qt.LeftToRight)
        self.label_207.setFrameShape(QFrame.NoFrame)
        self.label_207.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_64.addWidget(self.label_207, 1, 0, 1, 1)

        self.label_206 = QLabel(self.layoutWidget_37)
        self.label_206.setObjectName(u"label_206")
        sizePolicy3.setHeightForWidth(self.label_206.sizePolicy().hasHeightForWidth())
        self.label_206.setSizePolicy(sizePolicy3)
        self.label_206.setMinimumSize(QSize(120, 30))
        self.label_206.setLayoutDirection(Qt.LeftToRight)
        self.label_206.setFrameShape(QFrame.NoFrame)
        self.label_206.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_64.addWidget(self.label_206, 0, 0, 1, 1)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.radioButton_trailer_listed = QRadioButton(self.layoutWidget_37)
        self.radioButton_trailer_listed.setObjectName(u"radioButton_trailer_listed")
        self.radioButton_trailer_listed.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_70.addWidget(self.radioButton_trailer_listed)

        self.radioButton_trailer_more = QRadioButton(self.layoutWidget_37)
        self.radioButton_trailer_more.setObjectName(u"radioButton_trailer_more")
        self.radioButton_trailer_more.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_70.addWidget(self.radioButton_trailer_more)

        self.radioButton_trailer_none = QRadioButton(self.layoutWidget_37)
        self.radioButton_trailer_none.setObjectName(u"radioButton_trailer_none")
        self.radioButton_trailer_none.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_70.addWidget(self.radioButton_trailer_none)


        self.gridLayout_64.addLayout(self.horizontalLayout_70, 2, 1, 1, 1)

        self.label_213 = QLabel(self.layoutWidget_37)
        self.label_213.setObjectName(u"label_213")
        sizePolicy3.setHeightForWidth(self.label_213.sizePolicy().hasHeightForWidth())
        self.label_213.setSizePolicy(sizePolicy3)
        self.label_213.setMinimumSize(QSize(120, 30))
        self.label_213.setLayoutDirection(Qt.LeftToRight)
        self.label_213.setFrameShape(QFrame.NoFrame)
        self.label_213.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_64.addWidget(self.label_213, 2, 0, 1, 1)

        self.groupBox_56 = QGroupBox(self.scrollAreaWidgetContents_8)
        self.groupBox_56.setObjectName(u"groupBox_56")
        self.groupBox_56.setGeometry(QRect(30, 2280, 701, 181))
        self.groupBox_56.setMinimumSize(QSize(200, 0))
        self.groupBox_56.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_33 = QWidget(self.groupBox_56)
        self.layoutWidget_33.setObjectName(u"layoutWidget_33")
        self.layoutWidget_33.setGeometry(QRect(20, 29, 661, 141))
        self.gridLayout_60 = QGridLayout(self.layoutWidget_33)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.gridLayout_60.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_extrafanart_website_exclude = QLineEdit(self.layoutWidget_33)
        self.lineEdit_extrafanart_website_exclude.setObjectName(u"lineEdit_extrafanart_website_exclude")
        sizePolicy2.setHeightForWidth(self.lineEdit_extrafanart_website_exclude.sizePolicy().hasHeightForWidth())
        self.lineEdit_extrafanart_website_exclude.setSizePolicy(sizePolicy2)
        self.lineEdit_extrafanart_website_exclude.setMinimumSize(QSize(300, 30))
        self.lineEdit_extrafanart_website_exclude.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_60.addWidget(self.lineEdit_extrafanart_website_exclude, 1, 1, 1, 1)

        self.label_193 = QLabel(self.layoutWidget_33)
        self.label_193.setObjectName(u"label_193")
        sizePolicy3.setHeightForWidth(self.label_193.sizePolicy().hasHeightForWidth())
        self.label_193.setSizePolicy(sizePolicy3)
        self.label_193.setMinimumSize(QSize(120, 30))
        self.label_193.setLayoutDirection(Qt.LeftToRight)
        self.label_193.setFrameShape(QFrame.NoFrame)
        self.label_193.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_60.addWidget(self.label_193, 1, 0, 1, 1)

        self.lineEdit_extrafanart_website = QLineEdit(self.layoutWidget_33)
        self.lineEdit_extrafanart_website.setObjectName(u"lineEdit_extrafanart_website")
        sizePolicy2.setHeightForWidth(self.lineEdit_extrafanart_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_extrafanart_website.setSizePolicy(sizePolicy2)
        self.lineEdit_extrafanart_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_extrafanart_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_60.addWidget(self.lineEdit_extrafanart_website, 0, 1, 1, 1)

        self.label_180 = QLabel(self.layoutWidget_33)
        self.label_180.setObjectName(u"label_180")
        sizePolicy3.setHeightForWidth(self.label_180.sizePolicy().hasHeightForWidth())
        self.label_180.setSizePolicy(sizePolicy3)
        self.label_180.setMinimumSize(QSize(120, 30))
        self.label_180.setLayoutDirection(Qt.LeftToRight)
        self.label_180.setFrameShape(QFrame.NoFrame)
        self.label_180.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_60.addWidget(self.label_180, 0, 0, 1, 1)

        self.label_212 = QLabel(self.layoutWidget_33)
        self.label_212.setObjectName(u"label_212")
        sizePolicy3.setHeightForWidth(self.label_212.sizePolicy().hasHeightForWidth())
        self.label_212.setSizePolicy(sizePolicy3)
        self.label_212.setMinimumSize(QSize(120, 30))
        self.label_212.setLayoutDirection(Qt.LeftToRight)
        self.label_212.setFrameShape(QFrame.NoFrame)
        self.label_212.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_60.addWidget(self.label_212, 2, 0, 1, 1)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.radioButton_extrafanart_listed = QRadioButton(self.layoutWidget_33)
        self.radioButton_extrafanart_listed.setObjectName(u"radioButton_extrafanart_listed")
        self.radioButton_extrafanart_listed.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_69.addWidget(self.radioButton_extrafanart_listed)

        self.radioButton_extrafanart_more = QRadioButton(self.layoutWidget_33)
        self.radioButton_extrafanart_more.setObjectName(u"radioButton_extrafanart_more")
        self.radioButton_extrafanart_more.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_69.addWidget(self.radioButton_extrafanart_more)

        self.radioButton_extrafanart_none = QRadioButton(self.layoutWidget_33)
        self.radioButton_extrafanart_none.setObjectName(u"radioButton_extrafanart_none")
        self.radioButton_extrafanart_none.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_69.addWidget(self.radioButton_extrafanart_none)


        self.gridLayout_60.addLayout(self.horizontalLayout_69, 2, 1, 1, 1)

        self.groupBox_55 = QGroupBox(self.scrollAreaWidgetContents_8)
        self.groupBox_55.setObjectName(u"groupBox_55")
        self.groupBox_55.setGeometry(QRect(30, 1880, 701, 181))
        self.groupBox_55.setMinimumSize(QSize(200, 0))
        self.groupBox_55.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_32 = QWidget(self.groupBox_55)
        self.layoutWidget_32.setObjectName(u"layoutWidget_32")
        self.layoutWidget_32.setGeometry(QRect(20, 29, 661, 141))
        self.gridLayout_59 = QGridLayout(self.layoutWidget_32)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.gridLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_192 = QLabel(self.layoutWidget_32)
        self.label_192.setObjectName(u"label_192")
        sizePolicy3.setHeightForWidth(self.label_192.sizePolicy().hasHeightForWidth())
        self.label_192.setSizePolicy(sizePolicy3)
        self.label_192.setMinimumSize(QSize(120, 30))
        self.label_192.setLayoutDirection(Qt.LeftToRight)
        self.label_192.setFrameShape(QFrame.NoFrame)
        self.label_192.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_59.addWidget(self.label_192, 1, 0, 1, 1)

        self.lineEdit_thumb_website = QLineEdit(self.layoutWidget_32)
        self.lineEdit_thumb_website.setObjectName(u"lineEdit_thumb_website")
        sizePolicy2.setHeightForWidth(self.lineEdit_thumb_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_thumb_website.setSizePolicy(sizePolicy2)
        self.lineEdit_thumb_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_thumb_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_59.addWidget(self.lineEdit_thumb_website, 0, 1, 1, 1)

        self.lineEdit_thumb_website_exclude = QLineEdit(self.layoutWidget_32)
        self.lineEdit_thumb_website_exclude.setObjectName(u"lineEdit_thumb_website_exclude")
        sizePolicy2.setHeightForWidth(self.lineEdit_thumb_website_exclude.sizePolicy().hasHeightForWidth())
        self.lineEdit_thumb_website_exclude.setSizePolicy(sizePolicy2)
        self.lineEdit_thumb_website_exclude.setMinimumSize(QSize(300, 30))
        self.lineEdit_thumb_website_exclude.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_59.addWidget(self.lineEdit_thumb_website_exclude, 1, 1, 1, 1)

        self.label_185 = QLabel(self.layoutWidget_32)
        self.label_185.setObjectName(u"label_185")
        sizePolicy3.setHeightForWidth(self.label_185.sizePolicy().hasHeightForWidth())
        self.label_185.setSizePolicy(sizePolicy3)
        self.label_185.setMinimumSize(QSize(120, 30))
        self.label_185.setLayoutDirection(Qt.LeftToRight)
        self.label_185.setFrameShape(QFrame.NoFrame)
        self.label_185.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_59.addWidget(self.label_185, 0, 0, 1, 1)

        self.label_203 = QLabel(self.layoutWidget_32)
        self.label_203.setObjectName(u"label_203")
        sizePolicy3.setHeightForWidth(self.label_203.sizePolicy().hasHeightForWidth())
        self.label_203.setSizePolicy(sizePolicy3)
        self.label_203.setMinimumSize(QSize(120, 30))
        self.label_203.setLayoutDirection(Qt.LeftToRight)
        self.label_203.setFrameShape(QFrame.NoFrame)
        self.label_203.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_59.addWidget(self.label_203, 2, 0, 1, 1)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.radioButton_thumb_listed = QRadioButton(self.layoutWidget_32)
        self.radioButton_thumb_listed.setObjectName(u"radioButton_thumb_listed")
        self.radioButton_thumb_listed.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_67.addWidget(self.radioButton_thumb_listed)

        self.radioButton_thumb_more = QRadioButton(self.layoutWidget_32)
        self.radioButton_thumb_more.setObjectName(u"radioButton_thumb_more")
        self.radioButton_thumb_more.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_67.addWidget(self.radioButton_thumb_more)

        self.radioButton_thumb_none = QRadioButton(self.layoutWidget_32)
        self.radioButton_thumb_none.setObjectName(u"radioButton_thumb_none")
        self.radioButton_thumb_none.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_67.addWidget(self.radioButton_thumb_none)


        self.gridLayout_59.addLayout(self.horizontalLayout_67, 2, 1, 1, 1)

        self.groupBox_59 = QGroupBox(self.scrollAreaWidgetContents_8)
        self.groupBox_59.setObjectName(u"groupBox_59")
        self.groupBox_59.setGeometry(QRect(30, 3080, 701, 181))
        self.groupBox_59.setMinimumSize(QSize(200, 0))
        self.groupBox_59.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_36 = QWidget(self.groupBox_59)
        self.layoutWidget_36.setObjectName(u"layoutWidget_36")
        self.layoutWidget_36.setGeometry(QRect(20, 20, 661, 151))
        self.gridLayout_63 = QGridLayout(self.layoutWidget_36)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.gridLayout_63.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_runtime_website = QLineEdit(self.layoutWidget_36)
        self.lineEdit_runtime_website.setObjectName(u"lineEdit_runtime_website")
        sizePolicy2.setHeightForWidth(self.lineEdit_runtime_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_runtime_website.setSizePolicy(sizePolicy2)
        self.lineEdit_runtime_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_runtime_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_63.addWidget(self.lineEdit_runtime_website, 0, 1, 1, 1)

        self.label_196 = QLabel(self.layoutWidget_36)
        self.label_196.setObjectName(u"label_196")
        sizePolicy3.setHeightForWidth(self.label_196.sizePolicy().hasHeightForWidth())
        self.label_196.setSizePolicy(sizePolicy3)
        self.label_196.setMinimumSize(QSize(120, 30))
        self.label_196.setLayoutDirection(Qt.LeftToRight)
        self.label_196.setFrameShape(QFrame.NoFrame)
        self.label_196.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_63.addWidget(self.label_196, 1, 0, 1, 1)

        self.lineEdit_runtime_website_exclude = QLineEdit(self.layoutWidget_36)
        self.lineEdit_runtime_website_exclude.setObjectName(u"lineEdit_runtime_website_exclude")
        sizePolicy2.setHeightForWidth(self.lineEdit_runtime_website_exclude.sizePolicy().hasHeightForWidth())
        self.lineEdit_runtime_website_exclude.setSizePolicy(sizePolicy2)
        self.lineEdit_runtime_website_exclude.setMinimumSize(QSize(300, 30))
        self.lineEdit_runtime_website_exclude.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_63.addWidget(self.lineEdit_runtime_website_exclude, 1, 1, 1, 1)

        self.label_181 = QLabel(self.layoutWidget_36)
        self.label_181.setObjectName(u"label_181")
        sizePolicy3.setHeightForWidth(self.label_181.sizePolicy().hasHeightForWidth())
        self.label_181.setSizePolicy(sizePolicy3)
        self.label_181.setMinimumSize(QSize(120, 30))
        self.label_181.setLayoutDirection(Qt.LeftToRight)
        self.label_181.setFrameShape(QFrame.NoFrame)
        self.label_181.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_63.addWidget(self.label_181, 0, 0, 1, 1)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.radioButton_runtime_listed = QRadioButton(self.layoutWidget_36)
        self.radioButton_runtime_listed.setObjectName(u"radioButton_runtime_listed")
        self.radioButton_runtime_listed.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_73.addWidget(self.radioButton_runtime_listed)

        self.radioButton_runtime_more = QRadioButton(self.layoutWidget_36)
        self.radioButton_runtime_more.setObjectName(u"radioButton_runtime_more")
        self.radioButton_runtime_more.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_73.addWidget(self.radioButton_runtime_more)

        self.radioButton_runtime_none = QRadioButton(self.layoutWidget_36)
        self.radioButton_runtime_none.setObjectName(u"radioButton_runtime_none")
        self.radioButton_runtime_none.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_73.addWidget(self.radioButton_runtime_none)


        self.gridLayout_63.addLayout(self.horizontalLayout_73, 2, 1, 1, 1)

        self.label_225 = QLabel(self.layoutWidget_36)
        self.label_225.setObjectName(u"label_225")
        sizePolicy3.setHeightForWidth(self.label_225.sizePolicy().hasHeightForWidth())
        self.label_225.setSizePolicy(sizePolicy3)
        self.label_225.setMinimumSize(QSize(120, 30))
        self.label_225.setLayoutDirection(Qt.LeftToRight)
        self.label_225.setFrameShape(QFrame.NoFrame)
        self.label_225.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_63.addWidget(self.label_225, 2, 0, 1, 1)

        self.groupBox_58 = QGroupBox(self.scrollAreaWidgetContents_8)
        self.groupBox_58.setObjectName(u"groupBox_58")
        self.groupBox_58.setGeometry(QRect(30, 2880, 701, 181))
        self.groupBox_58.setMinimumSize(QSize(200, 0))
        self.groupBox_58.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_35 = QWidget(self.groupBox_58)
        self.layoutWidget_35.setObjectName(u"layoutWidget_35")
        self.layoutWidget_35.setGeometry(QRect(20, 29, 661, 141))
        self.gridLayout_62 = QGridLayout(self.layoutWidget_35)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.gridLayout_62.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_release_website = QLineEdit(self.layoutWidget_35)
        self.lineEdit_release_website.setObjectName(u"lineEdit_release_website")
        sizePolicy2.setHeightForWidth(self.lineEdit_release_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_release_website.setSizePolicy(sizePolicy2)
        self.lineEdit_release_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_release_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_62.addWidget(self.lineEdit_release_website, 0, 1, 1, 1)

        self.label_182 = QLabel(self.layoutWidget_35)
        self.label_182.setObjectName(u"label_182")
        sizePolicy3.setHeightForWidth(self.label_182.sizePolicy().hasHeightForWidth())
        self.label_182.setSizePolicy(sizePolicy3)
        self.label_182.setMinimumSize(QSize(120, 30))
        self.label_182.setLayoutDirection(Qt.LeftToRight)
        self.label_182.setFrameShape(QFrame.NoFrame)
        self.label_182.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_62.addWidget(self.label_182, 0, 0, 1, 1)

        self.label_195 = QLabel(self.layoutWidget_35)
        self.label_195.setObjectName(u"label_195")
        sizePolicy3.setHeightForWidth(self.label_195.sizePolicy().hasHeightForWidth())
        self.label_195.setSizePolicy(sizePolicy3)
        self.label_195.setMinimumSize(QSize(120, 30))
        self.label_195.setLayoutDirection(Qt.LeftToRight)
        self.label_195.setFrameShape(QFrame.NoFrame)
        self.label_195.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_62.addWidget(self.label_195, 1, 0, 1, 1)

        self.lineEdit_release_website_exclude = QLineEdit(self.layoutWidget_35)
        self.lineEdit_release_website_exclude.setObjectName(u"lineEdit_release_website_exclude")
        sizePolicy2.setHeightForWidth(self.lineEdit_release_website_exclude.sizePolicy().hasHeightForWidth())
        self.lineEdit_release_website_exclude.setSizePolicy(sizePolicy2)
        self.lineEdit_release_website_exclude.setMinimumSize(QSize(300, 30))
        self.lineEdit_release_website_exclude.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_62.addWidget(self.lineEdit_release_website_exclude, 1, 1, 1, 1)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.radioButton_release_listed = QRadioButton(self.layoutWidget_35)
        self.radioButton_release_listed.setObjectName(u"radioButton_release_listed")
        self.radioButton_release_listed.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_72.addWidget(self.radioButton_release_listed)

        self.radioButton_release_more = QRadioButton(self.layoutWidget_35)
        self.radioButton_release_more.setObjectName(u"radioButton_release_more")
        self.radioButton_release_more.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_72.addWidget(self.radioButton_release_more)

        self.radioButton_release_none = QRadioButton(self.layoutWidget_35)
        self.radioButton_release_none.setObjectName(u"radioButton_release_none")
        self.radioButton_release_none.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_72.addWidget(self.radioButton_release_none)


        self.gridLayout_62.addLayout(self.horizontalLayout_72, 2, 1, 1, 1)

        self.label_224 = QLabel(self.layoutWidget_35)
        self.label_224.setObjectName(u"label_224")
        sizePolicy3.setHeightForWidth(self.label_224.sizePolicy().hasHeightForWidth())
        self.label_224.setSizePolicy(sizePolicy3)
        self.label_224.setMinimumSize(QSize(120, 30))
        self.label_224.setLayoutDirection(Qt.LeftToRight)
        self.label_224.setFrameShape(QFrame.NoFrame)
        self.label_224.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_62.addWidget(self.label_224, 2, 0, 1, 1)

        self.groupBox_57 = QGroupBox(self.scrollAreaWidgetContents_8)
        self.groupBox_57.setObjectName(u"groupBox_57")
        self.groupBox_57.setGeometry(QRect(30, 3280, 701, 181))
        self.groupBox_57.setMinimumSize(QSize(200, 0))
        self.groupBox_57.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_34 = QWidget(self.groupBox_57)
        self.layoutWidget_34.setObjectName(u"layoutWidget_34")
        self.layoutWidget_34.setGeometry(QRect(20, 29, 661, 141))
        self.gridLayout_61 = QGridLayout(self.layoutWidget_34)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.gridLayout_61.setContentsMargins(0, 0, 0, 0)
        self.label_194 = QLabel(self.layoutWidget_34)
        self.label_194.setObjectName(u"label_194")
        sizePolicy3.setHeightForWidth(self.label_194.sizePolicy().hasHeightForWidth())
        self.label_194.setSizePolicy(sizePolicy3)
        self.label_194.setMinimumSize(QSize(120, 30))
        self.label_194.setLayoutDirection(Qt.LeftToRight)
        self.label_194.setFrameShape(QFrame.NoFrame)
        self.label_194.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_61.addWidget(self.label_194, 1, 0, 1, 1)

        self.label_183 = QLabel(self.layoutWidget_34)
        self.label_183.setObjectName(u"label_183")
        sizePolicy3.setHeightForWidth(self.label_183.sizePolicy().hasHeightForWidth())
        self.label_183.setSizePolicy(sizePolicy3)
        self.label_183.setMinimumSize(QSize(120, 30))
        self.label_183.setLayoutDirection(Qt.LeftToRight)
        self.label_183.setFrameShape(QFrame.NoFrame)
        self.label_183.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_61.addWidget(self.label_183, 0, 0, 1, 1)

        self.lineEdit_score_website = QLineEdit(self.layoutWidget_34)
        self.lineEdit_score_website.setObjectName(u"lineEdit_score_website")
        sizePolicy2.setHeightForWidth(self.lineEdit_score_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_score_website.setSizePolicy(sizePolicy2)
        self.lineEdit_score_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_score_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_61.addWidget(self.lineEdit_score_website, 0, 1, 1, 1)

        self.lineEdit_score_website_exclude = QLineEdit(self.layoutWidget_34)
        self.lineEdit_score_website_exclude.setObjectName(u"lineEdit_score_website_exclude")
        sizePolicy2.setHeightForWidth(self.lineEdit_score_website_exclude.sizePolicy().hasHeightForWidth())
        self.lineEdit_score_website_exclude.setSizePolicy(sizePolicy2)
        self.lineEdit_score_website_exclude.setMinimumSize(QSize(300, 30))
        self.lineEdit_score_website_exclude.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_61.addWidget(self.lineEdit_score_website_exclude, 1, 1, 1, 1)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.radioButton_score_listed = QRadioButton(self.layoutWidget_34)
        self.radioButton_score_listed.setObjectName(u"radioButton_score_listed")
        self.radioButton_score_listed.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_74.addWidget(self.radioButton_score_listed)

        self.radioButton_score_more = QRadioButton(self.layoutWidget_34)
        self.radioButton_score_more.setObjectName(u"radioButton_score_more")
        self.radioButton_score_more.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_74.addWidget(self.radioButton_score_more)

        self.radioButton_score_none = QRadioButton(self.layoutWidget_34)
        self.radioButton_score_none.setObjectName(u"radioButton_score_none")
        self.radioButton_score_none.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_74.addWidget(self.radioButton_score_none)


        self.gridLayout_61.addLayout(self.horizontalLayout_74, 2, 1, 1, 1)

        self.label_226 = QLabel(self.layoutWidget_34)
        self.label_226.setObjectName(u"label_226")
        sizePolicy3.setHeightForWidth(self.label_226.sizePolicy().hasHeightForWidth())
        self.label_226.setSizePolicy(sizePolicy3)
        self.label_226.setMinimumSize(QSize(120, 30))
        self.label_226.setLayoutDirection(Qt.LeftToRight)
        self.label_226.setFrameShape(QFrame.NoFrame)
        self.label_226.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_61.addWidget(self.label_226, 2, 0, 1, 1)

        self.groupBox_50 = QGroupBox(self.scrollAreaWidgetContents_8)
        self.groupBox_50.setObjectName(u"groupBox_50")
        self.groupBox_50.setGeometry(QRect(30, 3480, 701, 181))
        self.groupBox_50.setMinimumSize(QSize(200, 0))
        self.groupBox_50.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_19 = QWidget(self.groupBox_50)
        self.layoutWidget_19.setObjectName(u"layoutWidget_19")
        self.layoutWidget_19.setGeometry(QRect(20, 29, 661, 141))
        self.gridLayout_47 = QGridLayout(self.layoutWidget_19)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.gridLayout_47.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_director_website = QLineEdit(self.layoutWidget_19)
        self.lineEdit_director_website.setObjectName(u"lineEdit_director_website")
        sizePolicy2.setHeightForWidth(self.lineEdit_director_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_director_website.setSizePolicy(sizePolicy2)
        self.lineEdit_director_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_director_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_47.addWidget(self.lineEdit_director_website, 0, 1, 1, 1)

        self.label_227 = QLabel(self.layoutWidget_19)
        self.label_227.setObjectName(u"label_227")
        sizePolicy3.setHeightForWidth(self.label_227.sizePolicy().hasHeightForWidth())
        self.label_227.setSizePolicy(sizePolicy3)
        self.label_227.setMinimumSize(QSize(120, 30))
        self.label_227.setLayoutDirection(Qt.LeftToRight)
        self.label_227.setFrameShape(QFrame.NoFrame)
        self.label_227.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_47.addWidget(self.label_227, 0, 0, 1, 1)

        self.label_228 = QLabel(self.layoutWidget_19)
        self.label_228.setObjectName(u"label_228")
        sizePolicy3.setHeightForWidth(self.label_228.sizePolicy().hasHeightForWidth())
        self.label_228.setSizePolicy(sizePolicy3)
        self.label_228.setMinimumSize(QSize(120, 30))
        self.label_228.setLayoutDirection(Qt.LeftToRight)
        self.label_228.setFrameShape(QFrame.NoFrame)
        self.label_228.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_47.addWidget(self.label_228, 1, 0, 1, 1)

        self.lineEdit_director_website_exclude = QLineEdit(self.layoutWidget_19)
        self.lineEdit_director_website_exclude.setObjectName(u"lineEdit_director_website_exclude")
        sizePolicy2.setHeightForWidth(self.lineEdit_director_website_exclude.sizePolicy().hasHeightForWidth())
        self.lineEdit_director_website_exclude.setSizePolicy(sizePolicy2)
        self.lineEdit_director_website_exclude.setMinimumSize(QSize(300, 30))
        self.lineEdit_director_website_exclude.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_47.addWidget(self.lineEdit_director_website_exclude, 1, 1, 1, 1)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.radioButton_director_listed = QRadioButton(self.layoutWidget_19)
        self.radioButton_director_listed.setObjectName(u"radioButton_director_listed")
        self.radioButton_director_listed.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_75.addWidget(self.radioButton_director_listed)

        self.radioButton_director_more = QRadioButton(self.layoutWidget_19)
        self.radioButton_director_more.setObjectName(u"radioButton_director_more")
        self.radioButton_director_more.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_75.addWidget(self.radioButton_director_more)

        self.radioButton_director_none = QRadioButton(self.layoutWidget_19)
        self.radioButton_director_none.setObjectName(u"radioButton_director_none")
        self.radioButton_director_none.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_75.addWidget(self.radioButton_director_none)


        self.gridLayout_47.addLayout(self.horizontalLayout_75, 2, 1, 1, 1)

        self.label_230 = QLabel(self.layoutWidget_19)
        self.label_230.setObjectName(u"label_230")
        sizePolicy3.setHeightForWidth(self.label_230.sizePolicy().hasHeightForWidth())
        self.label_230.setSizePolicy(sizePolicy3)
        self.label_230.setMinimumSize(QSize(120, 30))
        self.label_230.setLayoutDirection(Qt.LeftToRight)
        self.label_230.setFrameShape(QFrame.NoFrame)
        self.label_230.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_47.addWidget(self.label_230, 2, 0, 1, 1)

        self.groupBox_63 = QGroupBox(self.scrollAreaWidgetContents_8)
        self.groupBox_63.setObjectName(u"groupBox_63")
        self.groupBox_63.setGeometry(QRect(30, 4280, 701, 131))
        self.groupBox_63.setMinimumSize(QSize(200, 0))
        self.groupBox_63.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_22 = QWidget(self.groupBox_63)
        self.layoutWidget_22.setObjectName(u"layoutWidget_22")
        self.layoutWidget_22.setGeometry(QRect(20, 29, 661, 91))
        self.gridLayout_54 = QGridLayout(self.layoutWidget_22)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.gridLayout_54.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.radioButton_wanted_listed = QRadioButton(self.layoutWidget_22)
        self.radioButton_wanted_listed.setObjectName(u"radioButton_wanted_listed")
        self.radioButton_wanted_listed.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_82.addWidget(self.radioButton_wanted_listed)

        self.radioButton_wanted_none = QRadioButton(self.layoutWidget_22)
        self.radioButton_wanted_none.setObjectName(u"radioButton_wanted_none")
        self.radioButton_wanted_none.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_82.addWidget(self.radioButton_wanted_none)


        self.gridLayout_54.addLayout(self.horizontalLayout_82, 1, 1, 1, 1)

        self.label_274 = QLabel(self.layoutWidget_22)
        self.label_274.setObjectName(u"label_274")
        sizePolicy3.setHeightForWidth(self.label_274.sizePolicy().hasHeightForWidth())
        self.label_274.setSizePolicy(sizePolicy3)
        self.label_274.setMinimumSize(QSize(120, 30))
        self.label_274.setLayoutDirection(Qt.LeftToRight)
        self.label_274.setFrameShape(QFrame.NoFrame)
        self.label_274.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_54.addWidget(self.label_274, 1, 0, 1, 1)

        self.lineEdit_wanted_website = QLineEdit(self.layoutWidget_22)
        self.lineEdit_wanted_website.setObjectName(u"lineEdit_wanted_website")
        sizePolicy2.setHeightForWidth(self.lineEdit_wanted_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_wanted_website.setSizePolicy(sizePolicy2)
        self.lineEdit_wanted_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_wanted_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_54.addWidget(self.lineEdit_wanted_website, 0, 1, 1, 1)

        self.label_307 = QLabel(self.layoutWidget_22)
        self.label_307.setObjectName(u"label_307")
        sizePolicy3.setHeightForWidth(self.label_307.sizePolicy().hasHeightForWidth())
        self.label_307.setSizePolicy(sizePolicy3)
        self.label_307.setMinimumSize(QSize(120, 30))
        self.label_307.setLayoutDirection(Qt.LeftToRight)
        self.label_307.setFrameShape(QFrame.NoFrame)
        self.label_307.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_54.addWidget(self.label_307, 0, 0, 1, 1)

        self.layoutWidget3 = QWidget(self.scrollAreaWidgetContents_8)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(30, 940, 701, 41))
        self.horizontalLayout_107 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.layoutWidget3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_107.addWidget(self.line_2)

        self.label_300 = QLabel(self.layoutWidget3)
        self.label_300.setObjectName(u"label_300")
        sizePolicy3.setHeightForWidth(self.label_300.sizePolicy().hasHeightForWidth())
        self.label_300.setSizePolicy(sizePolicy3)
        self.label_300.setMinimumSize(QSize(130, 0))
        self.label_300.setLayoutDirection(Qt.RightToLeft)
        self.label_300.setStyleSheet(u"color: rgb(255, 38, 0);\n"
"font: 13pt;\n"
"font-weight:bold\n"
"")
        self.label_300.setFrameShape(QFrame.NoFrame)
        self.label_300.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_300.setWordWrap(False)

        self.horizontalLayout_107.addWidget(self.label_300)

        self.line = QFrame(self.layoutWidget3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_107.addWidget(self.line)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.scrollArea_6 = QScrollArea(self.tab_4)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setEnabled(True)
        self.scrollArea_6.setGeometry(QRect(0, 0, 796, 658))
        sizePolicy5.setHeightForWidth(self.scrollArea_6.sizePolicy().hasHeightForWidth())
        self.scrollArea_6.setSizePolicy(sizePolicy5)
        self.scrollArea_6.setFrameShape(QFrame.Box)
        self.scrollArea_6.setLineWidth(0)
        self.scrollArea_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_6.setWidgetResizable(False)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 760, 1870))
        self.groupBox_24 = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.groupBox_24.setGeometry(QRect(30, 20, 701, 451))
        self.groupBox_24.setMinimumSize(QSize(500, 0))
        self.horizontalLayoutWidget_14 = QWidget(self.groupBox_24)
        self.horizontalLayoutWidget_14.setObjectName(u"horizontalLayoutWidget_14")
        self.horizontalLayoutWidget_14.setGeometry(QRect(60, 30, 621, 31))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_14)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.checkBox_download_poster = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_poster.setObjectName(u"checkBox_download_poster")

        self.horizontalLayout_16.addWidget(self.checkBox_download_poster)

        self.checkBox_download_thumb = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_thumb.setObjectName(u"checkBox_download_thumb")

        self.horizontalLayout_16.addWidget(self.checkBox_download_thumb)

        self.checkBox_download_fanart = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_fanart.setObjectName(u"checkBox_download_fanart")

        self.horizontalLayout_16.addWidget(self.checkBox_download_fanart)

        self.checkBox_download_extrafanart = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_extrafanart.setObjectName(u"checkBox_download_extrafanart")

        self.horizontalLayout_16.addWidget(self.checkBox_download_extrafanart)

        self.checkBox_download_trailer = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_trailer.setObjectName(u"checkBox_download_trailer")

        self.horizontalLayout_16.addWidget(self.checkBox_download_trailer)

        self.checkBox_download_nfo = QCheckBox(self.horizontalLayoutWidget_14)
        self.checkBox_download_nfo.setObjectName(u"checkBox_download_nfo")

        self.horizontalLayout_16.addWidget(self.checkBox_download_nfo)

        self.layoutWidget4 = QWidget(self.groupBox_24)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(60, 210, 621, 208))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_88 = QHBoxLayout()
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.checkBox_ignore_pic_fail = QCheckBox(self.layoutWidget4)
        self.checkBox_ignore_pic_fail.setObjectName(u"checkBox_ignore_pic_fail")
        sizePolicy3.setHeightForWidth(self.checkBox_ignore_pic_fail.sizePolicy().hasHeightForWidth())
        self.checkBox_ignore_pic_fail.setSizePolicy(sizePolicy3)
        self.checkBox_ignore_pic_fail.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_88.addWidget(self.checkBox_ignore_pic_fail)

        self.label_275 = QLabel(self.layoutWidget4)
        self.label_275.setObjectName(u"label_275")
        sizePolicy2.setHeightForWidth(self.label_275.sizePolicy().hasHeightForWidth())
        self.label_275.setSizePolicy(sizePolicy2)
        self.label_275.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.horizontalLayout_88.addWidget(self.label_275)


        self.verticalLayout_2.addLayout(self.horizontalLayout_88)

        self.horizontalLayout_110 = QHBoxLayout()
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.checkBox_ignore_youma = QCheckBox(self.layoutWidget4)
        self.checkBox_ignore_youma.setObjectName(u"checkBox_ignore_youma")
        sizePolicy3.setHeightForWidth(self.checkBox_ignore_youma.sizePolicy().hasHeightForWidth())
        self.checkBox_ignore_youma.setSizePolicy(sizePolicy3)
        self.checkBox_ignore_youma.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_110.addWidget(self.checkBox_ignore_youma)

        self.label_326 = QLabel(self.layoutWidget4)
        self.label_326.setObjectName(u"label_326")
        sizePolicy2.setHeightForWidth(self.label_326.sizePolicy().hasHeightForWidth())
        self.label_326.setSizePolicy(sizePolicy2)
        self.label_326.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.horizontalLayout_110.addWidget(self.label_326)


        self.verticalLayout_2.addLayout(self.horizontalLayout_110)

        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.checkBox_ignore_wuma = QCheckBox(self.layoutWidget4)
        self.checkBox_ignore_wuma.setObjectName(u"checkBox_ignore_wuma")
        sizePolicy3.setHeightForWidth(self.checkBox_ignore_wuma.sizePolicy().hasHeightForWidth())
        self.checkBox_ignore_wuma.setSizePolicy(sizePolicy3)
        self.checkBox_ignore_wuma.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_87.addWidget(self.checkBox_ignore_wuma)

        self.label_273 = QLabel(self.layoutWidget4)
        self.label_273.setObjectName(u"label_273")
        sizePolicy2.setHeightForWidth(self.label_273.sizePolicy().hasHeightForWidth())
        self.label_273.setSizePolicy(sizePolicy2)
        self.label_273.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.horizontalLayout_87.addWidget(self.label_273)


        self.verticalLayout_2.addLayout(self.horizontalLayout_87)

        self.horizontalLayout_90 = QHBoxLayout()
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.checkBox_ignore_fc2 = QCheckBox(self.layoutWidget4)
        self.checkBox_ignore_fc2.setObjectName(u"checkBox_ignore_fc2")
        sizePolicy3.setHeightForWidth(self.checkBox_ignore_fc2.sizePolicy().hasHeightForWidth())
        self.checkBox_ignore_fc2.setSizePolicy(sizePolicy3)
        self.checkBox_ignore_fc2.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_90.addWidget(self.checkBox_ignore_fc2)

        self.label_292 = QLabel(self.layoutWidget4)
        self.label_292.setObjectName(u"label_292")
        sizePolicy2.setHeightForWidth(self.label_292.sizePolicy().hasHeightForWidth())
        self.label_292.setSizePolicy(sizePolicy2)
        self.label_292.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.horizontalLayout_90.addWidget(self.label_292)


        self.verticalLayout_2.addLayout(self.horizontalLayout_90)

        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.checkBox_ignore_guochan = QCheckBox(self.layoutWidget4)
        self.checkBox_ignore_guochan.setObjectName(u"checkBox_ignore_guochan")
        sizePolicy3.setHeightForWidth(self.checkBox_ignore_guochan.sizePolicy().hasHeightForWidth())
        self.checkBox_ignore_guochan.setSizePolicy(sizePolicy3)
        self.checkBox_ignore_guochan.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_94.addWidget(self.checkBox_ignore_guochan)

        self.label_305 = QLabel(self.layoutWidget4)
        self.label_305.setObjectName(u"label_305")
        sizePolicy2.setHeightForWidth(self.label_305.sizePolicy().hasHeightForWidth())
        self.label_305.setSizePolicy(sizePolicy2)
        self.label_305.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.horizontalLayout_94.addWidget(self.label_305)


        self.verticalLayout_2.addLayout(self.horizontalLayout_94)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.checkBox_ignore_size = QCheckBox(self.layoutWidget4)
        self.checkBox_ignore_size.setObjectName(u"checkBox_ignore_size")
        sizePolicy3.setHeightForWidth(self.checkBox_ignore_size.sizePolicy().hasHeightForWidth())
        self.checkBox_ignore_size.setSizePolicy(sizePolicy3)
        self.checkBox_ignore_size.setMinimumSize(QSize(10, 0))

        self.horizontalLayout_42.addWidget(self.checkBox_ignore_size)

        self.label_272 = QLabel(self.layoutWidget4)
        self.label_272.setObjectName(u"label_272")
        sizePolicy2.setHeightForWidth(self.label_272.sizePolicy().hasHeightForWidth())
        self.label_272.setSizePolicy(sizePolicy2)
        self.label_272.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.horizontalLayout_42.addWidget(self.label_272)


        self.verticalLayout_2.addLayout(self.horizontalLayout_42)

        self.layoutWidget5 = QWidget(self.groupBox_24)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(60, 70, 621, 131))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_85 = QLabel(self.layoutWidget5)
        self.label_85.setObjectName(u"label_85")
        sizePolicy3.setHeightForWidth(self.label_85.sizePolicy().hasHeightForWidth())
        self.label_85.setSizePolicy(sizePolicy3)
        self.label_85.setBaseSize(QSize(0, 0))
        self.label_85.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_85.setLayoutDirection(Qt.LeftToRight)
        self.label_85.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_85.setScaledContents(False)
        self.label_85.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_85.setWordWrap(False)
        self.label_85.setMargin(0)
        self.label_85.setIndent(0)
        self.label_85.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_3.addWidget(self.label_85)

        self.label_310 = QLabel(self.groupBox_24)
        self.label_310.setObjectName(u"label_310")
        self.label_310.setGeometry(QRect(60, 410, 621, 41))
        sizePolicy3.setHeightForWidth(self.label_310.sizePolicy().hasHeightForWidth())
        self.label_310.setSizePolicy(sizePolicy3)
        self.label_310.setMinimumSize(QSize(130, 0))
        self.label_310.setLayoutDirection(Qt.RightToLeft)
        self.label_310.setStyleSheet(u"color: rgb(255, 38, 0);\n"
"font-weight:bold")
        self.label_310.setFrameShape(QFrame.NoFrame)
        self.label_310.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_310.setWordWrap(True)
        self.groupBox_33 = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_33.setObjectName(u"groupBox_33")
        self.groupBox_33.setGeometry(QRect(30, 490, 701, 131))
        self.groupBox_33.setMinimumSize(QSize(500, 0))
        self.horizontalLayoutWidget_18 = QWidget(self.groupBox_33)
        self.horizontalLayoutWidget_18.setObjectName(u"horizontalLayoutWidget_18")
        self.horizontalLayoutWidget_18.setGeometry(QRect(60, 30, 621, 31))
        self.horizontalLayout_23 = QHBoxLayout(self.horizontalLayoutWidget_18)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.checkBox_old_poster = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_poster.setObjectName(u"checkBox_old_poster")

        self.horizontalLayout_23.addWidget(self.checkBox_old_poster)

        self.checkBox_old_thumb = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_thumb.setObjectName(u"checkBox_old_thumb")

        self.horizontalLayout_23.addWidget(self.checkBox_old_thumb)

        self.checkBox_old_fanart = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_fanart.setObjectName(u"checkBox_old_fanart")

        self.horizontalLayout_23.addWidget(self.checkBox_old_fanart)

        self.checkBox_old_extrafanart = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_extrafanart.setObjectName(u"checkBox_old_extrafanart")

        self.horizontalLayout_23.addWidget(self.checkBox_old_extrafanart)

        self.checkBox_old_trailer = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_trailer.setObjectName(u"checkBox_old_trailer")

        self.horizontalLayout_23.addWidget(self.checkBox_old_trailer)

        self.checkBox_old_nfo = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_nfo.setObjectName(u"checkBox_old_nfo")

        self.horizontalLayout_23.addWidget(self.checkBox_old_nfo)

        self.checkBox_old_extrafanart_copy = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_extrafanart_copy.setObjectName(u"checkBox_old_extrafanart_copy")

        self.horizontalLayout_23.addWidget(self.checkBox_old_extrafanart_copy)

        self.checkBox_old_theme_videos = QCheckBox(self.horizontalLayoutWidget_18)
        self.checkBox_old_theme_videos.setObjectName(u"checkBox_old_theme_videos")

        self.horizontalLayout_23.addWidget(self.checkBox_old_theme_videos)

        self.label_79 = QLabel(self.groupBox_33)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(60, 70, 621, 51))
        sizePolicy2.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy2)
        self.label_79.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_79.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_79.setWordWrap(True)
        self.label_79.setTextInteractionFlags(Qt.NoTextInteraction)
        self.groupBox_51 = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_51.setObjectName(u"groupBox_51")
        self.groupBox_51.setGeometry(QRect(30, 1560, 701, 211))
        self.groupBox_51.setStyleSheet(u"font:\"Courier\";")
        self.label_87 = QLabel(self.groupBox_51)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(60, 70, 641, 71))
        sizePolicy2.setHeightForWidth(self.label_87.sizePolicy().hasHeightForWidth())
        self.label_87.setSizePolicy(sizePolicy2)
        self.label_87.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_87.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_87.setWordWrap(True)
        self.label_87.setTextInteractionFlags(Qt.NoTextInteraction)
        self.horizontalLayoutWidget_20 = QWidget(self.groupBox_51)
        self.horizontalLayoutWidget_20.setObjectName(u"horizontalLayoutWidget_20")
        self.horizontalLayoutWidget_20.setGeometry(QRect(60, 30, 621, 31))
        self.horizontalLayout_25 = QHBoxLayout(self.horizontalLayoutWidget_20)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.checkBox_theme_videos = QCheckBox(self.horizontalLayoutWidget_20)
        self.checkBox_theme_videos.setObjectName(u"checkBox_theme_videos")

        self.horizontalLayout_25.addWidget(self.checkBox_theme_videos)

        self.pushButton_add_all_theme_videos = QPushButton(self.groupBox_51)
        self.pushButton_add_all_theme_videos.setObjectName(u"pushButton_add_all_theme_videos")
        self.pushButton_add_all_theme_videos.setGeometry(QRect(150, 140, 161, 40))
        self.pushButton_add_all_theme_videos.setStyleSheet(u"")
        self.pushButton_del_all_theme_videos = QPushButton(self.groupBox_51)
        self.pushButton_del_all_theme_videos.setObjectName(u"pushButton_del_all_theme_videos")
        self.pushButton_del_all_theme_videos.setGeometry(QRect(340, 140, 181, 40))
        self.groupBox_34 = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_34.setObjectName(u"groupBox_34")
        self.groupBox_34.setGeometry(QRect(30, 1280, 701, 261))
        self.groupBox_34.setMinimumSize(QSize(500, 0))
        self.horizontalLayoutWidget_19 = QWidget(self.groupBox_34)
        self.horizontalLayoutWidget_19.setObjectName(u"horizontalLayoutWidget_19")
        self.horizontalLayoutWidget_19.setGeometry(QRect(60, 30, 621, 37))
        self.horizontalLayout_24 = QHBoxLayout(self.horizontalLayoutWidget_19)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.checkBox_download_extrafanart_copy = QCheckBox(self.horizontalLayoutWidget_19)
        self.checkBox_download_extrafanart_copy.setObjectName(u"checkBox_download_extrafanart_copy")
        sizePolicy3.setHeightForWidth(self.checkBox_download_extrafanart_copy.sizePolicy().hasHeightForWidth())
        self.checkBox_download_extrafanart_copy.setSizePolicy(sizePolicy3)
        self.checkBox_download_extrafanart_copy.setMinimumSize(QSize(160, 30))

        self.horizontalLayout_24.addWidget(self.checkBox_download_extrafanart_copy)

        self.lineEdit_extrafanart_dir = QLineEdit(self.horizontalLayoutWidget_19)
        self.lineEdit_extrafanart_dir.setObjectName(u"lineEdit_extrafanart_dir")
        sizePolicy2.setHeightForWidth(self.lineEdit_extrafanart_dir.sizePolicy().hasHeightForWidth())
        self.lineEdit_extrafanart_dir.setSizePolicy(sizePolicy2)
        self.lineEdit_extrafanart_dir.setMinimumSize(QSize(300, 30))
        self.lineEdit_extrafanart_dir.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_24.addWidget(self.lineEdit_extrafanart_dir)

        self.label_59 = QLabel(self.groupBox_34)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(60, 80, 631, 101))
        sizePolicy2.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy2)
        self.label_59.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_59.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_59.setWordWrap(True)
        self.label_59.setTextInteractionFlags(Qt.NoTextInteraction)
        self.pushButton_add_all_extrafanart_copy = QPushButton(self.groupBox_34)
        self.pushButton_add_all_extrafanart_copy.setObjectName(u"pushButton_add_all_extrafanart_copy")
        self.pushButton_add_all_extrafanart_copy.setGeometry(QRect(150, 190, 161, 40))
        self.pushButton_add_all_extrafanart_copy.setStyleSheet(u"")
        self.pushButton_del_all_extrafanart_copy = QPushButton(self.groupBox_34)
        self.pushButton_del_all_extrafanart_copy.setObjectName(u"pushButton_del_all_extrafanart_copy")
        self.pushButton_del_all_extrafanart_copy.setGeometry(QRect(340, 190, 181, 40))
        self.groupBox_52 = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_52.setObjectName(u"groupBox_52")
        self.groupBox_52.setGeometry(QRect(30, 640, 701, 401))
        self.groupBox_52.setMinimumSize(QSize(500, 0))
        self.horizontalLayoutWidget_21 = QWidget(self.groupBox_52)
        self.horizontalLayoutWidget_21.setObjectName(u"horizontalLayoutWidget_21")
        self.horizontalLayoutWidget_21.setGeometry(QRect(60, 30, 621, 31))
        self.horizontalLayout_33 = QHBoxLayout(self.horizontalLayoutWidget_21)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.checkBox_hd_poster = QCheckBox(self.horizontalLayoutWidget_21)
        self.checkBox_hd_poster.setObjectName(u"checkBox_hd_poster")

        self.horizontalLayout_33.addWidget(self.checkBox_hd_poster)

        self.checkBox_hd_thumb = QCheckBox(self.horizontalLayoutWidget_21)
        self.checkBox_hd_thumb.setObjectName(u"checkBox_hd_thumb")

        self.horizontalLayout_33.addWidget(self.checkBox_hd_thumb)

        self.label_92 = QLabel(self.groupBox_52)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setGeometry(QRect(60, 60, 641, 31))
        sizePolicy2.setHeightForWidth(self.label_92.sizePolicy().hasHeightForWidth())
        self.label_92.setSizePolicy(sizePolicy2)
        self.label_92.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.horizontalLayoutWidget_22 = QWidget(self.groupBox_52)
        self.horizontalLayoutWidget_22.setObjectName(u"horizontalLayoutWidget_22")
        self.horizontalLayoutWidget_22.setGeometry(QRect(80, 170, 601, 31))
        self.horizontalLayout_143 = QHBoxLayout(self.horizontalLayoutWidget_22)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalLayout_143.setContentsMargins(0, 0, 0, 0)
        self.checkBox_google_big_pic = QCheckBox(self.horizontalLayoutWidget_22)
        self.checkBox_google_big_pic.setObjectName(u"checkBox_google_big_pic")
        sizePolicy3.setHeightForWidth(self.checkBox_google_big_pic.sizePolicy().hasHeightForWidth())
        self.checkBox_google_big_pic.setSizePolicy(sizePolicy3)

        self.horizontalLayout_143.addWidget(self.checkBox_google_big_pic)

        self.label_399 = QLabel(self.horizontalLayoutWidget_22)
        self.label_399.setObjectName(u"label_399")
        sizePolicy2.setHeightForWidth(self.label_399.sizePolicy().hasHeightForWidth())
        self.label_399.setSizePolicy(sizePolicy2)
        self.label_399.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.horizontalLayout_143.addWidget(self.label_399)

        self.lineEdit_google_used = QLineEdit(self.groupBox_52)
        self.lineEdit_google_used.setObjectName(u"lineEdit_google_used")
        self.lineEdit_google_used.setGeometry(QRect(110, 250, 571, 30))
        sizePolicy2.setHeightForWidth(self.lineEdit_google_used.sizePolicy().hasHeightForWidth())
        self.lineEdit_google_used.setSizePolicy(sizePolicy2)
        self.lineEdit_google_used.setMinimumSize(QSize(300, 30))
        self.lineEdit_google_used.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.label_311 = QLabel(self.groupBox_52)
        self.label_311.setObjectName(u"label_311")
        self.label_311.setGeometry(QRect(110, 310, 231, 30))
        sizePolicy3.setHeightForWidth(self.label_311.sizePolicy().hasHeightForWidth())
        self.label_311.setSizePolicy(sizePolicy3)
        self.label_311.setMinimumSize(QSize(130, 30))
        self.label_311.setLayoutDirection(Qt.RightToLeft)
        self.label_311.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_google_exclude = QLineEdit(self.groupBox_52)
        self.lineEdit_google_exclude.setObjectName(u"lineEdit_google_exclude")
        self.lineEdit_google_exclude.setGeometry(QRect(110, 340, 571, 30))
        sizePolicy2.setHeightForWidth(self.lineEdit_google_exclude.sizePolicy().hasHeightForWidth())
        self.lineEdit_google_exclude.setSizePolicy(sizePolicy2)
        self.lineEdit_google_exclude.setMinimumSize(QSize(300, 30))
        self.lineEdit_google_exclude.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.label_343 = QLabel(self.groupBox_52)
        self.label_343.setObjectName(u"label_343")
        self.label_343.setGeometry(QRect(110, 280, 441, 31))
        sizePolicy2.setHeightForWidth(self.label_343.sizePolicy().hasHeightForWidth())
        self.label_343.setSizePolicy(sizePolicy2)
        self.label_343.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.layoutWidget6 = QWidget(self.groupBox_52)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(100, 210, 470, 32))
        self.horizontalLayout_105 = QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.radioButton_google_first = QRadioButton(self.layoutWidget6)
        self.radioButton_google_first.setObjectName(u"radioButton_google_first")
        self.radioButton_google_first.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.radioButton_google_first.sizePolicy().hasHeightForWidth())
        self.radioButton_google_first.setSizePolicy(sizePolicy3)
        self.radioButton_google_first.setMinimumSize(QSize(90, 30))
        self.radioButton_google_first.setAutoRepeatDelay(300)

        self.horizontalLayout_105.addWidget(self.radioButton_google_first)

        self.radioButton_google_only = QRadioButton(self.layoutWidget6)
        self.radioButton_google_only.setObjectName(u"radioButton_google_only")
        self.radioButton_google_only.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.radioButton_google_only.sizePolicy().hasHeightForWidth())
        self.radioButton_google_only.setSizePolicy(sizePolicy3)
        self.radioButton_google_only.setMinimumSize(QSize(90, 30))
        self.radioButton_google_only.setAutoRepeatDelay(300)

        self.horizontalLayout_105.addWidget(self.radioButton_google_only)

        self.horizontalLayoutWidget_24 = QWidget(self.groupBox_52)
        self.horizontalLayoutWidget_24.setObjectName(u"horizontalLayoutWidget_24")
        self.horizontalLayoutWidget_24.setGeometry(QRect(80, 90, 601, 31))
        self.horizontalLayout_38 = QHBoxLayout(self.horizontalLayoutWidget_24)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.checkBox_amazon_big_pic = QCheckBox(self.horizontalLayoutWidget_24)
        self.checkBox_amazon_big_pic.setObjectName(u"checkBox_amazon_big_pic")
        sizePolicy3.setHeightForWidth(self.checkBox_amazon_big_pic.sizePolicy().hasHeightForWidth())
        self.checkBox_amazon_big_pic.setSizePolicy(sizePolicy3)

        self.horizontalLayout_38.addWidget(self.checkBox_amazon_big_pic)

        self.label_397 = QLabel(self.horizontalLayoutWidget_24)
        self.label_397.setObjectName(u"label_397")
        sizePolicy2.setHeightForWidth(self.label_397.sizePolicy().hasHeightForWidth())
        self.label_397.setSizePolicy(sizePolicy2)
        self.label_397.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.horizontalLayout_38.addWidget(self.label_397)

        self.horizontalLayoutWidget_25 = QWidget(self.groupBox_52)
        self.horizontalLayoutWidget_25.setObjectName(u"horizontalLayoutWidget_25")
        self.horizontalLayoutWidget_25.setGeometry(QRect(80, 130, 601, 31))
        self.horizontalLayout_130 = QHBoxLayout(self.horizontalLayoutWidget_25)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.checkBox_official_big_pic = QCheckBox(self.horizontalLayoutWidget_25)
        self.checkBox_official_big_pic.setObjectName(u"checkBox_official_big_pic")
        sizePolicy3.setHeightForWidth(self.checkBox_official_big_pic.sizePolicy().hasHeightForWidth())
        self.checkBox_official_big_pic.setSizePolicy(sizePolicy3)

        self.horizontalLayout_130.addWidget(self.checkBox_official_big_pic)

        self.label_398 = QLabel(self.horizontalLayoutWidget_25)
        self.label_398.setObjectName(u"label_398")
        sizePolicy2.setHeightForWidth(self.label_398.sizePolicy().hasHeightForWidth())
        self.label_398.setSizePolicy(sizePolicy2)
        self.label_398.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.horizontalLayout_130.addWidget(self.label_398)

        self.groupBox_66 = QGroupBox(self.scrollAreaWidgetContents_6)
        self.groupBox_66.setObjectName(u"groupBox_66")
        self.groupBox_66.setGeometry(QRect(30, 1060, 701, 201))
        self.groupBox_66.setStyleSheet(u"font:\"Courier\";")
        self.label_333 = QLabel(self.groupBox_66)
        self.label_333.setObjectName(u"label_333")
        self.label_333.setGeometry(QRect(60, 70, 641, 51))
        sizePolicy2.setHeightForWidth(self.label_333.sizePolicy().hasHeightForWidth())
        self.label_333.setSizePolicy(sizePolicy2)
        self.label_333.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_333.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_333.setWordWrap(True)
        self.label_333.setTextInteractionFlags(Qt.NoTextInteraction)
        self.horizontalLayoutWidget_23 = QWidget(self.groupBox_66)
        self.horizontalLayoutWidget_23.setObjectName(u"horizontalLayoutWidget_23")
        self.horizontalLayoutWidget_23.setGeometry(QRect(60, 30, 621, 31))
        self.horizontalLayout_113 = QHBoxLayout(self.horizontalLayoutWidget_23)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.checkBox_extras = QCheckBox(self.horizontalLayoutWidget_23)
        self.checkBox_extras.setObjectName(u"checkBox_extras")

        self.horizontalLayout_113.addWidget(self.checkBox_extras)

        self.pushButton_add_all_extras = QPushButton(self.groupBox_66)
        self.pushButton_add_all_extras.setObjectName(u"pushButton_add_all_extras")
        self.pushButton_add_all_extras.setGeometry(QRect(150, 130, 161, 40))
        self.pushButton_add_all_extras.setStyleSheet(u"")
        self.pushButton_del_all_extras = QPushButton(self.groupBox_66)
        self.pushButton_del_all_extras.setObjectName(u"pushButton_del_all_extras")
        self.pushButton_del_all_extras.setGeometry(QRect(340, 130, 181, 40))
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.scrollArea_7 = QScrollArea(self.tab_3)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setGeometry(QRect(0, 0, 796, 658))
        self.scrollArea_7.setFrameShape(QFrame.Box)
        self.scrollArea_7.setLineWidth(0)
        self.scrollArea_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_7.setWidgetResizable(False)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 760, 3420))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents_7.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_7.setSizePolicy(sizePolicy1)
        self.groupBox_8 = QGroupBox(self.scrollAreaWidgetContents_7)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(30, 20, 701, 611))
        self.groupBox_8.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_8 = QWidget(self.groupBox_8)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(20, 30, 661, 561))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_prevent_char = QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_prevent_char.setObjectName(u"lineEdit_prevent_char")
        self.lineEdit_prevent_char.setMinimumSize(QSize(450, 30))
        self.lineEdit_prevent_char.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_8.addWidget(self.lineEdit_prevent_char, 6, 1, 1, 1)

        self.lineEdit_media_name = QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_media_name.setObjectName(u"lineEdit_media_name")
        self.lineEdit_media_name.setMinimumSize(QSize(450, 30))
        self.lineEdit_media_name.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_8.addWidget(self.lineEdit_media_name, 4, 1, 1, 1)

        self.label_66 = QLabel(self.gridLayoutWidget_8)
        self.label_66.setObjectName(u"label_66")
        sizePolicy2.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy2)
        self.label_66.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_66.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_66.setWordWrap(True)
        self.label_66.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout_8.addWidget(self.label_66, 1, 1, 1, 1)

        self.label_63 = QLabel(self.gridLayoutWidget_8)
        self.label_63.setObjectName(u"label_63")
        sizePolicy3.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy3)
        self.label_63.setMinimumSize(QSize(0, 0))
        self.label_63.setLayoutDirection(Qt.RightToLeft)
        self.label_63.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_63, 2, 0, 1, 1)

        self.lineEdit_dir_name = QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_dir_name.setObjectName(u"lineEdit_dir_name")
        self.lineEdit_dir_name.setMinimumSize(QSize(450, 30))
        self.lineEdit_dir_name.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_8.addWidget(self.lineEdit_dir_name, 0, 1, 1, 1)

        self.label_43 = QLabel(self.gridLayoutWidget_8)
        self.label_43.setObjectName(u"label_43")
        sizePolicy7.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy7)
        self.label_43.setMinimumSize(QSize(130, 0))
        self.label_43.setLayoutDirection(Qt.RightToLeft)
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_43, 0, 0, 1, 1)

        self.label_240 = QLabel(self.gridLayoutWidget_8)
        self.label_240.setObjectName(u"label_240")
        sizePolicy3.setHeightForWidth(self.label_240.sizePolicy().hasHeightForWidth())
        self.label_240.setSizePolicy(sizePolicy3)
        self.label_240.setMinimumSize(QSize(0, 0))
        self.label_240.setLayoutDirection(Qt.RightToLeft)
        self.label_240.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_240, 6, 0, 1, 1)

        self.label_68 = QLabel(self.gridLayoutWidget_8)
        self.label_68.setObjectName(u"label_68")
        sizePolicy2.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy2)
        self.label_68.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_8.addWidget(self.label_68, 5, 1, 1, 1)

        self.label_67 = QLabel(self.gridLayoutWidget_8)
        self.label_67.setObjectName(u"label_67")
        sizePolicy3.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy3)
        self.label_67.setMinimumSize(QSize(0, 0))
        self.label_67.setLayoutDirection(Qt.RightToLeft)
        self.label_67.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_67, 4, 0, 1, 1)

        self.label_61 = QLabel(self.gridLayoutWidget_8)
        self.label_61.setObjectName(u"label_61")
        sizePolicy2.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy2)
        self.label_61.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_8.addWidget(self.label_61, 3, 1, 1, 1)

        self.label_239 = QLabel(self.gridLayoutWidget_8)
        self.label_239.setObjectName(u"label_239")
        sizePolicy2.setHeightForWidth(self.label_239.sizePolicy().hasHeightForWidth())
        self.label_239.setSizePolicy(sizePolicy2)
        self.label_239.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_8.addWidget(self.label_239, 7, 1, 1, 1)

        self.lineEdit_local_name = QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_local_name.setObjectName(u"lineEdit_local_name")
        self.lineEdit_local_name.setMinimumSize(QSize(450, 30))
        self.lineEdit_local_name.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_8.addWidget(self.lineEdit_local_name, 2, 1, 1, 1)

        self.label_147 = QLabel(self.gridLayoutWidget_8)
        self.label_147.setObjectName(u"label_147")
        sizePolicy.setHeightForWidth(self.label_147.sizePolicy().hasHeightForWidth())
        self.label_147.setSizePolicy(sizePolicy)
        self.label_147.setMinimumSize(QSize(0, 0))
        self.label_147.setLayoutDirection(Qt.RightToLeft)
        self.label_147.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_147, 1, 0, 1, 1)

        self.groupBox_38 = QGroupBox(self.scrollAreaWidgetContents_7)
        self.groupBox_38.setObjectName(u"groupBox_38")
        self.groupBox_38.setGeometry(QRect(30, 1990, 701, 441))
        self.groupBox_38.setMinimumSize(QSize(200, 0))
        self.groupBox_38.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_22 = QWidget(self.groupBox_38)
        self.gridLayoutWidget_22.setObjectName(u"gridLayoutWidget_22")
        self.gridLayoutWidget_22.setGeometry(QRect(60, 30, 621, 111))
        self.gridLayout_22 = QGridLayout(self.gridLayoutWidget_22)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_98 = QLabel(self.gridLayoutWidget_22)
        self.label_98.setObjectName(u"label_98")
        sizePolicy2.setHeightForWidth(self.label_98.sizePolicy().hasHeightForWidth())
        self.label_98.setSizePolicy(sizePolicy2)
        self.label_98.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_22.addWidget(self.label_98, 1, 1, 1, 1)

        self.radioButton_cd_part_lower = QRadioButton(self.gridLayoutWidget_22)
        self.radioButton_cd_part_lower.setObjectName(u"radioButton_cd_part_lower")
        sizePolicy3.setHeightForWidth(self.radioButton_cd_part_lower.sizePolicy().hasHeightForWidth())
        self.radioButton_cd_part_lower.setSizePolicy(sizePolicy3)
        self.radioButton_cd_part_lower.setMinimumSize(QSize(120, 0))
        self.radioButton_cd_part_lower.setAutoExclusive(True)

        self.gridLayout_22.addWidget(self.radioButton_cd_part_lower, 0, 0, 1, 1)

        self.label_97 = QLabel(self.gridLayoutWidget_22)
        self.label_97.setObjectName(u"label_97")
        sizePolicy2.setHeightForWidth(self.label_97.sizePolicy().hasHeightForWidth())
        self.label_97.setSizePolicy(sizePolicy2)
        self.label_97.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_22.addWidget(self.label_97, 0, 1, 1, 1)

        self.radioButton_cd_part_upper = QRadioButton(self.gridLayoutWidget_22)
        self.radioButton_cd_part_upper.setObjectName(u"radioButton_cd_part_upper")
        self.radioButton_cd_part_upper.setMinimumSize(QSize(80, 0))
        self.radioButton_cd_part_upper.setAutoExclusive(True)

        self.gridLayout_22.addWidget(self.radioButton_cd_part_upper, 1, 0, 1, 1)

        self.radioButton_cd_part_digital = QRadioButton(self.gridLayoutWidget_22)
        self.radioButton_cd_part_digital.setObjectName(u"radioButton_cd_part_digital")
        self.radioButton_cd_part_digital.setMinimumSize(QSize(80, 0))
        self.radioButton_cd_part_digital.setAutoExclusive(True)

        self.gridLayout_22.addWidget(self.radioButton_cd_part_digital, 2, 0, 1, 1)

        self.label_349 = QLabel(self.gridLayoutWidget_22)
        self.label_349.setObjectName(u"label_349")
        sizePolicy2.setHeightForWidth(self.label_349.sizePolicy().hasHeightForWidth())
        self.label_349.setSizePolicy(sizePolicy2)
        self.label_349.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_22.addWidget(self.label_349, 2, 1, 1, 1)

        self.label_99 = QLabel(self.groupBox_38)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(60, 150, 611, 20))
        sizePolicy2.setHeightForWidth(self.label_99.sizePolicy().hasHeightForWidth())
        self.label_99.setSizePolicy(sizePolicy2)
        self.label_99.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.checkBox_cd_part_a = QCheckBox(self.groupBox_38)
        self.checkBox_cd_part_a.setObjectName(u"checkBox_cd_part_a")
        self.checkBox_cd_part_a.setGeometry(QRect(160, 180, 481, 30))
        sizePolicy4.setHeightForWidth(self.checkBox_cd_part_a.sizePolicy().hasHeightForWidth())
        self.checkBox_cd_part_a.setSizePolicy(sizePolicy4)
        self.checkBox_cd_part_a.setMinimumSize(QSize(100, 30))
        self.label_350 = QLabel(self.groupBox_38)
        self.label_350.setObjectName(u"label_350")
        self.label_350.setGeometry(QRect(20, 180, 131, 30))
        sizePolicy3.setHeightForWidth(self.label_350.sizePolicy().hasHeightForWidth())
        self.label_350.setSizePolicy(sizePolicy3)
        self.label_350.setMinimumSize(QSize(130, 30))
        self.label_350.setLayoutDirection(Qt.LeftToRight)
        self.label_350.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.checkBox_cd_part_01 = QCheckBox(self.groupBox_38)
        self.checkBox_cd_part_01.setObjectName(u"checkBox_cd_part_01")
        self.checkBox_cd_part_01.setGeometry(QRect(160, 270, 211, 30))
        sizePolicy4.setHeightForWidth(self.checkBox_cd_part_01.sizePolicy().hasHeightForWidth())
        self.checkBox_cd_part_01.setSizePolicy(sizePolicy4)
        self.checkBox_cd_part_01.setMinimumSize(QSize(100, 30))
        self.checkBox_cd_part_1_xxx = QCheckBox(self.groupBox_38)
        self.checkBox_cd_part_1_xxx.setObjectName(u"checkBox_cd_part_1_xxx")
        self.checkBox_cd_part_1_xxx.setGeometry(QRect(160, 310, 291, 30))
        sizePolicy4.setHeightForWidth(self.checkBox_cd_part_1_xxx.sizePolicy().hasHeightForWidth())
        self.checkBox_cd_part_1_xxx.setSizePolicy(sizePolicy4)
        self.checkBox_cd_part_1_xxx.setMinimumSize(QSize(100, 30))
        self.label_408 = QLabel(self.groupBox_38)
        self.label_408.setObjectName(u"label_408")
        self.label_408.setGeometry(QRect(10, 350, 141, 30))
        sizePolicy3.setHeightForWidth(self.label_408.sizePolicy().hasHeightForWidth())
        self.label_408.setSizePolicy(sizePolicy3)
        self.label_408.setMinimumSize(QSize(130, 30))
        self.label_408.setLayoutDirection(Qt.LeftToRight)
        self.label_408.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.checkBox_cd_part_space = QCheckBox(self.groupBox_38)
        self.checkBox_cd_part_space.setObjectName(u"checkBox_cd_part_space")
        self.checkBox_cd_part_space.setGeometry(QRect(320, 350, 110, 30))
        sizePolicy4.setHeightForWidth(self.checkBox_cd_part_space.sizePolicy().hasHeightForWidth())
        self.checkBox_cd_part_space.setSizePolicy(sizePolicy4)
        self.checkBox_cd_part_space.setMinimumSize(QSize(100, 30))
        self.checkBox_cd_part_underline = QCheckBox(self.groupBox_38)
        self.checkBox_cd_part_underline.setObjectName(u"checkBox_cd_part_underline")
        self.checkBox_cd_part_underline.setGeometry(QRect(160, 350, 121, 30))
        sizePolicy4.setHeightForWidth(self.checkBox_cd_part_underline.sizePolicy().hasHeightForWidth())
        self.checkBox_cd_part_underline.setSizePolicy(sizePolicy4)
        self.checkBox_cd_part_underline.setMinimumSize(QSize(100, 30))
        self.checkBox_cd_part_point = QCheckBox(self.groupBox_38)
        self.checkBox_cd_part_point.setObjectName(u"checkBox_cd_part_point")
        self.checkBox_cd_part_point.setGeometry(QRect(460, 350, 110, 30))
        sizePolicy4.setHeightForWidth(self.checkBox_cd_part_point.sizePolicy().hasHeightForWidth())
        self.checkBox_cd_part_point.setSizePolicy(sizePolicy4)
        self.checkBox_cd_part_point.setMinimumSize(QSize(100, 30))
        self.label_409 = QLabel(self.groupBox_38)
        self.label_409.setObjectName(u"label_409")
        self.label_409.setGeometry(QRect(160, 390, 261, 20))
        sizePolicy2.setHeightForWidth(self.label_409.sizePolicy().hasHeightForWidth())
        self.label_409.setSizePolicy(sizePolicy2)
        self.label_409.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.checkBox_cd_part_c = QCheckBox(self.groupBox_38)
        self.checkBox_cd_part_c.setObjectName(u"checkBox_cd_part_c")
        self.checkBox_cd_part_c.setGeometry(QRect(200, 210, 481, 30))
        sizePolicy4.setHeightForWidth(self.checkBox_cd_part_c.sizePolicy().hasHeightForWidth())
        self.checkBox_cd_part_c.setSizePolicy(sizePolicy4)
        self.checkBox_cd_part_c.setMinimumSize(QSize(100, 30))
        self.label_430 = QLabel(self.groupBox_38)
        self.label_430.setObjectName(u"label_430")
        self.label_430.setGeometry(QRect(210, 240, 431, 20))
        sizePolicy2.setHeightForWidth(self.label_430.sizePolicy().hasHeightForWidth())
        self.label_430.setSizePolicy(sizePolicy2)
        self.label_430.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.groupBox_77 = QGroupBox(self.scrollAreaWidgetContents_7)
        self.groupBox_77.setObjectName(u"groupBox_77")
        self.groupBox_77.setGeometry(QRect(30, 1080, 701, 351))
        self.groupBox_77.setStyleSheet(u"font:\"Courier\";")
        self.lineEdit_file_name_max = QLineEdit(self.groupBox_77)
        self.lineEdit_file_name_max.setObjectName(u"lineEdit_file_name_max")
        self.lineEdit_file_name_max.setGeometry(QRect(157, 128, 521, 30))
        self.lineEdit_file_name_max.setMinimumSize(QSize(450, 30))
        self.lineEdit_file_name_max.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.label_171 = QLabel(self.groupBox_77)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setGeometry(QRect(21, 36, 130, 16))
        sizePolicy7.setHeightForWidth(self.label_171.sizePolicy().hasHeightForWidth())
        self.label_171.setSizePolicy(sizePolicy7)
        self.label_171.setMinimumSize(QSize(130, 0))
        self.label_171.setLayoutDirection(Qt.RightToLeft)
        self.label_171.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_167 = QLabel(self.groupBox_77)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setGeometry(QRect(45, 227, 106, 16))
        sizePolicy3.setHeightForWidth(self.label_167.sizePolicy().hasHeightForWidth())
        self.label_167.setSizePolicy(sizePolicy3)
        self.label_167.setMinimumSize(QSize(0, 0))
        self.label_167.setLayoutDirection(Qt.RightToLeft)
        self.label_167.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_169 = QLabel(self.groupBox_77)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setGeometry(QRect(157, 77, 523, 40))
        sizePolicy2.setHeightForWidth(self.label_169.sizePolicy().hasHeightForWidth())
        self.label_169.setSizePolicy(sizePolicy2)
        self.label_169.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_169.setWordWrap(True)
        self.label_169.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_170 = QLabel(self.groupBox_77)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setGeometry(QRect(45, 135, 106, 16))
        sizePolicy3.setHeightForWidth(self.label_170.sizePolicy().hasHeightForWidth())
        self.label_170.setSizePolicy(sizePolicy3)
        self.label_170.setMinimumSize(QSize(0, 0))
        self.label_170.setLayoutDirection(Qt.RightToLeft)
        self.label_170.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_172 = QLabel(self.groupBox_77)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setGeometry(QRect(157, 169, 523, 40))
        sizePolicy2.setHeightForWidth(self.label_172.sizePolicy().hasHeightForWidth())
        self.label_172.setSizePolicy(sizePolicy2)
        self.label_172.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_172.setWordWrap(True)
        self.label_172.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_168 = QLabel(self.groupBox_77)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setGeometry(QRect(157, 268, 464, 16))
        sizePolicy2.setHeightForWidth(self.label_168.sizePolicy().hasHeightForWidth())
        self.label_168.setSizePolicy(sizePolicy2)
        self.label_168.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.lineEdit_folder_name_max = QLineEdit(self.groupBox_77)
        self.lineEdit_folder_name_max.setObjectName(u"lineEdit_folder_name_max")
        self.lineEdit_folder_name_max.setGeometry(QRect(157, 36, 521, 30))
        self.lineEdit_folder_name_max.setMinimumSize(QSize(450, 30))
        self.lineEdit_folder_name_max.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.lineEdit_actor_name_max = QLineEdit(self.groupBox_77)
        self.lineEdit_actor_name_max.setObjectName(u"lineEdit_actor_name_max")
        self.lineEdit_actor_name_max.setGeometry(QRect(157, 220, 521, 30))
        self.lineEdit_actor_name_max.setMinimumSize(QSize(450, 30))
        self.lineEdit_actor_name_max.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.lineEdit_actor_name_more = QLineEdit(self.groupBox_77)
        self.lineEdit_actor_name_more.setObjectName(u"lineEdit_actor_name_more")
        self.lineEdit_actor_name_more.setGeometry(QRect(157, 302, 211, 30))
        self.lineEdit_actor_name_more.setMinimumSize(QSize(0, 30))
        self.lineEdit_actor_name_more.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.label_288 = QLabel(self.groupBox_77)
        self.label_288.setObjectName(u"label_288")
        self.label_288.setGeometry(QRect(21, 370, 130, 30))
        sizePolicy3.setHeightForWidth(self.label_288.sizePolicy().hasHeightForWidth())
        self.label_288.setSizePolicy(sizePolicy3)
        self.label_288.setMinimumSize(QSize(130, 30))
        self.label_288.setLayoutDirection(Qt.RightToLeft)
        self.label_288.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_287 = QLabel(self.groupBox_77)
        self.label_287.setObjectName(u"label_287")
        self.label_287.setGeometry(QRect(21, 82, 130, 30))
        sizePolicy3.setHeightForWidth(self.label_287.sizePolicy().hasHeightForWidth())
        self.label_287.setSizePolicy(sizePolicy3)
        self.label_287.setMinimumSize(QSize(130, 30))
        self.label_287.setLayoutDirection(Qt.RightToLeft)
        self.label_287.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_289 = QLabel(self.groupBox_77)
        self.label_289.setObjectName(u"label_289")
        self.label_289.setGeometry(QRect(21, 174, 130, 30))
        sizePolicy3.setHeightForWidth(self.label_289.sizePolicy().hasHeightForWidth())
        self.label_289.setSizePolicy(sizePolicy3)
        self.label_289.setMinimumSize(QSize(130, 30))
        self.label_289.setLayoutDirection(Qt.RightToLeft)
        self.label_289.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_290 = QLabel(self.groupBox_77)
        self.label_290.setObjectName(u"label_290")
        self.label_290.setGeometry(QRect(21, 261, 130, 30))
        sizePolicy3.setHeightForWidth(self.label_290.sizePolicy().hasHeightForWidth())
        self.label_290.setSizePolicy(sizePolicy3)
        self.label_290.setMinimumSize(QSize(130, 30))
        self.label_290.setLayoutDirection(Qt.RightToLeft)
        self.label_290.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.groupBox_46 = QGroupBox(self.scrollAreaWidgetContents_7)
        self.groupBox_46.setObjectName(u"groupBox_46")
        self.groupBox_46.setGeometry(QRect(30, 1450, 701, 521))
        self.groupBox_46.setMinimumSize(QSize(200, 0))
        self.groupBox_46.setMaximumSize(QSize(739, 16777215))
        self.label_285 = QLabel(self.groupBox_46)
        self.label_285.setObjectName(u"label_285")
        self.label_285.setGeometry(QRect(300, 480, 130, 16))
        sizePolicy3.setHeightForWidth(self.label_285.sizePolicy().hasHeightForWidth())
        self.label_285.setSizePolicy(sizePolicy3)
        self.label_285.setMinimumSize(QSize(130, 0))
        self.label_285.setLayoutDirection(Qt.RightToLeft)
        self.label_285.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_youma_style = QLineEdit(self.groupBox_46)
        self.lineEdit_youma_style.setObjectName(u"lineEdit_youma_style")
        self.lineEdit_youma_style.setGeometry(QRect(157, 352, 450, 30))
        self.lineEdit_youma_style.setMinimumSize(QSize(450, 30))
        self.lineEdit_youma_style.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.label_281 = QLabel(self.groupBox_46)
        self.label_281.setObjectName(u"label_281")
        self.label_281.setGeometry(QRect(21, 201, 130, 16))
        sizePolicy3.setHeightForWidth(self.label_281.sizePolicy().hasHeightForWidth())
        self.label_281.setSizePolicy(sizePolicy3)
        self.label_281.setMinimumSize(QSize(130, 0))
        self.label_281.setLayoutDirection(Qt.RightToLeft)
        self.label_281.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_189 = QLabel(self.groupBox_46)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setGeometry(QRect(21, 247, 130, 16))
        sizePolicy3.setHeightForWidth(self.label_189.sizePolicy().hasHeightForWidth())
        self.label_189.setSizePolicy(sizePolicy3)
        self.label_189.setMinimumSize(QSize(130, 0))
        self.label_189.setLayoutDirection(Qt.RightToLeft)
        self.label_189.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_117 = QLabel(self.groupBox_46)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setGeometry(QRect(157, 189, 523, 40))
        sizePolicy2.setHeightForWidth(self.label_117.sizePolicy().hasHeightForWidth())
        self.label_117.setSizePolicy(sizePolicy2)
        self.label_117.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_117.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_117.setWordWrap(True)
        self.label_117.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_282 = QLabel(self.groupBox_46)
        self.label_282.setObjectName(u"label_282")
        self.label_282.setGeometry(QRect(21, 99, 130, 16))
        sizePolicy3.setHeightForWidth(self.label_282.sizePolicy().hasHeightForWidth())
        self.label_282.setSizePolicy(sizePolicy3)
        self.label_282.setMinimumSize(QSize(130, 0))
        self.label_282.setLayoutDirection(Qt.RightToLeft)
        self.label_282.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_wuma_style = QLineEdit(self.groupBox_46)
        self.lineEdit_wuma_style.setObjectName(u"lineEdit_wuma_style")
        self.lineEdit_wuma_style.setGeometry(QRect(157, 240, 450, 30))
        self.lineEdit_wuma_style.setMinimumSize(QSize(450, 30))
        self.lineEdit_wuma_style.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.label_175 = QLabel(self.groupBox_46)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setGeometry(QRect(21, 155, 130, 16))
        sizePolicy3.setHeightForWidth(self.label_175.sizePolicy().hasHeightForWidth())
        self.label_175.setSizePolicy(sizePolicy3)
        self.label_175.setMinimumSize(QSize(130, 0))
        self.label_175.setLayoutDirection(Qt.RightToLeft)
        self.label_175.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_umr_style = QLineEdit(self.groupBox_46)
        self.lineEdit_umr_style.setObjectName(u"lineEdit_umr_style")
        self.lineEdit_umr_style.setGeometry(QRect(157, 36, 450, 30))
        self.lineEdit_umr_style.setMinimumSize(QSize(450, 30))
        self.lineEdit_umr_style.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.label_284 = QLabel(self.groupBox_46)
        self.label_284.setObjectName(u"label_284")
        self.label_284.setGeometry(QRect(21, 401, 130, 16))
        sizePolicy3.setHeightForWidth(self.label_284.sizePolicy().hasHeightForWidth())
        self.label_284.setSizePolicy(sizePolicy3)
        self.label_284.setMinimumSize(QSize(130, 0))
        self.label_284.setLayoutDirection(Qt.RightToLeft)
        self.label_284.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_190 = QLabel(self.groupBox_46)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setGeometry(QRect(21, 359, 130, 16))
        sizePolicy3.setHeightForWidth(self.label_190.sizePolicy().hasHeightForWidth())
        self.label_190.setSizePolicy(sizePolicy3)
        self.label_190.setMinimumSize(QSize(130, 0))
        self.label_190.setLayoutDirection(Qt.RightToLeft)
        self.label_190.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_137 = QLabel(self.groupBox_46)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setGeometry(QRect(157, 281, 523, 60))
        sizePolicy2.setHeightForWidth(self.label_137.sizePolicy().hasHeightForWidth())
        self.label_137.setSizePolicy(sizePolicy2)
        self.label_137.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_137.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_137.setWordWrap(True)
        self.label_137.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_116 = QLabel(self.groupBox_46)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setGeometry(QRect(157, 77, 523, 60))
        sizePolicy2.setHeightForWidth(self.label_116.sizePolicy().hasHeightForWidth())
        self.label_116.setSizePolicy(sizePolicy2)
        self.label_116.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_116.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_116.setWordWrap(True)
        self.label_116.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_283 = QLabel(self.groupBox_46)
        self.label_283.setObjectName(u"label_283")
        self.label_283.setGeometry(QRect(21, 303, 130, 16))
        sizePolicy3.setHeightForWidth(self.label_283.sizePolicy().hasHeightForWidth())
        self.label_283.setSizePolicy(sizePolicy3)
        self.label_283.setMinimumSize(QSize(130, 0))
        self.label_283.setLayoutDirection(Qt.RightToLeft)
        self.label_283.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_174 = QLabel(self.groupBox_46)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setGeometry(QRect(21, 43, 130, 16))
        sizePolicy3.setHeightForWidth(self.label_174.sizePolicy().hasHeightForWidth())
        self.label_174.setSizePolicy(sizePolicy3)
        self.label_174.setMinimumSize(QSize(130, 0))
        self.label_174.setLayoutDirection(Qt.RightToLeft)
        self.label_174.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_leak_style = QLineEdit(self.groupBox_46)
        self.lineEdit_leak_style.setObjectName(u"lineEdit_leak_style")
        self.lineEdit_leak_style.setGeometry(QRect(157, 148, 450, 30))
        self.lineEdit_leak_style.setMinimumSize(QSize(450, 30))
        self.lineEdit_leak_style.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.label_145 = QLabel(self.groupBox_46)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setGeometry(QRect(157, 393, 464, 32))
        sizePolicy2.setHeightForWidth(self.label_145.sizePolicy().hasHeightForWidth())
        self.label_145.setSizePolicy(sizePolicy2)
        self.label_145.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_235 = QLabel(self.groupBox_46)
        self.label_235.setObjectName(u"label_235")
        self.label_235.setGeometry(QRect(157, 479, 511, 16))
        sizePolicy2.setHeightForWidth(self.label_235.sizePolicy().hasHeightForWidth())
        self.label_235.setSizePolicy(sizePolicy2)
        self.label_235.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_234 = QLabel(self.groupBox_46)
        self.label_234.setObjectName(u"label_234")
        self.label_234.setGeometry(QRect(21, 437, 130, 30))
        sizePolicy3.setHeightForWidth(self.label_234.sizePolicy().hasHeightForWidth())
        self.label_234.setSizePolicy(sizePolicy3)
        self.label_234.setMinimumSize(QSize(130, 30))
        self.label_234.setLayoutDirection(Qt.LeftToRight)
        self.label_234.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_286 = QLabel(self.groupBox_46)
        self.label_286.setObjectName(u"label_286")
        self.label_286.setGeometry(QRect(21, 479, 130, 16))
        sizePolicy3.setHeightForWidth(self.label_286.sizePolicy().hasHeightForWidth())
        self.label_286.setSizePolicy(sizePolicy3)
        self.label_286.setMinimumSize(QSize(130, 0))
        self.label_286.setLayoutDirection(Qt.RightToLeft)
        self.label_286.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.checkBox_foldername_mosaic = QCheckBox(self.groupBox_46)
        self.checkBox_foldername_mosaic.setObjectName(u"checkBox_foldername_mosaic")
        self.checkBox_foldername_mosaic.setGeometry(QRect(160, 440, 100, 30))
        sizePolicy4.setHeightForWidth(self.checkBox_foldername_mosaic.sizePolicy().hasHeightForWidth())
        self.checkBox_foldername_mosaic.setSizePolicy(sizePolicy4)
        self.checkBox_foldername_mosaic.setMinimumSize(QSize(100, 30))
        self.checkBox_filename_mosaic = QCheckBox(self.groupBox_46)
        self.checkBox_filename_mosaic.setObjectName(u"checkBox_filename_mosaic")
        self.checkBox_filename_mosaic.setGeometry(QRect(410, 440, 206, 30))
        sizePolicy4.setHeightForWidth(self.checkBox_filename_mosaic.sizePolicy().hasHeightForWidth())
        self.checkBox_filename_mosaic.setSizePolicy(sizePolicy4)
        self.checkBox_filename_mosaic.setMinimumSize(QSize(100, 30))
        self.groupBox_37 = QGroupBox(self.scrollAreaWidgetContents_7)
        self.groupBox_37.setObjectName(u"groupBox_37")
        self.groupBox_37.setGeometry(QRect(30, 2450, 701, 121))
        self.groupBox_37.setMinimumSize(QSize(200, 0))
        self.groupBox_37.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_21 = QWidget(self.groupBox_37)
        self.gridLayoutWidget_21.setObjectName(u"gridLayoutWidget_21")
        self.gridLayoutWidget_21.setGeometry(QRect(60, 30, 621, 71))
        self.gridLayout_21 = QGridLayout(self.gridLayoutWidget_21)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.radioButton_pic_with_filename = QRadioButton(self.gridLayoutWidget_21)
        self.radioButton_pic_with_filename.setObjectName(u"radioButton_pic_with_filename")
        sizePolicy3.setHeightForWidth(self.radioButton_pic_with_filename.sizePolicy().hasHeightForWidth())
        self.radioButton_pic_with_filename.setSizePolicy(sizePolicy3)
        self.radioButton_pic_with_filename.setMinimumSize(QSize(166, 0))
        self.radioButton_pic_with_filename.setAutoExclusive(True)

        self.gridLayout_21.addWidget(self.radioButton_pic_with_filename, 0, 0, 1, 1)

        self.radioButton_pic_no_filename = QRadioButton(self.gridLayoutWidget_21)
        self.radioButton_pic_no_filename.setObjectName(u"radioButton_pic_no_filename")
        self.radioButton_pic_no_filename.setMinimumSize(QSize(80, 0))
        self.radioButton_pic_no_filename.setAutoExclusive(True)

        self.gridLayout_21.addWidget(self.radioButton_pic_no_filename, 1, 0, 1, 1)

        self.label_95 = QLabel(self.gridLayoutWidget_21)
        self.label_95.setObjectName(u"label_95")
        sizePolicy2.setHeightForWidth(self.label_95.sizePolicy().hasHeightForWidth())
        self.label_95.setSizePolicy(sizePolicy2)
        self.label_95.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_21.addWidget(self.label_95, 0, 1, 1, 1)

        self.label_96 = QLabel(self.gridLayoutWidget_21)
        self.label_96.setObjectName(u"label_96")
        sizePolicy2.setHeightForWidth(self.label_96.sizePolicy().hasHeightForWidth())
        self.label_96.setSizePolicy(sizePolicy2)
        self.label_96.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_21.addWidget(self.label_96, 1, 1, 1, 1)

        self.groupBox_62 = QGroupBox(self.scrollAreaWidgetContents_7)
        self.groupBox_62.setObjectName(u"groupBox_62")
        self.groupBox_62.setGeometry(QRect(30, 2590, 701, 121))
        self.groupBox_62.setMinimumSize(QSize(200, 0))
        self.groupBox_62.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_28 = QWidget(self.groupBox_62)
        self.gridLayoutWidget_28.setObjectName(u"gridLayoutWidget_28")
        self.gridLayoutWidget_28.setGeometry(QRect(60, 30, 621, 71))
        self.gridLayout_38 = QGridLayout(self.gridLayoutWidget_28)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(0, 0, 0, 0)
        self.radioButton_trailer_with_filename = QRadioButton(self.gridLayoutWidget_28)
        self.radioButton_trailer_with_filename.setObjectName(u"radioButton_trailer_with_filename")
        sizePolicy3.setHeightForWidth(self.radioButton_trailer_with_filename.sizePolicy().hasHeightForWidth())
        self.radioButton_trailer_with_filename.setSizePolicy(sizePolicy3)
        self.radioButton_trailer_with_filename.setMinimumSize(QSize(166, 0))
        self.radioButton_trailer_with_filename.setAutoExclusive(True)

        self.gridLayout_38.addWidget(self.radioButton_trailer_with_filename, 0, 0, 1, 1)

        self.radioButton_trailer_no_filename = QRadioButton(self.gridLayoutWidget_28)
        self.radioButton_trailer_no_filename.setObjectName(u"radioButton_trailer_no_filename")
        self.radioButton_trailer_no_filename.setMinimumSize(QSize(80, 0))
        self.radioButton_trailer_no_filename.setAutoExclusive(True)

        self.gridLayout_38.addWidget(self.radioButton_trailer_no_filename, 1, 0, 1, 1)

        self.label_115 = QLabel(self.gridLayoutWidget_28)
        self.label_115.setObjectName(u"label_115")
        sizePolicy2.setHeightForWidth(self.label_115.sizePolicy().hasHeightForWidth())
        self.label_115.setSizePolicy(sizePolicy2)
        self.label_115.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_38.addWidget(self.label_115, 0, 1, 1, 1)

        self.label_122 = QLabel(self.gridLayoutWidget_28)
        self.label_122.setObjectName(u"label_122")
        sizePolicy2.setHeightForWidth(self.label_122.sizePolicy().hasHeightForWidth())
        self.label_122.setSizePolicy(sizePolicy2)
        self.label_122.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_38.addWidget(self.label_122, 1, 1, 1, 1)

        self.groupBox_40 = QGroupBox(self.scrollAreaWidgetContents_7)
        self.groupBox_40.setObjectName(u"groupBox_40")
        self.groupBox_40.setGeometry(QRect(30, 650, 701, 411))
        self.groupBox_40.setMinimumSize(QSize(200, 0))
        self.groupBox_40.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_26 = QWidget(self.groupBox_40)
        self.gridLayoutWidget_26.setObjectName(u"gridLayoutWidget_26")
        self.gridLayoutWidget_26.setGeometry(QRect(20, 30, 661, 361))
        self.gridLayout_26 = QGridLayout(self.gridLayoutWidget_26)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_407 = QLabel(self.gridLayoutWidget_26)
        self.label_407.setObjectName(u"label_407")
        sizePolicy3.setHeightForWidth(self.label_407.sizePolicy().hasHeightForWidth())
        self.label_407.setSizePolicy(sizePolicy3)
        self.label_407.setMinimumSize(QSize(130, 30))
        self.label_407.setLayoutDirection(Qt.RightToLeft)
        self.label_407.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.label_407, 2, 0, 1, 1)

        self.label_146 = QLabel(self.gridLayoutWidget_26)
        self.label_146.setObjectName(u"label_146")
        sizePolicy2.setHeightForWidth(self.label_146.sizePolicy().hasHeightForWidth())
        self.label_146.setSizePolicy(sizePolicy2)
        self.label_146.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_26.addWidget(self.label_146, 5, 1, 1, 1)

        self.checkBox_number_del_num = QCheckBox(self.gridLayoutWidget_26)
        self.checkBox_number_del_num.setObjectName(u"checkBox_number_del_num")
        sizePolicy4.setHeightForWidth(self.checkBox_number_del_num.sizePolicy().hasHeightForWidth())
        self.checkBox_number_del_num.setSizePolicy(sizePolicy4)
        self.checkBox_number_del_num.setMinimumSize(QSize(100, 30))

        self.gridLayout_26.addWidget(self.checkBox_number_del_num, 1, 1, 1, 1)

        self.lineEdit_actor_no_name = QLineEdit(self.gridLayoutWidget_26)
        self.lineEdit_actor_no_name.setObjectName(u"lineEdit_actor_no_name")
        self.lineEdit_actor_no_name.setMinimumSize(QSize(450, 30))
        self.lineEdit_actor_no_name.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_26.addWidget(self.lineEdit_actor_no_name, 6, 1, 1, 1)

        self.checkBox_actor_del_char = QCheckBox(self.gridLayoutWidget_26)
        self.checkBox_actor_del_char.setObjectName(u"checkBox_actor_del_char")
        sizePolicy4.setHeightForWidth(self.checkBox_actor_del_char.sizePolicy().hasHeightForWidth())
        self.checkBox_actor_del_char.setSizePolicy(sizePolicy4)
        self.checkBox_actor_del_char.setMinimumSize(QSize(100, 30))

        self.gridLayout_26.addWidget(self.checkBox_actor_del_char, 2, 1, 1, 1)

        self.label_319 = QLabel(self.gridLayoutWidget_26)
        self.label_319.setObjectName(u"label_319")
        sizePolicy3.setHeightForWidth(self.label_319.sizePolicy().hasHeightForWidth())
        self.label_319.setSizePolicy(sizePolicy3)
        self.label_319.setMinimumSize(QSize(130, 30))
        self.label_319.setLayoutDirection(Qt.RightToLeft)
        self.label_319.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.label_319, 1, 0, 1, 1)

        self.label_197 = QLabel(self.gridLayoutWidget_26)
        self.label_197.setObjectName(u"label_197")
        sizePolicy3.setHeightForWidth(self.label_197.sizePolicy().hasHeightForWidth())
        self.label_197.setSizePolicy(sizePolicy3)
        self.label_197.setMinimumSize(QSize(130, 0))
        self.label_197.setLayoutDirection(Qt.RightToLeft)
        self.label_197.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.label_197, 4, 0, 1, 1)

        self.checkBox_title_del_actor = QCheckBox(self.gridLayoutWidget_26)
        self.checkBox_title_del_actor.setObjectName(u"checkBox_title_del_actor")

        self.gridLayout_26.addWidget(self.checkBox_title_del_actor, 0, 1, 1, 1)

        self.lineEdit_release_rule = QLineEdit(self.gridLayoutWidget_26)
        self.lineEdit_release_rule.setObjectName(u"lineEdit_release_rule")
        self.lineEdit_release_rule.setMinimumSize(QSize(450, 30))
        self.lineEdit_release_rule.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_26.addWidget(self.lineEdit_release_rule, 8, 1, 1, 1)

        self.label_276 = QLabel(self.gridLayoutWidget_26)
        self.label_276.setObjectName(u"label_276")
        sizePolicy3.setHeightForWidth(self.label_276.sizePolicy().hasHeightForWidth())
        self.label_276.setSizePolicy(sizePolicy3)
        self.label_276.setMinimumSize(QSize(130, 0))
        self.label_276.setLayoutDirection(Qt.RightToLeft)
        self.label_276.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.label_276, 8, 0, 1, 1)

        self.label_302 = QLabel(self.gridLayoutWidget_26)
        self.label_302.setObjectName(u"label_302")
        sizePolicy2.setHeightForWidth(self.label_302.sizePolicy().hasHeightForWidth())
        self.label_302.setSizePolicy(sizePolicy2)
        self.label_302.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_26.addWidget(self.label_302, 9, 1, 1, 1)

        self.lineEdit_suffix_sort = QLineEdit(self.gridLayoutWidget_26)
        self.lineEdit_suffix_sort.setObjectName(u"lineEdit_suffix_sort")
        self.lineEdit_suffix_sort.setMinimumSize(QSize(450, 30))
        self.lineEdit_suffix_sort.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_26.addWidget(self.lineEdit_suffix_sort, 4, 1, 1, 1)

        self.label_100 = QLabel(self.gridLayoutWidget_26)
        self.label_100.setObjectName(u"label_100")
        sizePolicy2.setHeightForWidth(self.label_100.sizePolicy().hasHeightForWidth())
        self.label_100.setSizePolicy(sizePolicy2)
        self.label_100.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_26.addWidget(self.label_100, 7, 1, 1, 1)

        self.label_320 = QLabel(self.gridLayoutWidget_26)
        self.label_320.setObjectName(u"label_320")
        sizePolicy3.setHeightForWidth(self.label_320.sizePolicy().hasHeightForWidth())
        self.label_320.setSizePolicy(sizePolicy3)
        self.label_320.setMinimumSize(QSize(130, 30))
        self.label_320.setLayoutDirection(Qt.RightToLeft)
        self.label_320.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.label_320, 0, 0, 1, 1)

        self.label_173 = QLabel(self.gridLayoutWidget_26)
        self.label_173.setObjectName(u"label_173")
        sizePolicy3.setHeightForWidth(self.label_173.sizePolicy().hasHeightForWidth())
        self.label_173.setSizePolicy(sizePolicy3)
        self.label_173.setMinimumSize(QSize(130, 0))
        self.label_173.setLayoutDirection(Qt.RightToLeft)
        self.label_173.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.label_173, 6, 0, 1, 1)

        self.checkBox_actor_fc2_seller = QCheckBox(self.gridLayoutWidget_26)
        self.checkBox_actor_fc2_seller.setObjectName(u"checkBox_actor_fc2_seller")
        sizePolicy4.setHeightForWidth(self.checkBox_actor_fc2_seller.sizePolicy().hasHeightForWidth())
        self.checkBox_actor_fc2_seller.setSizePolicy(sizePolicy4)
        self.checkBox_actor_fc2_seller.setMinimumSize(QSize(100, 30))

        self.gridLayout_26.addWidget(self.checkBox_actor_fc2_seller, 3, 1, 1, 1)

        self.groupBox_65 = QGroupBox(self.scrollAreaWidgetContents_7)
        self.groupBox_65.setObjectName(u"groupBox_65")
        self.groupBox_65.setGeometry(QRect(30, 2730, 701, 301))
        self.groupBox_65.setMinimumSize(QSize(200, 0))
        self.groupBox_65.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_35 = QWidget(self.groupBox_65)
        self.gridLayoutWidget_35.setObjectName(u"gridLayoutWidget_35")
        self.gridLayoutWidget_35.setGeometry(QRect(60, 30, 621, 77))
        self.gridLayout_43 = QGridLayout(self.gridLayoutWidget_35)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setContentsMargins(0, 0, 0, 0)
        self.radioButton_definition_height = QRadioButton(self.gridLayoutWidget_35)
        self.radioButton_definition_height.setObjectName(u"radioButton_definition_height")
        sizePolicy3.setHeightForWidth(self.radioButton_definition_height.sizePolicy().hasHeightForWidth())
        self.radioButton_definition_height.setSizePolicy(sizePolicy3)
        self.radioButton_definition_height.setMinimumSize(QSize(166, 0))
        self.radioButton_definition_height.setAutoExclusive(True)

        self.gridLayout_43.addWidget(self.radioButton_definition_height, 0, 0, 1, 1)

        self.radioButton_definition_hd = QRadioButton(self.gridLayoutWidget_35)
        self.radioButton_definition_hd.setObjectName(u"radioButton_definition_hd")
        self.radioButton_definition_hd.setMinimumSize(QSize(80, 0))
        self.radioButton_definition_hd.setAutoExclusive(True)

        self.gridLayout_43.addWidget(self.radioButton_definition_hd, 1, 0, 1, 1)

        self.label_329 = QLabel(self.gridLayoutWidget_35)
        self.label_329.setObjectName(u"label_329")
        sizePolicy2.setHeightForWidth(self.label_329.sizePolicy().hasHeightForWidth())
        self.label_329.setSizePolicy(sizePolicy2)
        self.label_329.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_43.addWidget(self.label_329, 0, 1, 1, 1)

        self.label_330 = QLabel(self.gridLayoutWidget_35)
        self.label_330.setObjectName(u"label_330")
        sizePolicy2.setHeightForWidth(self.label_330.sizePolicy().hasHeightForWidth())
        self.label_330.setSizePolicy(sizePolicy2)
        self.label_330.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_330.setWordWrap(True)

        self.gridLayout_43.addWidget(self.label_330, 1, 1, 1, 1)

        self.label_331 = QLabel(self.groupBox_65)
        self.label_331.setObjectName(u"label_331")
        self.label_331.setGeometry(QRect(60, 120, 621, 41))
        sizePolicy2.setHeightForWidth(self.label_331.sizePolicy().hasHeightForWidth())
        self.label_331.setSizePolicy(sizePolicy2)
        self.label_331.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_331.setWordWrap(True)
        self.frame_6 = QFrame(self.groupBox_65)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(30, 160, 661, 51))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.layoutWidget_26 = QWidget(self.frame_6)
        self.layoutWidget_26.setObjectName(u"layoutWidget_26")
        self.layoutWidget_26.setGeometry(QRect(140, 10, 471, 32))
        self.horizontalLayout_112 = QHBoxLayout(self.layoutWidget_26)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.radioButton_videosize_video = QRadioButton(self.layoutWidget_26)
        self.radioButton_videosize_video.setObjectName(u"radioButton_videosize_video")
        self.radioButton_videosize_video.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_112.addWidget(self.radioButton_videosize_video)

        self.radioButton_videosize_path = QRadioButton(self.layoutWidget_26)
        self.radioButton_videosize_path.setObjectName(u"radioButton_videosize_path")

        self.horizontalLayout_112.addWidget(self.radioButton_videosize_path)

        self.radioButton_videosize_none = QRadioButton(self.layoutWidget_26)
        self.radioButton_videosize_none.setObjectName(u"radioButton_videosize_none")
        sizePolicy3.setHeightForWidth(self.radioButton_videosize_none.sizePolicy().hasHeightForWidth())
        self.radioButton_videosize_none.setSizePolicy(sizePolicy3)

        self.horizontalLayout_112.addWidget(self.radioButton_videosize_none)

        self.label_332 = QLabel(self.frame_6)
        self.label_332.setObjectName(u"label_332")
        self.label_332.setGeometry(QRect(0, 20, 130, 16))
        sizePolicy3.setHeightForWidth(self.label_332.sizePolicy().hasHeightForWidth())
        self.label_332.setSizePolicy(sizePolicy3)
        self.label_332.setMinimumSize(QSize(130, 0))
        self.label_332.setLayoutDirection(Qt.RightToLeft)
        self.label_332.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_357 = QLabel(self.groupBox_65)
        self.label_357.setObjectName(u"label_357")
        self.label_357.setGeometry(QRect(31, 218, 130, 30))
        sizePolicy3.setHeightForWidth(self.label_357.sizePolicy().hasHeightForWidth())
        self.label_357.setSizePolicy(sizePolicy3)
        self.label_357.setMinimumSize(QSize(130, 30))
        self.label_357.setLayoutDirection(Qt.LeftToRight)
        self.label_357.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.checkBox_filename_4k = QCheckBox(self.groupBox_65)
        self.checkBox_filename_4k.setObjectName(u"checkBox_filename_4k")
        self.checkBox_filename_4k.setGeometry(QRect(420, 221, 206, 30))
        sizePolicy4.setHeightForWidth(self.checkBox_filename_4k.sizePolicy().hasHeightForWidth())
        self.checkBox_filename_4k.setSizePolicy(sizePolicy4)
        self.checkBox_filename_4k.setMinimumSize(QSize(100, 30))
        self.label_358 = QLabel(self.groupBox_65)
        self.label_358.setObjectName(u"label_358")
        self.label_358.setGeometry(QRect(167, 260, 511, 16))
        sizePolicy2.setHeightForWidth(self.label_358.sizePolicy().hasHeightForWidth())
        self.label_358.setSizePolicy(sizePolicy2)
        self.label_358.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.checkBox_foldername_4k = QCheckBox(self.groupBox_65)
        self.checkBox_foldername_4k.setObjectName(u"checkBox_foldername_4k")
        self.checkBox_foldername_4k.setGeometry(QRect(170, 221, 100, 30))
        sizePolicy4.setHeightForWidth(self.checkBox_foldername_4k.sizePolicy().hasHeightForWidth())
        self.checkBox_foldername_4k.setSizePolicy(sizePolicy4)
        self.checkBox_foldername_4k.setMinimumSize(QSize(100, 30))
        self.groupBox_67 = QGroupBox(self.scrollAreaWidgetContents_7)
        self.groupBox_67.setObjectName(u"groupBox_67")
        self.groupBox_67.setGeometry(QRect(30, 3050, 701, 271))
        self.groupBox_67.setMinimumSize(QSize(200, 0))
        self.groupBox_67.setMaximumSize(QSize(739, 16777215))
        self.label_353 = QLabel(self.groupBox_67)
        self.label_353.setObjectName(u"label_353")
        self.label_353.setGeometry(QRect(40, 30, 130, 30))
        sizePolicy3.setHeightForWidth(self.label_353.sizePolicy().hasHeightForWidth())
        self.label_353.setSizePolicy(sizePolicy3)
        self.label_353.setMinimumSize(QSize(130, 30))
        self.label_353.setLayoutDirection(Qt.LeftToRight)
        self.label_353.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_352 = QLabel(self.groupBox_67)
        self.label_352.setObjectName(u"label_352")
        self.label_352.setGeometry(QRect(50, 60, 621, 131))
        sizePolicy2.setHeightForWidth(self.label_352.sizePolicy().hasHeightForWidth())
        self.label_352.setSizePolicy(sizePolicy2)
        self.label_352.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_352.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_352.setOpenExternalLinks(True)
        self.label_351 = QLabel(self.groupBox_67)
        self.label_351.setObjectName(u"label_351")
        self.label_351.setGeometry(QRect(50, 220, 611, 16))
        sizePolicy2.setHeightForWidth(self.label_351.sizePolicy().hasHeightForWidth())
        self.label_351.setSizePolicy(sizePolicy2)
        self.label_351.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_354 = QLabel(self.groupBox_67)
        self.label_354.setObjectName(u"label_354")
        self.label_354.setGeometry(QRect(40, 190, 130, 30))
        sizePolicy3.setHeightForWidth(self.label_354.sizePolicy().hasHeightForWidth())
        self.label_354.setSizePolicy(sizePolicy3)
        self.label_354.setMinimumSize(QSize(130, 30))
        self.label_354.setLayoutDirection(Qt.LeftToRight)
        self.label_354.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.scrollArea_11 = QScrollArea(self.tab_6)
        self.scrollArea_11.setObjectName(u"scrollArea_11")
        self.scrollArea_11.setGeometry(QRect(0, 0, 796, 658))
        self.scrollArea_11.setFrameShape(QFrame.Box)
        self.scrollArea_11.setLineWidth(0)
        self.scrollArea_11.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_11.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_11.setWidgetResizable(False)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 760, 2100))
        self.groupBox_79 = QGroupBox(self.scrollAreaWidgetContents_11)
        self.groupBox_79.setObjectName(u"groupBox_79")
        self.groupBox_79.setGeometry(QRect(30, 20, 701, 181))
        self.groupBox_79.setMinimumSize(QSize(200, 0))
        self.groupBox_79.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_2 = QWidget(self.groupBox_79)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 30, 661, 141))
        self.gridLayout_32 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_81 = QLabel(self.layoutWidget_2)
        self.label_81.setObjectName(u"label_81")
        sizePolicy3.setHeightForWidth(self.label_81.sizePolicy().hasHeightForWidth())
        self.label_81.setSizePolicy(sizePolicy3)
        self.label_81.setMinimumSize(QSize(130, 30))
        self.label_81.setLayoutDirection(Qt.LeftToRight)
        self.label_81.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_32.addWidget(self.label_81, 0, 0, 1, 1)

        self.label_60 = QLabel(self.layoutWidget_2)
        self.label_60.setObjectName(u"label_60")
        sizePolicy2.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy2)
        self.label_60.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_32.addWidget(self.label_60, 3, 1, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.checkBox_youdao = QCheckBox(self.layoutWidget_2)
        self.checkBox_youdao.setObjectName(u"checkBox_youdao")
        self.checkBox_youdao.setMinimumSize(QSize(93, 30))

        self.horizontalLayout_20.addWidget(self.checkBox_youdao)

        self.checkBox_google = QCheckBox(self.layoutWidget_2)
        self.checkBox_google.setObjectName(u"checkBox_google")
        self.checkBox_google.setMinimumSize(QSize(93, 30))

        self.horizontalLayout_20.addWidget(self.checkBox_google)

        self.checkBox_deepl = QCheckBox(self.layoutWidget_2)
        self.checkBox_deepl.setObjectName(u"checkBox_deepl")
        self.checkBox_deepl.setMinimumSize(QSize(93, 30))

        self.horizontalLayout_20.addWidget(self.checkBox_deepl)


        self.gridLayout_32.addLayout(self.horizontalLayout_20, 0, 1, 1, 1)

        self.lineEdit_deepl_key = QLineEdit(self.layoutWidget_2)
        self.lineEdit_deepl_key.setObjectName(u"lineEdit_deepl_key")
        sizePolicy2.setHeightForWidth(self.lineEdit_deepl_key.sizePolicy().hasHeightForWidth())
        self.lineEdit_deepl_key.setSizePolicy(sizePolicy2)
        self.lineEdit_deepl_key.setMinimumSize(QSize(300, 30))
        self.lineEdit_deepl_key.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_32.addWidget(self.lineEdit_deepl_key, 2, 1, 1, 1)

        self.label_80 = QLabel(self.layoutWidget_2)
        self.label_80.setObjectName(u"label_80")
        sizePolicy3.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy3)
        self.label_80.setMinimumSize(QSize(130, 30))
        self.label_80.setLayoutDirection(Qt.LeftToRight)
        self.label_80.setFrameShape(QFrame.NoFrame)
        self.label_80.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_32.addWidget(self.label_80, 2, 0, 1, 1)

        self.label_164 = QLabel(self.layoutWidget_2)
        self.label_164.setObjectName(u"label_164")
        sizePolicy2.setHeightForWidth(self.label_164.sizePolicy().hasHeightForWidth())
        self.label_164.setSizePolicy(sizePolicy2)
        self.label_164.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_32.addWidget(self.label_164, 1, 1, 1, 1)

        self.groupBox_82 = QGroupBox(self.scrollAreaWidgetContents_11)
        self.groupBox_82.setObjectName(u"groupBox_82")
        self.groupBox_82.setGeometry(QRect(30, 220, 701, 251))
        self.groupBox_82.setMinimumSize(QSize(200, 0))
        self.groupBox_82.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_9 = QWidget(self.groupBox_82)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(20, 30, 661, 211))
        self.gridLayout_45 = QGridLayout(self.layoutWidget_9)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_title_sehua = QCheckBox(self.layoutWidget_9)
        self.checkBox_title_sehua.setObjectName(u"checkBox_title_sehua")

        self.horizontalLayout_2.addWidget(self.checkBox_title_sehua)

        self.checkBox_title_yesjav = QCheckBox(self.layoutWidget_9)
        self.checkBox_title_yesjav.setObjectName(u"checkBox_title_yesjav")

        self.horizontalLayout_2.addWidget(self.checkBox_title_yesjav)

        self.checkBox_title_translate = QCheckBox(self.layoutWidget_9)
        self.checkBox_title_translate.setObjectName(u"checkBox_title_translate")

        self.horizontalLayout_2.addWidget(self.checkBox_title_translate)


        self.gridLayout_45.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)

        self.label_242 = QLabel(self.layoutWidget_9)
        self.label_242.setObjectName(u"label_242")
        sizePolicy3.setHeightForWidth(self.label_242.sizePolicy().hasHeightForWidth())
        self.label_242.setSizePolicy(sizePolicy3)
        self.label_242.setMinimumSize(QSize(130, 30))
        self.label_242.setLayoutDirection(Qt.LeftToRight)
        self.label_242.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_45.addWidget(self.label_242, 0, 0, 1, 1)

        self.label_74 = QLabel(self.layoutWidget_9)
        self.label_74.setObjectName(u"label_74")
        sizePolicy2.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy2)
        self.label_74.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_45.addWidget(self.label_74, 1, 1, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.radioButton_title_zh_cn = QRadioButton(self.layoutWidget_9)
        self.radioButton_title_zh_cn.setObjectName(u"radioButton_title_zh_cn")
        self.radioButton_title_zh_cn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_18.addWidget(self.radioButton_title_zh_cn)

        self.radioButton_title_zh_tw = QRadioButton(self.layoutWidget_9)
        self.radioButton_title_zh_tw.setObjectName(u"radioButton_title_zh_tw")

        self.horizontalLayout_18.addWidget(self.radioButton_title_zh_tw)

        self.radioButton_title_jp = QRadioButton(self.layoutWidget_9)
        self.radioButton_title_jp.setObjectName(u"radioButton_title_jp")

        self.horizontalLayout_18.addWidget(self.radioButton_title_jp)


        self.gridLayout_45.addLayout(self.horizontalLayout_18, 0, 1, 1, 1)

        self.label_236 = QLabel(self.layoutWidget_9)
        self.label_236.setObjectName(u"label_236")
        sizePolicy2.setHeightForWidth(self.label_236.sizePolicy().hasHeightForWidth())
        self.label_236.setSizePolicy(sizePolicy2)
        self.label_236.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_45.addWidget(self.label_236, 5, 1, 1, 1)

        self.label_160 = QLabel(self.layoutWidget_9)
        self.label_160.setObjectName(u"label_160")
        sizePolicy2.setHeightForWidth(self.label_160.sizePolicy().hasHeightForWidth())
        self.label_160.setSizePolicy(sizePolicy2)
        self.label_160.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_45.addWidget(self.label_160, 3, 1, 1, 1)

        self.checkBox_title_sehua_2 = QCheckBox(self.layoutWidget_9)
        self.checkBox_title_sehua_2.setObjectName(u"checkBox_title_sehua_2")

        self.gridLayout_45.addWidget(self.checkBox_title_sehua_2, 4, 1, 1, 1)

        self.label_244 = QLabel(self.layoutWidget_9)
        self.label_244.setObjectName(u"label_244")
        sizePolicy3.setHeightForWidth(self.label_244.sizePolicy().hasHeightForWidth())
        self.label_244.setSizePolicy(sizePolicy3)
        self.label_244.setMinimumSize(QSize(130, 30))
        self.label_244.setLayoutDirection(Qt.LeftToRight)
        self.label_244.setFrameShape(QFrame.NoFrame)
        self.label_244.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_45.addWidget(self.label_244, 2, 0, 1, 1)

        self.groupBox_83 = QGroupBox(self.scrollAreaWidgetContents_11)
        self.groupBox_83.setObjectName(u"groupBox_83")
        self.groupBox_83.setGeometry(QRect(30, 490, 701, 221))
        self.groupBox_83.setMinimumSize(QSize(200, 0))
        self.groupBox_83.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_13 = QWidget(self.groupBox_83)
        self.layoutWidget_13.setObjectName(u"layoutWidget_13")
        self.layoutWidget_13.setGeometry(QRect(20, 30, 661, 131))
        self.gridLayout_48 = QGridLayout(self.layoutWidget_13)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_133 = QLabel(self.layoutWidget_13)
        self.label_133.setObjectName(u"label_133")
        sizePolicy3.setHeightForWidth(self.label_133.sizePolicy().hasHeightForWidth())
        self.label_133.setSizePolicy(sizePolicy3)
        self.label_133.setMinimumSize(QSize(130, 30))
        self.label_133.setLayoutDirection(Qt.LeftToRight)
        self.label_133.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_48.addWidget(self.label_133, 0, 0, 1, 1)

        self.label_176 = QLabel(self.layoutWidget_13)
        self.label_176.setObjectName(u"label_176")
        sizePolicy2.setHeightForWidth(self.label_176.sizePolicy().hasHeightForWidth())
        self.label_176.setSizePolicy(sizePolicy2)
        self.label_176.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_48.addWidget(self.label_176, 2, 1, 1, 1)

        self.label_166 = QLabel(self.layoutWidget_13)
        self.label_166.setObjectName(u"label_166")
        sizePolicy3.setHeightForWidth(self.label_166.sizePolicy().hasHeightForWidth())
        self.label_166.setSizePolicy(sizePolicy3)
        self.label_166.setMinimumSize(QSize(130, 30))
        self.label_166.setLayoutDirection(Qt.LeftToRight)
        self.label_166.setFrameShape(QFrame.NoFrame)
        self.label_166.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_48.addWidget(self.label_166, 1, 0, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.radioButton_outline_zh_cn = QRadioButton(self.layoutWidget_13)
        self.radioButton_outline_zh_cn.setObjectName(u"radioButton_outline_zh_cn")
        self.radioButton_outline_zh_cn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_22.addWidget(self.radioButton_outline_zh_cn)

        self.radioButton_outline_zh_tw = QRadioButton(self.layoutWidget_13)
        self.radioButton_outline_zh_tw.setObjectName(u"radioButton_outline_zh_tw")

        self.horizontalLayout_22.addWidget(self.radioButton_outline_zh_tw)

        self.radioButton_outline_jp = QRadioButton(self.layoutWidget_13)
        self.radioButton_outline_jp.setObjectName(u"radioButton_outline_jp")

        self.horizontalLayout_22.addWidget(self.radioButton_outline_jp)


        self.gridLayout_48.addLayout(self.horizontalLayout_22, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox_outline_translate = QCheckBox(self.layoutWidget_13)
        self.checkBox_outline_translate.setObjectName(u"checkBox_outline_translate")

        self.horizontalLayout.addWidget(self.checkBox_outline_translate)

        self.checkBox_show_translate_from = QCheckBox(self.layoutWidget_13)
        self.checkBox_show_translate_from.setObjectName(u"checkBox_show_translate_from")

        self.horizontalLayout.addWidget(self.checkBox_show_translate_from)


        self.gridLayout_48.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.frame_5 = QFrame(self.groupBox_83)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(20, 160, 661, 51))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.layoutWidget_24 = QWidget(self.frame_5)
        self.layoutWidget_24.setObjectName(u"layoutWidget_24")
        self.layoutWidget_24.setGeometry(QRect(140, 10, 521, 32))
        self.horizontalLayout_111 = QHBoxLayout(self.layoutWidget_24)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.radioButton_trans_show_zh_jp = QRadioButton(self.layoutWidget_24)
        self.radioButton_trans_show_zh_jp.setObjectName(u"radioButton_trans_show_zh_jp")

        self.horizontalLayout_111.addWidget(self.radioButton_trans_show_zh_jp)

        self.radioButton_trans_show_jp_zh = QRadioButton(self.layoutWidget_24)
        self.radioButton_trans_show_jp_zh.setObjectName(u"radioButton_trans_show_jp_zh")
        self.radioButton_trans_show_jp_zh.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_111.addWidget(self.radioButton_trans_show_jp_zh)

        self.radioButton_trans_show_one = QRadioButton(self.layoutWidget_24)
        self.radioButton_trans_show_one.setObjectName(u"radioButton_trans_show_one")

        self.horizontalLayout_111.addWidget(self.radioButton_trans_show_one)

        self.label_328 = QLabel(self.frame_5)
        self.label_328.setObjectName(u"label_328")
        self.label_328.setGeometry(QRect(0, 20, 130, 16))
        sizePolicy3.setHeightForWidth(self.label_328.sizePolicy().hasHeightForWidth())
        self.label_328.setSizePolicy(sizePolicy3)
        self.label_328.setMinimumSize(QSize(130, 0))
        self.label_328.setLayoutDirection(Qt.RightToLeft)
        self.label_328.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.groupBox_84 = QGroupBox(self.scrollAreaWidgetContents_11)
        self.groupBox_84.setObjectName(u"groupBox_84")
        self.groupBox_84.setGeometry(QRect(30, 730, 701, 421))
        self.groupBox_84.setMinimumSize(QSize(200, 0))
        self.groupBox_84.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_20 = QWidget(self.groupBox_84)
        self.layoutWidget_20.setObjectName(u"layoutWidget_20")
        self.layoutWidget_20.setGeometry(QRect(20, 30, 661, 381))
        self.gridLayout_50 = QGridLayout(self.layoutWidget_20)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_250 = QLabel(self.layoutWidget_20)
        self.label_250.setObjectName(u"label_250")
        sizePolicy3.setHeightForWidth(self.label_250.sizePolicy().hasHeightForWidth())
        self.label_250.setSizePolicy(sizePolicy3)
        self.label_250.setMinimumSize(QSize(130, 30))
        self.label_250.setLayoutDirection(Qt.LeftToRight)
        self.label_250.setFrameShape(QFrame.NoFrame)
        self.label_250.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_50.addWidget(self.label_250, 1, 0, 1, 1)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.radioButton_actor_zh_cn = QRadioButton(self.layoutWidget_20)
        self.radioButton_actor_zh_cn.setObjectName(u"radioButton_actor_zh_cn")
        self.radioButton_actor_zh_cn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_35.addWidget(self.radioButton_actor_zh_cn)

        self.radioButton_actor_zh_tw = QRadioButton(self.layoutWidget_20)
        self.radioButton_actor_zh_tw.setObjectName(u"radioButton_actor_zh_tw")

        self.horizontalLayout_35.addWidget(self.radioButton_actor_zh_tw)

        self.radioButton_actor_jp = QRadioButton(self.layoutWidget_20)
        self.radioButton_actor_jp.setObjectName(u"radioButton_actor_jp")

        self.horizontalLayout_35.addWidget(self.radioButton_actor_jp)


        self.gridLayout_50.addLayout(self.horizontalLayout_35, 0, 1, 1, 1)

        self.label_249 = QLabel(self.layoutWidget_20)
        self.label_249.setObjectName(u"label_249")
        sizePolicy4.setHeightForWidth(self.label_249.sizePolicy().hasHeightForWidth())
        self.label_249.setSizePolicy(sizePolicy4)
        self.label_249.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_249.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_249.setWordWrap(True)
        self.label_249.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_50.addWidget(self.label_249, 2, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkBox_actor_realname = QCheckBox(self.layoutWidget_20)
        self.checkBox_actor_realname.setObjectName(u"checkBox_actor_realname")

        self.horizontalLayout_8.addWidget(self.checkBox_actor_realname)

        self.checkBox_actor_translate = QCheckBox(self.layoutWidget_20)
        self.checkBox_actor_translate.setObjectName(u"checkBox_actor_translate")

        self.horizontalLayout_8.addWidget(self.checkBox_actor_translate)


        self.gridLayout_50.addLayout(self.horizontalLayout_8, 1, 1, 1, 1)

        self.label_248 = QLabel(self.layoutWidget_20)
        self.label_248.setObjectName(u"label_248")
        sizePolicy3.setHeightForWidth(self.label_248.sizePolicy().hasHeightForWidth())
        self.label_248.setSizePolicy(sizePolicy3)
        self.label_248.setMinimumSize(QSize(130, 30))
        self.label_248.setLayoutDirection(Qt.LeftToRight)
        self.label_248.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_50.addWidget(self.label_248, 0, 0, 1, 1)

        self.groupBox_85 = QGroupBox(self.scrollAreaWidgetContents_11)
        self.groupBox_85.setObjectName(u"groupBox_85")
        self.groupBox_85.setGeometry(QRect(30, 1170, 701, 151))
        self.groupBox_85.setMinimumSize(QSize(200, 0))
        self.groupBox_85.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_21 = QWidget(self.groupBox_85)
        self.layoutWidget_21.setObjectName(u"layoutWidget_21")
        self.layoutWidget_21.setGeometry(QRect(20, 30, 661, 111))
        self.gridLayout_51 = QGridLayout(self.layoutWidget_21)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.gridLayout_51.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.radioButton_tag_zh_cn = QRadioButton(self.layoutWidget_21)
        self.radioButton_tag_zh_cn.setObjectName(u"radioButton_tag_zh_cn")
        self.radioButton_tag_zh_cn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_36.addWidget(self.radioButton_tag_zh_cn)

        self.radioButton_tag_zh_tw = QRadioButton(self.layoutWidget_21)
        self.radioButton_tag_zh_tw.setObjectName(u"radioButton_tag_zh_tw")

        self.horizontalLayout_36.addWidget(self.radioButton_tag_zh_tw)

        self.radioButton_tag_jp = QRadioButton(self.layoutWidget_21)
        self.radioButton_tag_jp.setObjectName(u"radioButton_tag_jp")

        self.horizontalLayout_36.addWidget(self.radioButton_tag_jp)


        self.gridLayout_51.addLayout(self.horizontalLayout_36, 0, 1, 1, 1)

        self.label_165 = QLabel(self.layoutWidget_21)
        self.label_165.setObjectName(u"label_165")
        sizePolicy2.setHeightForWidth(self.label_165.sizePolicy().hasHeightForWidth())
        self.label_165.setSizePolicy(sizePolicy2)
        self.label_165.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_165.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_51.addWidget(self.label_165, 2, 1, 1, 1)

        self.checkBox_tag_translate = QCheckBox(self.layoutWidget_21)
        self.checkBox_tag_translate.setObjectName(u"checkBox_tag_translate")

        self.gridLayout_51.addWidget(self.checkBox_tag_translate, 1, 1, 1, 1)

        self.label_251 = QLabel(self.layoutWidget_21)
        self.label_251.setObjectName(u"label_251")
        sizePolicy3.setHeightForWidth(self.label_251.sizePolicy().hasHeightForWidth())
        self.label_251.setSizePolicy(sizePolicy3)
        self.label_251.setMinimumSize(QSize(130, 30))
        self.label_251.setLayoutDirection(Qt.LeftToRight)
        self.label_251.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_51.addWidget(self.label_251, 0, 0, 1, 1)

        self.label_253 = QLabel(self.layoutWidget_21)
        self.label_253.setObjectName(u"label_253")
        sizePolicy3.setHeightForWidth(self.label_253.sizePolicy().hasHeightForWidth())
        self.label_253.setSizePolicy(sizePolicy3)
        self.label_253.setMinimumSize(QSize(130, 30))
        self.label_253.setLayoutDirection(Qt.LeftToRight)
        self.label_253.setFrameShape(QFrame.NoFrame)
        self.label_253.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_51.addWidget(self.label_253, 1, 0, 1, 1)

        self.groupBox_86 = QGroupBox(self.scrollAreaWidgetContents_11)
        self.groupBox_86.setObjectName(u"groupBox_86")
        self.groupBox_86.setGeometry(QRect(30, 1340, 701, 151))
        self.groupBox_86.setMinimumSize(QSize(200, 0))
        self.groupBox_86.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_23 = QWidget(self.groupBox_86)
        self.layoutWidget_23.setObjectName(u"layoutWidget_23")
        self.layoutWidget_23.setGeometry(QRect(20, 30, 661, 111))
        self.gridLayout_53 = QGridLayout(self.layoutWidget_23)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.gridLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_255 = QLabel(self.layoutWidget_23)
        self.label_255.setObjectName(u"label_255")
        sizePolicy3.setHeightForWidth(self.label_255.sizePolicy().hasHeightForWidth())
        self.label_255.setSizePolicy(sizePolicy3)
        self.label_255.setMinimumSize(QSize(130, 30))
        self.label_255.setLayoutDirection(Qt.LeftToRight)
        self.label_255.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_53.addWidget(self.label_255, 0, 0, 1, 1)

        self.label_256 = QLabel(self.layoutWidget_23)
        self.label_256.setObjectName(u"label_256")
        sizePolicy3.setHeightForWidth(self.label_256.sizePolicy().hasHeightForWidth())
        self.label_256.setSizePolicy(sizePolicy3)
        self.label_256.setMinimumSize(QSize(130, 30))
        self.label_256.setLayoutDirection(Qt.LeftToRight)
        self.label_256.setFrameShape(QFrame.NoFrame)
        self.label_256.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_53.addWidget(self.label_256, 1, 0, 1, 1)

        self.label_245 = QLabel(self.layoutWidget_23)
        self.label_245.setObjectName(u"label_245")
        sizePolicy2.setHeightForWidth(self.label_245.sizePolicy().hasHeightForWidth())
        self.label_245.setSizePolicy(sizePolicy2)
        self.label_245.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_245.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_53.addWidget(self.label_245, 2, 1, 1, 1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.radioButton_series_zh_cn = QRadioButton(self.layoutWidget_23)
        self.radioButton_series_zh_cn.setObjectName(u"radioButton_series_zh_cn")
        self.radioButton_series_zh_cn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_27.addWidget(self.radioButton_series_zh_cn)

        self.radioButton_series_zh_tw = QRadioButton(self.layoutWidget_23)
        self.radioButton_series_zh_tw.setObjectName(u"radioButton_series_zh_tw")

        self.horizontalLayout_27.addWidget(self.radioButton_series_zh_tw)

        self.radioButton_series_jp = QRadioButton(self.layoutWidget_23)
        self.radioButton_series_jp.setObjectName(u"radioButton_series_jp")

        self.horizontalLayout_27.addWidget(self.radioButton_series_jp)


        self.gridLayout_53.addLayout(self.horizontalLayout_27, 0, 1, 1, 1)

        self.checkBox_series_translate = QCheckBox(self.layoutWidget_23)
        self.checkBox_series_translate.setObjectName(u"checkBox_series_translate")

        self.gridLayout_53.addWidget(self.checkBox_series_translate, 1, 1, 1, 1)

        self.groupBox_87 = QGroupBox(self.scrollAreaWidgetContents_11)
        self.groupBox_87.setObjectName(u"groupBox_87")
        self.groupBox_87.setGeometry(QRect(30, 1510, 701, 151))
        self.groupBox_87.setMinimumSize(QSize(200, 0))
        self.groupBox_87.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_25 = QWidget(self.groupBox_87)
        self.layoutWidget_25.setObjectName(u"layoutWidget_25")
        self.layoutWidget_25.setGeometry(QRect(20, 30, 661, 111))
        self.gridLayout_55 = QGridLayout(self.layoutWidget_25)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.gridLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_259 = QLabel(self.layoutWidget_25)
        self.label_259.setObjectName(u"label_259")
        sizePolicy3.setHeightForWidth(self.label_259.sizePolicy().hasHeightForWidth())
        self.label_259.setSizePolicy(sizePolicy3)
        self.label_259.setMinimumSize(QSize(130, 30))
        self.label_259.setLayoutDirection(Qt.LeftToRight)
        self.label_259.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_259, 0, 0, 1, 1)

        self.label_260 = QLabel(self.layoutWidget_25)
        self.label_260.setObjectName(u"label_260")
        sizePolicy3.setHeightForWidth(self.label_260.sizePolicy().hasHeightForWidth())
        self.label_260.setSizePolicy(sizePolicy3)
        self.label_260.setMinimumSize(QSize(130, 30))
        self.label_260.setLayoutDirection(Qt.LeftToRight)
        self.label_260.setFrameShape(QFrame.NoFrame)
        self.label_260.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_260, 1, 0, 1, 1)

        self.label_247 = QLabel(self.layoutWidget_25)
        self.label_247.setObjectName(u"label_247")
        sizePolicy2.setHeightForWidth(self.label_247.sizePolicy().hasHeightForWidth())
        self.label_247.setSizePolicy(sizePolicy2)
        self.label_247.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_247.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_247, 2, 1, 1, 1)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.radioButton_studio_zh_cn = QRadioButton(self.layoutWidget_25)
        self.radioButton_studio_zh_cn.setObjectName(u"radioButton_studio_zh_cn")
        self.radioButton_studio_zh_cn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_39.addWidget(self.radioButton_studio_zh_cn)

        self.radioButton_studio_zh_tw = QRadioButton(self.layoutWidget_25)
        self.radioButton_studio_zh_tw.setObjectName(u"radioButton_studio_zh_tw")

        self.horizontalLayout_39.addWidget(self.radioButton_studio_zh_tw)

        self.radioButton_studio_jp = QRadioButton(self.layoutWidget_25)
        self.radioButton_studio_jp.setObjectName(u"radioButton_studio_jp")

        self.horizontalLayout_39.addWidget(self.radioButton_studio_jp)


        self.gridLayout_55.addLayout(self.horizontalLayout_39, 0, 1, 1, 1)

        self.checkBox_studio_translate = QCheckBox(self.layoutWidget_25)
        self.checkBox_studio_translate.setObjectName(u"checkBox_studio_translate")

        self.gridLayout_55.addWidget(self.checkBox_studio_translate, 1, 1, 1, 1)

        self.groupBox_88 = QGroupBox(self.scrollAreaWidgetContents_11)
        self.groupBox_88.setObjectName(u"groupBox_88")
        self.groupBox_88.setGeometry(QRect(30, 1680, 701, 151))
        self.groupBox_88.setMinimumSize(QSize(200, 0))
        self.groupBox_88.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_27 = QWidget(self.groupBox_88)
        self.layoutWidget_27.setObjectName(u"layoutWidget_27")
        self.layoutWidget_27.setGeometry(QRect(20, 30, 661, 111))
        self.gridLayout_57 = QGridLayout(self.layoutWidget_27)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.gridLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_264 = QLabel(self.layoutWidget_27)
        self.label_264.setObjectName(u"label_264")
        sizePolicy3.setHeightForWidth(self.label_264.sizePolicy().hasHeightForWidth())
        self.label_264.setSizePolicy(sizePolicy3)
        self.label_264.setMinimumSize(QSize(130, 30))
        self.label_264.setLayoutDirection(Qt.LeftToRight)
        self.label_264.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_57.addWidget(self.label_264, 0, 0, 1, 1)

        self.label_265 = QLabel(self.layoutWidget_27)
        self.label_265.setObjectName(u"label_265")
        sizePolicy3.setHeightForWidth(self.label_265.sizePolicy().hasHeightForWidth())
        self.label_265.setSizePolicy(sizePolicy3)
        self.label_265.setMinimumSize(QSize(130, 30))
        self.label_265.setLayoutDirection(Qt.LeftToRight)
        self.label_265.setFrameShape(QFrame.NoFrame)
        self.label_265.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_57.addWidget(self.label_265, 1, 0, 1, 1)

        self.label_266 = QLabel(self.layoutWidget_27)
        self.label_266.setObjectName(u"label_266")
        sizePolicy2.setHeightForWidth(self.label_266.sizePolicy().hasHeightForWidth())
        self.label_266.setSizePolicy(sizePolicy2)
        self.label_266.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_266.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_57.addWidget(self.label_266, 2, 1, 1, 1)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.radioButton_publisher_zh_cn = QRadioButton(self.layoutWidget_27)
        self.radioButton_publisher_zh_cn.setObjectName(u"radioButton_publisher_zh_cn")
        self.radioButton_publisher_zh_cn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_47.addWidget(self.radioButton_publisher_zh_cn)

        self.radioButton_publisher_zh_tw = QRadioButton(self.layoutWidget_27)
        self.radioButton_publisher_zh_tw.setObjectName(u"radioButton_publisher_zh_tw")

        self.horizontalLayout_47.addWidget(self.radioButton_publisher_zh_tw)

        self.radioButton_publisher_jp = QRadioButton(self.layoutWidget_27)
        self.radioButton_publisher_jp.setObjectName(u"radioButton_publisher_jp")

        self.horizontalLayout_47.addWidget(self.radioButton_publisher_jp)


        self.gridLayout_57.addLayout(self.horizontalLayout_47, 0, 1, 1, 1)

        self.checkBox_publisher_translate = QCheckBox(self.layoutWidget_27)
        self.checkBox_publisher_translate.setObjectName(u"checkBox_publisher_translate")

        self.gridLayout_57.addWidget(self.checkBox_publisher_translate, 1, 1, 1, 1)

        self.groupBox_89 = QGroupBox(self.scrollAreaWidgetContents_11)
        self.groupBox_89.setObjectName(u"groupBox_89")
        self.groupBox_89.setGeometry(QRect(30, 1850, 701, 151))
        self.groupBox_89.setMinimumSize(QSize(200, 0))
        self.groupBox_89.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_29 = QWidget(self.groupBox_89)
        self.layoutWidget_29.setObjectName(u"layoutWidget_29")
        self.layoutWidget_29.setGeometry(QRect(20, 30, 661, 111))
        self.gridLayout_58 = QGridLayout(self.layoutWidget_29)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.gridLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_267 = QLabel(self.layoutWidget_29)
        self.label_267.setObjectName(u"label_267")
        sizePolicy3.setHeightForWidth(self.label_267.sizePolicy().hasHeightForWidth())
        self.label_267.setSizePolicy(sizePolicy3)
        self.label_267.setMinimumSize(QSize(130, 30))
        self.label_267.setLayoutDirection(Qt.LeftToRight)
        self.label_267.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_58.addWidget(self.label_267, 0, 0, 1, 1)

        self.label_268 = QLabel(self.layoutWidget_29)
        self.label_268.setObjectName(u"label_268")
        sizePolicy3.setHeightForWidth(self.label_268.sizePolicy().hasHeightForWidth())
        self.label_268.setSizePolicy(sizePolicy3)
        self.label_268.setMinimumSize(QSize(130, 30))
        self.label_268.setLayoutDirection(Qt.LeftToRight)
        self.label_268.setFrameShape(QFrame.NoFrame)
        self.label_268.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_58.addWidget(self.label_268, 1, 0, 1, 1)

        self.label_269 = QLabel(self.layoutWidget_29)
        self.label_269.setObjectName(u"label_269")
        sizePolicy2.setHeightForWidth(self.label_269.sizePolicy().hasHeightForWidth())
        self.label_269.setSizePolicy(sizePolicy2)
        self.label_269.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_269.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_58.addWidget(self.label_269, 2, 1, 1, 1)

        self.checkBox_director_translate = QCheckBox(self.layoutWidget_29)
        self.checkBox_director_translate.setObjectName(u"checkBox_director_translate")

        self.gridLayout_58.addWidget(self.checkBox_director_translate, 1, 1, 1, 1)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.radioButton_director_zh_cn = QRadioButton(self.layoutWidget_29)
        self.radioButton_director_zh_cn.setObjectName(u"radioButton_director_zh_cn")
        self.radioButton_director_zh_cn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_49.addWidget(self.radioButton_director_zh_cn)

        self.radioButton_director_zh_tw = QRadioButton(self.layoutWidget_29)
        self.radioButton_director_zh_tw.setObjectName(u"radioButton_director_zh_tw")

        self.horizontalLayout_49.addWidget(self.radioButton_director_zh_tw)

        self.radioButton_director_jp = QRadioButton(self.layoutWidget_29)
        self.radioButton_director_jp.setObjectName(u"radioButton_director_jp")

        self.horizontalLayout_49.addWidget(self.radioButton_director_jp)


        self.gridLayout_58.addLayout(self.horizontalLayout_49, 0, 1, 1, 1)

        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_11)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.scrollArea_9 = QScrollArea(self.tab_2)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        self.scrollArea_9.setGeometry(QRect(0, 0, 796, 658))
        self.scrollArea_9.setFrameShape(QFrame.Box)
        self.scrollArea_9.setLineWidth(0)
        self.scrollArea_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_9.setWidgetResizable(False)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 760, 860))
        self.groupBox_20 = QGroupBox(self.scrollAreaWidgetContents_10)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setGeometry(QRect(30, 20, 701, 271))
        self.groupBox_20.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_17 = QWidget(self.groupBox_20)
        self.gridLayoutWidget_17.setObjectName(u"gridLayoutWidget_17")
        self.gridLayoutWidget_17.setGeometry(QRect(20, 30, 661, 221))
        self.gridLayout_17 = QGridLayout(self.gridLayoutWidget_17)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_cnword_style = QLineEdit(self.gridLayoutWidget_17)
        self.lineEdit_cnword_style.setObjectName(u"lineEdit_cnword_style")
        self.lineEdit_cnword_style.setMinimumSize(QSize(450, 30))
        self.lineEdit_cnword_style.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_17.addWidget(self.lineEdit_cnword_style, 2, 1, 1, 1)

        self.label_89 = QLabel(self.gridLayoutWidget_17)
        self.label_89.setObjectName(u"label_89")
        sizePolicy3.setHeightForWidth(self.label_89.sizePolicy().hasHeightForWidth())
        self.label_89.setSizePolicy(sizePolicy3)
        self.label_89.setMinimumSize(QSize(130, 30))
        self.label_89.setLayoutDirection(Qt.RightToLeft)
        self.label_89.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_17.addWidget(self.label_89, 0, 0, 1, 1)

        self.lineEdit_cnword_char = QLineEdit(self.gridLayoutWidget_17)
        self.lineEdit_cnword_char.setObjectName(u"lineEdit_cnword_char")
        self.lineEdit_cnword_char.setMinimumSize(QSize(450, 30))
        self.lineEdit_cnword_char.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_17.addWidget(self.lineEdit_cnword_char, 0, 1, 1, 1)

        self.label_90 = QLabel(self.gridLayoutWidget_17)
        self.label_90.setObjectName(u"label_90")
        sizePolicy2.setHeightForWidth(self.label_90.sizePolicy().hasHeightForWidth())
        self.label_90.setSizePolicy(sizePolicy2)
        self.label_90.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_17.addWidget(self.label_90, 3, 1, 1, 1)

        self.label_91 = QLabel(self.gridLayoutWidget_17)
        self.label_91.setObjectName(u"label_91")
        sizePolicy2.setHeightForWidth(self.label_91.sizePolicy().hasHeightForWidth())
        self.label_91.setSizePolicy(sizePolicy2)
        self.label_91.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_91.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_17.addWidget(self.label_91, 1, 1, 1, 1)

        self.label_69 = QLabel(self.gridLayoutWidget_17)
        self.label_69.setObjectName(u"label_69")
        sizePolicy3.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy3)
        self.label_69.setMinimumSize(QSize(0, 30))
        self.label_69.setLayoutDirection(Qt.RightToLeft)
        self.label_69.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_17.addWidget(self.label_69, 2, 0, 1, 1)

        self.label_119 = QLabel(self.gridLayoutWidget_17)
        self.label_119.setObjectName(u"label_119")
        sizePolicy2.setHeightForWidth(self.label_119.sizePolicy().hasHeightForWidth())
        self.label_119.setSizePolicy(sizePolicy2)
        self.label_119.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_17.addWidget(self.label_119, 5, 1, 1, 1)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.checkBox_foldername = QCheckBox(self.gridLayoutWidget_17)
        self.checkBox_foldername.setObjectName(u"checkBox_foldername")
        sizePolicy4.setHeightForWidth(self.checkBox_foldername.sizePolicy().hasHeightForWidth())
        self.checkBox_foldername.setSizePolicy(sizePolicy4)
        self.checkBox_foldername.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_26.addWidget(self.checkBox_foldername)

        self.checkBox_filename = QCheckBox(self.gridLayoutWidget_17)
        self.checkBox_filename.setObjectName(u"checkBox_filename")
        sizePolicy4.setHeightForWidth(self.checkBox_filename.sizePolicy().hasHeightForWidth())
        self.checkBox_filename.setSizePolicy(sizePolicy4)
        self.checkBox_filename.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_26.addWidget(self.checkBox_filename)


        self.gridLayout_17.addLayout(self.horizontalLayout_26, 4, 1, 1, 1)

        self.label_120 = QLabel(self.gridLayoutWidget_17)
        self.label_120.setObjectName(u"label_120")
        sizePolicy3.setHeightForWidth(self.label_120.sizePolicy().hasHeightForWidth())
        self.label_120.setSizePolicy(sizePolicy3)
        self.label_120.setMinimumSize(QSize(130, 30))
        self.label_120.setLayoutDirection(Qt.LeftToRight)
        self.label_120.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_17.addWidget(self.label_120, 4, 0, 1, 1)

        self.groupBox_45 = QGroupBox(self.scrollAreaWidgetContents_10)
        self.groupBox_45.setObjectName(u"groupBox_45")
        self.groupBox_45.setGeometry(QRect(30, 310, 701, 451))
        self.groupBox_45.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_27 = QWidget(self.groupBox_45)
        self.gridLayoutWidget_27.setObjectName(u"gridLayoutWidget_27")
        self.gridLayoutWidget_27.setGeometry(QRect(20, 30, 661, 186))
        self.gridLayout_27 = QGridLayout(self.gridLayoutWidget_27)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_113 = QLabel(self.gridLayoutWidget_27)
        self.label_113.setObjectName(u"label_113")
        sizePolicy2.setHeightForWidth(self.label_113.sizePolicy().hasHeightForWidth())
        self.label_113.setSizePolicy(sizePolicy2)
        self.label_113.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_27.addWidget(self.label_113, 3, 1, 1, 1)

        self.label_124 = QLabel(self.gridLayoutWidget_27)
        self.label_124.setObjectName(u"label_124")
        sizePolicy3.setHeightForWidth(self.label_124.sizePolicy().hasHeightForWidth())
        self.label_124.setSizePolicy(sizePolicy3)
        self.label_124.setMinimumSize(QSize(130, 30))
        self.label_124.setLayoutDirection(Qt.LeftToRight)
        self.label_124.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.label_124, 1, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_102 = QLabel(self.gridLayoutWidget_27)
        self.label_102.setObjectName(u"label_102")
        sizePolicy2.setHeightForWidth(self.label_102.sizePolicy().hasHeightForWidth())
        self.label_102.setSizePolicy(sizePolicy2)
        self.label_102.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.horizontalLayout_10.addWidget(self.label_102)

        self.label_download_sub_zip = QLabel(self.gridLayoutWidget_27)
        self.label_download_sub_zip.setObjectName(u"label_download_sub_zip")
        sizePolicy2.setHeightForWidth(self.label_download_sub_zip.sizePolicy().hasHeightForWidth())
        self.label_download_sub_zip.setSizePolicy(sizePolicy2)
        self.label_download_sub_zip.setMinimumSize(QSize(0, 0))
        self.label_download_sub_zip.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.label_download_sub_zip.setLayoutDirection(Qt.LeftToRight)
        self.label_download_sub_zip.setStyleSheet(u"color: rgb(10, 52, 255);")
        self.label_download_sub_zip.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_download_sub_zip)


        self.gridLayout_27.addLayout(self.horizontalLayout_10, 1, 1, 1, 1)

        self.label_111 = QLabel(self.gridLayoutWidget_27)
        self.label_111.setObjectName(u"label_111")
        sizePolicy3.setHeightForWidth(self.label_111.sizePolicy().hasHeightForWidth())
        self.label_111.setSizePolicy(sizePolicy3)
        self.label_111.setMinimumSize(QSize(130, 30))
        self.label_111.setLayoutDirection(Qt.LeftToRight)
        self.label_111.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.label_111, 0, 0, 1, 1)

        self.label_112 = QLabel(self.gridLayoutWidget_27)
        self.label_112.setObjectName(u"label_112")
        sizePolicy3.setHeightForWidth(self.label_112.sizePolicy().hasHeightForWidth())
        self.label_112.setSizePolicy(sizePolicy3)
        self.label_112.setMinimumSize(QSize(130, 0))
        self.label_112.setLayoutDirection(Qt.RightToLeft)
        self.label_112.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.label_112, 2, 0, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.radioButton_add_sub_on = QRadioButton(self.gridLayoutWidget_27)
        self.radioButton_add_sub_on.setObjectName(u"radioButton_add_sub_on")
        self.radioButton_add_sub_on.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_21.addWidget(self.radioButton_add_sub_on)

        self.radioButton_add_sub_off = QRadioButton(self.gridLayoutWidget_27)
        self.radioButton_add_sub_off.setObjectName(u"radioButton_add_sub_off")

        self.horizontalLayout_21.addWidget(self.radioButton_add_sub_off)


        self.gridLayout_27.addLayout(self.horizontalLayout_21, 2, 1, 1, 1)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.lineEdit_sub_folder = QLineEdit(self.gridLayoutWidget_27)
        self.lineEdit_sub_folder.setObjectName(u"lineEdit_sub_folder")
        sizePolicy2.setHeightForWidth(self.lineEdit_sub_folder.sizePolicy().hasHeightForWidth())
        self.lineEdit_sub_folder.setSizePolicy(sizePolicy2)
        self.lineEdit_sub_folder.setMinimumSize(QSize(300, 30))
        self.lineEdit_sub_folder.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_28.addWidget(self.lineEdit_sub_folder)

        self.pushButton_select_subtitle_folder = QPushButton(self.gridLayoutWidget_27)
        self.pushButton_select_subtitle_folder.setObjectName(u"pushButton_select_subtitle_folder")
        sizePolicy3.setHeightForWidth(self.pushButton_select_subtitle_folder.sizePolicy().hasHeightForWidth())
        self.pushButton_select_subtitle_folder.setSizePolicy(sizePolicy3)
        self.pushButton_select_subtitle_folder.setMinimumSize(QSize(110, 40))

        self.horizontalLayout_28.addWidget(self.pushButton_select_subtitle_folder)


        self.gridLayout_27.addLayout(self.horizontalLayout_28, 0, 1, 1, 1)

        self.pushButton_add_sub_for_all_video = QPushButton(self.groupBox_45)
        self.pushButton_add_sub_for_all_video.setObjectName(u"pushButton_add_sub_for_all_video")
        self.pushButton_add_sub_for_all_video.setGeometry(QRect(160, 220, 411, 40))
        self.label_125 = QLabel(self.groupBox_45)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setGeometry(QRect(161, 309, 504, 131))
        sizePolicy2.setHeightForWidth(self.label_125.sizePolicy().hasHeightForWidth())
        self.label_125.setSizePolicy(sizePolicy2)
        self.label_125.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_125.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_125.setTextInteractionFlags(Qt.NoTextInteraction)
        self.checkBox_sub_add_chs = QCheckBox(self.groupBox_45)
        self.checkBox_sub_add_chs.setObjectName(u"checkBox_sub_add_chs")
        self.checkBox_sub_add_chs.setGeometry(QRect(162, 272, 169, 30))
        sizePolicy4.setHeightForWidth(self.checkBox_sub_add_chs.sizePolicy().hasHeightForWidth())
        self.checkBox_sub_add_chs.setSizePolicy(sizePolicy4)
        self.checkBox_sub_add_chs.setMinimumSize(QSize(100, 30))
        self.checkBox_sub_rescrape = QCheckBox(self.groupBox_45)
        self.checkBox_sub_rescrape.setObjectName(u"checkBox_sub_rescrape")
        self.checkBox_sub_rescrape.setGeometry(QRect(425, 272, 236, 30))
        sizePolicy4.setHeightForWidth(self.checkBox_sub_rescrape.sizePolicy().hasHeightForWidth())
        self.checkBox_sub_rescrape.setSizePolicy(sizePolicy4)
        self.checkBox_sub_rescrape.setMinimumSize(QSize(100, 30))
        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_10)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab4 = QWidget()
        self.tab4.setObjectName(u"tab4")
        self.scrollArea_4 = QScrollArea(self.tab4)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setGeometry(QRect(0, 0, 796, 658))
        self.scrollArea_4.setFrameShape(QFrame.Box)
        self.scrollArea_4.setLineWidth(0)
        self.scrollArea_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setWidgetResizable(False)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 760, 1670))
        self.groupBox_26 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.groupBox_26.setGeometry(QRect(30, 1010, 701, 561))
        self.groupBox_26.setStyleSheet(u"font:\"Courier\";")
        self.label_118 = QLabel(self.groupBox_26)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setGeometry(QRect(50, 70, 631, 461))
        sizePolicy2.setHeightForWidth(self.label_118.sizePolicy().hasHeightForWidth())
        self.label_118.setSizePolicy(sizePolicy2)
        self.label_118.setMouseTracking(True)
        self.label_118.setStyleSheet(u"color: rgb(8, 128, 128);\n"
"line-height:50px")
        self.label_118.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_118.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_download_mark_zip = QLabel(self.groupBox_26)
        self.label_download_mark_zip.setObjectName(u"label_download_mark_zip")
        self.label_download_mark_zip.setGeometry(QRect(30, 30, 141, 30))
        sizePolicy3.setHeightForWidth(self.label_download_mark_zip.sizePolicy().hasHeightForWidth())
        self.label_download_mark_zip.setSizePolicy(sizePolicy3)
        self.label_download_mark_zip.setMinimumSize(QSize(0, 0))
        self.label_download_mark_zip.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.label_download_mark_zip.setLayoutDirection(Qt.RightToLeft)
        self.label_download_mark_zip.setStyleSheet(u"color: rgb(10, 52, 255);")
        self.label_download_mark_zip.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_31 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_31.setObjectName(u"groupBox_31")
        self.groupBox_31.setGeometry(QRect(30, 20, 701, 511))
        self.groupBox_31.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_24 = QWidget(self.groupBox_31)
        self.gridLayoutWidget_24.setObjectName(u"gridLayoutWidget_24")
        self.gridLayoutWidget_24.setGeometry(QRect(20, 30, 661, 461))
        self.gridLayout_24 = QGridLayout(self.gridLayoutWidget_24)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.radioButton_not_fixed_position = QRadioButton(self.gridLayoutWidget_24)
        self.radioButton_not_fixed_position.setObjectName(u"radioButton_not_fixed_position")
        sizePolicy4.setHeightForWidth(self.radioButton_not_fixed_position.sizePolicy().hasHeightForWidth())
        self.radioButton_not_fixed_position.setSizePolicy(sizePolicy4)
        self.radioButton_not_fixed_position.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.radioButton_not_fixed_position)

        self.radioButton_fixed_corner = QRadioButton(self.gridLayoutWidget_24)
        self.radioButton_fixed_corner.setObjectName(u"radioButton_fixed_corner")
        sizePolicy4.setHeightForWidth(self.radioButton_fixed_corner.sizePolicy().hasHeightForWidth())
        self.radioButton_fixed_corner.setSizePolicy(sizePolicy4)
        self.radioButton_fixed_corner.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.radioButton_fixed_corner)

        self.radioButton_fixed_position = QRadioButton(self.gridLayoutWidget_24)
        self.radioButton_fixed_position.setObjectName(u"radioButton_fixed_position")
        sizePolicy4.setHeightForWidth(self.radioButton_fixed_position.sizePolicy().hasHeightForWidth())
        self.radioButton_fixed_position.setSizePolicy(sizePolicy4)
        self.radioButton_fixed_position.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.radioButton_fixed_position)


        self.gridLayout_24.addLayout(self.horizontalLayout_5, 6, 1, 1, 1)

        self.label_138 = QLabel(self.gridLayoutWidget_24)
        self.label_138.setObjectName(u"label_138")
        sizePolicy2.setHeightForWidth(self.label_138.sizePolicy().hasHeightForWidth())
        self.label_138.setSizePolicy(sizePolicy2)
        self.label_138.setMouseTracking(True)
        self.label_138.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_138.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_138.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_24.addWidget(self.label_138, 5, 1, 1, 1)

        self.label_135 = QLabel(self.gridLayoutWidget_24)
        self.label_135.setObjectName(u"label_135")
        sizePolicy3.setHeightForWidth(self.label_135.sizePolicy().hasHeightForWidth())
        self.label_135.setSizePolicy(sizePolicy3)
        self.label_135.setMinimumSize(QSize(0, 0))
        self.label_135.setLayoutDirection(Qt.RightToLeft)
        self.label_135.setFrameShape(QFrame.NoFrame)
        self.label_135.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_24.addWidget(self.label_135, 4, 0, 1, 1)

        self.label_128 = QLabel(self.gridLayoutWidget_24)
        self.label_128.setObjectName(u"label_128")
        sizePolicy3.setHeightForWidth(self.label_128.sizePolicy().hasHeightForWidth())
        self.label_128.setSizePolicy(sizePolicy3)
        self.label_128.setMinimumSize(QSize(130, 0))
        self.label_128.setLayoutDirection(Qt.RightToLeft)
        self.label_128.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_24.addWidget(self.label_128, 0, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.checkBox_sub = QCheckBox(self.gridLayoutWidget_24)
        self.checkBox_sub.setObjectName(u"checkBox_sub")
        sizePolicy4.setHeightForWidth(self.checkBox_sub.sizePolicy().hasHeightForWidth())
        self.checkBox_sub.setSizePolicy(sizePolicy4)
        self.checkBox_sub.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_14.addWidget(self.checkBox_sub)

        self.checkBox_censored = QCheckBox(self.gridLayoutWidget_24)
        self.checkBox_censored.setObjectName(u"checkBox_censored")
        sizePolicy4.setHeightForWidth(self.checkBox_censored.sizePolicy().hasHeightForWidth())
        self.checkBox_censored.setSizePolicy(sizePolicy4)
        self.checkBox_censored.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_14.addWidget(self.checkBox_censored)

        self.checkBox_umr = QCheckBox(self.gridLayoutWidget_24)
        self.checkBox_umr.setObjectName(u"checkBox_umr")
        sizePolicy4.setHeightForWidth(self.checkBox_umr.sizePolicy().hasHeightForWidth())
        self.checkBox_umr.setSizePolicy(sizePolicy4)
        self.checkBox_umr.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_14.addWidget(self.checkBox_umr)

        self.checkBox_leak = QCheckBox(self.gridLayoutWidget_24)
        self.checkBox_leak.setObjectName(u"checkBox_leak")
        sizePolicy4.setHeightForWidth(self.checkBox_leak.sizePolicy().hasHeightForWidth())
        self.checkBox_leak.setSizePolicy(sizePolicy4)
        self.checkBox_leak.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_14.addWidget(self.checkBox_leak)

        self.checkBox_uncensored = QCheckBox(self.gridLayoutWidget_24)
        self.checkBox_uncensored.setObjectName(u"checkBox_uncensored")
        sizePolicy4.setHeightForWidth(self.checkBox_uncensored.sizePolicy().hasHeightForWidth())
        self.checkBox_uncensored.setSizePolicy(sizePolicy4)
        self.checkBox_uncensored.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_14.addWidget(self.checkBox_uncensored)

        self.checkBox_hd = QCheckBox(self.gridLayoutWidget_24)
        self.checkBox_hd.setObjectName(u"checkBox_hd")
        sizePolicy4.setHeightForWidth(self.checkBox_hd.sizePolicy().hasHeightForWidth())
        self.checkBox_hd.setSizePolicy(sizePolicy4)
        self.checkBox_hd.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_14.addWidget(self.checkBox_hd)


        self.gridLayout_24.addLayout(self.horizontalLayout_14, 4, 1, 1, 1)

        self.label_140 = QLabel(self.gridLayoutWidget_24)
        self.label_140.setObjectName(u"label_140")
        sizePolicy2.setHeightForWidth(self.label_140.sizePolicy().hasHeightForWidth())
        self.label_140.setSizePolicy(sizePolicy2)
        self.label_140.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_24.addWidget(self.label_140, 3, 1, 1, 1)

        self.label_141 = QLabel(self.gridLayoutWidget_24)
        self.label_141.setObjectName(u"label_141")
        sizePolicy2.setHeightForWidth(self.label_141.sizePolicy().hasHeightForWidth())
        self.label_141.setSizePolicy(sizePolicy2)
        self.label_141.setMouseTracking(True)
        self.label_141.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_141.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_141.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_24.addWidget(self.label_141, 7, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBox_poster_mark = QCheckBox(self.gridLayoutWidget_24)
        self.checkBox_poster_mark.setObjectName(u"checkBox_poster_mark")
        sizePolicy4.setHeightForWidth(self.checkBox_poster_mark.sizePolicy().hasHeightForWidth())
        self.checkBox_poster_mark.setSizePolicy(sizePolicy4)
        self.checkBox_poster_mark.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_7.addWidget(self.checkBox_poster_mark)

        self.checkBox_thumb_mark = QCheckBox(self.gridLayoutWidget_24)
        self.checkBox_thumb_mark.setObjectName(u"checkBox_thumb_mark")
        sizePolicy4.setHeightForWidth(self.checkBox_thumb_mark.sizePolicy().hasHeightForWidth())
        self.checkBox_thumb_mark.setSizePolicy(sizePolicy4)
        self.checkBox_thumb_mark.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_7.addWidget(self.checkBox_thumb_mark)

        self.checkBox_fanart_mark = QCheckBox(self.gridLayoutWidget_24)
        self.checkBox_fanart_mark.setObjectName(u"checkBox_fanart_mark")
        sizePolicy4.setHeightForWidth(self.checkBox_fanart_mark.sizePolicy().hasHeightForWidth())
        self.checkBox_fanart_mark.setSizePolicy(sizePolicy4)
        self.checkBox_fanart_mark.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_7.addWidget(self.checkBox_fanart_mark)


        self.gridLayout_24.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)

        self.label_139 = QLabel(self.gridLayoutWidget_24)
        self.label_139.setObjectName(u"label_139")
        sizePolicy3.setHeightForWidth(self.label_139.sizePolicy().hasHeightForWidth())
        self.label_139.setSizePolicy(sizePolicy3)
        self.label_139.setMinimumSize(QSize(0, 0))
        self.label_139.setLayoutDirection(Qt.RightToLeft)
        self.label_139.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_24.addWidget(self.label_139, 2, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSlider_mark_size = CustomQSlider(self.gridLayoutWidget_24)
        self.horizontalSlider_mark_size.setObjectName(u"horizontalSlider_mark_size")
        sizePolicy3.setHeightForWidth(self.horizontalSlider_mark_size.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_mark_size.setSizePolicy(sizePolicy3)
        self.horizontalSlider_mark_size.setMinimumSize(QSize(400, 30))
        self.horizontalSlider_mark_size.setMaximumSize(QSize(500, 30))
        self.horizontalSlider_mark_size.setMinimum(1)
        self.horizontalSlider_mark_size.setMaximum(40)
        self.horizontalSlider_mark_size.setPageStep(1)
        self.horizontalSlider_mark_size.setValue(5)
        self.horizontalSlider_mark_size.setSliderPosition(5)
        self.horizontalSlider_mark_size.setOrientation(Qt.Horizontal)

        self.horizontalLayout_15.addWidget(self.horizontalSlider_mark_size)

        self.lcdNumber_mark_size = QLCDNumber(self.gridLayoutWidget_24)
        self.lcdNumber_mark_size.setObjectName(u"lcdNumber_mark_size")
        sizePolicy9.setHeightForWidth(self.lcdNumber_mark_size.sizePolicy().hasHeightForWidth())
        self.lcdNumber_mark_size.setSizePolicy(sizePolicy9)
        self.lcdNumber_mark_size.setMinimumSize(QSize(30, 30))
        self.lcdNumber_mark_size.setMaximumSize(QSize(70, 30))
        self.lcdNumber_mark_size.setSmallDecimalPoint(False)
        self.lcdNumber_mark_size.setDigitCount(2)
        self.lcdNumber_mark_size.setProperty(u"intValue", 5)

        self.horizontalLayout_15.addWidget(self.lcdNumber_mark_size)


        self.gridLayout_24.addLayout(self.horizontalLayout_15, 2, 1, 1, 1)

        self.label_127 = QLabel(self.gridLayoutWidget_24)
        self.label_127.setObjectName(u"label_127")
        sizePolicy3.setHeightForWidth(self.label_127.sizePolicy().hasHeightForWidth())
        self.label_127.setSizePolicy(sizePolicy3)
        self.label_127.setMinimumSize(QSize(0, 0))
        self.label_127.setLayoutDirection(Qt.RightToLeft)
        self.label_127.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_24.addWidget(self.label_127, 6, 0, 1, 1)

        self.label_130 = QLabel(self.gridLayoutWidget_24)
        self.label_130.setObjectName(u"label_130")
        sizePolicy2.setHeightForWidth(self.label_130.sizePolicy().hasHeightForWidth())
        self.label_130.setSizePolicy(sizePolicy2)
        self.label_130.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_24.addWidget(self.label_130, 1, 1, 1, 1)

        self.groupBox_36 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_36.setObjectName(u"groupBox_36")
        self.groupBox_36.setGeometry(QRect(30, 550, 701, 101))
        self.groupBox_36.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_30 = QWidget(self.groupBox_36)
        self.gridLayoutWidget_30.setObjectName(u"gridLayoutWidget_30")
        self.gridLayoutWidget_30.setGeometry(QRect(20, 30, 664, 51))
        self.gridLayout_30 = QGridLayout(self.gridLayoutWidget_30)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radioButton_top_left = QRadioButton(self.gridLayoutWidget_30)
        self.radioButton_top_left.setObjectName(u"radioButton_top_left")
        sizePolicy4.setHeightForWidth(self.radioButton_top_left.sizePolicy().hasHeightForWidth())
        self.radioButton_top_left.setSizePolicy(sizePolicy4)
        self.radioButton_top_left.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.radioButton_top_left)

        self.radioButton_top_right = QRadioButton(self.gridLayoutWidget_30)
        self.radioButton_top_right.setObjectName(u"radioButton_top_right")
        sizePolicy4.setHeightForWidth(self.radioButton_top_right.sizePolicy().hasHeightForWidth())
        self.radioButton_top_right.setSizePolicy(sizePolicy4)
        self.radioButton_top_right.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.radioButton_top_right)

        self.radioButton_bottom_right = QRadioButton(self.gridLayoutWidget_30)
        self.radioButton_bottom_right.setObjectName(u"radioButton_bottom_right")
        sizePolicy4.setHeightForWidth(self.radioButton_bottom_right.sizePolicy().hasHeightForWidth())
        self.radioButton_bottom_right.setSizePolicy(sizePolicy4)
        self.radioButton_bottom_right.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.radioButton_bottom_right)

        self.radioButton_bottom_left = QRadioButton(self.gridLayoutWidget_30)
        self.radioButton_bottom_left.setObjectName(u"radioButton_bottom_left")
        sizePolicy4.setHeightForWidth(self.radioButton_bottom_left.sizePolicy().hasHeightForWidth())
        self.radioButton_bottom_left.setSizePolicy(sizePolicy4)
        self.radioButton_bottom_left.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.radioButton_bottom_left)


        self.gridLayout_30.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)

        self.label_126 = QLabel(self.gridLayoutWidget_30)
        self.label_126.setObjectName(u"label_126")
        sizePolicy3.setHeightForWidth(self.label_126.sizePolicy().hasHeightForWidth())
        self.label_126.setSizePolicy(sizePolicy3)
        self.label_126.setMinimumSize(QSize(130, 0))
        self.label_126.setLayoutDirection(Qt.RightToLeft)
        self.label_126.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_30.addWidget(self.label_126, 0, 0, 1, 1)

        self.groupBox_42 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_42.setObjectName(u"groupBox_42")
        self.groupBox_42.setGeometry(QRect(30, 790, 701, 201))
        self.groupBox_42.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_31 = QWidget(self.groupBox_42)
        self.gridLayoutWidget_31.setObjectName(u"gridLayoutWidget_31")
        self.gridLayoutWidget_31.setGeometry(QRect(20, 30, 664, 59))
        self.gridLayout_31 = QGridLayout(self.gridLayoutWidget_31)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.radioButton_top_left_sub = QRadioButton(self.gridLayoutWidget_31)
        self.radioButton_top_left_sub.setObjectName(u"radioButton_top_left_sub")
        sizePolicy4.setHeightForWidth(self.radioButton_top_left_sub.sizePolicy().hasHeightForWidth())
        self.radioButton_top_left_sub.setSizePolicy(sizePolicy4)
        self.radioButton_top_left_sub.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_6.addWidget(self.radioButton_top_left_sub)

        self.radioButton_top_right_sub = QRadioButton(self.gridLayoutWidget_31)
        self.radioButton_top_right_sub.setObjectName(u"radioButton_top_right_sub")
        sizePolicy4.setHeightForWidth(self.radioButton_top_right_sub.sizePolicy().hasHeightForWidth())
        self.radioButton_top_right_sub.setSizePolicy(sizePolicy4)
        self.radioButton_top_right_sub.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_6.addWidget(self.radioButton_top_right_sub)

        self.radioButton_bottom_right_sub = QRadioButton(self.gridLayoutWidget_31)
        self.radioButton_bottom_right_sub.setObjectName(u"radioButton_bottom_right_sub")
        sizePolicy4.setHeightForWidth(self.radioButton_bottom_right_sub.sizePolicy().hasHeightForWidth())
        self.radioButton_bottom_right_sub.setSizePolicy(sizePolicy4)
        self.radioButton_bottom_right_sub.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_6.addWidget(self.radioButton_bottom_right_sub)

        self.radioButton_bottom_left_sub = QRadioButton(self.gridLayoutWidget_31)
        self.radioButton_bottom_left_sub.setObjectName(u"radioButton_bottom_left_sub")
        sizePolicy4.setHeightForWidth(self.radioButton_bottom_left_sub.sizePolicy().hasHeightForWidth())
        self.radioButton_bottom_left_sub.setSizePolicy(sizePolicy4)
        self.radioButton_bottom_left_sub.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_6.addWidget(self.radioButton_bottom_left_sub)


        self.gridLayout_31.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)

        self.label_131 = QLabel(self.gridLayoutWidget_31)
        self.label_131.setObjectName(u"label_131")
        sizePolicy3.setHeightForWidth(self.label_131.sizePolicy().hasHeightForWidth())
        self.label_131.setSizePolicy(sizePolicy3)
        self.label_131.setMinimumSize(QSize(130, 0))
        self.label_131.setLayoutDirection(Qt.RightToLeft)
        self.label_131.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_31.addWidget(self.label_131, 0, 0, 1, 1)

        self.gridLayoutWidget_29 = QWidget(self.groupBox_42)
        self.gridLayoutWidget_29.setObjectName(u"gridLayoutWidget_29")
        self.gridLayoutWidget_29.setGeometry(QRect(20, 80, 664, 51))
        self.gridLayout_29 = QGridLayout(self.gridLayoutWidget_29)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.radioButton_top_left_mosaic = QRadioButton(self.gridLayoutWidget_29)
        self.radioButton_top_left_mosaic.setObjectName(u"radioButton_top_left_mosaic")
        sizePolicy4.setHeightForWidth(self.radioButton_top_left_mosaic.sizePolicy().hasHeightForWidth())
        self.radioButton_top_left_mosaic.setSizePolicy(sizePolicy4)
        self.radioButton_top_left_mosaic.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_12.addWidget(self.radioButton_top_left_mosaic)

        self.radioButton_top_right_mosaic = QRadioButton(self.gridLayoutWidget_29)
        self.radioButton_top_right_mosaic.setObjectName(u"radioButton_top_right_mosaic")
        sizePolicy4.setHeightForWidth(self.radioButton_top_right_mosaic.sizePolicy().hasHeightForWidth())
        self.radioButton_top_right_mosaic.setSizePolicy(sizePolicy4)
        self.radioButton_top_right_mosaic.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_12.addWidget(self.radioButton_top_right_mosaic)

        self.radioButton_bottom_right_mosaic = QRadioButton(self.gridLayoutWidget_29)
        self.radioButton_bottom_right_mosaic.setObjectName(u"radioButton_bottom_right_mosaic")
        sizePolicy4.setHeightForWidth(self.radioButton_bottom_right_mosaic.sizePolicy().hasHeightForWidth())
        self.radioButton_bottom_right_mosaic.setSizePolicy(sizePolicy4)
        self.radioButton_bottom_right_mosaic.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_12.addWidget(self.radioButton_bottom_right_mosaic)

        self.radioButton_bottom_left_mosaic = QRadioButton(self.gridLayoutWidget_29)
        self.radioButton_bottom_left_mosaic.setObjectName(u"radioButton_bottom_left_mosaic")
        sizePolicy4.setHeightForWidth(self.radioButton_bottom_left_mosaic.sizePolicy().hasHeightForWidth())
        self.radioButton_bottom_left_mosaic.setSizePolicy(sizePolicy4)
        self.radioButton_bottom_left_mosaic.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_12.addWidget(self.radioButton_bottom_left_mosaic)


        self.gridLayout_29.addLayout(self.horizontalLayout_12, 0, 1, 1, 1)

        self.label_134 = QLabel(self.gridLayoutWidget_29)
        self.label_134.setObjectName(u"label_134")
        sizePolicy3.setHeightForWidth(self.label_134.sizePolicy().hasHeightForWidth())
        self.label_134.setSizePolicy(sizePolicy3)
        self.label_134.setMinimumSize(QSize(130, 30))
        self.label_134.setLayoutDirection(Qt.RightToLeft)
        self.label_134.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_29.addWidget(self.label_134, 0, 0, 1, 1)

        self.gridLayoutWidget_32 = QWidget(self.groupBox_42)
        self.gridLayoutWidget_32.setObjectName(u"gridLayoutWidget_32")
        self.gridLayoutWidget_32.setGeometry(QRect(20, 120, 664, 59))
        self.gridLayout_39 = QGridLayout(self.gridLayoutWidget_32)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.radioButton_top_left_hd = QRadioButton(self.gridLayoutWidget_32)
        self.radioButton_top_left_hd.setObjectName(u"radioButton_top_left_hd")
        sizePolicy4.setHeightForWidth(self.radioButton_top_left_hd.sizePolicy().hasHeightForWidth())
        self.radioButton_top_left_hd.setSizePolicy(sizePolicy4)
        self.radioButton_top_left_hd.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_46.addWidget(self.radioButton_top_left_hd)

        self.radioButton_top_right_hd = QRadioButton(self.gridLayoutWidget_32)
        self.radioButton_top_right_hd.setObjectName(u"radioButton_top_right_hd")
        sizePolicy4.setHeightForWidth(self.radioButton_top_right_hd.sizePolicy().hasHeightForWidth())
        self.radioButton_top_right_hd.setSizePolicy(sizePolicy4)
        self.radioButton_top_right_hd.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_46.addWidget(self.radioButton_top_right_hd)

        self.radioButton_bottom_right_hd = QRadioButton(self.gridLayoutWidget_32)
        self.radioButton_bottom_right_hd.setObjectName(u"radioButton_bottom_right_hd")
        sizePolicy4.setHeightForWidth(self.radioButton_bottom_right_hd.sizePolicy().hasHeightForWidth())
        self.radioButton_bottom_right_hd.setSizePolicy(sizePolicy4)
        self.radioButton_bottom_right_hd.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_46.addWidget(self.radioButton_bottom_right_hd)

        self.radioButton_bottom_left_hd = QRadioButton(self.gridLayoutWidget_32)
        self.radioButton_bottom_left_hd.setObjectName(u"radioButton_bottom_left_hd")
        sizePolicy4.setHeightForWidth(self.radioButton_bottom_left_hd.sizePolicy().hasHeightForWidth())
        self.radioButton_bottom_left_hd.setSizePolicy(sizePolicy4)
        self.radioButton_bottom_left_hd.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_46.addWidget(self.radioButton_bottom_left_hd)


        self.gridLayout_39.addLayout(self.horizontalLayout_46, 0, 1, 1, 1)

        self.label_216 = QLabel(self.gridLayoutWidget_32)
        self.label_216.setObjectName(u"label_216")
        sizePolicy3.setHeightForWidth(self.label_216.sizePolicy().hasHeightForWidth())
        self.label_216.setSizePolicy(sizePolicy3)
        self.label_216.setMinimumSize(QSize(130, 0))
        self.label_216.setLayoutDirection(Qt.RightToLeft)
        self.label_216.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_39.addWidget(self.label_216, 0, 0, 1, 1)

        self.groupBox_39 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_39.setObjectName(u"groupBox_39")
        self.groupBox_39.setGeometry(QRect(30, 670, 701, 101))
        self.groupBox_39.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_33 = QWidget(self.groupBox_39)
        self.gridLayoutWidget_33.setObjectName(u"gridLayoutWidget_33")
        self.gridLayoutWidget_33.setGeometry(QRect(20, 30, 664, 51))
        self.gridLayout_42 = QGridLayout(self.gridLayoutWidget_33)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.radioButton_top_left_corner = QRadioButton(self.gridLayoutWidget_33)
        self.radioButton_top_left_corner.setObjectName(u"radioButton_top_left_corner")
        sizePolicy4.setHeightForWidth(self.radioButton_top_left_corner.sizePolicy().hasHeightForWidth())
        self.radioButton_top_left_corner.setSizePolicy(sizePolicy4)
        self.radioButton_top_left_corner.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_53.addWidget(self.radioButton_top_left_corner)

        self.radioButton_top_right_corner = QRadioButton(self.gridLayoutWidget_33)
        self.radioButton_top_right_corner.setObjectName(u"radioButton_top_right_corner")
        sizePolicy4.setHeightForWidth(self.radioButton_top_right_corner.sizePolicy().hasHeightForWidth())
        self.radioButton_top_right_corner.setSizePolicy(sizePolicy4)
        self.radioButton_top_right_corner.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_53.addWidget(self.radioButton_top_right_corner)

        self.radioButton_bottom_right_corner = QRadioButton(self.gridLayoutWidget_33)
        self.radioButton_bottom_right_corner.setObjectName(u"radioButton_bottom_right_corner")
        sizePolicy4.setHeightForWidth(self.radioButton_bottom_right_corner.sizePolicy().hasHeightForWidth())
        self.radioButton_bottom_right_corner.setSizePolicy(sizePolicy4)
        self.radioButton_bottom_right_corner.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_53.addWidget(self.radioButton_bottom_right_corner)

        self.radioButton_bottom_left_corner = QRadioButton(self.gridLayoutWidget_33)
        self.radioButton_bottom_left_corner.setObjectName(u"radioButton_bottom_left_corner")
        sizePolicy4.setHeightForWidth(self.radioButton_bottom_left_corner.sizePolicy().hasHeightForWidth())
        self.radioButton_bottom_left_corner.setSizePolicy(sizePolicy4)
        self.radioButton_bottom_left_corner.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_53.addWidget(self.radioButton_bottom_left_corner)


        self.gridLayout_42.addLayout(self.horizontalLayout_53, 0, 1, 1, 1)

        self.label_233 = QLabel(self.gridLayoutWidget_33)
        self.label_233.setObjectName(u"label_233")
        sizePolicy3.setHeightForWidth(self.label_233.sizePolicy().hasHeightForWidth())
        self.label_233.setSizePolicy(sizePolicy3)
        self.label_233.setMinimumSize(QSize(130, 0))
        self.label_233.setLayoutDirection(Qt.RightToLeft)
        self.label_233.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_42.addWidget(self.label_233, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.tabWidget.addTab(self.tab4, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.scrollArea_13 = QScrollArea(self.tab_7)
        self.scrollArea_13.setObjectName(u"scrollArea_13")
        self.scrollArea_13.setGeometry(QRect(0, 0, 796, 658))
        self.scrollArea_13.setFrameShape(QFrame.Box)
        self.scrollArea_13.setLineWidth(0)
        self.scrollArea_13.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_13.setWidgetResizable(False)
        self.scrollAreaWidgetContents_13 = QWidget()
        self.scrollAreaWidgetContents_13.setObjectName(u"scrollAreaWidgetContents_13")
        self.scrollAreaWidgetContents_13.setGeometry(QRect(0, 0, 796, 1100))
        self.groupBox_81 = QGroupBox(self.scrollAreaWidgetContents_13)
        self.groupBox_81.setObjectName(u"groupBox_81")
        self.groupBox_81.setGeometry(QRect(30, 20, 701, 981))
        self.groupBox_81.setMinimumSize(QSize(200, 0))
        self.groupBox_81.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_10 = QWidget(self.groupBox_81)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.layoutWidget_10.setGeometry(QRect(20, 30, 661, 931))
        self.gridLayout_40 = QGridLayout(self.layoutWidget_10)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_146 = QHBoxLayout()
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.label_402 = QLabel(self.layoutWidget_10)
        self.label_402.setObjectName(u"label_402")
        sizePolicy3.setHeightForWidth(self.label_402.sizePolicy().hasHeightForWidth())
        self.label_402.setSizePolicy(sizePolicy3)
        self.label_402.setMinimumSize(QSize(20, 0))
        self.label_402.setLayoutDirection(Qt.LeftToRight)
        self.label_402.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_146.addWidget(self.label_402)

        self.checkBox_nfo_all_actor = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_all_actor.setObjectName(u"checkBox_nfo_all_actor")

        self.horizontalLayout_146.addWidget(self.checkBox_nfo_all_actor)


        self.gridLayout_40.addLayout(self.horizontalLayout_146, 11, 1, 1, 1)

        self.label_391 = QLabel(self.layoutWidget_10)
        self.label_391.setObjectName(u"label_391")
        sizePolicy3.setHeightForWidth(self.label_391.sizePolicy().hasHeightForWidth())
        self.label_391.setSizePolicy(sizePolicy3)
        self.label_391.setMinimumSize(QSize(130, 30))
        self.label_391.setLayoutDirection(Qt.LeftToRight)
        self.label_391.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_391, 8, 0, 1, 1)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.checkBox_tag_letters = QCheckBox(self.layoutWidget_10)
        self.checkBox_tag_letters.setObjectName(u"checkBox_tag_letters")

        self.horizontalLayout_37.addWidget(self.checkBox_tag_letters)

        self.checkBox_tag_actor = QCheckBox(self.layoutWidget_10)
        self.checkBox_tag_actor.setObjectName(u"checkBox_tag_actor")

        self.horizontalLayout_37.addWidget(self.checkBox_tag_actor)

        self.checkBox_tag_definition = QCheckBox(self.layoutWidget_10)
        self.checkBox_tag_definition.setObjectName(u"checkBox_tag_definition")

        self.horizontalLayout_37.addWidget(self.checkBox_tag_definition)

        self.checkBox_tag_cnword = QCheckBox(self.layoutWidget_10)
        self.checkBox_tag_cnword.setObjectName(u"checkBox_tag_cnword")

        self.horizontalLayout_37.addWidget(self.checkBox_tag_cnword)


        self.gridLayout_40.addLayout(self.horizontalLayout_37, 14, 1, 1, 1)

        self.label_413 = QLabel(self.layoutWidget_10)
        self.label_413.setObjectName(u"label_413")
        sizePolicy3.setHeightForWidth(self.label_413.sizePolicy().hasHeightForWidth())
        self.label_413.setSizePolicy(sizePolicy3)
        self.label_413.setMinimumSize(QSize(130, 30))
        self.label_413.setLayoutDirection(Qt.LeftToRight)
        self.label_413.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_413, 16, 0, 1, 1)

        self.label_396 = QLabel(self.layoutWidget_10)
        self.label_396.setObjectName(u"label_396")
        sizePolicy2.setHeightForWidth(self.label_396.sizePolicy().hasHeightForWidth())
        self.label_396.setSizePolicy(sizePolicy2)
        self.label_396.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_40.addWidget(self.label_396, 5, 1, 1, 1)

        self.lineEdit_nfo_tagline = QLineEdit(self.layoutWidget_10)
        self.lineEdit_nfo_tagline.setObjectName(u"lineEdit_nfo_tagline")
        sizePolicy2.setHeightForWidth(self.lineEdit_nfo_tagline.sizePolicy().hasHeightForWidth())
        self.lineEdit_nfo_tagline.setSizePolicy(sizePolicy2)
        self.lineEdit_nfo_tagline.setMinimumSize(QSize(0, 30))
        self.lineEdit_nfo_tagline.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_40.addWidget(self.lineEdit_nfo_tagline, 6, 1, 1, 1)

        self.horizontalLayout_135 = QHBoxLayout()
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.checkBox_nfo_sorttitle = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_sorttitle.setObjectName(u"checkBox_nfo_sorttitle")
        sizePolicy3.setHeightForWidth(self.checkBox_nfo_sorttitle.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_sorttitle.setSizePolicy(sizePolicy3)
        self.checkBox_nfo_sorttitle.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_135.addWidget(self.checkBox_nfo_sorttitle)

        self.checkBox_nfo_originaltitle = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_originaltitle.setObjectName(u"checkBox_nfo_originaltitle")

        self.horizontalLayout_135.addWidget(self.checkBox_nfo_originaltitle)


        self.gridLayout_40.addLayout(self.horizontalLayout_135, 0, 1, 1, 1)

        self.horizontalLayout_114 = QHBoxLayout()
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.checkBox_nfo_genre = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_genre.setObjectName(u"checkBox_nfo_genre")
        sizePolicy3.setHeightForWidth(self.checkBox_nfo_genre.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_genre.setSizePolicy(sizePolicy3)
        self.checkBox_nfo_genre.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_114.addWidget(self.checkBox_nfo_genre)

        self.checkBox_nfo_actor_set = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_actor_set.setObjectName(u"checkBox_nfo_actor_set")
        sizePolicy3.setHeightForWidth(self.checkBox_nfo_actor_set.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_actor_set.setSizePolicy(sizePolicy3)
        self.checkBox_nfo_actor_set.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_114.addWidget(self.checkBox_nfo_actor_set)

        self.checkBox_nfo_set = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_set.setObjectName(u"checkBox_nfo_set")
        sizePolicy2.setHeightForWidth(self.checkBox_nfo_set.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_set.setSizePolicy(sizePolicy2)
        self.checkBox_nfo_set.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_114.addWidget(self.checkBox_nfo_set)


        self.gridLayout_40.addLayout(self.horizontalLayout_114, 20, 1, 1, 1)

        self.horizontalLayout_108 = QHBoxLayout()
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.checkBox_nfo_poster = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_poster.setObjectName(u"checkBox_nfo_poster")

        self.horizontalLayout_108.addWidget(self.checkBox_nfo_poster)

        self.checkBox_nfo_cover = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_cover.setObjectName(u"checkBox_nfo_cover")

        self.horizontalLayout_108.addWidget(self.checkBox_nfo_cover)

        self.checkBox_nfo_trailer = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_trailer.setObjectName(u"checkBox_nfo_trailer")

        self.horizontalLayout_108.addWidget(self.checkBox_nfo_trailer)

        self.checkBox_nfo_website = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_website.setObjectName(u"checkBox_nfo_website")

        self.horizontalLayout_108.addWidget(self.checkBox_nfo_website)


        self.gridLayout_40.addLayout(self.horizontalLayout_108, 22, 1, 1, 1)

        self.label_301 = QLabel(self.layoutWidget_10)
        self.label_301.setObjectName(u"label_301")
        sizePolicy3.setHeightForWidth(self.label_301.sizePolicy().hasHeightForWidth())
        self.label_301.setSizePolicy(sizePolicy3)
        self.label_301.setMinimumSize(QSize(130, 30))
        self.label_301.setLayoutDirection(Qt.LeftToRight)
        self.label_301.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_301, 15, 0, 1, 1)

        self.label_335 = QLabel(self.layoutWidget_10)
        self.label_335.setObjectName(u"label_335")
        sizePolicy3.setHeightForWidth(self.label_335.sizePolicy().hasHeightForWidth())
        self.label_335.setSizePolicy(sizePolicy3)
        self.label_335.setMinimumSize(QSize(130, 30))
        self.label_335.setLayoutDirection(Qt.LeftToRight)
        self.label_335.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_335, 3, 0, 1, 1)

        self.label_209 = QLabel(self.layoutWidget_10)
        self.label_209.setObjectName(u"label_209")
        sizePolicy3.setHeightForWidth(self.label_209.sizePolicy().hasHeightForWidth())
        self.label_209.setSizePolicy(sizePolicy3)
        self.label_209.setMinimumSize(QSize(130, 30))
        self.label_209.setLayoutDirection(Qt.LeftToRight)
        self.label_209.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_209, 1, 0, 1, 1)

        self.label_387 = QLabel(self.layoutWidget_10)
        self.label_387.setObjectName(u"label_387")
        sizePolicy3.setHeightForWidth(self.label_387.sizePolicy().hasHeightForWidth())
        self.label_387.setSizePolicy(sizePolicy3)
        self.label_387.setMinimumSize(QSize(130, 30))
        self.label_387.setLayoutDirection(Qt.LeftToRight)
        self.label_387.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_387, 6, 0, 1, 1)

        self.label_163 = QLabel(self.layoutWidget_10)
        self.label_163.setObjectName(u"label_163")
        sizePolicy3.setHeightForWidth(self.label_163.sizePolicy().hasHeightForWidth())
        self.label_163.setSizePolicy(sizePolicy3)
        self.label_163.setMinimumSize(QSize(130, 30))
        self.label_163.setLayoutDirection(Qt.LeftToRight)
        self.label_163.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_163, 0, 0, 1, 1)

        self.label_388 = QLabel(self.layoutWidget_10)
        self.label_388.setObjectName(u"label_388")
        sizePolicy3.setHeightForWidth(self.label_388.sizePolicy().hasHeightForWidth())
        self.label_388.setSizePolicy(sizePolicy3)
        self.label_388.setMinimumSize(QSize(130, 30))
        self.label_388.setLayoutDirection(Qt.LeftToRight)
        self.label_388.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_388, 21, 0, 1, 1)

        self.horizontalLayout_136 = QHBoxLayout()
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.checkBox_nfo_outline = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_outline.setObjectName(u"checkBox_nfo_outline")
        sizePolicy3.setHeightForWidth(self.checkBox_nfo_outline.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_outline.setSizePolicy(sizePolicy3)
        self.checkBox_nfo_outline.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_136.addWidget(self.checkBox_nfo_outline)

        self.checkBox_nfo_plot = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_plot.setObjectName(u"checkBox_nfo_plot")
        sizePolicy3.setHeightForWidth(self.checkBox_nfo_plot.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_plot.setSizePolicy(sizePolicy3)
        self.checkBox_nfo_plot.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_136.addWidget(self.checkBox_nfo_plot)

        self.checkBox_nfo_originalplot = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_originalplot.setObjectName(u"checkBox_nfo_originalplot")

        self.horizontalLayout_136.addWidget(self.checkBox_nfo_originalplot)


        self.gridLayout_40.addLayout(self.horizontalLayout_136, 2, 1, 1, 1)

        self.horizontalLayout_144 = QHBoxLayout()
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.label_412 = QLabel(self.layoutWidget_10)
        self.label_412.setObjectName(u"label_412")
        sizePolicy10.setHeightForWidth(self.label_412.sizePolicy().hasHeightForWidth())
        self.label_412.setSizePolicy(sizePolicy10)
        self.label_412.setMinimumSize(QSize(0, 30))
        self.label_412.setLayoutDirection(Qt.LeftToRight)
        self.label_412.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_412.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_144.addWidget(self.label_412)

        self.lineEdit_nfo_tag_series = QLineEdit(self.layoutWidget_10)
        self.lineEdit_nfo_tag_series.setObjectName(u"lineEdit_nfo_tag_series")
        sizePolicy2.setHeightForWidth(self.lineEdit_nfo_tag_series.sizePolicy().hasHeightForWidth())
        self.lineEdit_nfo_tag_series.setSizePolicy(sizePolicy2)
        self.lineEdit_nfo_tag_series.setMinimumSize(QSize(0, 30))
        self.lineEdit_nfo_tag_series.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_144.addWidget(self.lineEdit_nfo_tag_series)


        self.gridLayout_40.addLayout(self.horizontalLayout_144, 16, 1, 1, 1)

        self.horizontalLayout_145 = QHBoxLayout()
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.label_416 = QLabel(self.layoutWidget_10)
        self.label_416.setObjectName(u"label_416")
        sizePolicy10.setHeightForWidth(self.label_416.sizePolicy().hasHeightForWidth())
        self.label_416.setSizePolicy(sizePolicy10)
        self.label_416.setMinimumSize(QSize(0, 30))
        self.label_416.setLayoutDirection(Qt.LeftToRight)
        self.label_416.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_416.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_145.addWidget(self.label_416)

        self.lineEdit_nfo_tag_studio = QLineEdit(self.layoutWidget_10)
        self.lineEdit_nfo_tag_studio.setObjectName(u"lineEdit_nfo_tag_studio")
        sizePolicy2.setHeightForWidth(self.lineEdit_nfo_tag_studio.sizePolicy().hasHeightForWidth())
        self.lineEdit_nfo_tag_studio.setSizePolicy(sizePolicy2)
        self.lineEdit_nfo_tag_studio.setMinimumSize(QSize(0, 30))
        self.lineEdit_nfo_tag_studio.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_145.addWidget(self.lineEdit_nfo_tag_studio)


        self.gridLayout_40.addLayout(self.horizontalLayout_145, 17, 1, 1, 1)

        self.horizontalLayout_142 = QHBoxLayout()
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.label_394 = QLabel(self.layoutWidget_10)
        self.label_394.setObjectName(u"label_394")
        sizePolicy3.setHeightForWidth(self.label_394.sizePolicy().hasHeightForWidth())
        self.label_394.setSizePolicy(sizePolicy3)
        self.label_394.setMinimumSize(QSize(20, 0))
        self.label_394.setLayoutDirection(Qt.LeftToRight)
        self.label_394.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_142.addWidget(self.label_394)

        self.checkBox_outline_cdata = QCheckBox(self.layoutWidget_10)
        self.checkBox_outline_cdata.setObjectName(u"checkBox_outline_cdata")

        self.horizontalLayout_142.addWidget(self.checkBox_outline_cdata)


        self.gridLayout_40.addLayout(self.horizontalLayout_142, 3, 1, 1, 1)

        self.label_390 = QLabel(self.layoutWidget_10)
        self.label_390.setObjectName(u"label_390")
        sizePolicy3.setHeightForWidth(self.label_390.sizePolicy().hasHeightForWidth())
        self.label_390.setSizePolicy(sizePolicy3)
        self.label_390.setMinimumSize(QSize(130, 30))
        self.label_390.setLayoutDirection(Qt.LeftToRight)
        self.label_390.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_390, 9, 0, 1, 1)

        self.horizontalLayout_139 = QHBoxLayout()
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.checkBox_nfo_score = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_score.setObjectName(u"checkBox_nfo_score")
        sizePolicy3.setHeightForWidth(self.checkBox_nfo_score.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_score.setSizePolicy(sizePolicy3)
        self.checkBox_nfo_score.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_139.addWidget(self.checkBox_nfo_score)

        self.checkBox_nfo_criticrating = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_criticrating.setObjectName(u"checkBox_nfo_criticrating")
        sizePolicy2.setHeightForWidth(self.checkBox_nfo_criticrating.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_criticrating.setSizePolicy(sizePolicy2)
        self.checkBox_nfo_criticrating.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_139.addWidget(self.checkBox_nfo_criticrating)


        self.gridLayout_40.addLayout(self.horizontalLayout_139, 9, 1, 1, 1)

        self.horizontalLayout_138 = QHBoxLayout()
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.checkBox_nfo_studio = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_studio.setObjectName(u"checkBox_nfo_studio")
        sizePolicy2.setHeightForWidth(self.checkBox_nfo_studio.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_studio.setSizePolicy(sizePolicy2)
        self.checkBox_nfo_studio.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_138.addWidget(self.checkBox_nfo_studio)

        self.checkBox_nfo_maker = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_maker.setObjectName(u"checkBox_nfo_maker")
        sizePolicy2.setHeightForWidth(self.checkBox_nfo_maker.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_maker.setSizePolicy(sizePolicy2)
        self.checkBox_nfo_maker.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_138.addWidget(self.checkBox_nfo_maker)

        self.checkBox_nfo_publisher = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_publisher.setObjectName(u"checkBox_nfo_publisher")
        sizePolicy2.setHeightForWidth(self.checkBox_nfo_publisher.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_publisher.setSizePolicy(sizePolicy2)

        self.horizontalLayout_138.addWidget(self.checkBox_nfo_publisher)

        self.checkBox_nfo_label = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_label.setObjectName(u"checkBox_nfo_label")
        sizePolicy2.setHeightForWidth(self.checkBox_nfo_label.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_label.setSizePolicy(sizePolicy2)
        self.checkBox_nfo_label.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_138.addWidget(self.checkBox_nfo_label)


        self.gridLayout_40.addLayout(self.horizontalLayout_138, 21, 1, 1, 1)

        self.label_419 = QLabel(self.layoutWidget_10)
        self.label_419.setObjectName(u"label_419")
        sizePolicy3.setHeightForWidth(self.label_419.sizePolicy().hasHeightForWidth())
        self.label_419.setSizePolicy(sizePolicy3)
        self.label_419.setMinimumSize(QSize(130, 30))
        self.label_419.setLayoutDirection(Qt.LeftToRight)
        self.label_419.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_419, 18, 0, 1, 1)

        self.label_417 = QLabel(self.layoutWidget_10)
        self.label_417.setObjectName(u"label_417")
        sizePolicy3.setHeightForWidth(self.label_417.sizePolicy().hasHeightForWidth())
        self.label_417.setSizePolicy(sizePolicy3)
        self.label_417.setMinimumSize(QSize(130, 30))
        self.label_417.setLayoutDirection(Qt.LeftToRight)
        self.label_417.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_417, 17, 0, 1, 1)

        self.horizontalLayout_91 = QHBoxLayout()
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.checkBox_tag_mosaic = QCheckBox(self.layoutWidget_10)
        self.checkBox_tag_mosaic.setObjectName(u"checkBox_tag_mosaic")

        self.horizontalLayout_91.addWidget(self.checkBox_tag_mosaic)

        self.checkBox_tag_series = QCheckBox(self.layoutWidget_10)
        self.checkBox_tag_series.setObjectName(u"checkBox_tag_series")

        self.horizontalLayout_91.addWidget(self.checkBox_tag_series)

        self.checkBox_tag_studio = QCheckBox(self.layoutWidget_10)
        self.checkBox_tag_studio.setObjectName(u"checkBox_tag_studio")

        self.horizontalLayout_91.addWidget(self.checkBox_tag_studio)

        self.checkBox_tag_publisher = QCheckBox(self.layoutWidget_10)
        self.checkBox_tag_publisher.setObjectName(u"checkBox_tag_publisher")

        self.horizontalLayout_91.addWidget(self.checkBox_tag_publisher)


        self.gridLayout_40.addLayout(self.horizontalLayout_91, 15, 1, 1, 1)

        self.horizontalLayout_140 = QHBoxLayout()
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.checkBox_nfo_series = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_series.setObjectName(u"checkBox_nfo_series")
        sizePolicy3.setHeightForWidth(self.checkBox_nfo_series.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_series.setSizePolicy(sizePolicy3)
        self.checkBox_nfo_series.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_140.addWidget(self.checkBox_nfo_series)

        self.checkBox_nfo_tag = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_tag.setObjectName(u"checkBox_nfo_tag")
        sizePolicy2.setHeightForWidth(self.checkBox_nfo_tag.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_tag.setSizePolicy(sizePolicy2)
        self.checkBox_nfo_tag.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_140.addWidget(self.checkBox_nfo_tag)


        self.gridLayout_40.addLayout(self.horizontalLayout_140, 12, 1, 1, 1)

        self.label_384 = QLabel(self.layoutWidget_10)
        self.label_384.setObjectName(u"label_384")
        sizePolicy3.setHeightForWidth(self.label_384.sizePolicy().hasHeightForWidth())
        self.label_384.setSizePolicy(sizePolicy3)
        self.label_384.setMinimumSize(QSize(130, 30))
        self.label_384.setLayoutDirection(Qt.LeftToRight)
        self.label_384.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_384, 2, 0, 1, 1)

        self.label_208 = QLabel(self.layoutWidget_10)
        self.label_208.setObjectName(u"label_208")
        sizePolicy3.setHeightForWidth(self.label_208.sizePolicy().hasHeightForWidth())
        self.label_208.setSizePolicy(sizePolicy3)
        self.label_208.setMinimumSize(QSize(130, 30))
        self.label_208.setLayoutDirection(Qt.LeftToRight)
        self.label_208.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_208, 12, 0, 1, 1)

        self.label_161 = QLabel(self.layoutWidget_10)
        self.label_161.setObjectName(u"label_161")
        sizePolicy3.setHeightForWidth(self.label_161.sizePolicy().hasHeightForWidth())
        self.label_161.setSizePolicy(sizePolicy3)
        self.label_161.setMinimumSize(QSize(130, 30))
        self.label_161.setLayoutDirection(Qt.LeftToRight)
        self.label_161.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_161, 14, 0, 1, 1)

        self.horizontalLayout_147 = QHBoxLayout()
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.label_418 = QLabel(self.layoutWidget_10)
        self.label_418.setObjectName(u"label_418")
        sizePolicy10.setHeightForWidth(self.label_418.sizePolicy().hasHeightForWidth())
        self.label_418.setSizePolicy(sizePolicy10)
        self.label_418.setMinimumSize(QSize(0, 30))
        self.label_418.setLayoutDirection(Qt.LeftToRight)
        self.label_418.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_418.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_147.addWidget(self.label_418)

        self.lineEdit_nfo_tag_publisher = QLineEdit(self.layoutWidget_10)
        self.lineEdit_nfo_tag_publisher.setObjectName(u"lineEdit_nfo_tag_publisher")
        sizePolicy2.setHeightForWidth(self.lineEdit_nfo_tag_publisher.sizePolicy().hasHeightForWidth())
        self.lineEdit_nfo_tag_publisher.setSizePolicy(sizePolicy2)
        self.lineEdit_nfo_tag_publisher.setMinimumSize(QSize(0, 30))
        self.lineEdit_nfo_tag_publisher.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_147.addWidget(self.lineEdit_nfo_tag_publisher)


        self.gridLayout_40.addLayout(self.horizontalLayout_147, 18, 1, 1, 1)

        self.horizontalLayout_137 = QHBoxLayout()
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.checkBox_nfo_release = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_release.setObjectName(u"checkBox_nfo_release")
        sizePolicy3.setHeightForWidth(self.checkBox_nfo_release.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_release.setSizePolicy(sizePolicy3)
        self.checkBox_nfo_release.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_137.addWidget(self.checkBox_nfo_release)

        self.checkBox_nfo_relasedate = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_relasedate.setObjectName(u"checkBox_nfo_relasedate")
        sizePolicy3.setHeightForWidth(self.checkBox_nfo_relasedate.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_relasedate.setSizePolicy(sizePolicy3)
        self.checkBox_nfo_relasedate.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_137.addWidget(self.checkBox_nfo_relasedate)

        self.checkBox_nfo_premiered = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_premiered.setObjectName(u"checkBox_nfo_premiered")

        self.horizontalLayout_137.addWidget(self.checkBox_nfo_premiered)


        self.gridLayout_40.addLayout(self.horizontalLayout_137, 4, 1, 1, 1)

        self.label_334 = QLabel(self.layoutWidget_10)
        self.label_334.setObjectName(u"label_334")
        sizePolicy3.setHeightForWidth(self.label_334.sizePolicy().hasHeightForWidth())
        self.label_334.setSizePolicy(sizePolicy3)
        self.label_334.setMinimumSize(QSize(130, 30))
        self.label_334.setLayoutDirection(Qt.LeftToRight)
        self.label_334.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_334, 20, 0, 1, 1)

        self.label_385 = QLabel(self.layoutWidget_10)
        self.label_385.setObjectName(u"label_385")
        sizePolicy3.setHeightForWidth(self.label_385.sizePolicy().hasHeightForWidth())
        self.label_385.setSizePolicy(sizePolicy3)
        self.label_385.setMinimumSize(QSize(130, 30))
        self.label_385.setLayoutDirection(Qt.LeftToRight)
        self.label_385.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_385, 4, 0, 1, 1)

        self.label_392 = QLabel(self.layoutWidget_10)
        self.label_392.setObjectName(u"label_392")
        sizePolicy3.setHeightForWidth(self.label_392.sizePolicy().hasHeightForWidth())
        self.label_392.setSizePolicy(sizePolicy3)
        self.label_392.setMinimumSize(QSize(130, 30))
        self.label_392.setLayoutDirection(Qt.LeftToRight)
        self.label_392.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_392, 7, 0, 1, 1)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.checkBox_nfo_year = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_year.setObjectName(u"checkBox_nfo_year")
        sizePolicy3.setHeightForWidth(self.checkBox_nfo_year.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_year.setSizePolicy(sizePolicy3)
        self.checkBox_nfo_year.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_40.addWidget(self.checkBox_nfo_year)

        self.checkBox_nfo_runtime = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_runtime.setObjectName(u"checkBox_nfo_runtime")
        sizePolicy3.setHeightForWidth(self.checkBox_nfo_runtime.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_runtime.setSizePolicy(sizePolicy3)
        self.checkBox_nfo_runtime.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_40.addWidget(self.checkBox_nfo_runtime)

        self.checkBox_nfo_wanted = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_wanted.setObjectName(u"checkBox_nfo_wanted")
        self.checkBox_nfo_wanted.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_40.addWidget(self.checkBox_nfo_wanted)


        self.gridLayout_40.addLayout(self.horizontalLayout_40, 8, 1, 1, 1)

        self.label_403 = QLabel(self.layoutWidget_10)
        self.label_403.setObjectName(u"label_403")
        sizePolicy3.setHeightForWidth(self.label_403.sizePolicy().hasHeightForWidth())
        self.label_403.setSizePolicy(sizePolicy3)
        self.label_403.setMinimumSize(QSize(130, 30))
        self.label_403.setLayoutDirection(Qt.LeftToRight)
        self.label_403.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_403, 11, 0, 1, 1)

        self.horizontalLayout_121 = QHBoxLayout()
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.label_393 = QLabel(self.layoutWidget_10)
        self.label_393.setObjectName(u"label_393")
        sizePolicy3.setHeightForWidth(self.label_393.sizePolicy().hasHeightForWidth())
        self.label_393.setSizePolicy(sizePolicy3)
        self.label_393.setMinimumSize(QSize(20, 0))
        self.label_393.setLayoutDirection(Qt.LeftToRight)
        self.label_393.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_121.addWidget(self.label_393)

        self.checkBox_nfo_title_cd = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_title_cd.setObjectName(u"checkBox_nfo_title_cd")

        self.horizontalLayout_121.addWidget(self.checkBox_nfo_title_cd)


        self.gridLayout_40.addLayout(self.horizontalLayout_121, 1, 1, 1, 1)

        self.horizontalLayout_141 = QHBoxLayout()
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.checkBox_nfo_country = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_country.setObjectName(u"checkBox_nfo_country")
        sizePolicy3.setHeightForWidth(self.checkBox_nfo_country.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_country.setSizePolicy(sizePolicy3)
        self.checkBox_nfo_country.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_141.addWidget(self.checkBox_nfo_country)

        self.checkBox_nfo_mpaa = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_mpaa.setObjectName(u"checkBox_nfo_mpaa")
        sizePolicy3.setHeightForWidth(self.checkBox_nfo_mpaa.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_mpaa.setSizePolicy(sizePolicy3)
        self.checkBox_nfo_mpaa.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_141.addWidget(self.checkBox_nfo_mpaa)

        self.checkBox_nfo_customrating = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_customrating.setObjectName(u"checkBox_nfo_customrating")

        self.horizontalLayout_141.addWidget(self.checkBox_nfo_customrating)


        self.gridLayout_40.addLayout(self.horizontalLayout_141, 7, 1, 1, 1)

        self.label_386 = QLabel(self.layoutWidget_10)
        self.label_386.setObjectName(u"label_386")
        sizePolicy3.setHeightForWidth(self.label_386.sizePolicy().hasHeightForWidth())
        self.label_386.setSizePolicy(sizePolicy3)
        self.label_386.setMinimumSize(QSize(130, 30))
        self.label_386.setLayoutDirection(Qt.LeftToRight)
        self.label_386.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_386, 10, 0, 1, 1)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.checkBox_nfo_actor = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_actor.setObjectName(u"checkBox_nfo_actor")
        sizePolicy3.setHeightForWidth(self.checkBox_nfo_actor.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_actor.setSizePolicy(sizePolicy3)
        self.checkBox_nfo_actor.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_34.addWidget(self.checkBox_nfo_actor)

        self.checkBox_nfo_director = QCheckBox(self.layoutWidget_10)
        self.checkBox_nfo_director.setObjectName(u"checkBox_nfo_director")
        sizePolicy2.setHeightForWidth(self.checkBox_nfo_director.sizePolicy().hasHeightForWidth())
        self.checkBox_nfo_director.setSizePolicy(sizePolicy2)
        self.checkBox_nfo_director.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_34.addWidget(self.checkBox_nfo_director)


        self.gridLayout_40.addLayout(self.horizontalLayout_34, 10, 1, 1, 1)

        self.label_395 = QLabel(self.layoutWidget_10)
        self.label_395.setObjectName(u"label_395")
        sizePolicy2.setHeightForWidth(self.label_395.sizePolicy().hasHeightForWidth())
        self.label_395.setSizePolicy(sizePolicy2)
        self.label_395.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_40.addWidget(self.label_395, 13, 1, 1, 1)

        self.label_150 = QLabel(self.layoutWidget_10)
        self.label_150.setObjectName(u"label_150")
        sizePolicy3.setHeightForWidth(self.label_150.sizePolicy().hasHeightForWidth())
        self.label_150.setSizePolicy(sizePolicy3)
        self.label_150.setMinimumSize(QSize(130, 30))
        self.label_150.setLayoutDirection(Qt.LeftToRight)
        self.label_150.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_150, 22, 0, 1, 1)

        self.label_428 = QLabel(self.layoutWidget_10)
        self.label_428.setObjectName(u"label_428")
        sizePolicy10.setHeightForWidth(self.label_428.sizePolicy().hasHeightForWidth())
        self.label_428.setSizePolicy(sizePolicy10)
        self.label_428.setMinimumSize(QSize(0, 30))
        self.label_428.setLayoutDirection(Qt.LeftToRight)
        self.label_428.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_428.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_428, 19, 1, 1, 1)

        self.label_429 = QLabel(self.layoutWidget_10)
        self.label_429.setObjectName(u"label_429")
        sizePolicy3.setHeightForWidth(self.label_429.sizePolicy().hasHeightForWidth())
        self.label_429.setSizePolicy(sizePolicy3)
        self.label_429.setMinimumSize(QSize(130, 30))
        self.label_429.setLayoutDirection(Qt.LeftToRight)
        self.label_429.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_429, 19, 0, 1, 1)

        self.label_389 = QLabel(self.groupBox_81)
        self.label_389.setObjectName(u"label_389")
        self.label_389.setGeometry(QRect(150, 0, 431, 21))
        sizePolicy2.setHeightForWidth(self.label_389.sizePolicy().hasHeightForWidth())
        self.label_389.setSizePolicy(sizePolicy2)
        self.label_389.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.pushButton_field_tips_nfo = QPushButton(self.scrollAreaWidgetContents_13)
        self.pushButton_field_tips_nfo.setObjectName(u"pushButton_field_tips_nfo")
        self.pushButton_field_tips_nfo.setGeometry(QRect(640, 20, 80, 26))
        sizePolicy3.setHeightForWidth(self.pushButton_field_tips_nfo.sizePolicy().hasHeightForWidth())
        self.pushButton_field_tips_nfo.setSizePolicy(sizePolicy3)
        self.pushButton_field_tips_nfo.setMinimumSize(QSize(0, 0))
        self.scrollArea_13.setWidget(self.scrollAreaWidgetContents_13)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.scrollArea_12 = QScrollArea(self.tab_5)
        self.scrollArea_12.setObjectName(u"scrollArea_12")
        self.scrollArea_12.setGeometry(QRect(0, 0, 796, 658))
        self.scrollArea_12.setFrameShape(QFrame.Box)
        self.scrollArea_12.setFrameShadow(QFrame.Sunken)
        self.scrollArea_12.setLineWidth(0)
        self.scrollArea_12.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_12.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_12.setWidgetResizable(False)
        self.scrollAreaWidgetContents_12 = QWidget()
        self.scrollAreaWidgetContents_12.setObjectName(u"scrollAreaWidgetContents_12")
        self.scrollAreaWidgetContents_12.setGeometry(QRect(0, 0, 770, 1550))
        self.groupBox_43 = QGroupBox(self.scrollAreaWidgetContents_12)
        self.groupBox_43.setObjectName(u"groupBox_43")
        self.groupBox_43.setGeometry(QRect(30, 20, 701, 321))
        self.groupBox_43.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_25 = QWidget(self.groupBox_43)
        self.gridLayoutWidget_25.setObjectName(u"gridLayoutWidget_25")
        self.gridLayoutWidget_25.setGeometry(QRect(20, 30, 661, 268))
        self.gridLayout_25 = QGridLayout(self.gridLayoutWidget_25)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_user_id = QLineEdit(self.gridLayoutWidget_25)
        self.lineEdit_user_id.setObjectName(u"lineEdit_user_id")
        sizePolicy2.setHeightForWidth(self.lineEdit_user_id.sizePolicy().hasHeightForWidth())
        self.lineEdit_user_id.setSizePolicy(sizePolicy2)
        self.lineEdit_user_id.setMinimumSize(QSize(300, 30))
        self.lineEdit_user_id.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_25.addWidget(self.lineEdit_user_id, 6, 1, 1, 1)

        self.label_104 = QLabel(self.gridLayoutWidget_25)
        self.label_104.setObjectName(u"label_104")
        sizePolicy3.setHeightForWidth(self.label_104.sizePolicy().hasHeightForWidth())
        self.label_104.setSizePolicy(sizePolicy3)
        self.label_104.setMinimumSize(QSize(130, 30))
        self.label_104.setLayoutDirection(Qt.LeftToRight)
        self.label_104.setFrameShape(QFrame.NoFrame)
        self.label_104.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_104, 1, 0, 1, 1)

        self.label_105 = QLabel(self.gridLayoutWidget_25)
        self.label_105.setObjectName(u"label_105")
        sizePolicy2.setHeightForWidth(self.label_105.sizePolicy().hasHeightForWidth())
        self.label_105.setSizePolicy(sizePolicy2)
        self.label_105.setMinimumSize(QSize(0, 0))
        self.label_105.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_25.addWidget(self.label_105, 5, 1, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.comboBox_pic_actor = QComboBox(self.gridLayoutWidget_25)
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.setObjectName(u"comboBox_pic_actor")
        self.comboBox_pic_actor.setMinimumSize(QSize(0, 40))
        self.comboBox_pic_actor.setMaxVisibleItems(30)

        self.horizontalLayout_19.addWidget(self.comboBox_pic_actor)

        self.pushButton_show_pic_actor = QPushButton(self.gridLayoutWidget_25)
        self.pushButton_show_pic_actor.setObjectName(u"pushButton_show_pic_actor")
        sizePolicy3.setHeightForWidth(self.pushButton_show_pic_actor.sizePolicy().hasHeightForWidth())
        self.pushButton_show_pic_actor.setSizePolicy(sizePolicy3)
        self.pushButton_show_pic_actor.setMinimumSize(QSize(110, 40))
        self.pushButton_show_pic_actor.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.pushButton_show_pic_actor)


        self.gridLayout_25.addLayout(self.horizontalLayout_19, 8, 1, 1, 1)

        self.horizontalLayout_103 = QHBoxLayout()
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.radioButton_server_emby = QRadioButton(self.gridLayoutWidget_25)
        self.radioButton_server_emby.setObjectName(u"radioButton_server_emby")
        self.radioButton_server_emby.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_103.addWidget(self.radioButton_server_emby)

        self.radioButton_server_jellyfin = QRadioButton(self.gridLayoutWidget_25)
        self.radioButton_server_jellyfin.setObjectName(u"radioButton_server_jellyfin")

        self.horizontalLayout_103.addWidget(self.radioButton_server_jellyfin)


        self.gridLayout_25.addLayout(self.horizontalLayout_103, 0, 1, 1, 1)

        self.lineEdit_emby_url = QLineEdit(self.gridLayoutWidget_25)
        self.lineEdit_emby_url.setObjectName(u"lineEdit_emby_url")
        sizePolicy2.setHeightForWidth(self.lineEdit_emby_url.sizePolicy().hasHeightForWidth())
        self.lineEdit_emby_url.setSizePolicy(sizePolicy2)
        self.lineEdit_emby_url.setMinimumSize(QSize(300, 30))
        self.lineEdit_emby_url.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_25.addWidget(self.lineEdit_emby_url, 1, 1, 1, 1)

        self.label_298 = QLabel(self.gridLayoutWidget_25)
        self.label_298.setObjectName(u"label_298")
        sizePolicy3.setHeightForWidth(self.label_298.sizePolicy().hasHeightForWidth())
        self.label_298.setSizePolicy(sizePolicy3)
        self.label_298.setMinimumSize(QSize(130, 30))
        self.label_298.setLayoutDirection(Qt.LeftToRight)
        self.label_298.setFrameShape(QFrame.NoFrame)
        self.label_298.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_298, 8, 0, 1, 1)

        self.label_121 = QLabel(self.gridLayoutWidget_25)
        self.label_121.setObjectName(u"label_121")
        sizePolicy2.setHeightForWidth(self.label_121.sizePolicy().hasHeightForWidth())
        self.label_121.setSizePolicy(sizePolicy2)
        self.label_121.setMinimumSize(QSize(0, 0))
        self.label_121.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_25.addWidget(self.label_121, 2, 1, 1, 1)

        self.label_306 = QLabel(self.gridLayoutWidget_25)
        self.label_306.setObjectName(u"label_306")
        sizePolicy3.setHeightForWidth(self.label_306.sizePolicy().hasHeightForWidth())
        self.label_306.setSizePolicy(sizePolicy3)
        self.label_306.setMinimumSize(QSize(130, 30))
        self.label_306.setLayoutDirection(Qt.LeftToRight)
        self.label_306.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_306, 0, 0, 1, 1)

        self.label_108 = QLabel(self.gridLayoutWidget_25)
        self.label_108.setObjectName(u"label_108")
        sizePolicy3.setHeightForWidth(self.label_108.sizePolicy().hasHeightForWidth())
        self.label_108.setSizePolicy(sizePolicy3)
        self.label_108.setMinimumSize(QSize(130, 30))
        self.label_108.setLayoutDirection(Qt.LeftToRight)
        self.label_108.setFrameShape(QFrame.NoFrame)
        self.label_108.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_108, 6, 0, 1, 1)

        self.label_107 = QLabel(self.gridLayoutWidget_25)
        self.label_107.setObjectName(u"label_107")
        sizePolicy3.setHeightForWidth(self.label_107.sizePolicy().hasHeightForWidth())
        self.label_107.setSizePolicy(sizePolicy3)
        self.label_107.setMinimumSize(QSize(130, 30))
        self.label_107.setLayoutDirection(Qt.LeftToRight)
        self.label_107.setFrameShape(QFrame.NoFrame)
        self.label_107.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_107, 3, 0, 1, 1)

        self.lineEdit_api_key = QLineEdit(self.gridLayoutWidget_25)
        self.lineEdit_api_key.setObjectName(u"lineEdit_api_key")
        sizePolicy2.setHeightForWidth(self.lineEdit_api_key.sizePolicy().hasHeightForWidth())
        self.lineEdit_api_key.setSizePolicy(sizePolicy2)
        self.lineEdit_api_key.setMinimumSize(QSize(300, 30))
        self.lineEdit_api_key.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_25.addWidget(self.lineEdit_api_key, 3, 1, 1, 1)

        self.label_109 = QLabel(self.gridLayoutWidget_25)
        self.label_109.setObjectName(u"label_109")
        sizePolicy2.setHeightForWidth(self.label_109.sizePolicy().hasHeightForWidth())
        self.label_109.setSizePolicy(sizePolicy2)
        self.label_109.setMinimumSize(QSize(0, 0))
        self.label_109.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_25.addWidget(self.label_109, 7, 1, 1, 1)

        self.groupBox_41 = QGroupBox(self.scrollAreaWidgetContents_12)
        self.groupBox_41.setObjectName(u"groupBox_41")
        self.groupBox_41.setGeometry(QRect(30, 770, 701, 501))
        self.groupBox_41.setMinimumSize(QSize(200, 0))
        self.groupBox_41.setMaximumSize(QSize(739, 16777215))
        self.pushButton_add_actor_pic = QPushButton(self.groupBox_41)
        self.pushButton_add_actor_pic.setObjectName(u"pushButton_add_actor_pic")
        self.pushButton_add_actor_pic.setGeometry(QRect(160, 440, 261, 40))
        self.label_297 = QLabel(self.groupBox_41)
        self.label_297.setObjectName(u"label_297")
        self.label_297.setGeometry(QRect(50, 20, 541, 41))
        sizePolicy2.setHeightForWidth(self.label_297.sizePolicy().hasHeightForWidth())
        self.label_297.setSizePolicy(sizePolicy2)
        self.label_297.setMinimumSize(QSize(0, 0))
        self.label_297.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_297.setWordWrap(True)
        self.checkBox_actor_photo_auto = QCheckBox(self.groupBox_41)
        self.checkBox_actor_photo_auto.setObjectName(u"checkBox_actor_photo_auto")
        self.checkBox_actor_photo_auto.setGeometry(QRect(450, 440, 191, 40))
        sizePolicy4.setHeightForWidth(self.checkBox_actor_photo_auto.sizePolicy().hasHeightForWidth())
        self.checkBox_actor_photo_auto.setSizePolicy(sizePolicy4)
        self.checkBox_actor_photo_auto.setMinimumSize(QSize(0, 30))
        self.frame_2 = QFrame(self.groupBox_41)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 370, 661, 51))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.layoutWidget_12 = QWidget(self.frame_2)
        self.layoutWidget_12.setObjectName(u"layoutWidget_12")
        self.layoutWidget_12.setGeometry(QRect(140, 1, 511, 41))
        self.horizontalLayout_96 = QHBoxLayout(self.layoutWidget_12)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.radioButton_actor_photo_all = QRadioButton(self.layoutWidget_12)
        self.radioButton_actor_photo_all.setObjectName(u"radioButton_actor_photo_all")
        self.radioButton_actor_photo_all.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_96.addWidget(self.radioButton_actor_photo_all)

        self.radioButton_actor_photo_miss = QRadioButton(self.layoutWidget_12)
        self.radioButton_actor_photo_miss.setObjectName(u"radioButton_actor_photo_miss")

        self.horizontalLayout_96.addWidget(self.radioButton_actor_photo_miss)

        self.label_296 = QLabel(self.frame_2)
        self.label_296.setObjectName(u"label_296")
        self.label_296.setGeometry(QRect(0, 5, 130, 31))
        sizePolicy3.setHeightForWidth(self.label_296.sizePolicy().hasHeightForWidth())
        self.label_296.setSizePolicy(sizePolicy3)
        self.label_296.setMinimumSize(QSize(130, 0))
        self.label_296.setLayoutDirection(Qt.RightToLeft)
        self.label_296.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.layoutWidget_8 = QWidget(self.groupBox_41)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(20, 60, 661, 301))
        self.gridLayout = QGridLayout(self.layoutWidget_8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_77 = QLabel(self.layoutWidget_8)
        self.label_77.setObjectName(u"label_77")
        sizePolicy2.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy2)
        self.label_77.setMinimumSize(QSize(0, 0))
        self.label_77.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout.addWidget(self.label_77, 6, 1, 1, 1)

        self.label_293 = QLabel(self.layoutWidget_8)
        self.label_293.setObjectName(u"label_293")
        sizePolicy3.setHeightForWidth(self.label_293.sizePolicy().hasHeightForWidth())
        self.label_293.setSizePolicy(sizePolicy3)
        self.label_293.setMinimumSize(QSize(130, 30))
        self.label_293.setLayoutDirection(Qt.LeftToRight)
        self.label_293.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_293, 0, 0, 1, 1)

        self.label_101 = QLabel(self.layoutWidget_8)
        self.label_101.setObjectName(u"label_101")
        sizePolicy3.setHeightForWidth(self.label_101.sizePolicy().hasHeightForWidth())
        self.label_101.setSizePolicy(sizePolicy3)
        self.label_101.setMinimumSize(QSize(130, 30))
        self.label_101.setLayoutDirection(Qt.LeftToRight)
        self.label_101.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_101, 5, 0, 1, 1)

        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.checkBox_actor_photo_ne_backdrop = QCheckBox(self.layoutWidget_8)
        self.checkBox_actor_photo_ne_backdrop.setObjectName(u"checkBox_actor_photo_ne_backdrop")
        sizePolicy2.setHeightForWidth(self.checkBox_actor_photo_ne_backdrop.sizePolicy().hasHeightForWidth())
        self.checkBox_actor_photo_ne_backdrop.setSizePolicy(sizePolicy2)
        self.checkBox_actor_photo_ne_backdrop.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_93.addWidget(self.checkBox_actor_photo_ne_backdrop)

        self.checkBox_actor_photo_ne_face = QCheckBox(self.layoutWidget_8)
        self.checkBox_actor_photo_ne_face.setObjectName(u"checkBox_actor_photo_ne_face")
        sizePolicy2.setHeightForWidth(self.checkBox_actor_photo_ne_face.sizePolicy().hasHeightForWidth())
        self.checkBox_actor_photo_ne_face.setSizePolicy(sizePolicy2)
        self.checkBox_actor_photo_ne_face.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_93.addWidget(self.checkBox_actor_photo_ne_face)

        self.checkBox_actor_photo_ne_new = QCheckBox(self.layoutWidget_8)
        self.checkBox_actor_photo_ne_new.setObjectName(u"checkBox_actor_photo_ne_new")
        sizePolicy2.setHeightForWidth(self.checkBox_actor_photo_ne_new.sizePolicy().hasHeightForWidth())
        self.checkBox_actor_photo_ne_new.setSizePolicy(sizePolicy2)
        self.checkBox_actor_photo_ne_new.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_93.addWidget(self.checkBox_actor_photo_ne_new)


        self.gridLayout.addLayout(self.horizontalLayout_93, 3, 1, 1, 1)

        self.lineEdit_net_actor_photo = QLineEdit(self.layoutWidget_8)
        self.lineEdit_net_actor_photo.setObjectName(u"lineEdit_net_actor_photo")
        sizePolicy2.setHeightForWidth(self.lineEdit_net_actor_photo.sizePolicy().hasHeightForWidth())
        self.lineEdit_net_actor_photo.setSizePolicy(sizePolicy2)
        self.lineEdit_net_actor_photo.setMinimumSize(QSize(300, 30))
        self.lineEdit_net_actor_photo.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_net_actor_photo, 1, 1, 1, 1)

        self.label_327 = QLabel(self.layoutWidget_8)
        self.label_327.setObjectName(u"label_327")
        sizePolicy3.setHeightForWidth(self.label_327.sizePolicy().hasHeightForWidth())
        self.label_327.setSizePolicy(sizePolicy3)
        self.label_327.setMinimumSize(QSize(130, 30))
        self.label_327.setLayoutDirection(Qt.LeftToRight)
        self.label_327.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_327, 3, 0, 1, 1)

        self.horizontalLayout_95 = QHBoxLayout()
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.radioButton_actor_photo_net = QRadioButton(self.layoutWidget_8)
        self.radioButton_actor_photo_net.setObjectName(u"radioButton_actor_photo_net")
        sizePolicy2.setHeightForWidth(self.radioButton_actor_photo_net.sizePolicy().hasHeightForWidth())
        self.radioButton_actor_photo_net.setSizePolicy(sizePolicy2)

        self.horizontalLayout_95.addWidget(self.radioButton_actor_photo_net)

        self.radioButton_actor_photo_local = QRadioButton(self.layoutWidget_8)
        self.radioButton_actor_photo_local.setObjectName(u"radioButton_actor_photo_local")
        sizePolicy3.setHeightForWidth(self.radioButton_actor_photo_local.sizePolicy().hasHeightForWidth())
        self.radioButton_actor_photo_local.setSizePolicy(sizePolicy3)
        self.radioButton_actor_photo_local.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_95.addWidget(self.radioButton_actor_photo_local)

        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.label_download_actor_zip = QLabel(self.layoutWidget_8)
        self.label_download_actor_zip.setObjectName(u"label_download_actor_zip")
        sizePolicy2.setHeightForWidth(self.label_download_actor_zip.sizePolicy().hasHeightForWidth())
        self.label_download_actor_zip.setSizePolicy(sizePolicy2)
        self.label_download_actor_zip.setMinimumSize(QSize(0, 0))
        self.label_download_actor_zip.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.label_download_actor_zip.setLayoutDirection(Qt.RightToLeft)
        self.label_download_actor_zip.setStyleSheet(u"color: rgb(10, 52, 255);")
        self.label_download_actor_zip.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_97.addWidget(self.label_download_actor_zip)


        self.horizontalLayout_95.addLayout(self.horizontalLayout_97)


        self.gridLayout.addLayout(self.horizontalLayout_95, 0, 1, 1, 1)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.lineEdit_actor_photo_folder = QLineEdit(self.layoutWidget_8)
        self.lineEdit_actor_photo_folder.setObjectName(u"lineEdit_actor_photo_folder")
        sizePolicy2.setHeightForWidth(self.lineEdit_actor_photo_folder.sizePolicy().hasHeightForWidth())
        self.lineEdit_actor_photo_folder.setSizePolicy(sizePolicy2)
        self.lineEdit_actor_photo_folder.setMinimumSize(QSize(300, 30))
        self.lineEdit_actor_photo_folder.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_30.addWidget(self.lineEdit_actor_photo_folder)

        self.pushButton_select_actor_photo_folder = QPushButton(self.layoutWidget_8)
        self.pushButton_select_actor_photo_folder.setObjectName(u"pushButton_select_actor_photo_folder")
        sizePolicy3.setHeightForWidth(self.pushButton_select_actor_photo_folder.sizePolicy().hasHeightForWidth())
        self.pushButton_select_actor_photo_folder.setSizePolicy(sizePolicy3)
        self.pushButton_select_actor_photo_folder.setMinimumSize(QSize(110, 40))

        self.horizontalLayout_30.addWidget(self.pushButton_select_actor_photo_folder)


        self.gridLayout.addLayout(self.horizontalLayout_30, 5, 1, 1, 1)

        self.label_303 = QLabel(self.layoutWidget_8)
        self.label_303.setObjectName(u"label_303")
        sizePolicy3.setHeightForWidth(self.label_303.sizePolicy().hasHeightForWidth())
        self.label_303.setSizePolicy(sizePolicy3)
        self.label_303.setMinimumSize(QSize(130, 30))
        self.label_303.setLayoutDirection(Qt.LeftToRight)
        self.label_303.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_303, 1, 0, 1, 1)

        self.label_123 = QLabel(self.layoutWidget_8)
        self.label_123.setObjectName(u"label_123")
        sizePolicy2.setHeightForWidth(self.label_123.sizePolicy().hasHeightForWidth())
        self.label_123.setSizePolicy(sizePolicy2)
        self.label_123.setMinimumSize(QSize(0, 0))
        self.label_123.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout.addWidget(self.label_123, 4, 1, 1, 1)

        self.label_159 = QLabel(self.layoutWidget_8)
        self.label_159.setObjectName(u"label_159")
        sizePolicy2.setHeightForWidth(self.label_159.sizePolicy().hasHeightForWidth())
        self.label_159.setSizePolicy(sizePolicy2)
        self.label_159.setMinimumSize(QSize(0, 0))
        self.label_159.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout.addWidget(self.label_159, 2, 1, 1, 1)

        self.pushButton_add_actor_pic.raise_()
        self.label_297.raise_()
        self.checkBox_actor_photo_auto.raise_()
        self.layoutWidget_8.raise_()
        self.frame_2.raise_()
        self.groupBox_64 = QGroupBox(self.scrollAreaWidgetContents_12)
        self.groupBox_64.setObjectName(u"groupBox_64")
        self.groupBox_64.setGeometry(QRect(30, 360, 701, 391))
        self.groupBox_64.setMinimumSize(QSize(200, 0))
        self.groupBox_64.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_14 = QWidget(self.groupBox_64)
        self.gridLayoutWidget_14.setObjectName(u"gridLayoutWidget_14")
        self.gridLayoutWidget_14.setGeometry(QRect(20, 60, 661, 191))
        self.gridLayout_14 = QGridLayout(self.gridLayoutWidget_14)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_92 = QHBoxLayout()
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.radioButton_actor_info_zh_cn = QRadioButton(self.gridLayoutWidget_14)
        self.radioButton_actor_info_zh_cn.setObjectName(u"radioButton_actor_info_zh_cn")
        self.radioButton_actor_info_zh_cn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_92.addWidget(self.radioButton_actor_info_zh_cn)

        self.radioButton_actor_info_zh_tw = QRadioButton(self.gridLayoutWidget_14)
        self.radioButton_actor_info_zh_tw.setObjectName(u"radioButton_actor_info_zh_tw")

        self.horizontalLayout_92.addWidget(self.radioButton_actor_info_zh_tw)

        self.radioButton_actor_info_ja = QRadioButton(self.gridLayoutWidget_14)
        self.radioButton_actor_info_ja.setObjectName(u"radioButton_actor_info_ja")

        self.horizontalLayout_92.addWidget(self.radioButton_actor_info_ja)


        self.gridLayout_14.addLayout(self.horizontalLayout_92, 0, 1, 1, 1)

        self.frame_8 = QFrame(self.gridLayoutWidget_14)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.layoutWidget_30 = QWidget(self.frame_8)
        self.layoutWidget_30.setObjectName(u"layoutWidget_30")
        self.layoutWidget_30.setGeometry(QRect(140, 10, 511, 32))
        self.horizontalLayout_153 = QHBoxLayout(self.layoutWidget_30)
        self.horizontalLayout_153.setObjectName(u"horizontalLayout_153")
        self.horizontalLayout_153.setContentsMargins(0, 0, 0, 0)
        self.radioButton_actor_info_all_2 = QRadioButton(self.layoutWidget_30)
        self.radioButton_actor_info_all_2.setObjectName(u"radioButton_actor_info_all_2")
        self.radioButton_actor_info_all_2.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_153.addWidget(self.radioButton_actor_info_all_2)

        self.radioButton_actor_info_miss_2 = QRadioButton(self.layoutWidget_30)
        self.radioButton_actor_info_miss_2.setObjectName(u"radioButton_actor_info_miss_2")

        self.horizontalLayout_153.addWidget(self.radioButton_actor_info_miss_2)

        self.label_431 = QLabel(self.frame_8)
        self.label_431.setObjectName(u"label_431")
        self.label_431.setGeometry(QRect(0, 0, 130, 41))
        sizePolicy3.setHeightForWidth(self.label_431.sizePolicy().hasHeightForWidth())
        self.label_431.setSizePolicy(sizePolicy3)
        self.label_431.setMinimumSize(QSize(130, 30))
        self.label_431.setLayoutDirection(Qt.LeftToRight)
        self.label_431.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_14.addWidget(self.frame_8, 3, 0, 1, 1)

        self.horizontalLayout_155 = QHBoxLayout()
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.lineEdit_actor_db_path = QLineEdit(self.gridLayoutWidget_14)
        self.lineEdit_actor_db_path.setObjectName(u"lineEdit_actor_db_path")
        sizePolicy2.setHeightForWidth(self.lineEdit_actor_db_path.sizePolicy().hasHeightForWidth())
        self.lineEdit_actor_db_path.setSizePolicy(sizePolicy2)
        self.lineEdit_actor_db_path.setMinimumSize(QSize(300, 30))
        self.lineEdit_actor_db_path.setStyleSheet(u"font: \"Courier\";\n"
"                                       border: 1px solid rgba(0,0,0, 50);\n"
"                                       border-radius: 15px;\n"
"                                   ")

        self.horizontalLayout_155.addWidget(self.lineEdit_actor_db_path)

        self.pushButton_select_actor_info_db = QPushButton(self.gridLayoutWidget_14)
        self.pushButton_select_actor_info_db.setObjectName(u"pushButton_select_actor_info_db")
        sizePolicy3.setHeightForWidth(self.pushButton_select_actor_info_db.sizePolicy().hasHeightForWidth())
        self.pushButton_select_actor_info_db.setSizePolicy(sizePolicy3)
        self.pushButton_select_actor_info_db.setMinimumSize(QSize(110, 40))

        self.horizontalLayout_155.addWidget(self.pushButton_select_actor_info_db)


        self.gridLayout_14.addLayout(self.horizontalLayout_155, 3, 1, 1, 1)

        self.frame_9 = QFrame(self.gridLayoutWidget_14)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.layoutWidget_38 = QWidget(self.frame_9)
        self.layoutWidget_38.setObjectName(u"layoutWidget_38")
        self.layoutWidget_38.setGeometry(QRect(140, 10, 511, 32))
        self.horizontalLayout_154 = QHBoxLayout(self.layoutWidget_38)
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.horizontalLayout_154.setContentsMargins(0, 0, 0, 0)
        self.radioButton_actor_info_all_3 = QRadioButton(self.layoutWidget_38)
        self.radioButton_actor_info_all_3.setObjectName(u"radioButton_actor_info_all_3")
        self.radioButton_actor_info_all_3.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_154.addWidget(self.radioButton_actor_info_all_3)

        self.radioButton_actor_info_miss_3 = QRadioButton(self.layoutWidget_38)
        self.radioButton_actor_info_miss_3.setObjectName(u"radioButton_actor_info_miss_3")

        self.horizontalLayout_154.addWidget(self.radioButton_actor_info_miss_3)


        self.gridLayout_14.addWidget(self.frame_9, 4, 0, 1, 1)

        self.horizontalLayout_158 = QHBoxLayout()
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.horizontalLayout_159 = QHBoxLayout()
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.horizontalLayout_159.setContentsMargins(20, -1, -1, -1)
        self.checkBox_actor_db = QCheckBox(self.gridLayoutWidget_14)
        self.checkBox_actor_db.setObjectName(u"checkBox_actor_db")
        sizePolicy3.setHeightForWidth(self.checkBox_actor_db.sizePolicy().hasHeightForWidth())
        self.checkBox_actor_db.setSizePolicy(sizePolicy3)
        self.checkBox_actor_db.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_159.addWidget(self.checkBox_actor_db)

        self.label_download_actor_db = QLabel(self.gridLayoutWidget_14)
        self.label_download_actor_db.setObjectName(u"label_download_actor_db")
        sizePolicy2.setHeightForWidth(self.label_download_actor_db.sizePolicy().hasHeightForWidth())
        self.label_download_actor_db.setSizePolicy(sizePolicy2)
        self.label_download_actor_db.setMinimumSize(QSize(0, 0))
        self.label_download_actor_db.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.label_download_actor_db.setLayoutDirection(Qt.LeftToRight)
        self.label_download_actor_db.setStyleSheet(u"color: rgb(10, 52, 255);")
        self.label_download_actor_db.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_159.addWidget(self.label_download_actor_db)

        self.horizontalLayout_160 = QHBoxLayout()
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")

        self.horizontalLayout_159.addLayout(self.horizontalLayout_160)


        self.horizontalLayout_158.addLayout(self.horizontalLayout_159)


        self.gridLayout_14.addLayout(self.horizontalLayout_158, 4, 1, 1, 1)

        self.label_291 = QLabel(self.gridLayoutWidget_14)
        self.label_291.setObjectName(u"label_291")
        sizePolicy3.setHeightForWidth(self.label_291.sizePolicy().hasHeightForWidth())
        self.label_291.setSizePolicy(sizePolicy3)
        self.label_291.setMinimumSize(QSize(130, 30))
        self.label_291.setLayoutDirection(Qt.LeftToRight)
        self.label_291.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_14.addWidget(self.label_291, 0, 0, 1, 1)

        self.horizontalLayout_98 = QHBoxLayout()
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.label_280 = QLabel(self.gridLayoutWidget_14)
        self.label_280.setObjectName(u"label_280")
        sizePolicy3.setHeightForWidth(self.label_280.sizePolicy().hasHeightForWidth())
        self.label_280.setSizePolicy(sizePolicy3)
        self.label_280.setMinimumSize(QSize(10, 0))
        self.label_280.setLayoutDirection(Qt.RightToLeft)
        self.label_280.setFrameShape(QFrame.NoFrame)
        self.label_280.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_98.addWidget(self.label_280)

        self.horizontalLayout_100 = QHBoxLayout()
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.checkBox_actor_info_translate = QCheckBox(self.gridLayoutWidget_14)
        self.checkBox_actor_info_translate.setObjectName(u"checkBox_actor_info_translate")
        sizePolicy3.setHeightForWidth(self.checkBox_actor_info_translate.sizePolicy().hasHeightForWidth())
        self.checkBox_actor_info_translate.setSizePolicy(sizePolicy3)
        self.checkBox_actor_info_translate.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_100.addWidget(self.checkBox_actor_info_translate)

        self.label_106 = QLabel(self.gridLayoutWidget_14)
        self.label_106.setObjectName(u"label_106")
        sizePolicy2.setHeightForWidth(self.label_106.sizePolicy().hasHeightForWidth())
        self.label_106.setSizePolicy(sizePolicy2)
        self.label_106.setMinimumSize(QSize(0, 0))
        self.label_106.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.horizontalLayout_100.addWidget(self.label_106)


        self.horizontalLayout_98.addLayout(self.horizontalLayout_100)


        self.gridLayout_14.addLayout(self.horizontalLayout_98, 2, 1, 1, 1)

        self.pushButton_add_actor_info = QPushButton(self.groupBox_64)
        self.pushButton_add_actor_info.setObjectName(u"pushButton_add_actor_info")
        self.pushButton_add_actor_info.setGeometry(QRect(160, 320, 261, 40))
        self.label_295 = QLabel(self.groupBox_64)
        self.label_295.setObjectName(u"label_295")
        self.label_295.setGeometry(QRect(50, 20, 631, 41))
        sizePolicy2.setHeightForWidth(self.label_295.sizePolicy().hasHeightForWidth())
        self.label_295.setSizePolicy(sizePolicy2)
        self.label_295.setMinimumSize(QSize(0, 0))
        self.label_295.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_295.setWordWrap(True)
        self.frame_4 = QFrame(self.groupBox_64)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 250, 661, 51))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.layoutWidget_15 = QWidget(self.frame_4)
        self.layoutWidget_15.setObjectName(u"layoutWidget_15")
        self.layoutWidget_15.setGeometry(QRect(140, 10, 511, 32))
        self.horizontalLayout_101 = QHBoxLayout(self.layoutWidget_15)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.radioButton_actor_info_all = QRadioButton(self.layoutWidget_15)
        self.radioButton_actor_info_all.setObjectName(u"radioButton_actor_info_all")
        self.radioButton_actor_info_all.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_101.addWidget(self.radioButton_actor_info_all)

        self.radioButton_actor_info_miss = QRadioButton(self.layoutWidget_15)
        self.radioButton_actor_info_miss.setObjectName(u"radioButton_actor_info_miss")

        self.horizontalLayout_101.addWidget(self.radioButton_actor_info_miss)

        self.label_299 = QLabel(self.frame_4)
        self.label_299.setObjectName(u"label_299")
        self.label_299.setGeometry(QRect(0, 20, 130, 16))
        sizePolicy3.setHeightForWidth(self.label_299.sizePolicy().hasHeightForWidth())
        self.label_299.setSizePolicy(sizePolicy3)
        self.label_299.setMinimumSize(QSize(130, 0))
        self.label_299.setLayoutDirection(Qt.RightToLeft)
        self.label_299.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.checkBox_actor_info_photo = QCheckBox(self.groupBox_64)
        self.checkBox_actor_info_photo.setObjectName(u"checkBox_actor_info_photo")
        self.checkBox_actor_info_photo.setGeometry(QRect(450, 320, 191, 40))
        sizePolicy4.setHeightForWidth(self.checkBox_actor_info_photo.sizePolicy().hasHeightForWidth())
        self.checkBox_actor_info_photo.setSizePolicy(sizePolicy4)
        self.checkBox_actor_info_photo.setMinimumSize(QSize(0, 30))
        self.groupBox_68 = QGroupBox(self.scrollAreaWidgetContents_12)
        self.groupBox_68.setObjectName(u"groupBox_68")
        self.groupBox_68.setGeometry(QRect(30, 1290, 701, 191))
        self.groupBox_68.setMinimumSize(QSize(200, 0))
        self.groupBox_68.setMaximumSize(QSize(739, 16777215))
        self.pushButton_add_actor_pic_kodi = QPushButton(self.groupBox_68)
        self.pushButton_add_actor_pic_kodi.setObjectName(u"pushButton_add_actor_pic_kodi")
        self.pushButton_add_actor_pic_kodi.setGeometry(QRect(160, 130, 161, 40))
        self.label_414 = QLabel(self.groupBox_68)
        self.label_414.setObjectName(u"label_414")
        self.label_414.setGeometry(QRect(50, 20, 631, 41))
        sizePolicy2.setHeightForWidth(self.label_414.sizePolicy().hasHeightForWidth())
        self.label_414.setSizePolicy(sizePolicy2)
        self.label_414.setMinimumSize(QSize(0, 0))
        self.label_414.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_414.setWordWrap(True)
        self.frame_7 = QFrame(self.groupBox_68)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(20, 60, 661, 51))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.layoutWidget_28 = QWidget(self.frame_7)
        self.layoutWidget_28.setObjectName(u"layoutWidget_28")
        self.layoutWidget_28.setGeometry(QRect(140, 10, 511, 32))
        self.horizontalLayout_148 = QHBoxLayout(self.layoutWidget_28)
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.horizontalLayout_148.setContentsMargins(0, 0, 0, 0)
        self.checkBox_actor_pic_replace = QCheckBox(self.layoutWidget_28)
        self.checkBox_actor_pic_replace.setObjectName(u"checkBox_actor_pic_replace")
        sizePolicy4.setHeightForWidth(self.checkBox_actor_pic_replace.sizePolicy().hasHeightForWidth())
        self.checkBox_actor_pic_replace.setSizePolicy(sizePolicy4)
        self.checkBox_actor_pic_replace.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_148.addWidget(self.checkBox_actor_pic_replace)

        self.label_415 = QLabel(self.frame_7)
        self.label_415.setObjectName(u"label_415")
        self.label_415.setGeometry(QRect(0, 20, 130, 16))
        sizePolicy3.setHeightForWidth(self.label_415.sizePolicy().hasHeightForWidth())
        self.label_415.setSizePolicy(sizePolicy3)
        self.label_415.setMinimumSize(QSize(130, 0))
        self.label_415.setLayoutDirection(Qt.RightToLeft)
        self.label_415.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_del_actor_folder = QPushButton(self.groupBox_68)
        self.pushButton_del_actor_folder.setObjectName(u"pushButton_del_actor_folder")
        self.pushButton_del_actor_folder.setGeometry(QRect(490, 130, 171, 40))
        self.checkBox_actor_photo_kodi = QCheckBox(self.groupBox_68)
        self.checkBox_actor_photo_kodi.setObjectName(u"checkBox_actor_photo_kodi")
        self.checkBox_actor_photo_kodi.setGeometry(QRect(340, 130, 141, 40))
        sizePolicy4.setHeightForWidth(self.checkBox_actor_photo_kodi.sizePolicy().hasHeightForWidth())
        self.checkBox_actor_photo_kodi.setSizePolicy(sizePolicy4)
        self.checkBox_actor_photo_kodi.setMinimumSize(QSize(0, 30))
        self.scrollArea_12.setWidget(self.scrollAreaWidgetContents_12)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.scrollArea_3 = QScrollArea(self.tab3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(0, 0, 796, 658))
        self.scrollArea_3.setFrameShape(QFrame.Box)
        self.scrollArea_3.setLineWidth(0)
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(False)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 760, 1450))
        self.groupBox_10 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(30, 350, 701, 531))
        self.groupBox_10.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_10 = QWidget(self.groupBox_10)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(20, 30, 661, 280))
        self.gridLayout_10 = QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_cookie_javbus = QPlainTextEdit(self.gridLayoutWidget_10)
        self.plainTextEdit_cookie_javbus.setObjectName(u"plainTextEdit_cookie_javbus")
        self.plainTextEdit_cookie_javbus.setMinimumSize(QSize(300, 80))
        self.plainTextEdit_cookie_javbus.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 1px;\n"
"font: \"Courier\";")

        self.gridLayout_10.addWidget(self.plainTextEdit_cookie_javbus, 2, 1, 1, 1)

        self.plainTextEdit_cookie_javdb = QPlainTextEdit(self.gridLayoutWidget_10)
        self.plainTextEdit_cookie_javdb.setObjectName(u"plainTextEdit_cookie_javdb")
        self.plainTextEdit_cookie_javdb.setMinimumSize(QSize(300, 80))
        self.plainTextEdit_cookie_javdb.setStyleSheet(u" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 1px;\n"
"font: \"Courier\";")

        self.gridLayout_10.addWidget(self.plainTextEdit_cookie_javdb, 0, 1, 1, 1)

        self.horizontalLayout_151 = QHBoxLayout()
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.pushButton_check_javdb_cookie = QPushButton(self.gridLayoutWidget_10)
        self.pushButton_check_javdb_cookie.setObjectName(u"pushButton_check_javdb_cookie")
        sizePolicy3.setHeightForWidth(self.pushButton_check_javdb_cookie.sizePolicy().hasHeightForWidth())
        self.pushButton_check_javdb_cookie.setSizePolicy(sizePolicy3)

        self.horizontalLayout_151.addWidget(self.pushButton_check_javdb_cookie)

        self.label_javdb_cookie_result = QLabel(self.gridLayoutWidget_10)
        self.label_javdb_cookie_result.setObjectName(u"label_javdb_cookie_result")
        sizePolicy6.setHeightForWidth(self.label_javdb_cookie_result.sizePolicy().hasHeightForWidth())
        self.label_javdb_cookie_result.setSizePolicy(sizePolicy6)
        self.label_javdb_cookie_result.setMinimumSize(QSize(0, 0))
        self.label_javdb_cookie_result.setLayoutDirection(Qt.RightToLeft)
        self.label_javdb_cookie_result.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_151.addWidget(self.label_javdb_cookie_result)


        self.gridLayout_10.addLayout(self.horizontalLayout_151, 1, 1, 1, 1)

        self.label_425 = QLabel(self.gridLayoutWidget_10)
        self.label_425.setObjectName(u"label_425")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.label_425.sizePolicy().hasHeightForWidth())
        self.label_425.setSizePolicy(sizePolicy11)
        self.label_425.setMinimumSize(QSize(0, 30))
        self.label_425.setLayoutDirection(Qt.RightToLeft)
        self.label_425.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_425, 2, 0, 1, 1)

        self.label_45 = QLabel(self.gridLayoutWidget_10)
        self.label_45.setObjectName(u"label_45")
        sizePolicy11.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy11)
        self.label_45.setMinimumSize(QSize(0, 30))
        self.label_45.setLayoutDirection(Qt.RightToLeft)
        self.label_45.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_45, 0, 0, 1, 1)

        self.horizontalLayout_152 = QHBoxLayout()
        self.horizontalLayout_152.setObjectName(u"horizontalLayout_152")
        self.pushButton_check_javbus_cookie = QPushButton(self.gridLayoutWidget_10)
        self.pushButton_check_javbus_cookie.setObjectName(u"pushButton_check_javbus_cookie")
        sizePolicy3.setHeightForWidth(self.pushButton_check_javbus_cookie.sizePolicy().hasHeightForWidth())
        self.pushButton_check_javbus_cookie.setSizePolicy(sizePolicy3)

        self.horizontalLayout_152.addWidget(self.pushButton_check_javbus_cookie)

        self.label_javbus_cookie_result = QLabel(self.gridLayoutWidget_10)
        self.label_javbus_cookie_result.setObjectName(u"label_javbus_cookie_result")
        sizePolicy6.setHeightForWidth(self.label_javbus_cookie_result.sizePolicy().hasHeightForWidth())
        self.label_javbus_cookie_result.setSizePolicy(sizePolicy6)
        self.label_javbus_cookie_result.setMinimumSize(QSize(0, 0))
        self.label_javbus_cookie_result.setLayoutDirection(Qt.RightToLeft)
        self.label_javbus_cookie_result.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_152.addWidget(self.label_javbus_cookie_result)


        self.gridLayout_10.addLayout(self.horizontalLayout_152, 3, 1, 1, 1)

        self.label_75 = QLabel(self.groupBox_10)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(60, 330, 611, 141))
        sizePolicy2.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy2)
        self.label_75.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_75.setScaledContents(True)
        self.label_75.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_75.setWordWrap(True)
        self.label_75.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_get_cookie_url = QLabel(self.groupBox_10)
        self.label_get_cookie_url.setObjectName(u"label_get_cookie_url")
        self.label_get_cookie_url.setGeometry(QRect(130, 480, 430, 21))
        self.label_get_cookie_url.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_get_cookie_url.setMouseTracking(False)
        self.label_get_cookie_url.setStyleSheet(u"color: rgb(10, 52, 255);")
        self.label_get_cookie_url.setScaledContents(False)
        self.label_get_cookie_url.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_get_cookie_url.setOpenExternalLinks(False)
        self.label_get_cookie_url.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label_7 = QLabel(self.groupBox_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 480, 71, 21))
        self.label_7.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.groupBox_28 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.groupBox_28.setGeometry(QRect(30, 20, 701, 311))
        self.groupBox_28.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_9 = QWidget(self.groupBox_28)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(20, 30, 671, 261))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.checkBox_net_ipv4_only = QCheckBox(self.gridLayoutWidget_9)
        self.checkBox_net_ipv4_only.setObjectName(u"checkBox_net_ipv4_only")

        self.gridLayout_9.addWidget(self.checkBox_net_ipv4_only, 5, 1, 1, 1)

        self.label_64 = QLabel(self.gridLayoutWidget_9)
        self.label_64.setObjectName(u"label_64")
        sizePolicy3.setHeightForWidth(self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy3)
        self.label_64.setMinimumSize(QSize(0, 0))
        self.label_64.setLayoutDirection(Qt.RightToLeft)
        self.label_64.setFrameShape(QFrame.NoFrame)
        self.label_64.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_64, 1, 0, 1, 1)

        self.label_65 = QLabel(self.gridLayoutWidget_9)
        self.label_65.setObjectName(u"label_65")
        sizePolicy3.setHeightForWidth(self.label_65.sizePolicy().hasHeightForWidth())
        self.label_65.setSizePolicy(sizePolicy3)
        self.label_65.setMinimumSize(QSize(0, 0))
        self.label_65.setLayoutDirection(Qt.RightToLeft)
        self.label_65.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_65, 4, 0, 1, 1)

        self.lineEdit_proxy = QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_proxy.setObjectName(u"lineEdit_proxy")
        sizePolicy2.setHeightForWidth(self.lineEdit_proxy.sizePolicy().hasHeightForWidth())
        self.lineEdit_proxy.setSizePolicy(sizePolicy2)
        self.lineEdit_proxy.setMinimumSize(QSize(300, 30))
        self.lineEdit_proxy.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_9.addWidget(self.lineEdit_proxy, 1, 1, 1, 1)

        self.label_103 = QLabel(self.gridLayoutWidget_9)
        self.label_103.setObjectName(u"label_103")
        sizePolicy2.setHeightForWidth(self.label_103.sizePolicy().hasHeightForWidth())
        self.label_103.setSizePolicy(sizePolicy2)
        self.label_103.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_9.addWidget(self.label_103, 2, 1, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.radioButton_proxy_http = QRadioButton(self.gridLayoutWidget_9)
        self.radioButton_proxy_http.setObjectName(u"radioButton_proxy_http")
        self.radioButton_proxy_http.setMinimumSize(QSize(93, 30))

        self.horizontalLayout_17.addWidget(self.radioButton_proxy_http)

        self.radioButton_proxy_socks5 = QRadioButton(self.gridLayoutWidget_9)
        self.radioButton_proxy_socks5.setObjectName(u"radioButton_proxy_socks5")
        self.radioButton_proxy_socks5.setMinimumSize(QSize(93, 30))

        self.horizontalLayout_17.addWidget(self.radioButton_proxy_socks5)

        self.radioButton_proxy_nouse = QRadioButton(self.gridLayoutWidget_9)
        self.radioButton_proxy_nouse.setObjectName(u"radioButton_proxy_nouse")
        self.radioButton_proxy_nouse.setMinimumSize(QSize(93, 30))

        self.horizontalLayout_17.addWidget(self.radioButton_proxy_nouse)


        self.gridLayout_9.addLayout(self.horizontalLayout_17, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSlider_timeout = CustomQSlider(self.gridLayoutWidget_9)
        self.horizontalSlider_timeout.setObjectName(u"horizontalSlider_timeout")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_timeout.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_timeout.setSizePolicy(sizePolicy8)
        self.horizontalSlider_timeout.setMinimumSize(QSize(300, 30))
        self.horizontalSlider_timeout.setMaximumSize(QSize(66666, 30))
        self.horizontalSlider_timeout.setLayoutDirection(Qt.LeftToRight)
        self.horizontalSlider_timeout.setAutoFillBackground(False)
        self.horizontalSlider_timeout.setMinimum(3)
        self.horizontalSlider_timeout.setMaximum(30)
        self.horizontalSlider_timeout.setPageStep(1)
        self.horizontalSlider_timeout.setValue(7)
        self.horizontalSlider_timeout.setTracking(True)
        self.horizontalSlider_timeout.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.horizontalSlider_timeout)

        self.lcdNumber_timeout = QLCDNumber(self.gridLayoutWidget_9)
        self.lcdNumber_timeout.setObjectName(u"lcdNumber_timeout")
        sizePolicy9.setHeightForWidth(self.lcdNumber_timeout.sizePolicy().hasHeightForWidth())
        self.lcdNumber_timeout.setSizePolicy(sizePolicy9)
        self.lcdNumber_timeout.setMinimumSize(QSize(30, 30))
        self.lcdNumber_timeout.setMaximumSize(QSize(70, 30))
        self.lcdNumber_timeout.setDigitCount(2)
        self.lcdNumber_timeout.setMode(QLCDNumber.Dec)
        self.lcdNumber_timeout.setProperty(u"intValue", 10)

        self.horizontalLayout_3.addWidget(self.lcdNumber_timeout)


        self.gridLayout_9.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)

        self.label_410 = QLabel(self.gridLayoutWidget_9)
        self.label_410.setObjectName(u"label_410")
        sizePolicy3.setHeightForWidth(self.label_410.sizePolicy().hasHeightForWidth())
        self.label_410.setSizePolicy(sizePolicy3)
        self.label_410.setMinimumSize(QSize(0, 30))
        self.label_410.setLayoutDirection(Qt.RightToLeft)
        self.label_410.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_410, 5, 0, 1, 1)

        self.horizontalLayout_retry = QHBoxLayout()
        self.horizontalLayout_retry.setObjectName(u"horizontalLayout_retry")
        self.horizontalSlider_retry = CustomQSlider(self.gridLayoutWidget_9)
        self.horizontalSlider_retry.setObjectName(u"horizontalSlider_retry")
        sizePolicy8.setHeightForWidth(self.horizontalSlider_retry.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_retry.setSizePolicy(sizePolicy8)
        self.horizontalSlider_retry.setMinimumSize(QSize(300, 30))
        self.horizontalSlider_retry.setMaximumSize(QSize(66666, 30))
        self.horizontalSlider_retry.setMouseTracking(False)
        self.horizontalSlider_retry.setLayoutDirection(Qt.LeftToRight)
        self.horizontalSlider_retry.setMinimum(2)
        self.horizontalSlider_retry.setMaximum(5)
        self.horizontalSlider_retry.setPageStep(1)
        self.horizontalSlider_retry.setValue(3)
        self.horizontalSlider_retry.setOrientation(Qt.Horizontal)

        self.horizontalLayout_retry.addWidget(self.horizontalSlider_retry)

        self.lcdNumber_retry = QLCDNumber(self.gridLayoutWidget_9)
        self.lcdNumber_retry.setObjectName(u"lcdNumber_retry")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.lcdNumber_retry.sizePolicy().hasHeightForWidth())
        self.lcdNumber_retry.setSizePolicy(sizePolicy12)
        self.lcdNumber_retry.setMinimumSize(QSize(30, 30))
        self.lcdNumber_retry.setMaximumSize(QSize(70, 30))
        self.lcdNumber_retry.setDigitCount(2)
        self.lcdNumber_retry.setProperty(u"intValue", 3)

        self.horizontalLayout_retry.addWidget(self.lcdNumber_retry)


        self.gridLayout_9.addLayout(self.horizontalLayout_retry, 4, 1, 1, 1)

        self.label_70 = QLabel(self.gridLayoutWidget_9)
        self.label_70.setObjectName(u"label_70")
        sizePolicy3.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy3)
        self.label_70.setMinimumSize(QSize(130, 0))
        self.label_70.setLayoutDirection(Qt.RightToLeft)
        self.label_70.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_70, 0, 0, 1, 1)

        self.label_73 = QLabel(self.gridLayoutWidget_9)
        self.label_73.setObjectName(u"label_73")
        sizePolicy3.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy3)
        self.label_73.setMinimumSize(QSize(0, 0))
        self.label_73.setLayoutDirection(Qt.RightToLeft)
        self.label_73.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_73, 3, 0, 1, 1)

        self.label_411 = QLabel(self.gridLayoutWidget_9)
        self.label_411.setObjectName(u"label_411")
        sizePolicy2.setHeightForWidth(self.label_411.sizePolicy().hasHeightForWidth())
        self.label_411.setSizePolicy(sizePolicy2)
        self.label_411.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_9.addWidget(self.label_411, 6, 1, 1, 1)

        self.groupBox_44 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_44.setObjectName(u"groupBox_44")
        self.groupBox_44.setGeometry(QRect(30, 1100, 701, 281))
        self.groupBox_44.setStyleSheet(u"font:\"Courier\";")
        self.label_110 = QLabel(self.groupBox_44)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setGeometry(QRect(60, 120, 581, 111))
        sizePolicy2.setHeightForWidth(self.label_110.sizePolicy().hasHeightForWidth())
        self.label_110.setSizePolicy(sizePolicy2)
        self.label_110.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_110.setOpenExternalLinks(True)
        self.gridLayoutWidget = QWidget(self.groupBox_44)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 30, 661, 62))
        self.gridLayout_12 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.comboBox_custom_website = QComboBox(self.gridLayoutWidget)
        self.comboBox_custom_website.setObjectName(u"comboBox_custom_website")
        self.comboBox_custom_website.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.comboBox_custom_website.sizePolicy().hasHeightForWidth())
        self.comboBox_custom_website.setSizePolicy(sizePolicy1)
        self.comboBox_custom_website.setMaxVisibleItems(20)

        self.gridLayout_12.addWidget(self.comboBox_custom_website, 0, 0, 1, 2)

        self.lineEdit_custom_website = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_custom_website.setObjectName(u"lineEdit_custom_website")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.lineEdit_custom_website.sizePolicy().hasHeightForWidth())
        self.lineEdit_custom_website.setSizePolicy(sizePolicy13)
        self.lineEdit_custom_website.setMinimumSize(QSize(300, 30))
        self.lineEdit_custom_website.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_custom_website.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_12.addWidget(self.lineEdit_custom_website, 0, 2, 1, 1)

        self.gridLayout_12.setColumnStretch(0, 2)
        self.gridLayout_12.setColumnStretch(2, 9)
        self.label_324 = QLabel(self.groupBox_44)
        self.label_324.setObjectName(u"label_324")
        self.label_324.setGeometry(QRect(140, 80, 621, 41))
        sizePolicy3.setHeightForWidth(self.label_324.sizePolicy().hasHeightForWidth())
        self.label_324.setSizePolicy(sizePolicy3)
        self.label_324.setMinimumSize(QSize(130, 0))
        self.label_324.setLayoutDirection(Qt.RightToLeft)
        self.label_324.setStyleSheet(u"color: rgb(255, 38, 0);\n"
"font-weight:bold")
        self.label_324.setFrameShape(QFrame.NoFrame)
        self.label_324.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_324.setWordWrap(True)
        self.groupBox_14 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setGeometry(QRect(30, 900, 701, 181))
        self.groupBox_14.setStyleSheet(u"font:\"Courier\";")
        self.gridLayoutWidget_11 = QWidget(self.groupBox_14)
        self.gridLayoutWidget_11.setObjectName(u"gridLayoutWidget_11")
        self.gridLayoutWidget_11.setGeometry(QRect(20, 30, 661, 51))
        self.gridLayout_65 = QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.gridLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_355 = QLabel(self.gridLayoutWidget_11)
        self.label_355.setObjectName(u"label_355")
        sizePolicy7.setHeightForWidth(self.label_355.sizePolicy().hasHeightForWidth())
        self.label_355.setSizePolicy(sizePolicy7)
        self.label_355.setMinimumSize(QSize(130, 30))
        self.label_355.setLayoutDirection(Qt.RightToLeft)
        self.label_355.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_65.addWidget(self.label_355, 0, 0, 1, 1)

        self.lineEdit_api_token_theporndb = QLineEdit(self.gridLayoutWidget_11)
        self.lineEdit_api_token_theporndb.setObjectName(u"lineEdit_api_token_theporndb")
        sizePolicy2.setHeightForWidth(self.lineEdit_api_token_theporndb.sizePolicy().hasHeightForWidth())
        self.lineEdit_api_token_theporndb.setSizePolicy(sizePolicy2)
        self.lineEdit_api_token_theporndb.setMinimumSize(QSize(300, 30))
        self.lineEdit_api_token_theporndb.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.gridLayout_65.addWidget(self.lineEdit_api_token_theporndb, 0, 1, 1, 1)

        self.label_356 = QLabel(self.groupBox_14)
        self.label_356.setObjectName(u"label_356")
        self.label_356.setGeometry(QRect(120, 90, 561, 41))
        sizePolicy2.setHeightForWidth(self.label_356.sizePolicy().hasHeightForWidth())
        self.label_356.setSizePolicy(sizePolicy2)
        self.label_356.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_356.setScaledContents(True)
        self.label_356.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_356.setWordWrap(True)
        self.label_356.setOpenExternalLinks(True)
        self.label_356.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)
        self.layoutWidget7 = QWidget(self.groupBox_14)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(160, 130, 441, 39))
        self.horizontalLayout_150 = QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.horizontalLayout_150.setContentsMargins(0, 0, 0, 0)
        self.checkBox_theporndb_hash = QCheckBox(self.layoutWidget7)
        self.checkBox_theporndb_hash.setObjectName(u"checkBox_theporndb_hash")
        sizePolicy3.setHeightForWidth(self.checkBox_theporndb_hash.sizePolicy().hasHeightForWidth())
        self.checkBox_theporndb_hash.setSizePolicy(sizePolicy3)

        self.horizontalLayout_150.addWidget(self.checkBox_theporndb_hash)

        self.label_422 = QLabel(self.layoutWidget7)
        self.label_422.setObjectName(u"label_422")
        sizePolicy2.setHeightForWidth(self.label_422.sizePolicy().hasHeightForWidth())
        self.label_422.setSizePolicy(sizePolicy2)
        self.label_422.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_422.setScaledContents(True)
        self.label_422.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_422.setWordWrap(True)
        self.label_422.setOpenExternalLinks(True)
        self.label_422.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.horizontalLayout_150.addWidget(self.label_422)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.tabWidget.addTab(self.tab3, "")
        self.tab5 = QWidget()
        self.tab5.setObjectName(u"tab5")
        self.tab5.setEnabled(True)
        self.scrollArea_5 = QScrollArea(self.tab5)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setGeometry(QRect(0, 0, 796, 658))
        self.scrollArea_5.setFrameShape(QFrame.Box)
        self.scrollArea_5.setLineWidth(0)
        self.scrollArea_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_5.setWidgetResizable(False)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 770, 1000))
        self.groupBox_17 = QGroupBox(self.scrollAreaWidgetContents_5)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setGeometry(QRect(30, 720, 701, 81))
        self.groupBox_17.setMinimumSize(QSize(200, 0))
        self.groupBox_17.setMaximumSize(QSize(739, 16777215))
        self.horizontalLayoutWidget_11 = QWidget(self.groupBox_17)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(60, 30, 621, 41))
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.radioButton_log_on = QRadioButton(self.horizontalLayoutWidget_11)
        self.radioButton_log_on.setObjectName(u"radioButton_log_on")

        self.horizontalLayout_13.addWidget(self.radioButton_log_on)

        self.radioButton_log_off = QRadioButton(self.horizontalLayoutWidget_11)
        self.radioButton_log_off.setObjectName(u"radioButton_log_off")

        self.horizontalLayout_13.addWidget(self.radioButton_log_off)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 620, 701, 81))
        self.groupBox_3.setMinimumSize(QSize(200, 0))
        self.groupBox_3.setMaximumSize(QSize(739, 16777215))
        self.layoutWidget_3 = QWidget(self.groupBox_3)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(60, 30, 623, 41))
        self.horizontalLayout_29 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.checkBox_show_web_log = QCheckBox(self.layoutWidget_3)
        self.checkBox_show_web_log.setObjectName(u"checkBox_show_web_log")
        sizePolicy4.setHeightForWidth(self.checkBox_show_web_log.sizePolicy().hasHeightForWidth())
        self.checkBox_show_web_log.setSizePolicy(sizePolicy4)
        self.checkBox_show_web_log.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_29.addWidget(self.checkBox_show_web_log)

        self.checkBox_show_from_log = QCheckBox(self.layoutWidget_3)
        self.checkBox_show_from_log.setObjectName(u"checkBox_show_from_log")
        sizePolicy4.setHeightForWidth(self.checkBox_show_from_log.sizePolicy().hasHeightForWidth())
        self.checkBox_show_from_log.setSizePolicy(sizePolicy4)
        self.checkBox_show_from_log.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_29.addWidget(self.checkBox_show_from_log)

        self.checkBox_show_data_log = QCheckBox(self.layoutWidget_3)
        self.checkBox_show_data_log.setObjectName(u"checkBox_show_data_log")
        sizePolicy4.setHeightForWidth(self.checkBox_show_data_log.sizePolicy().hasHeightForWidth())
        self.checkBox_show_data_log.setSizePolicy(sizePolicy4)
        self.checkBox_show_data_log.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_29.addWidget(self.checkBox_show_data_log)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(30, 820, 701, 81))
        self.groupBox_4.setMinimumSize(QSize(200, 0))
        self.groupBox_4.setMaximumSize(QSize(739, 16777215))
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox_4)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(60, 30, 621, 41))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.radioButton_update_on = QRadioButton(self.horizontalLayoutWidget_7)
        self.radioButton_update_on.setObjectName(u"radioButton_update_on")

        self.horizontalLayout_9.addWidget(self.radioButton_update_on)

        self.radioButton_update_off = QRadioButton(self.horizontalLayoutWidget_7)
        self.radioButton_update_off.setObjectName(u"radioButton_update_off")

        self.horizontalLayout_9.addWidget(self.radioButton_update_off)

        self.groupBox_12 = QGroupBox(self.scrollAreaWidgetContents_5)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(30, 20, 701, 581))
        self.groupBox_12.setMinimumSize(QSize(200, 0))
        self.groupBox_12.setMaximumSize(QSize(739, 16777215))
        self.gridLayoutWidget_20 = QWidget(self.groupBox_12)
        self.gridLayoutWidget_20.setObjectName(u"gridLayoutWidget_20")
        self.gridLayoutWidget_20.setGeometry(QRect(30, 30, 665, 531))
        self.gridLayout_20 = QGridLayout(self.gridLayoutWidget_20)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.gridLayoutWidget_20)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget8 = QWidget(self.frame)
        self.layoutWidget8.setObjectName(u"layoutWidget8")
        self.layoutWidget8.setGeometry(QRect(0, -10, 550, 51))
        self.horizontalLayout_62 = QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.checkBox_hide_window_title = QCheckBox(self.layoutWidget8)
        self.checkBox_hide_window_title.setObjectName(u"checkBox_hide_window_title")

        self.horizontalLayout_62.addWidget(self.checkBox_hide_window_title)

        self.checkBox_dark_mode = QCheckBox(self.layoutWidget8)
        self.checkBox_dark_mode.setObjectName(u"checkBox_dark_mode")
        self.checkBox_dark_mode.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_62.addWidget(self.checkBox_dark_mode)


        self.gridLayout_20.addWidget(self.frame, 9, 1, 1, 1)

        self.horizontalLayout_dock = QHBoxLayout()
        self.horizontalLayout_dock.setObjectName(u"horizontalLayout_dock")
        self.checkBox_hide_dock_icon = QCheckBox(self.gridLayoutWidget_20)
        self.checkBox_hide_dock_icon.setObjectName(u"checkBox_hide_dock_icon")
        sizePolicy3.setHeightForWidth(self.checkBox_hide_dock_icon.sizePolicy().hasHeightForWidth())
        self.checkBox_hide_dock_icon.setSizePolicy(sizePolicy3)
        self.checkBox_hide_dock_icon.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_dock.addWidget(self.checkBox_hide_dock_icon)

        self.label_42 = QLabel(self.gridLayoutWidget_20)
        self.label_42.setObjectName(u"label_42")
        sizePolicy3.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy3)
        self.label_42.setMinimumSize(QSize(0, 30))
        self.label_42.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_42.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_dock.addWidget(self.label_42)

        self.checkBox_hide_menu_icon = QCheckBox(self.gridLayoutWidget_20)
        self.checkBox_hide_menu_icon.setObjectName(u"checkBox_hide_menu_icon")
        sizePolicy2.setHeightForWidth(self.checkBox_hide_menu_icon.sizePolicy().hasHeightForWidth())
        self.checkBox_hide_menu_icon.setSizePolicy(sizePolicy2)
        self.checkBox_hide_menu_icon.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_dock.addWidget(self.checkBox_hide_menu_icon)


        self.gridLayout_20.addLayout(self.horizontalLayout_dock, 8, 1, 1, 1)

        self.label_321 = QLabel(self.gridLayoutWidget_20)
        self.label_321.setObjectName(u"label_321")
        sizePolicy3.setHeightForWidth(self.label_321.sizePolicy().hasHeightForWidth())
        self.label_321.setSizePolicy(sizePolicy3)
        self.label_321.setMinimumSize(QSize(0, 0))
        self.label_321.setLayoutDirection(Qt.RightToLeft)
        self.label_321.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.label_321, 3, 0, 1, 1)

        self.horizontalLayout_102 = QHBoxLayout()
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.checkBox_auto_start = QCheckBox(self.gridLayoutWidget_20)
        self.checkBox_auto_start.setObjectName(u"checkBox_auto_start")
        sizePolicy4.setHeightForWidth(self.checkBox_auto_start.sizePolicy().hasHeightForWidth())
        self.checkBox_auto_start.setSizePolicy(sizePolicy4)
        self.checkBox_auto_start.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_102.addWidget(self.checkBox_auto_start)

        self.checkBox_auto_exit = QCheckBox(self.gridLayoutWidget_20)
        self.checkBox_auto_exit.setObjectName(u"checkBox_auto_exit")
        sizePolicy4.setHeightForWidth(self.checkBox_auto_exit.sizePolicy().hasHeightForWidth())
        self.checkBox_auto_exit.setSizePolicy(sizePolicy4)
        self.checkBox_auto_exit.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_102.addWidget(self.checkBox_auto_exit)


        self.gridLayout_20.addLayout(self.horizontalLayout_102, 2, 1, 1, 1)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.checkBox_show_dialog_exit = QCheckBox(self.gridLayoutWidget_20)
        self.checkBox_show_dialog_exit.setObjectName(u"checkBox_show_dialog_exit")
        sizePolicy4.setHeightForWidth(self.checkBox_show_dialog_exit.sizePolicy().hasHeightForWidth())
        self.checkBox_show_dialog_exit.setSizePolicy(sizePolicy4)
        self.checkBox_show_dialog_exit.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_55.addWidget(self.checkBox_show_dialog_exit)

        self.checkBox_show_dialog_stop_scrape = QCheckBox(self.gridLayoutWidget_20)
        self.checkBox_show_dialog_stop_scrape.setObjectName(u"checkBox_show_dialog_stop_scrape")
        sizePolicy4.setHeightForWidth(self.checkBox_show_dialog_stop_scrape.sizePolicy().hasHeightForWidth())
        self.checkBox_show_dialog_stop_scrape.setSizePolicy(sizePolicy4)
        self.checkBox_show_dialog_stop_scrape.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_55.addWidget(self.checkBox_show_dialog_stop_scrape)


        self.gridLayout_20.addLayout(self.horizontalLayout_55, 6, 1, 1, 1)

        self.horizontalLayout_104 = QHBoxLayout()
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.checkBox_timed_scrape = QCheckBox(self.gridLayoutWidget_20)
        self.checkBox_timed_scrape.setObjectName(u"checkBox_timed_scrape")
        sizePolicy9.setHeightForWidth(self.checkBox_timed_scrape.sizePolicy().hasHeightForWidth())
        self.checkBox_timed_scrape.setSizePolicy(sizePolicy9)
        self.checkBox_timed_scrape.setMinimumSize(QSize(0, 30))
        self.checkBox_timed_scrape.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_104.addWidget(self.checkBox_timed_scrape)

        self.lineEdit_timed_interval = QLineEdit(self.gridLayoutWidget_20)
        self.lineEdit_timed_interval.setObjectName(u"lineEdit_timed_interval")
        sizePolicy3.setHeightForWidth(self.lineEdit_timed_interval.sizePolicy().hasHeightForWidth())
        self.lineEdit_timed_interval.setSizePolicy(sizePolicy3)
        self.lineEdit_timed_interval.setMinimumSize(QSize(0, 30))
        self.lineEdit_timed_interval.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.lineEdit_timed_interval.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_104.addWidget(self.lineEdit_timed_interval)

        self.label_84 = QLabel(self.gridLayoutWidget_20)
        self.label_84.setObjectName(u"label_84")
        sizePolicy2.setHeightForWidth(self.label_84.sizePolicy().hasHeightForWidth())
        self.label_84.setSizePolicy(sizePolicy2)
        self.label_84.setMinimumSize(QSize(0, 30))
        self.label_84.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_104.addWidget(self.label_84)


        self.gridLayout_20.addLayout(self.horizontalLayout_104, 4, 1, 1, 1)

        self.label_308 = QLabel(self.gridLayoutWidget_20)
        self.label_308.setObjectName(u"label_308")
        sizePolicy3.setHeightForWidth(self.label_308.sizePolicy().hasHeightForWidth())
        self.label_308.setSizePolicy(sizePolicy3)
        self.label_308.setMinimumSize(QSize(0, 0))
        self.label_308.setLayoutDirection(Qt.RightToLeft)
        self.label_308.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.label_308, 2, 0, 1, 1)

        self.label_309 = QLabel(self.gridLayoutWidget_20)
        self.label_309.setObjectName(u"label_309")
        sizePolicy3.setHeightForWidth(self.label_309.sizePolicy().hasHeightForWidth())
        self.label_309.setSizePolicy(sizePolicy3)
        self.label_309.setMinimumSize(QSize(0, 0))
        self.label_309.setLayoutDirection(Qt.RightToLeft)
        self.label_309.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.label_309, 4, 0, 1, 1)

        self.label_277 = QLabel(self.gridLayoutWidget_20)
        self.label_277.setObjectName(u"label_277")
        sizePolicy3.setHeightForWidth(self.label_277.sizePolicy().hasHeightForWidth())
        self.label_277.setSizePolicy(sizePolicy3)
        self.label_277.setMinimumSize(QSize(0, 0))
        self.label_277.setLayoutDirection(Qt.RightToLeft)
        self.label_277.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.label_277, 6, 0, 1, 1)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.lineEdit_config_folder = QLineEdit(self.gridLayoutWidget_20)
        self.lineEdit_config_folder.setObjectName(u"lineEdit_config_folder")
        sizePolicy2.setHeightForWidth(self.lineEdit_config_folder.sizePolicy().hasHeightForWidth())
        self.lineEdit_config_folder.setSizePolicy(sizePolicy2)
        self.lineEdit_config_folder.setMinimumSize(QSize(0, 30))
        self.lineEdit_config_folder.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")

        self.horizontalLayout_63.addWidget(self.lineEdit_config_folder)

        self.pushButton_select_config_folder = QPushButton(self.gridLayoutWidget_20)
        self.pushButton_select_config_folder.setObjectName(u"pushButton_select_config_folder")
        sizePolicy3.setHeightForWidth(self.pushButton_select_config_folder.sizePolicy().hasHeightForWidth())
        self.pushButton_select_config_folder.setSizePolicy(sizePolicy3)
        self.pushButton_select_config_folder.setMinimumSize(QSize(110, 40))

        self.horizontalLayout_63.addWidget(self.pushButton_select_config_folder)


        self.gridLayout_20.addLayout(self.horizontalLayout_63, 0, 1, 1, 1)

        self.horizontalLayout_89 = QHBoxLayout()
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.checkBox_remain_task = QCheckBox(self.gridLayoutWidget_20)
        self.checkBox_remain_task.setObjectName(u"checkBox_remain_task")
        sizePolicy4.setHeightForWidth(self.checkBox_remain_task.sizePolicy().hasHeightForWidth())
        self.checkBox_remain_task.setSizePolicy(sizePolicy4)
        self.checkBox_remain_task.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_89.addWidget(self.checkBox_remain_task)


        self.gridLayout_20.addLayout(self.horizontalLayout_89, 5, 1, 1, 1)

        self.label_279 = QLabel(self.gridLayoutWidget_20)
        self.label_279.setObjectName(u"label_279")
        sizePolicy3.setHeightForWidth(self.label_279.sizePolicy().hasHeightForWidth())
        self.label_279.setSizePolicy(sizePolicy3)
        self.label_279.setMinimumSize(QSize(0, 0))
        self.label_279.setLayoutDirection(Qt.RightToLeft)
        self.label_279.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.label_279, 5, 0, 1, 1)

        self.label_40 = QLabel(self.gridLayoutWidget_20)
        self.label_40.setObjectName(u"label_40")
        sizePolicy2.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy2)
        self.label_40.setStyleSheet(u"color: rgb(8, 128, 128);")

        self.gridLayout_20.addWidget(self.label_40, 1, 1, 1, 1)

        self.horizontalLayout_149 = QHBoxLayout()
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.checkBox_dialog_qt = QCheckBox(self.gridLayoutWidget_20)
        self.checkBox_dialog_qt.setObjectName(u"checkBox_dialog_qt")
        sizePolicy3.setHeightForWidth(self.checkBox_dialog_qt.sizePolicy().hasHeightForWidth())
        self.checkBox_dialog_qt.setSizePolicy(sizePolicy3)

        self.horizontalLayout_149.addWidget(self.checkBox_dialog_qt)

        self.label_421 = QLabel(self.gridLayoutWidget_20)
        self.label_421.setObjectName(u"label_421")
        sizePolicy2.setHeightForWidth(self.label_421.sizePolicy().hasHeightForWidth())
        self.label_421.setSizePolicy(sizePolicy2)
        self.label_421.setMinimumSize(QSize(0, 30))
        self.label_421.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_421.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_149.addWidget(self.label_421)


        self.gridLayout_20.addLayout(self.horizontalLayout_149, 10, 1, 1, 1)

        self.label_314 = QLabel(self.gridLayoutWidget_20)
        self.label_314.setObjectName(u"label_314")
        sizePolicy3.setHeightForWidth(self.label_314.sizePolicy().hasHeightForWidth())
        self.label_314.setSizePolicy(sizePolicy3)
        self.label_314.setMinimumSize(QSize(0, 30))
        self.label_314.setLayoutDirection(Qt.RightToLeft)
        self.label_314.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.label_314, 8, 0, 1, 1)

        self.label_243 = QLabel(self.gridLayoutWidget_20)
        self.label_243.setObjectName(u"label_243")
        sizePolicy3.setHeightForWidth(self.label_243.sizePolicy().hasHeightForWidth())
        self.label_243.setSizePolicy(sizePolicy3)
        self.label_243.setMinimumSize(QSize(0, 0))
        self.label_243.setLayoutDirection(Qt.RightToLeft)
        self.label_243.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.label_243, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.gridLayoutWidget_20)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.layoutWidget_17 = QWidget(self.frame_3)
        self.layoutWidget_17.setObjectName(u"layoutWidget_17")
        self.layoutWidget_17.setGeometry(QRect(0, 0, 551, 32))
        self.horizontalLayout_106 = QHBoxLayout(self.layoutWidget_17)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.radioButton_hide_close = QRadioButton(self.layoutWidget_17)
        self.radioButton_hide_close.setObjectName(u"radioButton_hide_close")
        self.radioButton_hide_close.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_106.addWidget(self.radioButton_hide_close)

        self.radioButton_hide_mini = QRadioButton(self.layoutWidget_17)
        self.radioButton_hide_mini.setObjectName(u"radioButton_hide_mini")

        self.horizontalLayout_106.addWidget(self.radioButton_hide_mini)

        self.radioButton_hide_none = QRadioButton(self.layoutWidget_17)
        self.radioButton_hide_none.setObjectName(u"radioButton_hide_none")

        self.horizontalLayout_106.addWidget(self.radioButton_hide_none)


        self.gridLayout_20.addWidget(self.frame_3, 7, 1, 1, 1)

        self.horizontalLayout_109 = QHBoxLayout()
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.checkBox_rest_scrape = QCheckBox(self.gridLayoutWidget_20)
        self.checkBox_rest_scrape.setObjectName(u"checkBox_rest_scrape")
        sizePolicy9.setHeightForWidth(self.checkBox_rest_scrape.sizePolicy().hasHeightForWidth())
        self.checkBox_rest_scrape.setSizePolicy(sizePolicy9)
        self.checkBox_rest_scrape.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_109.addWidget(self.checkBox_rest_scrape)

        self.lineEdit_rest_count = QLineEdit(self.gridLayoutWidget_20)
        self.lineEdit_rest_count.setObjectName(u"lineEdit_rest_count")
        sizePolicy3.setHeightForWidth(self.lineEdit_rest_count.sizePolicy().hasHeightForWidth())
        self.lineEdit_rest_count.setSizePolicy(sizePolicy3)
        self.lineEdit_rest_count.setMinimumSize(QSize(0, 30))
        self.lineEdit_rest_count.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.lineEdit_rest_count.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_109.addWidget(self.lineEdit_rest_count)

        self.label_52 = QLabel(self.gridLayoutWidget_20)
        self.label_52.setObjectName(u"label_52")
        sizePolicy3.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy3)
        self.label_52.setMinimumSize(QSize(0, 30))
        self.label_52.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_109.addWidget(self.label_52)

        self.lineEdit_rest_time = QLineEdit(self.gridLayoutWidget_20)
        self.lineEdit_rest_time.setObjectName(u"lineEdit_rest_time")
        sizePolicy3.setHeightForWidth(self.lineEdit_rest_time.sizePolicy().hasHeightForWidth())
        self.lineEdit_rest_time.setSizePolicy(sizePolicy3)
        self.lineEdit_rest_time.setMinimumSize(QSize(0, 30))
        self.lineEdit_rest_time.setStyleSheet(u" font: \"Courier\";\n"
" border: 1px solid rgba(0,0,0, 50);\n"
" border-radius: 15px;\n"
"")
        self.lineEdit_rest_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_109.addWidget(self.lineEdit_rest_time)

        self.label_71 = QLabel(self.gridLayoutWidget_20)
        self.label_71.setObjectName(u"label_71")
        sizePolicy2.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy2)
        self.label_71.setMinimumSize(QSize(0, 30))
        self.label_71.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_109.addWidget(self.label_71)


        self.gridLayout_20.addLayout(self.horizontalLayout_109, 3, 1, 1, 1)

        self.label_313 = QLabel(self.gridLayoutWidget_20)
        self.label_313.setObjectName(u"label_313")
        sizePolicy3.setHeightForWidth(self.label_313.sizePolicy().hasHeightForWidth())
        self.label_313.setSizePolicy(sizePolicy3)
        self.label_313.setMinimumSize(QSize(0, 30))
        self.label_313.setLayoutDirection(Qt.RightToLeft)
        self.label_313.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.label_313, 7, 0, 1, 1)

        self.label_246 = QLabel(self.gridLayoutWidget_20)
        self.label_246.setObjectName(u"label_246")
        sizePolicy3.setHeightForWidth(self.label_246.sizePolicy().hasHeightForWidth())
        self.label_246.setSizePolicy(sizePolicy3)
        self.label_246.setMinimumSize(QSize(0, 30))
        self.label_246.setLayoutDirection(Qt.RightToLeft)
        self.label_246.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.label_246, 9, 0, 1, 1)

        self.label_420 = QLabel(self.gridLayoutWidget_20)
        self.label_420.setObjectName(u"label_420")
        sizePolicy3.setHeightForWidth(self.label_420.sizePolicy().hasHeightForWidth())
        self.label_420.setSizePolicy(sizePolicy3)
        self.label_420.setMinimumSize(QSize(0, 30))
        self.label_420.setLayoutDirection(Qt.RightToLeft)
        self.label_420.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.label_420, 10, 0, 1, 1)

        self.label_426 = QLabel(self.gridLayoutWidget_20)
        self.label_426.setObjectName(u"label_426")
        sizePolicy3.setHeightForWidth(self.label_426.sizePolicy().hasHeightForWidth())
        self.label_426.setSizePolicy(sizePolicy3)
        self.label_426.setMinimumSize(QSize(0, 30))
        self.label_426.setLayoutDirection(Qt.RightToLeft)
        self.label_426.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.label_426, 11, 0, 1, 1)

        self.horizontalLayout_dock_2 = QHBoxLayout()
        self.horizontalLayout_dock_2.setObjectName(u"horizontalLayout_dock_2")
        self.checkBox_highdpi_passthrough = QCheckBox(self.gridLayoutWidget_20)
        self.checkBox_highdpi_passthrough.setObjectName(u"checkBox_highdpi_passthrough")
        sizePolicy3.setHeightForWidth(self.checkBox_highdpi_passthrough.sizePolicy().hasHeightForWidth())
        self.checkBox_highdpi_passthrough.setSizePolicy(sizePolicy3)
        self.checkBox_highdpi_passthrough.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_dock_2.addWidget(self.checkBox_highdpi_passthrough)

        self.label_427 = QLabel(self.gridLayoutWidget_20)
        self.label_427.setObjectName(u"label_427")
        sizePolicy2.setHeightForWidth(self.label_427.sizePolicy().hasHeightForWidth())
        self.label_427.setSizePolicy(sizePolicy2)
        self.label_427.setMinimumSize(QSize(0, 30))
        self.label_427.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_427.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_dock_2.addWidget(self.label_427)


        self.gridLayout_20.addLayout(self.horizontalLayout_dock_2, 11, 1, 1, 1)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.tabWidget.addTab(self.tab5, "")
        self.label_config = QLabel(self.page_setting)
        self.label_config.setObjectName(u"label_config")
        self.label_config.setGeometry(QRect(0, 620, 799, 74))
        self.pushButton_init_config = QPushButton(self.page_setting)
        self.pushButton_init_config.setObjectName(u"pushButton_init_config")
        self.pushButton_init_config.setGeometry(QRect(380, 630, 91, 40))
        self.pushButton_save_config = QPushButton(self.page_setting)
        self.pushButton_save_config.setObjectName(u"pushButton_save_config")
        self.pushButton_save_config.setGeometry(QRect(490, 630, 241, 50))
        self.comboBox_change_config = QComboBox(self.page_setting)
        self.comboBox_change_config.setObjectName(u"comboBox_change_config")
        self.comboBox_change_config.setGeometry(QRect(100, 635, 151, 30))
        sizePolicy4.setHeightForWidth(self.comboBox_change_config.sizePolicy().hasHeightForWidth())
        self.comboBox_change_config.setSizePolicy(sizePolicy4)
        self.comboBox_change_config.setMinimumSize(QSize(0, 30))
        self.comboBox_change_config.setMaximumSize(QSize(16000, 40))
        self.comboBox_change_config.setSizeIncrement(QSize(0, 0))
        self.comboBox_change_config.setFocusPolicy(Qt.NoFocus)
        self.comboBox_change_config.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.comboBox_change_config.setStyleSheet(u"")
        self.comboBox_change_config.setMaxVisibleItems(30)
        self.comboBox_change_config.setDuplicatesEnabled(False)
        self.comboBox_change_config.setFrame(False)
        self.label_241 = QLabel(self.page_setting)
        self.label_241.setObjectName(u"label_241")
        self.label_241.setGeometry(QRect(20, 629, 81, 40))
        sizePolicy2.setHeightForWidth(self.label_241.sizePolicy().hasHeightForWidth())
        self.label_241.setSizePolicy(sizePolicy2)
        self.label_241.setMinimumSize(QSize(0, 0))
        self.label_241.setLayoutDirection(Qt.RightToLeft)
        self.label_241.setFrameShape(QFrame.NoFrame)
        self.label_241.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_save_new_config = QPushButton(self.page_setting)
        self.pushButton_save_new_config.setObjectName(u"pushButton_save_new_config")
        self.pushButton_save_new_config.setGeometry(QRect(270, 630, 91, 40))
        self.widget_show_success = QWidget(self.page_setting)
        self.widget_show_success.setObjectName(u"widget_show_success")
        self.widget_show_success.setGeometry(QRect(4, 0, 0, 0))
        self.widget_show_success.setAutoFillBackground(False)
        self.textBrowser_show_success_list = QTextBrowser(self.widget_show_success)
        self.textBrowser_show_success_list.setObjectName(u"textBrowser_show_success_list")
        self.textBrowser_show_success_list.setEnabled(True)
        self.textBrowser_show_success_list.setGeometry(QRect(10, 30, 791, 421))
        self.textBrowser_show_success_list.setFocusPolicy(Qt.StrongFocus)
        self.textBrowser_show_success_list.setStyleSheet(u"")
        self.textBrowser_show_success_list.setFrameShape(QFrame.Box)
        self.textBrowser_show_success_list.setFrameShadow(QFrame.Raised)
        self.textBrowser_show_success_list.setReadOnly(False)
        self.textBrowser_show_success_list.setOverwriteMode(False)
        self.textBrowser_show_success_list.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.textBrowser_show_success_list.setOpenExternalLinks(True)
        self.textBrowser_show_success_list.setOpenLinks(True)
        self.pushButton_success_list_close = QPushButton(self.widget_show_success)
        self.pushButton_success_list_close.setObjectName(u"pushButton_success_list_close")
        self.pushButton_success_list_close.setGeometry(QRect(550, 460, 91, 40))
        self.pushButton_success_list_clear = QPushButton(self.widget_show_success)
        self.pushButton_success_list_clear.setObjectName(u"pushButton_success_list_clear")
        self.pushButton_success_list_clear.setGeometry(QRect(240, 460, 91, 40))
        self.pushButton_success_list_save = QPushButton(self.widget_show_success)
        self.pushButton_success_list_save.setObjectName(u"pushButton_success_list_save")
        self.pushButton_success_list_save.setGeometry(QRect(440, 460, 91, 40))
        self.label_success_title = QLabel(self.widget_show_success)
        self.label_success_title.setObjectName(u"label_success_title")
        self.label_success_title.setGeometry(QRect(10, 0, 791, 31))
        sizePolicy5.setHeightForWidth(self.label_success_title.sizePolicy().hasHeightForWidth())
        self.label_success_title.setSizePolicy(sizePolicy5)
        self.label_success_title.setMinimumSize(QSize(0, 0))
        self.label_success_title.setLayoutDirection(Qt.RightToLeft)
        self.label_success_title.setFrameShape(QFrame.NoFrame)
        self.label_success_title.setAlignment(Qt.AlignCenter)
        self.widget_show_tips = QWidget(self.page_setting)
        self.widget_show_tips.setObjectName(u"widget_show_tips")
        self.widget_show_tips.setGeometry(QRect(4, 0, 0, 0))
        self.widget_show_tips.setAutoFillBackground(False)
        self.textBrowser_show_tips = QTextBrowser(self.widget_show_tips)
        self.textBrowser_show_tips.setObjectName(u"textBrowser_show_tips")
        self.textBrowser_show_tips.setEnabled(True)
        self.textBrowser_show_tips.setGeometry(QRect(10, 30, 791, 421))
        self.textBrowser_show_tips.setFocusPolicy(Qt.StrongFocus)
        self.textBrowser_show_tips.setStyleSheet(u"")
        self.textBrowser_show_tips.setFrameShape(QFrame.Box)
        self.textBrowser_show_tips.setFrameShadow(QFrame.Raised)
        self.textBrowser_show_tips.setReadOnly(False)
        self.textBrowser_show_tips.setOverwriteMode(False)
        self.textBrowser_show_tips.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.textBrowser_show_tips.setOpenExternalLinks(True)
        self.textBrowser_show_tips.setOpenLinks(True)
        self.pushButton_show_tips_close = QPushButton(self.widget_show_tips)
        self.pushButton_show_tips_close.setObjectName(u"pushButton_show_tips_close")
        self.pushButton_show_tips_close.setGeometry(QRect(550, 460, 91, 40))
        self.label_show_tips_title = QLabel(self.widget_show_tips)
        self.label_show_tips_title.setObjectName(u"label_show_tips_title")
        self.label_show_tips_title.setGeometry(QRect(10, 0, 791, 30))
        sizePolicy5.setHeightForWidth(self.label_show_tips_title.sizePolicy().hasHeightForWidth())
        self.label_show_tips_title.setSizePolicy(sizePolicy5)
        self.label_show_tips_title.setMinimumSize(QSize(0, 0))
        self.label_show_tips_title.setLayoutDirection(Qt.RightToLeft)
        self.label_show_tips_title.setFrameShape(QFrame.NoFrame)
        self.label_show_tips_title.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_setting)
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.textBrowser_about = QTextBrowser(self.page_about)
        self.textBrowser_about.setObjectName(u"textBrowser_about")
        self.textBrowser_about.setGeometry(QRect(30, 0, 790, 689))
        self.textBrowser_about.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.page_about)
        self.widget_setting = QWidget(self.centralwidget)
        self.widget_setting.setObjectName(u"widget_setting")
        self.widget_setting.setGeometry(QRect(0, 0, 210, 700))
        self.widget_setting.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_show_version = QLabel(self.widget_setting)
        self.label_show_version.setObjectName(u"label_show_version")
        self.label_show_version.setGeometry(QRect(0, 489, 210, 201))
        self.label_show_version.setLineWidth(0)
        self.label_show_version.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_local_number = QLabel(self.widget_setting)
        self.label_local_number.setObjectName(u"label_local_number")
        self.label_local_number.setGeometry(QRect(0, 680, 21, 21))
        self.label_local_number.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_local_number.setStyleSheet(u"border:0px solid rgba(0, 0, 0, 80);")
        self.label_local_number.setFrameShape(QFrame.Box)
        self.label_local_number.setLineWidth(0)
        self.label_local_number.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.widget_buttons = QWidget(self.widget_setting)
        self.widget_buttons.setObjectName(u"widget_buttons")
        self.widget_buttons.setGeometry(QRect(0, 50, 210, 341))
        self.layoutWidget9 = QWidget(self.widget_buttons)
        self.layoutWidget9.setObjectName(u"layoutWidget9")
        self.layoutWidget9.setGeometry(QRect(0, 0, 211, 282))
        self.verticalLayout = QVBoxLayout(self.layoutWidget9)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(18, 0, 18, 0)
        self.pushButton_main = QPushButton(self.layoutWidget9)
        self.pushButton_main.setObjectName(u"pushButton_main")
        sizePolicy.setHeightForWidth(self.pushButton_main.sizePolicy().hasHeightForWidth())
        self.pushButton_main.setSizePolicy(sizePolicy)
        self.pushButton_main.setMinimumSize(QSize(0, 40))
        self.pushButton_main.setMaximumSize(QSize(16777215, 40))
        self.pushButton_main.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_main.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.pushButton_main)

        self.verticalSpacer_2 = QSpacerItem(20, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton_log = QPushButton(self.layoutWidget9)
        self.pushButton_log.setObjectName(u"pushButton_log")
        self.pushButton_log.setMinimumSize(QSize(0, 40))
        self.pushButton_log.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.pushButton_log)

        self.verticalSpacer = QSpacerItem(20, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_tool = QPushButton(self.layoutWidget9)
        self.pushButton_tool.setObjectName(u"pushButton_tool")
        self.pushButton_tool.setMinimumSize(QSize(0, 40))
        self.pushButton_tool.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.pushButton_tool)

        self.verticalSpacer_6 = QSpacerItem(20, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.pushButton_setting = QPushButton(self.layoutWidget9)
        self.pushButton_setting.setObjectName(u"pushButton_setting")
        self.pushButton_setting.setMinimumSize(QSize(0, 40))
        self.pushButton_setting.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.pushButton_setting)

        self.verticalSpacer_4 = QSpacerItem(20, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.pushButton_net = QPushButton(self.layoutWidget9)
        self.pushButton_net.setObjectName(u"pushButton_net")
        self.pushButton_net.setMinimumSize(QSize(0, 40))
        self.pushButton_net.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.pushButton_net)

        self.verticalSpacer_5 = QSpacerItem(20, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.pushButton_about = QPushButton(self.layoutWidget9)
        self.pushButton_about.setObjectName(u"pushButton_about")
        self.pushButton_about.setMinimumSize(QSize(0, 40))
        self.pushButton_about.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.pushButton_about)

        self.left_backgroud_widget = QWidget(self.widget_setting)
        self.left_backgroud_widget.setObjectName(u"left_backgroud_widget")
        self.left_backgroud_widget.setGeometry(QRect(0, 0, 210, 700))
        self.close_widget = QWidget(self.widget_setting)
        self.close_widget.setObjectName(u"close_widget")
        self.close_widget.setGeometry(QRect(0, 0, 101, 41))
        self.pushButton_close = QPushButton(self.close_widget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(10, 10, 20, 20))
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy14.setHorizontalStretch(20)
        sizePolicy14.setVerticalStretch(20)
        sizePolicy14.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy14)
        self.pushButton_close.setMinimumSize(QSize(20, 20))
        self.pushButton_close.setMaximumSize(QSize(20, 20))
        self.pushButton_close.setBaseSize(QSize(0, 0))
        self.pushButton_close.setMouseTracking(True)
        self.pushButton_close.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_close.setStyleSheet(u"QPushButton{\n"
"	font: 900 14pt \"Tahoma\";\n"
"	color:#F14C4C;\n"
"	background:#F14C4C;\n"
"	border-radius:8px;\n"
"	margin:2px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:black;\n"
"	background:#FF6058;\n"
"}")
        self.pushButton_min = QPushButton(self.close_widget)
        self.pushButton_min.setObjectName(u"pushButton_min")
        self.pushButton_min.setGeometry(QRect(35, 10, 20, 20))
        sizePolicy14.setHeightForWidth(self.pushButton_min.sizePolicy().hasHeightForWidth())
        self.pushButton_min.setSizePolicy(sizePolicy14)
        self.pushButton_min.setMinimumSize(QSize(20, 20))
        self.pushButton_min.setMaximumSize(QSize(20, 20))
        self.pushButton_min.setBaseSize(QSize(0, 0))
        self.pushButton_min.setMouseTracking(True)
        self.pushButton_min.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_min.setStyleSheet(u"QPushButton{\n"
"	font: 900 14pt \"Tahoma\";\n"
"	color:#FFBC3C;\n"
"	background:#FFBC3C;\n"
"	border-radius:8px;\n"
"	margin:2px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:black;\n"
"	background:#FFBC3C;\n"
"}\n"
"")
        self.left_backgroud_widget.raise_()
        self.label_show_version.raise_()
        self.label_local_number.raise_()
        self.widget_buttons.raise_()
        self.close_widget.raise_()
        self.progressBar_scrape = QProgressBar(self.centralwidget)
        self.progressBar_scrape.setObjectName(u"progressBar_scrape")
        self.progressBar_scrape.setGeometry(QRect(209, -1, 823, 7))
        self.progressBar_scrape.setMinimumSize(QSize(0, 2))
        self.progressBar_scrape.setSizeIncrement(QSize(0, 0))
        self.progressBar_scrape.setBaseSize(QSize(0, 0))
        self.progressBar_scrape.setStyleSheet(u"QProgressBar::chunk {\n"
"   background-color: #5777FF;\n"
"   width: 3px;\n"
"}\n"
"QProgressBar {\n"
"   border: 0px solid rgba(51,102,153,80);\n"
"   border-radius: 0px;\n"
"   text-align: center;\n"
"   background-color: rgba(255,255,255,0);\n"
"}")
        self.progressBar_scrape.setValue(24)
        self.layoutWidget10 = QWidget(self.centralwidget)
        self.layoutWidget10.setObjectName(u"layoutWidget10")
        self.layoutWidget10.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout_41 = QHBoxLayout(self.layoutWidget10)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget11 = QWidget(self.centralwidget)
        self.layoutWidget11.setObjectName(u"layoutWidget11")
        self.layoutWidget11.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout_52 = QHBoxLayout(self.layoutWidget11)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget12 = QWidget(self.centralwidget)
        self.layoutWidget12.setObjectName(u"layoutWidget12")
        self.layoutWidget12.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout_64 = QHBoxLayout(self.layoutWidget12)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget13 = QWidget(self.centralwidget)
        self.layoutWidget13.setObjectName(u"layoutWidget13")
        self.layoutWidget13.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout_99 = QHBoxLayout(self.layoutWidget13)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget14 = QWidget(self.centralwidget)
        self.layoutWidget14.setObjectName(u"layoutWidget14")
        self.layoutWidget14.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout_118 = QHBoxLayout(self.layoutWidget14)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.horizontalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget15 = QWidget(self.centralwidget)
        self.layoutWidget15.setObjectName(u"layoutWidget15")
        self.layoutWidget15.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout_129 = QHBoxLayout(self.layoutWidget15)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget16 = QWidget(self.centralwidget)
        self.layoutWidget16.setObjectName(u"layoutWidget16")
        self.layoutWidget16.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout_131 = QHBoxLayout(self.layoutWidget16)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget17 = QWidget(self.centralwidget)
        self.layoutWidget17.setObjectName(u"layoutWidget17")
        self.layoutWidget17.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout_43 = QHBoxLayout(self.layoutWidget17)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.widget_nfo = QWidget(self.centralwidget)
        self.widget_nfo.setObjectName(u"widget_nfo")
        self.widget_nfo.setGeometry(QRect(10, 10, 20, 20))
        self.scrollArea_nfo = QScrollArea(self.widget_nfo)
        self.scrollArea_nfo.setObjectName(u"scrollArea_nfo")
        self.scrollArea_nfo.setGeometry(QRect(9, 29, 771, 591))
        self.scrollArea_nfo.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_nfo.setWidgetResizable(False)
        self.scrollAreaWidgetContents_nfo = QWidget()
        self.scrollAreaWidgetContents_nfo.setObjectName(u"scrollAreaWidgetContents_nfo")
        self.scrollAreaWidgetContents_nfo.setGeometry(QRect(0, 0, 752, 1300))
        self.label_19 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(9, 330, 81, 40))
        self.label_19.setLineWidth(0)
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_359 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_359.setObjectName(u"label_359")
        self.label_359.setGeometry(QRect(40, 140, 50, 40))
        self.label_359.setLineWidth(0)
        self.label_359.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_360 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_360.setObjectName(u"label_360")
        self.label_360.setGeometry(QRect(40, 80, 50, 40))
        self.label_360.setLineWidth(0)
        self.label_360.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_361 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_361.setObjectName(u"label_361")
        self.label_361.setGeometry(QRect(9, 220, 81, 40))
        self.label_361.setLineWidth(0)
        self.label_361.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_362 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_362.setObjectName(u"label_362")
        self.label_362.setGeometry(QRect(40, 660, 50, 40))
        self.label_362.setLineWidth(0)
        self.label_362.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_363 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_363.setObjectName(u"label_363")
        self.label_363.setGeometry(QRect(9, 800, 81, 40))
        self.label_363.setLineWidth(0)
        self.label_363.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_364 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_364.setObjectName(u"label_364")
        self.label_364.setGeometry(QRect(380, 800, 81, 40))
        self.label_364.setLineWidth(0)
        self.label_364.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_365 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_365.setObjectName(u"label_365")
        self.label_365.setGeometry(QRect(380, 920, 81, 40))
        self.label_365.setLineWidth(0)
        self.label_365.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_366 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_366.setObjectName(u"label_366")
        self.label_366.setGeometry(QRect(9, 920, 81, 40))
        self.label_366.setLineWidth(0)
        self.label_366.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_367 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_367.setObjectName(u"label_367")
        self.label_367.setGeometry(QRect(380, 980, 81, 40))
        self.label_367.setLineWidth(0)
        self.label_367.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_368 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_368.setObjectName(u"label_368")
        self.label_368.setGeometry(QRect(9, 980, 81, 40))
        self.label_368.setLineWidth(0)
        self.label_368.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_369 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_369.setObjectName(u"label_369")
        self.label_369.setGeometry(QRect(360, 80, 50, 40))
        self.label_369.setLineWidth(0)
        self.label_369.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.comboBox_nfo = QComboBox(self.scrollAreaWidgetContents_nfo)
        self.comboBox_nfo.addItem("")
        self.comboBox_nfo.addItem("")
        self.comboBox_nfo.addItem("")
        self.comboBox_nfo.setObjectName(u"comboBox_nfo")
        self.comboBox_nfo.setGeometry(QRect(420, 80, 103, 40))
        self.label_371 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_371.setObjectName(u"label_371")
        self.label_371.setGeometry(QRect(9, 490, 81, 40))
        self.label_371.setLineWidth(0)
        self.label_371.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_372 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_372.setObjectName(u"label_372")
        self.label_372.setGeometry(QRect(9, 270, 81, 40))
        self.label_372.setLineWidth(0)
        self.label_372.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_375 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_375.setObjectName(u"label_375")
        self.label_375.setGeometry(QRect(9, 1050, 81, 40))
        self.label_375.setLineWidth(0)
        self.label_375.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_376 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_376.setObjectName(u"label_376")
        self.label_376.setGeometry(QRect(-1, 1110, 91, 40))
        self.label_376.setLineWidth(0)
        self.label_376.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_377 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_377.setObjectName(u"label_377")
        self.label_377.setGeometry(QRect(-1, 1170, 91, 40))
        self.label_377.setLineWidth(0)
        self.label_377.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_378 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_378.setObjectName(u"label_378")
        self.label_378.setGeometry(QRect(0, 1230, 91, 40))
        self.label_378.setLineWidth(0)
        self.label_378.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_370 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_370.setObjectName(u"label_370")
        self.label_370.setGeometry(QRect(100, 190, 561, 20))
        sizePolicy2.setHeightForWidth(self.label_370.sizePolicy().hasHeightForWidth())
        self.label_370.setSizePolicy(sizePolicy2)
        self.label_370.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_379 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_379.setObjectName(u"label_379")
        self.label_379.setGeometry(QRect(100, 770, 561, 20))
        sizePolicy2.setHeightForWidth(self.label_379.sizePolicy().hasHeightForWidth())
        self.label_379.setSizePolicy(sizePolicy2)
        self.label_379.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_373 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_373.setObjectName(u"label_373")
        self.label_373.setGeometry(QRect(9, 860, 81, 40))
        self.label_373.setLineWidth(0)
        self.label_373.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_374 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_374.setObjectName(u"label_374")
        self.label_374.setGeometry(QRect(380, 860, 81, 40))
        self.label_374.setLineWidth(0)
        self.label_374.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_380 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_380.setObjectName(u"label_380")
        self.label_380.setGeometry(QRect(540, 80, 51, 40))
        self.label_380.setLineWidth(0)
        self.label_380.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_nfo_number = QLineEdit(self.scrollAreaWidgetContents_nfo)
        self.lineEdit_nfo_number.setObjectName(u"lineEdit_nfo_number")
        self.lineEdit_nfo_number.setGeometry(QRect(100, 80, 241, 40))
        self.lineEdit_nfo_year = QLineEdit(self.scrollAreaWidgetContents_nfo)
        self.lineEdit_nfo_year.setObjectName(u"lineEdit_nfo_year")
        self.lineEdit_nfo_year.setGeometry(QRect(600, 80, 121, 40))
        self.lineEdit_nfo_actor = QLineEdit(self.scrollAreaWidgetContents_nfo)
        self.lineEdit_nfo_actor.setObjectName(u"lineEdit_nfo_actor")
        self.lineEdit_nfo_actor.setGeometry(QRect(100, 140, 621, 40))
        self.lineEdit_nfo_title = QLineEdit(self.scrollAreaWidgetContents_nfo)
        self.lineEdit_nfo_title.setObjectName(u"lineEdit_nfo_title")
        self.lineEdit_nfo_title.setGeometry(QRect(100, 220, 621, 40))
        self.lineEdit_nfo_originaltitle = QLineEdit(self.scrollAreaWidgetContents_nfo)
        self.lineEdit_nfo_originaltitle.setObjectName(u"lineEdit_nfo_originaltitle")
        self.lineEdit_nfo_originaltitle.setGeometry(QRect(100, 270, 621, 40))
        self.textEdit_nfo_outline = QTextEdit(self.scrollAreaWidgetContents_nfo)
        self.textEdit_nfo_outline.setObjectName(u"textEdit_nfo_outline")
        self.textEdit_nfo_outline.setGeometry(QRect(100, 330, 621, 151))
        self.textEdit_nfo_originalplot = QTextEdit(self.scrollAreaWidgetContents_nfo)
        self.textEdit_nfo_originalplot.setObjectName(u"textEdit_nfo_originalplot")
        self.textEdit_nfo_originalplot.setGeometry(QRect(100, 490, 621, 151))
        self.lineEdit_nfo_release = QLineEdit(self.scrollAreaWidgetContents_nfo)
        self.lineEdit_nfo_release.setObjectName(u"lineEdit_nfo_release")
        self.lineEdit_nfo_release.setGeometry(QRect(100, 800, 241, 40))
        self.lineEdit_nfo_score = QLineEdit(self.scrollAreaWidgetContents_nfo)
        self.lineEdit_nfo_score.setObjectName(u"lineEdit_nfo_score")
        self.lineEdit_nfo_score.setGeometry(QRect(100, 860, 241, 40))
        self.lineEdit_nfo_director = QLineEdit(self.scrollAreaWidgetContents_nfo)
        self.lineEdit_nfo_director.setObjectName(u"lineEdit_nfo_director")
        self.lineEdit_nfo_director.setGeometry(QRect(100, 920, 241, 40))
        self.lineEdit_nfo_studio = QLineEdit(self.scrollAreaWidgetContents_nfo)
        self.lineEdit_nfo_studio.setObjectName(u"lineEdit_nfo_studio")
        self.lineEdit_nfo_studio.setGeometry(QRect(100, 980, 241, 40))
        self.lineEdit_nfo_series = QLineEdit(self.scrollAreaWidgetContents_nfo)
        self.lineEdit_nfo_series.setObjectName(u"lineEdit_nfo_series")
        self.lineEdit_nfo_series.setGeometry(QRect(480, 920, 241, 40))
        self.lineEdit_nfo_publisher = QLineEdit(self.scrollAreaWidgetContents_nfo)
        self.lineEdit_nfo_publisher.setObjectName(u"lineEdit_nfo_publisher")
        self.lineEdit_nfo_publisher.setGeometry(QRect(480, 980, 241, 40))
        self.lineEdit_nfo_wanted = QLineEdit(self.scrollAreaWidgetContents_nfo)
        self.lineEdit_nfo_wanted.setObjectName(u"lineEdit_nfo_wanted")
        self.lineEdit_nfo_wanted.setGeometry(QRect(480, 860, 241, 40))
        self.lineEdit_nfo_runtime = QLineEdit(self.scrollAreaWidgetContents_nfo)
        self.lineEdit_nfo_runtime.setObjectName(u"lineEdit_nfo_runtime")
        self.lineEdit_nfo_runtime.setGeometry(QRect(480, 800, 241, 40))
        self.lineEdit_nfo_poster = QLineEdit(self.scrollAreaWidgetContents_nfo)
        self.lineEdit_nfo_poster.setObjectName(u"lineEdit_nfo_poster")
        self.lineEdit_nfo_poster.setGeometry(QRect(100, 1050, 621, 40))
        self.lineEdit_nfo_cover = QLineEdit(self.scrollAreaWidgetContents_nfo)
        self.lineEdit_nfo_cover.setObjectName(u"lineEdit_nfo_cover")
        self.lineEdit_nfo_cover.setGeometry(QRect(100, 1110, 621, 40))
        self.lineEdit_nfo_trailer = QLineEdit(self.scrollAreaWidgetContents_nfo)
        self.lineEdit_nfo_trailer.setObjectName(u"lineEdit_nfo_trailer")
        self.lineEdit_nfo_trailer.setGeometry(QRect(100, 1170, 621, 40))
        self.lineEdit_nfo_website = QLineEdit(self.scrollAreaWidgetContents_nfo)
        self.lineEdit_nfo_website.setObjectName(u"lineEdit_nfo_website")
        self.lineEdit_nfo_website.setGeometry(QRect(100, 1230, 621, 40))
        self.label_nfo = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_nfo.setObjectName(u"label_nfo")
        self.label_nfo.setGeometry(QRect(100, 20, 621, 41))
        self.label_nfo.setWordWrap(True)
        self.label_381 = QLabel(self.scrollAreaWidgetContents_nfo)
        self.label_381.setObjectName(u"label_381")
        self.label_381.setGeometry(QRect(40, 20, 50, 40))
        self.label_381.setLineWidth(0)
        self.label_381.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.textEdit_nfo_tag = QTextEdit(self.scrollAreaWidgetContents_nfo)
        self.textEdit_nfo_tag.setObjectName(u"textEdit_nfo_tag")
        self.textEdit_nfo_tag.setGeometry(QRect(100, 660, 621, 101))
        self.scrollArea_nfo.setWidget(self.scrollAreaWidgetContents_nfo)
        self.pushButton_nfo_save = QPushButton(self.widget_nfo)
        self.pushButton_nfo_save.setObjectName(u"pushButton_nfo_save")
        self.pushButton_nfo_save.setGeometry(QRect(260, 630, 91, 40))
        self.pushButton_nfo_close = QPushButton(self.widget_nfo)
        self.pushButton_nfo_close.setObjectName(u"pushButton_nfo_close")
        self.pushButton_nfo_close.setGeometry(QRect(480, 630, 91, 40))
        self.label_4 = QLabel(self.widget_nfo)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(360, 5, 58, 21))
        self.label_save_tips = QLabel(self.widget_nfo)
        self.label_save_tips.setObjectName(u"label_save_tips")
        self.label_save_tips.setGeometry(QRect(10, 640, 231, 20))
        sizePolicy2.setHeightForWidth(self.label_save_tips.sizePolicy().hasHeightForWidth())
        self.label_save_tips.setSizePolicy(sizePolicy2)
        self.label_save_tips.setStyleSheet(u"color: rgb(8, 128, 128);")
        self.label_save_tips.setAlignment(Qt.AlignCenter)
        MDCx.setCentralWidget(self.centralwidget)
        self.layoutWidget9.raise_()
        self.layoutWidget9.raise_()
        self.layoutWidget9.raise_()
        self.layoutWidget9.raise_()
        self.widget_setting.raise_()
        self.layoutWidget9.raise_()
        self.layoutWidget9.raise_()
        self.layoutWidget9.raise_()
        self.layoutWidget9.raise_()
        self.progressBar_scrape.raise_()
        self.stackedWidget.raise_()
        self.widget_nfo.raise_()

        self.retranslateUi(MDCx)

        self.stackedWidget.setCurrentIndex(3)
        self.pushButton_open_nfo.setDefault(False)
        self.pushButton_show_hide_logs.setDefault(False)
        self.pushButton_save_failed_list.setDefault(False)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_tips_read_mode.setDefault(False)
        self.pushButton_tips_update_mode.setDefault(False)
        self.pushButton_tips_sort_mode.setDefault(False)
        self.pushButton_tips_normal_mode.setDefault(False)
        self.pushButton_tips_soft.setDefault(False)
        self.pushButton_tips_hard.setDefault(False)


        QMetaObject.connectSlotsByName(MDCx)
    # setupUi

    def retranslateUi(self, MDCx):
        MDCx.setWindowTitle(QCoreApplication.translate("MDCx", u"MDCx", None))
        self.stackedWidget.setStyleSheet("")
        self.pushButton_start_cap.setText(QCoreApplication.translate("MDCx", u"\u5f00\u59cb", None))
        self.label_number1.setText(QCoreApplication.translate("MDCx", u"\u756a\u53f7\uff1a", None))
        self.label_number.setText("")
        self.label_13.setText(QCoreApplication.translate("MDCx", u"\u65e5\u671f\uff1a", None))
        self.label_release.setText("")
        self.label_actor1.setText(QCoreApplication.translate("MDCx", u"\u6f14\u5458\uff1a", None))
        self.label_actor.setText("")
        self.label_outline.setText("")
        self.label_18.setText(QCoreApplication.translate("MDCx", u"\u7b80\u4ecb\uff1a", None))
        self.label_title.setText("")
        self.label_title1.setText(QCoreApplication.translate("MDCx", u"\u6807\u9898\uff1a", None))
        self.label_director.setText("")
        self.label_publish.setText("")
        self.label_23.setText(QCoreApplication.translate("MDCx", u"\u5bfc\u6f14\uff1a", None))
        self.label_24.setText(QCoreApplication.translate("MDCx", u"\u53d1\u884c\uff1a", None))
        self.label_studio.setText("")
        self.label_series.setText("")
        self.label_30.setText(QCoreApplication.translate("MDCx", u"\u5236\u4f5c\uff1a", None))
        self.label_31.setText(QCoreApplication.translate("MDCx", u"\u7cfb\u5217\uff1a", None))
        self.label_tag.setText("")
        self.label_33.setText(QCoreApplication.translate("MDCx", u"\u6807\u7b7e\uff1a", None))
        self.checkBox_cover.setText(QCoreApplication.translate("MDCx", u"\u663e\u793a\u5c01\u9762", None))
        self.label_result.setText(QCoreApplication.translate("MDCx", u" \u7b49\u5f85\u5f00\u59cb ...", None))
        self.label_22.setText(QCoreApplication.translate("MDCx", u"\u65f6\u957f\uff1a", None))
        self.label_runtime.setText("")
        self.label_thumb.setText(QCoreApplication.translate("MDCx", u"\u7f29\u7565\u56fe", None))
        self.label_poster.setText(QCoreApplication.translate("MDCx", u"\u5c01\u9762\u56fe", None))
        self.label_poster1.setText(QCoreApplication.translate("MDCx", u"\u5c01\u9762\uff1a", None))
        ___qtreewidgetitem = self.treeWidget_number.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MDCx", u"111", None));

        __sortingEnabled = self.treeWidget_number.isSortingEnabled()
        self.treeWidget_number.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget_number.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MDCx", u"\u6210\u529f", None));
        ___qtreewidgetitem2 = self.treeWidget_number.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MDCx", u"\u5931\u8d25", None));
        self.treeWidget_number.setSortingEnabled(__sortingEnabled)

        self.label_file_path.setText(QCoreApplication.translate("MDCx", u"\u89c6\u9891\u76ee\u5f55\u8bbe\u7f6e\uff1a\u3010\u8bbe\u7f6e\u3011-\u3010\u76ee\u5f55\u3011-\u3010\u5f85\u522e\u524a\u89c6\u9891\u76ee\u5f55\u3011\u3002\u7a0b\u5e8f\u5c06\u522e\u524a\u8be5\u76ee\u5f55\u53ca\u5b50\u76ee\u5f55\u7684\u6240\u6709\u6587\u4ef6\u3002", None))
        self.label_source.setText("")
        self.pushButton_select_media_folder.setText(QCoreApplication.translate("MDCx", u"\u9009\u62e9\u76ee\u5f55", None))
        self.label_poster_size.setText("")
        self.label_thumb_size.setText("")
        self.pushButton_play.setText("")
        self.pushButton_open_folder.setText("")
        self.pushButton_open_nfo.setText("")
        self.pushButton_right_menu.setText("")
        self.pushButton_tree_clear.setText("")
        self.textBrowser_log_main_2.setHtml(QCoreApplication.translate("MDCx", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">       </p></body></html>", None))
        self.pushButton_start_cap2.setText(QCoreApplication.translate("MDCx", u"\u5f00\u59cb", None))
        self.textBrowser_log_main.setHtml(QCoreApplication.translate("MDCx", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">       </p></body></html>", None))
        self.pushButton_show_hide_logs.setText("")
        self.pushButton_view_failed_list.setText(QCoreApplication.translate("MDCx", u"\u5931\u8d25 0", None))
        self.textBrowser_log_main_3.setHtml(QCoreApplication.translate("MDCx", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">       </p></body></html>", None))
        self.pushButton_scraper_failed_list.setText(QCoreApplication.translate("MDCx", u"\u5f53\u6709\u5931\u8d25\u4efb\u52a1\u65f6\uff0c\u70b9\u51fb\u53ef\u4ee5\u4e00\u952e\u522e\u524a\u5f53\u524d\u5931\u8d25\u5217\u8868", None))
        self.pushButton_save_failed_list.setText("")
        self.pushButton_check_net.setText(QCoreApplication.translate("MDCx", u"\u5f00\u59cb\u68c0\u6d4b", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MDCx", u"\u5355\u6587\u4ef6\u522e\u524a\uff08\u6307\u5b9a\u67d0\u4e2a\u6587\u4ef6\u7684\u756a\u53f7\u7f51\u5740\u8fdb\u884c\u522e\u524a\uff0c\u5f53\u5b58\u5728\u76f8\u540c\u756a\u53f7\u65f6\u53ef\u7528\u8fd9\u4e2a\uff09", None))
        self.pushButton_select_file.setText(QCoreApplication.translate("MDCx", u"\u9009\u62e9\u6587\u4ef6", None))
        self.label_10.setText(QCoreApplication.translate("MDCx", u"*\u756a\u53f7\u7f51\u5740\uff1a", None))
        self.pushButton_start_single_file.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a", None))
        self.label_3.setText(QCoreApplication.translate("MDCx", u"*\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.label.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u8981\u586b\u5199\u7f51\u7ad9\u9996\u9875\u5730\u5740\uff01\uff01\uff01\u8981\u586b\u5199\u8be5\u756a\u53f7\u7684\u7f51\u9875\u5730\u5740\uff01\uff01\uff01\u7136\u540e\u9009\u62e9\u5bf9\u5e94\u7f51\u7ad9\uff0c\u70b9\u51fb\u522e\u524a\u5373\u53ef\uff01", None))
        self.pushButton_select_file_clear_info.setText(QCoreApplication.translate("MDCx", u"\u6e05\u7a7a\u4fe1\u606f", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MDCx", u"\u88c1\u526a\u56fe\u7247\uff08\u5c06\u67d0\u4e2a\u56fe\u7247\u88c1\u526a\u4e3a\u5c01\u9762\u56fe\u5927\u5c0f\uff0c\u652f\u6301\u52a0\u6c34\u5370\uff09", None))
        self.pushButton_select_thumb.setText(QCoreApplication.translate("MDCx", u"\u9009\u62e9\u56fe\u7247", None))
        self.label_6.setText(QCoreApplication.translate("MDCx", u"\u6b64\u5de5\u5177\u652f\u6301\u62d6\u52a8\u9009\u62e9\u88c1\u526a\u8303\u56f4\uff0c\u53ef\u5c06\u56fe\u7247\u88c1\u526a\u4e3a\u5c01\u9762\u56fe\uff08poster\uff09\u3002", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MDCx", u"\u68c0\u67e5\u6f14\u5458\u7f3a\u5931\u756a\u53f7\uff08\u68c0\u67e5\u8d44\u6e90\u5e93\u4e2d\u6307\u5b9a\u6f14\u5458\u672c\u5730\u7f3a\u5931\u7684\u756a\u53f7\uff09", None))
        self.label_53.setText(QCoreApplication.translate("MDCx", u"\u6f14\u5458\u540d\uff1a", None))
        self.label_72.setText(QCoreApplication.translate("MDCx", u"\u672c\u5730\u8d44\u6e90\u5e93\uff1a", None))
        self.pushButton_find_missing_number.setText(QCoreApplication.translate("MDCx", u"\u68c0\u67e5\u7f3a\u5931\u756a\u53f7", None))
        self.pushButton_select_local_library.setText(QCoreApplication.translate("MDCx", u"\u9009\u62e9\u76ee\u5f55", None))
        self.label_62.setText(QCoreApplication.translate("MDCx", u"\u672c\u5730\u8d44\u6e90\u5e93\u548c\u6f14\u5458\u540d\u90fd\u53ef\u4ee5\u586b\u5199\u591a\u4e2a\uff0c\u4ee5\u9017\u53f7\u5206\u5f00\uff08\u4e2d\u82f1\u6587\u9017\u53f7\u90fd\u53ef\u4ee5\uff09", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MDCx", u"\u79fb\u52a8\u89c6\u9891\u3001\u5b57\u5e55\uff08\u5c06\u5f85\u522e\u524a\u76ee\u5f55\u4e0b\u6240\u6709\u5b50\u76ee\u5f55\u4e2d\u7684\u89c6\u9891\u79fb\u52a8\u5230\u4e00\u4e2a\u76ee\u5f55\u4e2d\u4ee5\u65b9\u4fbf\u8fdb\u884c\u67e5\u770b\uff09", None))
        self.pushButton_move_mp4.setText(QCoreApplication.translate("MDCx", u"\u5f00\u59cb\u79fb\u52a8", None))
        self.label_41.setText(QCoreApplication.translate("MDCx", u"\u6392\u9664\u76ee\u5f55\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("MDCx", u"\u79fb\u52a8\u300c\u5f85\u522e\u524a\u89c6\u9891\u76ee\u5f55\u300d\u4e2d\u7684\u6240\u6709\u89c6\u9891\u548c\u5b57\u5e55\u5230\u300c\u5f85\u522e\u524a\u89c6\u9891\u76ee\u5f55\u300d\u4e0b\u7684\u300cMovie_moved\u300d\u76ee\u5f55\u4e0b\u3002", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MDCx", u"\u8f6f\u94fe\u63a5\u52a9\u624b\uff08\u5c06\u6302\u8f7d\u7684\u7f51\u76d8\u6587\u4ef6\u76ee\u5f55\u53ca\u5b50\u76ee\u5f55\u4e2d\u7684\u6240\u6709\u89c6\u9891\u4e00\u952e\u521b\u5efa\u8f6f\u94fe\u63a5\u5230\u672c\u5730\uff09", None))
        self.label_338.setText(QCoreApplication.translate("MDCx", u"\u672c\u5730\u76ee\u5f55\uff1a", None))
        self.label_339.setText(QCoreApplication.translate("MDCx", u"\u7f51\u76d8\u76ee\u5f55\uff1a", None))
        self.pushButton_creat_symlink.setText(QCoreApplication.translate("MDCx", u"\u4e00\u952e\u521b\u5efa\u8f6f\u94fe\u63a5", None))
        self.pushButton_select_netdisk_path.setText(QCoreApplication.translate("MDCx", u"\u9009\u62e9\u76ee\u5f55", None))
        self.label_340.setText(QCoreApplication.translate("MDCx", u"\u672c\u5730\u76ee\u5f55\u4e2d\u7684\u8f6f\u94fe\u63a5\u6587\u4ef6\u4f4d\u7f6e\u5c06\u540c\u6b65\u6309\u7167\u7f51\u76d8\u7684\u6587\u4ef6\u76ee\u5f55\u7ed3\u6784\u521b\u5efa", None))
        self.pushButton_select_localdisk_path.setText(QCoreApplication.translate("MDCx", u"\u9009\u62e9\u76ee\u5f55", None))
        self.checkBox_copy_netdisk_nfo.setText(QCoreApplication.translate("MDCx", u"\u540c\u65f6\u590d\u5236\u7f51\u76d8\u76ee\u5f55\u7684nfo\u3001\u56fe\u7247\u3001\u5b57\u5e55\u6587\u4ef6\u5230\u8f6f\u94fe\u63a5\u76ee\u5f55", None))
        self.label_341.setText(QCoreApplication.translate("MDCx", u"\u52fe\u9009\u540e\u5c06\u540c\u65f6\u590d\u5236\u7f51\u76d8\u4e2d\u522e\u524a\u597d\u7684nfo\u7b49\u6587\u4ef6\u5230\u672c\u5730\uff0c\u6216\u8005\u4f60\u4e5f\u53ef\u4ee5\u91cd\u65b0\u522e\u524a\u8fd9\u4e9b\u8f6f\u94fe\u63a5", None))
        self.checkBox_create_link.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u8fc7\u7a0b\u4e2d\u81ea\u52a8\u521b\u5efa\u8f6f\u94fe\u63a5", None))
#if QT_CONFIG(accessibility)
        self.tabWidget.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.scrollArea_2.setStyleSheet("")
        self.groupBox_16.setTitle(QCoreApplication.translate("MDCx", u"\u522e\u524a\u76ee\u5f55", None))
        self.pushButton_select_softlink_folder.setText(QCoreApplication.translate("MDCx", u"\u9009\u62e9\u76ee\u5f55", None))
        self.label_58.setText(QCoreApplication.translate("MDCx", u"\u6307\u4e0d\u60f3\u8981\u522e\u524a\u7684\u76ee\u5f55\uff0c\u53ef\u4ee5\u586b\u5199\u591a\u4e2a\u76ee\u5f55\uff0c\u4ee5\u9017\u53f7\u5206\u5f00\uff08\u4e2d\u82f1\u6587\u9017\u53f7\u90fd\u53ef\u4ee5\uff09", None))
        self.label_49.setText(QCoreApplication.translate("MDCx", u"\u5f85\u522e\u524a\u89c6\u9891\u76ee\u5f55\uff1a", None))
        self.checkBox_no_escape_dir.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u6392\u9664", None))
        self.label_56.setText(QCoreApplication.translate("MDCx", u"\u6307\u542b\u6709\u89c6\u9891\u7684\u6587\u4ef6\u5939\uff0c\u5c06\u522e\u524a\u8be5\u76ee\u5f55\uff08\u542b\u5b50\u76ee\u5f55\uff09\u6240\u6709\u89c6\u9891\u7684\u5143\u6570\u636e\u4fe1\u606f", None))
        self.checkBox_scrape_softlink_path.setText(QCoreApplication.translate("MDCx", u"\u5728\u4ee5\u4e0b\u76ee\u5f55\u4e3a\u5f85\u522e\u524a\u76ee\u5f55\u4e2d\u7684\u89c6\u9891\u521b\u5efa\u8f6f\u94fe\u63a5\uff0c\u7136\u540e\u522e\u524a\u4ee5\u4e0b\u76ee\u5f55\uff08\u9002\u5408\u7f51\u76d8\u7528\u6237\uff09", None))
        self.label_47.setText(QCoreApplication.translate("MDCx", u"\u6210\u529f\u8f93\u51fa\u76ee\u5f55\uff1a", None))
        self.pushButton_select_media_folder_setting_page.setText(QCoreApplication.translate("MDCx", u"\u9009\u62e9\u76ee\u5f55", None))
        self.label_48.setText(QCoreApplication.translate("MDCx", u"\u6392\u9664\u76ee\u5f55\uff1a", None))
        self.label_57.setText(QCoreApplication.translate("MDCx", u"\u6307\u522e\u524a\u5931\u8d25\u65f6\uff0c\u89c6\u9891\u5c06\u79fb\u52a8\u5230\u8fd9\u4e2a\u6587\u4ef6\u5939\u3002\u8f93\u51fa\u76ee\u5f55\u53ef\u4ee5\u4e0d\u5728\u5f85\u522e\u524a\u89c6\u9891\u76ee\u5f55\u4e0b", None))
        self.pushButton_select_failed_folder.setText(QCoreApplication.translate("MDCx", u"\u9009\u62e9\u76ee\u5f55", None))
        self.label_382.setText("")
        self.label_46.setText(QCoreApplication.translate("MDCx", u"\u5931\u8d25\u8f93\u51fa\u76ee\u5f55\uff1a", None))
        self.pushButton_select_sucess_folder.setText(QCoreApplication.translate("MDCx", u"\u9009\u62e9\u76ee\u5f55", None))
        self.label_29.setText(QCoreApplication.translate("MDCx", u"\u6307\u522e\u524a\u6210\u529f\u65f6\uff0c\u89c6\u9891\u5c06\u79fb\u52a8\u5230\u8fd9\u4e2a\u6587\u4ef6\u5939\u3002\u8f93\u51fa\u76ee\u5f55\u53ef\u4ee5\u4e0d\u5728\u5f85\u522e\u524a\u89c6\u9891\u76ee\u5f55\u4e0b", None))
        self.label_383.setText(QCoreApplication.translate("MDCx", u"\u5982\u679c\u521b\u5efa\u8f6f\u94fe\u63a5\u65f6\u8981\u590d\u5236\u56fe\u7247\u548cNFO\uff0c\u8bf7\u5230\u300c\u5de5\u5177\u300d-\u300c\u8f6f\u94fe\u63a5\u52a9\u624b\u300d\u52fe\u9009\u5373\u53ef\n"
"1\uff0c\u8f6f\u94fe\u63a5\u8def\u5f84\u652f\u6301\u547d\u540d\u5b57\u6bb5\uff1a\n"
"  end_folder_name \uff08\u6307\u5f85\u522e\u524a\u76ee\u5f55\u4e0a\u6700\u540e\u7684\u6587\u4ef6\u5939\u540d\uff0c\u662f\u56fa\u5b9a\u7684\u540d\u5b57\uff09\n"
"2\uff0c\u6210\u529f/\u5931\u8d25\u8f93\u51fa\u76ee\u5f55\u652f\u6301\u547d\u540d\u5b57\u6bb5\uff1aend_folder_name\u3001 \n"
"  first_folder_name \uff08\u6307\u5f85\u522e\u524a\u76ee\u5f55\u4e0b\u7b2c\u4e00\u5c42\u5b50\u6587\u4ef6\u5939\u540d\uff0c\u662f\u52a8\u6001\u7684\u540d\u5b57\uff09", None))
        self.groupBox_32.setTitle(QCoreApplication.translate("MDCx", u"\u6587\u4ef6\u626b\u63cf\u8bbe\u7f6e", None))
        self.label_336.setText(QCoreApplication.translate("MDCx", u"\u68c0\u67e5\u8f6f\u94fe\u63a5\uff1a", None))
        self.label_337.setText(QCoreApplication.translate("MDCx", u"\u52fe\u9009\u540e\u5c06\u68c0\u67e5\u8f6f\u94fe\u63a5\u6587\u4ef6\u6307\u5411\u7684\u76ee\u6807\u6587\u4ef6\u662f\u5426\u5b58\u5728\uff0c\u82e5\u4e0d\u5b58\u5728\u5219\u4f1a\u5220\u9664\u8be5\u8f6f\u94fe\u63a5", None))
        self.label_348.setText(QCoreApplication.translate("MDCx", u"\u652f\u6301\u8bb0\u5f55\u548c\u8df3\u8fc7\u5df2\u522e\u524a\u6210\u529f\u7684\u6587\u4ef6\uff0c\u907f\u514d\u65b0\u589e\u89c6\u9891\u65f6\u91cd\u590d\u522e\u524a\u4e4b\u524d\u6210\u529f\u7684\u6587\u4ef6", None))
        self.checkBox_skip_success_file.setText(QCoreApplication.translate("MDCx", u"\u8df3\u8fc7\u4e4b\u524d\u5df2\u522e\u524a\u6210\u529f\u7684\u6587\u4ef6", None))
        self.checkBox_record_success_file.setText(QCoreApplication.translate("MDCx", u"\u8bb0\u5f55\u522e\u524a\u6210\u529f\u7684\u6587\u4ef6\u5217\u8868", None))
        self.pushButton_view_success_file.setText(QCoreApplication.translate("MDCx", u"\u67e5\u770b", None))
        self.checkBox_no_escape_file.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u8df3\u8fc7", None))
        self.label_346.setText(QCoreApplication.translate("MDCx", u"\u8df3\u8fc7\u5df2\u522e\u524a\u6587\u4ef6\uff1a", None))
        self.label_88.setText(QCoreApplication.translate("MDCx", u"\u8bc6\u522b\u756a\u53f7\u65f6\uff0c\u5c06\u5148\u8fc7\u6ee4\u591a\u4f59\u5b57\u7b26\u518d\u8fdb\u884c\u8bc6\u522b\u3002\uff08\u586b\u5199\u65f6\u4ee5\u9017\u53f7\u5206\u5272\uff0c\u4e0d\u7528\u533a\u5206\u5927\u5c0f\u5199\uff09", None))
        self.checkBox_check_symlink.setText(QCoreApplication.translate("MDCx", u"\u68c0\u67e5\u5e76\u6e05\u7406\u5931\u6548\u7684\u8f6f\u94fe\u63a5", None))
        self.checkBox_check_symlink_definition.setText(QCoreApplication.translate("MDCx", u"\u83b7\u53d6\u8f6f\u94fe\u63a5\u6307\u5411\u7684\u539f\u6587\u4ef6\u7684\u5206\u8fa8\u7387", None))
        self.label_94.setText(QCoreApplication.translate("MDCx", u"\u7528\u4e8e\u8fc7\u6ee4\u672c\u5730\u7684\u4e00\u4e9b\u5e7f\u544a\u89c6\u9891\uff0c\u6b64\u5904\u586b\u5199\u6587\u4ef6\u5927\u5c0f\uff0c\u5c0f\u4e8e\u8be5\u5927\u5c0f\u7684\u89c6\u9891\u5c06\u8df3\u8fc7\u522e\u524a", None))
        self.label_83.setText(QCoreApplication.translate("MDCx", u"\u8fc7\u6ee4\u6587\u4ef6\u540d\u591a\u4f59\u5b57\u7b26\uff1a", None))
        self.label_93.setText(QCoreApplication.translate("MDCx", u"\u8df3\u8fc7\u5c0f\u6587\u4ef6(MB) <\uff1a", None))
        self.groupBox_61.setTitle(QCoreApplication.translate("MDCx", u"\u6587\u4ef6\u6e05\u7406\u8bbe\u7f6e", None))
        self.checkBox_clean_file_ext.setText(QCoreApplication.translate("MDCx", u"\u542f\u7528", None))
        self.label_177.setText(QCoreApplication.translate("MDCx", u"\u6269\u5c55\u540d\u7b49\u4e8e\uff1a", None))
        self.label_184.setText(QCoreApplication.translate("MDCx", u"\u6587\u4ef6\u540d\u5305\u542b\uff1a", None))
        self.checkBox_clean_excluded_file_ext.setText(QCoreApplication.translate("MDCx", u"\u542f\u7528", None))
        self.label_178.setText(QCoreApplication.translate("MDCx", u"\u6587\u4ef6\u540d\u7b49\u4e8e\uff1a", None))
        self.label_262.setText(QCoreApplication.translate("MDCx", u"\u26a0\ufe0f \u6e05\u7406\u6587\u4ef6\u89c4\u5219", None))
        self.checkBox_clean_file_contains.setText(QCoreApplication.translate("MDCx", u"\u542f\u7528", None))
        self.label_199.setText(QCoreApplication.translate("MDCx", u"\u4ee5\u4e0b\u5df2\u542f\u7528\u7684\u89c4\u5219\u4e2d\u6709\u4efb\u4e00\u547d\u4e2d\u65f6\uff0c\u6587\u4ef6\u5c06\u88ab\u6e05\u7406\u3002\uff08\u591a\u4e2a\u5185\u5bb9\u4ee5\uff5c\u5206\u5272\uff0c\u533a\u5206\u5927\u5c0f\u5199\uff09", None))
        self.label_261.setText(QCoreApplication.translate("MDCx", u"\u6587\u4ef6\u540d\u5305\u542b\uff1a", None))
        self.label_270.setText(QCoreApplication.translate("MDCx", u"\u26a0\ufe0f \u4e0d\u6e05\u7406\u6587\u4ef6\u89c4\u5219", None))
        self.checkBox_clean_excluded_file_contains.setText(QCoreApplication.translate("MDCx", u"\u542f\u7528", None))
        self.label_202.setText(QCoreApplication.translate("MDCx", u"\u6269\u5c55\u540d\u7b49\u4e8e\uff1a", None))
        self.label_263.setText(QCoreApplication.translate("MDCx", u"\u6587\u4ef6\u5927\u5c0f(KB)<=\uff1a", None))
        self.label_162.setText(QCoreApplication.translate("MDCx", u"\u4ee5\u4e0b\u5df2\u542f\u7528\u7684\u89c4\u5219\u4e2d\u6709\u4efb\u4e00\u547d\u4e2d\u65f6\uff0c\u6587\u4ef6\u5c06\u4e0d\u88ab\u6e05\u7406\u3002\uff08\u4f1a\u4f18\u5148\u5904\u7406\u4e0d\u6e05\u7406\u6587\u4ef6\u89c4\u5219\uff09", None))
        self.checkBox_clean_file_size.setText(QCoreApplication.translate("MDCx", u"\u542f\u7528", None))
        self.checkBox_clean_file_name.setText(QCoreApplication.translate("MDCx", u"\u542f\u7528", None))
        self.pushButton_check_and_clean_files.setText(QCoreApplication.translate("MDCx", u"\u70b9\u51fb\u68c0\u67e5\u5f85\u522e\u524a\u76ee\u5f55\u5e76\u6e05\u7406\u6587\u4ef6", None))
        self.checkBox_auto_clean.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u65f6\u81ea\u52a8\u6e05\u7406", None))
        self.checkBox_i_agree_clean.setText(QCoreApplication.translate("MDCx", u"\u6211\u5df2\u540c\u610f\uff1a\u65e0\u8bba\u51fa\u73b0\u4efb\u4f55\u95ee\u9898\uff0c\u5747\u4e0e\u5f00\u53d1\u8005\u65e0\u5173\uff0c\u540e\u679c\u81ea\u884c\u627f\u62c5\u3002", None))
        self.checkBox_i_understand_clean.setText(QCoreApplication.translate("MDCx", u"\u6211\u5df2\u77e5\u6653\uff1a\u6587\u4ef6\u5220\u9664\u540e\u65e0\u6cd5\u6062\u590d\uff01\u64cd\u4f5c\u987b\u8c28\u614e\uff01", None))
        self.label_271.setText(QCoreApplication.translate("MDCx", u"\u26a0\ufe0f \u4f7f\u7528\u524d\u8bf7\u786e\u8ba4\u89c4\u5219\u662f\u5426\u5df2\u542f\u7528\uff01\uff01\uff01\u4e0d\u542f\u7528\u4e0d\u751f\u6548\uff01\uff01\uff01", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MDCx", u"\u6587\u4ef6\u683c\u5f0f\u8bbe\u7f6e", None))
        self.label_78.setText(QCoreApplication.translate("MDCx", u"\u5b57\u5e55\u683c\u5f0f\uff1a", None))
        self.label_50.setText(QCoreApplication.translate("MDCx", u"\u89c6\u9891\u683c\u5f0f\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MDCx", u" \u522e\u524a\u76ee\u5f55 ", None))
        self.groupBox.setTitle(QCoreApplication.translate("MDCx", u"\u522e\u524a\u6a21\u5f0f", None))
        self.radioButton_mode_sort.setText(QCoreApplication.translate("MDCx", u"\u89c6\u9891\u6a21\u5f0f", None))
        self.label_231.setText("")
        self.label_312.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u522e\u524a\uff0c\u8bfb\u53d6\u672c\u5730\u4fe1\u606f\u5e76\u663e\u793a\uff0c\u9002\u5408\u68c0\u67e5\u5a92\u4f53\u5e93\u6216\u5a92\u4f53\u5e93\u91cd\u65b0\u6574\u7406\u5206\u7c7b", None))
        self.pushButton_tips_read_mode.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_tips_read_mode.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.radioButton_mode_common.setText(QCoreApplication.translate("MDCx", u"\u6b63\u5e38\u6a21\u5f0f", None))
        self.checkBox_read_has_nfo_update.setText(QCoreApplication.translate("MDCx", u"\u672c\u5730\u5df2\u522e\u524a\u6210\u529f\u7684\u6587\u4ef6\uff0c\u91cd\u65b0\u6574\u7406\u5206\u7c7b\uff08\u6309\u66f4\u65b0\u6a21\u5f0f\u89c4\u5219\uff09", None))
        self.label_345.setText(QCoreApplication.translate("MDCx", u"\u65e0\u9700\u8054\u7f51", None))
        self.label_252.setText("")
        self.checkBox_read_translate_again.setText(QCoreApplication.translate("MDCx", u"\u91cd\u65b0\u7ffb\u8bd1\u6620\u5c04 nfo \u7684\u4fe1\u606f", None))
        self.label_37.setText(QCoreApplication.translate("MDCx", u"\u5c06\u6309\u300c\u8bbe\u7f6e\u300d-\u300c\u7ffb\u8bd1\u300d\uff0c\u66f4\u65b0 nfo \u4fe1\u606f", None))
        self.checkBox_read_download_file_again.setText(QCoreApplication.translate("MDCx", u"\u91cd\u65b0\u4e0b\u8f7d\u56fe\u7247\u7b49\u6587\u4ef6\uff08nfo \u9700\u6709\u94fe\u63a5\uff09", None))
        self.label_347.setText(QCoreApplication.translate("MDCx", u"\u5c06\u6309\u300c\u8bbe\u7f6e\u300d-\u300c\u4e0b\u8f7d\u300d\uff0c\u66f4\u65b0\u6587\u4ef6", None))
        self.checkBox_read_no_nfo_scrape.setText(QCoreApplication.translate("MDCx", u"\u672c\u5730\u4e4b\u524d\u522e\u524a\u5931\u8d25\u7684\u6587\u4ef6\uff0c\u91cd\u65b0\u522e\u524a\uff08\u6309\u66f4\u65b0\u6a21\u5f0f\u89c4\u5219\uff09", None))
        self.label_36.setText(QCoreApplication.translate("MDCx", u"\u6d41\u7a0b\u540c\u6b63\u5e38\u6a21\u5f0f\uff0c\u4f46\u547d\u540d\u6309\u7167\u66f4\u65b0\u6a21\u5f0f\u89c4\u5219\u6267\u884c\uff08\u5728\u4e0b\u65b9\u8bbe\u7f6e\uff09\uff0c\u9002\u5408\u4e8c\u6b21\u522e\u524a", None))
        self.pushButton_tips_update_mode.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_tips_update_mode.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.radioButton_mode_read.setText(QCoreApplication.translate("MDCx", u"\u8bfb\u53d6\u6a21\u5f0f", None))
        self.radioButton_mode_update.setText(QCoreApplication.translate("MDCx", u"\u66f4\u65b0\u6a21\u5f0f", None))
        self.label_15.setText(QCoreApplication.translate("MDCx", u"\u6267\u884c\uff1a\u522e\u524a->\u91cd\u547d\u540d\uff0c\u4ec5\u6574\u7406\u672c\u5730\u89c6\u9891\uff0c\u4e0d\u4e0b\u8f7d\u56fe\u7247\uff0c\u9002\u5408\u4e0d\u8981\u6d77\u62a5\u5899\u7684\u60c5\u51b5", None))
        self.pushButton_tips_sort_mode.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_tips_sort_mode.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.checkBox_sortmode_delpic.setText(QCoreApplication.translate("MDCx", u"\u5220\u9664\u672c\u5730\u5df2\u4e0b\u8f7d\u7684\u56fe\u7247\u548c nfo \u6587\u4ef6", None))
        self.label_27.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u52fe\u9009\uff0c\u5219\u4e0d\u5220\u9664", None))
        self.label_344.setText("")
        self.label_11.setText(QCoreApplication.translate("MDCx", u"\u6267\u884c\uff1a\u522e\u524a->\u4e0b\u8f7d\u5c01\u9762->\u91cd\u547d\u540d->\u6c34\u5370\u7b49\u5168\u90e8\u64cd\u4f5c\uff0c\u9002\u5408\u8981\u6d77\u62a5\u5899\u7684\u60c5\u51b5", None))
        self.pushButton_tips_normal_mode.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_tips_normal_mode.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.groupBox_27.setTitle(QCoreApplication.translate("MDCx", u"\u522e\u524a\u6210\u529f\u540e\u79fb\u52a8\u6587\u4ef6", None))
        self.gridLayoutWidget_6.setStyleSheet(QCoreApplication.translate("MDCx", u"color: rgb(80, 80, 80);", None))
        self.label_54.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u6210\u529f\u65f6\uff0c\u79fb\u52a8\u6587\u4ef6\u5230\u6210\u529f\u8f93\u51fa\u76ee\u5f55", None))
        self.label_55.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u6210\u529f\u65f6\uff0c\u4e0d\u79fb\u52a8\u6587\u4ef6\u4f4d\u7f6e\uff0c\u4ecd\u5728\u539f\u76ee\u5f55\uff08\u9002\u5408\u5df2\u6574\u7406\u597d\u6587\u4ef6\u5939\u6216\u4e8c\u6b21\u522e\u524a\u573a\u666f\uff09", None))
        self.radioButton_succ_move_on.setText(QCoreApplication.translate("MDCx", u"\u5f00", None))
        self.radioButton_succ_move_off.setText(QCoreApplication.translate("MDCx", u"\u5173", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MDCx", u"\u522e\u524a\u5931\u8d25\u65f6\u79fb\u52a8\u6587\u4ef6", None))
        self.label_34.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u5931\u8d25\u540e\uff0c\u79fb\u52a8\u6587\u4ef6\u5230\u5931\u8d25\u8f93\u51fa\u76ee\u5f55", None))
        self.label_35.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u5931\u8d25\u540e\uff0c\u4e0d\u79fb\u52a8\u6587\u4ef6\u4f4d\u7f6e\uff0c\u4ecd\u5728\u539f\u76ee\u5f55", None))
        self.radioButton_fail_move_on.setText(QCoreApplication.translate("MDCx", u"\u5f00", None))
        self.radioButton_fail_move_off.setText(QCoreApplication.translate("MDCx", u"\u5173", None))
        self.groupBox_30.setTitle(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7ed3\u675f\u540e\u5220\u9664\u7a7a\u6587\u4ef6\u5939", None))
        self.label_44.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7ed3\u675f\u540e\uff0c\u5220\u9664\u522e\u524a\u76ee\u5f55\u4e2d\u7684\u6240\u6709\u7a7a\u6587\u4ef6\u5939", None))
        self.label_51.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7ed3\u675f\u540e\uff0c\u4e0d\u5220\u9664\u7a7a\u6587\u4ef6\u5939", None))
        self.radioButton_del_empty_folder_on.setText(QCoreApplication.translate("MDCx", u"\u5f00", None))
        self.radioButton_del_empty_folder_off.setText(QCoreApplication.translate("MDCx", u"\u5173", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MDCx", u"\u66f4\u65b0\u6a21\u5f0f\u89c4\u5219", None))
        self.label_219.setText("")
        self.label_218.setText(QCoreApplication.translate("MDCx", u"D\u76ee\u5f55\u547d\u540d\u89c4\u5219  ", None))
        self.label_14.setText(QCoreApplication.translate("MDCx", u"\u66f4\u65b0\u89c6\u9891\u540c\u7ea7\u76ee\u5f55\u4e0b\u7684\u5185\u5bb9\uff0c\u5373\uff1a../A/B/C[NEW].mp4", None))
        self.label_20.setText(QCoreApplication.translate("MDCx", u"\u5728\u89c6\u9891\u6240\u5728\u76ee\u5f55\u4e0b\u4e3a\u89c6\u9891\u521b\u5efaD\u76ee\u5f55\uff0c\u5e76\u66f4\u65b0C\u5185\u5bb9\uff0c\u5373\uff1a../A/B/D/C[NEW].mp4", None))
        self.label_220.setText("")
        self.label_210.setText(QCoreApplication.translate("MDCx", u"B\u76ee\u5f55\u547d\u540d\u89c4\u5219  ", None))
        self.radioButton_update_b_c.setText(QCoreApplication.translate("MDCx", u"\u66f4\u65b0B\u548cC", None))
        self.label_25.setText(QCoreApplication.translate("MDCx", u"\u66f4\u65b0\u89c6\u9891\u6240\u5728\u76ee\u5f55\u53ca\u8be5\u76ee\u5f55\u4e0b\u7684\u5185\u5bb9\uff0c\u5373\uff1a../A/B[NEW]/C[NEW].mp4", None))
        self.radioButton_update_d_c.setText(QCoreApplication.translate("MDCx", u"\u521b\u5efaD\u76ee\u5f55", None))
        self.radioButton_update_c.setText(QCoreApplication.translate("MDCx", u"\u53ea\u66f4\u65b0C", None))
        self.label_221.setText("")
        self.checkBox_update_a.setText(QCoreApplication.translate("MDCx", u"\u540c\u65f6\u66f4\u65b0A\u76ee\u5f55  ", None))
        self.label_12.setText(QCoreApplication.translate("MDCx", u"\u5047\u5b9a\u89c6\u9891\u6587\u4ef6\u73b0\u5728\u7684\u8def\u5f84\u662f\uff1a ../A/B/C.mp4", None))
        self.label_21.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>\u26a0\ufe0f \u4fdd\u7559\u6587\u4ef6\uff1a\u8bf7\u5230 \u8bbe\u7f6e > \u4e0b\u8f7d > \u4fdd\u7559\u65e7\u6587\u4ef6 \u6216 \u4e0b\u8f7d\uff0c\u8bbe\u7f6e\u8981\u4fdd\u7559\u6216\u66f4\u65b0\u7684\u6587\u4ef6\u5185\u5bb9<br>\n"
"\u26a0\ufe0f \u8df3\u8fc7\u6587\u4ef6\uff1a\u5728\u89c6\u9891\u76ee\u5f55\u65b0\u5efa\u4e00\u4e2a\u540d\u4e3a skip \u7684\u7a7a\u6587\u4ef6\uff0c\u5373\u53ef\u81ea\u52a8\u8df3\u8fc7\u8be5\u76ee\u5f55\u53ca\u5b50\u76ee\u5f55\uff08\u6240\u6709\u6a21\u5f0f\u5747\u6709\u6548\uff09<br>\n"
"\u26a0\ufe0f \u79fb\u52a8\u6587\u4ef6\uff1a\u5931\u8d25\u65f6\u4e0d\u79fb\u52a8\u6587\u4ef6\uff0c\u6210\u529f\u65f6\u6309\u66f4\u65b0\u6a21\u5f0f\u89c4\u5219\u79fb\u52a8<br>\n"
"\u26a0\ufe0f \u91cd\u547d\u540d\u6587\u4ef6\uff1a\u5728\u300c\u6210\u529f\u540e\u91cd\u547d\u540d\u6587\u4ef6\u300d\u4e2d\u8bbe\u7f6e\u662f\u5426\u91cd\u547d\u540d\uff0c\u547d\u540d\u89c4\u5219\u540c\u300c\u547d\u540d\u300d-\u300c\u89c6\u9891\u6587\u4ef6\u540d\u300d</p>", None))
        self.label_304.setText("")
        self.groupBox_18.setTitle(QCoreApplication.translate("MDCx", u"\u522e\u524a\u6210\u529f\u540e\u91cd\u547d\u540d\u6587\u4ef6", None))
        self.label_38.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u6210\u529f\u65f6\uff0c\u6309\u300c\u547d\u540d\u300d-\u300c\u89c6\u9891\u547d\u540d\u89c4\u5219\u300d-\u300c\u89c6\u9891\u6587\u4ef6\u540d\u300d\u91cd\u547d\u540d\u6587\u4ef6", None))
        self.label_39.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u6210\u529f\u65f6\uff0c\u7ee7\u7eed\u4f7f\u7528\u539f\u6765\u6587\u4ef6\u540d", None))
        self.radioButton_succ_rename_on.setText(QCoreApplication.translate("MDCx", u"\u5f00", None))
        self.radioButton_succ_rename_off.setText(QCoreApplication.translate("MDCx", u"\u5173", None))
        self.groupBox_53.setTitle(QCoreApplication.translate("MDCx", u"\u591a\u7ebf\u7a0b\u522e\u524a", None))
        self.label_237.setText(QCoreApplication.translate("MDCx", u"javdb\u5ef6\u65f6(\u79d2)", None))
        self.label_26.setText(QCoreApplication.translate("MDCx", u"\u8bbe\u7f6e javdb \u5ef6\u65f6\u53ef\u964d\u4f4e javdb \u88ab\u5c01\u6982\u7387\uff0c\u5c06\u57281/2\u5ef6\u65f6-1\u5ef6\u65f6\u4e4b\u95f4\u968f\u673a\u3002", None))
        self.label_82.setText(QCoreApplication.translate("MDCx", u"\u7ebf\u7a0b\u6570\u91cf", None))
        self.label_238.setText(QCoreApplication.translate("MDCx", u"\u7ebf\u7a0b\u95f4\u9694(\u79d2)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MDCx", u"\u522e\u524a\u6210\u529f\u540e\u5728\u8f93\u51fa\u76ee\u5f55\u521b\u5efa\u8f6f\u94fe\u63a5\u6216\u786c\u94fe\u63a5", None))
        self.radioButton_soft_off.setText(QCoreApplication.translate("MDCx", u"\u5173", None))
        self.radioButton_soft_on.setText(QCoreApplication.translate("MDCx", u"\u521b\u5efa\u8f6f\u94fe\u63a5", None))
        self.label_link_off.setText(QCoreApplication.translate("MDCx", u"\u9002\u5408 NAS \u548c\u786c\u76d8\u7528\u6237\u3002\u672c\u5730\u515a\u53ef\u968f\u5fc3\u6240\u6b32\u6574\u7406\u6587\u4ef6\u3002\n"
"\u6ce8\u610f\uff1a\u9009\u62e9\u6b64\u9879\uff0c\u4e0b\u9762\u7684\u300c\u6210\u529f\u540e\u79fb\u52a8\u6587\u4ef6\u300d\u300c\u5931\u8d25\u540e\u79fb\u52a8\u6587\u4ef6\u300d\u624d\u4f1a\u751f\u6548", None))
        self.radioButton_hard_on.setText(QCoreApplication.translate("MDCx", u"\u521b\u5efa\u786c\u94fe\u63a5", None))
#if QT_CONFIG(tooltip)
        self.label_softlink.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_softlink.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_softlink.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.label_softlink.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.label_softlink.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_softlink.setText(QCoreApplication.translate("MDCx", u"\u9002\u5408\u7f51\u76d8\u7528\u6237\u3002\u522e\u524a\u8d44\u6599\u5b58\u672c\u5730\uff0cEmby \u52a0\u8f7d\u5feb\uff0c\u7f51\u76d8\u8bfb\u5199\u5c11\u3002\n"
"\u6ce8\u610f\uff1aWindows \u7528\u6237\uff0c\u6210\u529f\u540e\u7684\u8f93\u51fa\u76ee\u5f55\u5fc5\u987b\u9009\u62e9\u672c\u5730\u78c1\u76d8\uff08\u7cfb\u7edf\u9650\u5236\uff09", None))
        self.pushButton_tips_soft.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_tips_soft.setShortcut("")
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.label_hardlink.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_hardlink.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_hardlink.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.label_hardlink.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.label_hardlink.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_hardlink.setText(QCoreApplication.translate("MDCx", u"\u9002\u5408 PT \u7528\u6237\u3002\u522e\u524a\u8d44\u6599\u540c\u76d8\u5355\u72ec\u5b58\u653e\uff0c\u4e0d\u5f71\u54cd\u5206\u4eab\u7387\u3002\n"
"\u6ce8\u610f\uff1aMac \u7528\u6237\uff0c\u8bf7\u9009\u62e9\u521b\u5efa\u8f6f\u8fde\u63a5\uff0c\u8f93\u51fa\u76ee\u5f55\u540c\u76d8\u5373\u53ef\uff08\u786c\u94fe\u63a5\u6709\u6743\u9650\u95ee\u9898\uff09", None))
        self.pushButton_tips_hard.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_tips_hard.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.label_342.setText(QCoreApplication.translate("MDCx", u"\u6ce8\uff1a\u8f6f\u786c\u94fe\u63a5\u4e0d\u4f1a\u79fb\u52a8\u548c\u91cd\u547d\u540d\u539f\u89c6\u9891\u6587\u4ef6\uff0c\u4ec5\u79fb\u52a8\u548c\u91cd\u547d\u540d\u94fe\u63a5\u6587\u4ef6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MDCx", u" \u522e\u524a\u6a21\u5f0f ", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("MDCx", u"\u6807\u9898", None))
        self.label_186.setText(QCoreApplication.translate("MDCx", u"\u6392\u9664\u7f51\u7ad9\uff1a", None))
        self.label_76.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u540c\u7f51\u7ad9\u5b57\u6bb5\u51c6\u786e\u5ea6\u4e0d\u540c\uff0c\u4f60\u53ef\u8bbe\u7f6e\u522e\u524a\u7f51\u7ad9\u7684\u987a\u5e8f\uff0c\u591a\u4e2a\u4ee5\u9017\u53f7\u5206\u9694", None))
        self.label_114.setText(QCoreApplication.translate("MDCx", u"\u539f\u6807\u9898\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.label_404.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u6807\u9898\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.checkBox_use_official_data.setText(QCoreApplication.translate("MDCx", u"\u4f18\u5148\u4f7f\u7528\u7247\u5546\u5b98\u7f51\u6570\u636e", None))
        self.label_401.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u8bbe\u7f6e\uff1a", None))
        self.label_400.setText(QCoreApplication.translate("MDCx", u"\u5f53\u6807\u9898\u8bed\u8a00\u8bbe\u7f6e\u4e3a\u4e2d\u6587\u65f6\uff0c\u5c06\u5c1d\u8bd5\u4ece\u8fd9\u4e9b\u7f51\u7ad9\u83b7\u53d6\u4e2d\u6587\u6807\u9898", None))
        self.label_86.setText(QCoreApplication.translate("MDCx", u"\u7528\u4e8e\u6392\u9664\u5b57\u6bb5\u4e0d\u5b58\u5728\u6216\u4e0d\u5408\u9002\u7684\u7f51\u7ad9\uff0c\u5728\u8bf7\u6c42\u8be5\u5b57\u6bb5\u7f51\u7ad9\u65f6\u5c06\u4e0d\u522e\u524a\u8fd9\u4e9b\u7f51\u7ad9", None))
        self.label_405.setText(QCoreApplication.translate("MDCx", u"\u90e8\u5206\u756a\u53f7\u53ef\u4ee5\u4ece\u5b98\u7f51\u83b7\u53d6\u6570\u636e\uff0c\u5982\u679c\u52fe\u9009\u6b64\u9879\uff0c\u5404\u5b57\u6bb5\u5c06\u4f18\u5148\u4f7f\u7528\u5b98\u7f51\u6570\u636e", None))
        self.pushButton_field_tips_website.setText(QCoreApplication.translate("MDCx", u"\u8be6\u7ec6\u8bf4\u660e", None))
        self.groupBox_76.setTitle(QCoreApplication.translate("MDCx", u"\u6807\u7b7e", None))
        self.label_144.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.label_188.setText(QCoreApplication.translate("MDCx", u"\u6392\u9664\u7f51\u7ad9\uff1a", None))
        self.radioButton_tag_listed.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u5217\u51fa\u7684\u7f51\u7ad9", None))
        self.radioButton_tag_more.setText(QCoreApplication.translate("MDCx", u"\u5c3d\u91cf\u8865\u5168\u5b57\u6bb5", None))
        self.radioButton_tag_none.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u5355\u72ec\u522e\u524a", None))
        self.label_214.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u8bbe\u7f6e\uff1a", None))
        self.groupBox_29.setTitle(QCoreApplication.translate("MDCx", u"\u7b80\u4ecb", None))
        self.label_142.setText(QCoreApplication.translate("MDCx", u"\u539f\u7b80\u4ecb\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.label_198.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u8bbe\u7f6e\uff1a", None))
        self.radioButton_outline_listed.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u5217\u51fa\u7684\u7f51\u7ad9", None))
        self.radioButton_outline_more.setText(QCoreApplication.translate("MDCx", u"\u5c3d\u91cf\u8865\u5168\u5b57\u6bb5", None))
        self.radioButton_outline_none.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u5355\u72ec\u522e\u524a", None))
        self.label_187.setText(QCoreApplication.translate("MDCx", u"\u6392\u9664\u7f51\u7ad9\uff1a", None))
        self.label_406.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u7b80\u4ecb\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.label_136.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>\u522e\u524a\u5217\u51fa\u7684\u7f51\u7ad9\uff1a\u4f9d\u6b21\u522e\u524a\u5217\u51fa\u7f51\u7ad9\uff0c\u6709\u7ed3\u679c\u65f6\u505c\u6b62\uff1b\u65e0\u7ed3\u679c\u65f6\u4e0d\u989d\u5916\u8054\u7f51\u522e\u524a\u65b0\u7f51\u7ad9<br>\n"
"\u5c3d\u91cf\u8865\u5168\u5b57\u6bb5\uff1a\u4f9d\u6b21\u522e\u524a\u5217\u51fa\u7f51\u7ad9\u548c\u756a\u53f7\u7c7b\u578b\u5269\u4f59\u7f51\u7ad9\uff0c\u76f4\u5230\u6709\u7ed3\u679c\u65f6\u505c\u6b62<br>\n"
"\u4e0d\u5355\u72ec\u522e\u524a\uff1a\u4e0d\u989d\u5916\u8054\u7f51\u522e\u524a\u65b0\u7f51\u7ad9\uff0c\u800c\u662f\u4ece\u5df2\u522e\u524a\u7f51\u7ad9\u6570\u636e\u4e2d\u53d6\u503c</p>", None))
        self.groupBox_80.setTitle(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7f51\u7ad9\uff08\u901f\u5ea6\u4f18\u5148\u6309\u8fd9\u4e2a\u987a\u5e8f\u522e\u524a\uff0c\u5b57\u6bb5\u4f18\u5148\u4e0e\u8fd9\u4e2a\u53d6\u4ea4\u96c6\uff09", None))
        self.label_151.setText(QCoreApplication.translate("MDCx", u"\u65e0\u7801\u756a\u53f7\uff1a", None))
        self.label_316.setText(QCoreApplication.translate("MDCx", u"\u52a8\u6f2b\u91cc\u756a\uff1a", None))
        self.label_322.setText(QCoreApplication.translate("MDCx", u"Mywife\uff1a", None))
        self.label_232.setText(QCoreApplication.translate("MDCx", u"\u53ef\u5230\u300c\u7f51\u7ad9\u504f\u597d\u300d-\u300c\u6307\u5b9a\u7f51\u7ad9\u300d\u6307\u5b9a mdtv\u3001hdouban\uff0c\u6216\u6587\u4ef6\u8def\u5f84\u542b\u6709\u300c\u56fd\u4ea7\u300d\u3001\u300c\u9ebb\u8c46\u300d\u65f6\uff0c\u5c06\u81ea\u52a8\u4f7f\u7528\u4ee5\u4e0a\u7f51\u7ad9\u522e\u524a\u56fd\u4ea7\u756a\u53f7", None))
        self.label_156.setText(QCoreApplication.translate("MDCx", u"\u6bd4\u5982\uff1a259LUXU-1111", None))
        self.label_157.setText(QCoreApplication.translate("MDCx", u"\u6bd4\u5982\uff1aFC2-111111", None))
        self.label_158.setText(QCoreApplication.translate("MDCx", u"\u6bd4\u5982\uff1asexart.11.11.11", None))
        self.label_149.setText(QCoreApplication.translate("MDCx", u"\u6b27\u7f8e\u756a\u53f7\uff1a", None))
        self.label_155.setText(QCoreApplication.translate("MDCx", u"\u6bd4\u5982\uff1a111111-111\uff0c111111_111\uff0cn1111\uff0cHEYZO-1111\uff0cSMD-111", None))
        self.label_318.setText(QCoreApplication.translate("MDCx", u"\u53ef\u5230\u300c\u7f51\u7ad9\u504f\u597d\u300d-\u300c\u6307\u5b9a\u7f51\u7ad9\u300d\u6307\u5b9a getchu\u3001dmm\u3001getchu_dmm\uff0c\u6216\u6587\u4ef6\u8def\u5f84\u542b\u6709\u300c\u91cc\u756a\u300d\u3001\u300c\u52a8\u6f2b\u300d\u65f6\uff0c\u5c06\u81ea\u52a8\u4f7f\u7528 getchu_dmm\uff08\u4e8c\u5408\u4e00\uff09 \u522e\u524a", None))
        self.label_323.setText(QCoreApplication.translate("MDCx", u"\u53ef\u5230\u300c\u7f51\u7ad9\u504f\u597d\u300d-\u300c\u6307\u5b9a\u7f51\u7ad9\u300d\u6307\u5b9a mywife\uff0c\u6216\u6587\u4ef6\u8def\u5f84\u542b\u6709 mywife\u65f6\uff0c\u5c06\u81ea\u52a8\u4f7f\u7528 mywife \u522e\u524a\uff08Mywife \u756a\u53f7\u89c4\u5219\uff1a Mywife No.1230\uff09", None))
        self.label_154.setText(QCoreApplication.translate("MDCx", u"\u6bd4\u5982\uff1aMIDE-111\uff0c\u4ee5\u53ca\u4e0d\u7b26\u5408\u4ee5\u4e0b\u7c7b\u578b\u7684\u756a\u53f7", None))
        self.label_152.setText(QCoreApplication.translate("MDCx", u"\u7d20\u4eba\u756a\u53f7\uff1a", None))
        self.label_153.setText(QCoreApplication.translate("MDCx", u"\u6709\u7801\u756a\u53f7\uff1a", None))
        self.label_148.setText(QCoreApplication.translate("MDCx", u"FC2\u756a\u53f7\uff1a", None))
        self.label_217.setText(QCoreApplication.translate("MDCx", u"\u56fd\u4ea7\u756a\u53f7\uff1a", None))
        self.groupBox_47.setTitle(QCoreApplication.translate("MDCx", u"\u6f14\u5458", None))
        self.label_143.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.label_179.setText(QCoreApplication.translate("MDCx", u"\u6392\u9664\u7f51\u7ad9\uff1a", None))
        self.label_200.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u8bbe\u7f6e\uff1a", None))
        self.radioButton_actor_listed.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u5217\u51fa\u7684\u7f51\u7ad9", None))
        self.radioButton_actor_more.setText(QCoreApplication.translate("MDCx", u"\u5c3d\u91cf\u8865\u5168\u5b57\u6bb5", None))
        self.radioButton_actor_none.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u5355\u72ec\u522e\u524a", None))
        self.groupBox_48.setTitle(QCoreApplication.translate("MDCx", u"\u7247\u5546", None))
        self.label_215.setText(QCoreApplication.translate("MDCx", u"\u6392\u9664\u7f51\u7ad9\uff1a", None))
        self.label_211.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.radioButton_studio_listed.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u5217\u51fa\u7684\u7f51\u7ad9", None))
        self.radioButton_studio_more.setText(QCoreApplication.translate("MDCx", u"\u5c3d\u91cf\u8865\u5168\u5b57\u6bb5", None))
        self.radioButton_studio_none.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u5355\u72ec\u522e\u524a", None))
        self.label_257.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u8bbe\u7f6e\uff1a", None))
        self.groupBox_35.setTitle(QCoreApplication.translate("MDCx", u"\u7cfb\u5217", None))
        self.label_201.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.label_205.setText(QCoreApplication.translate("MDCx", u"\u6392\u9664\u7f51\u7ad9\uff1a", None))
        self.radioButton_series_listed.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u5217\u51fa\u7684\u7f51\u7ad9", None))
        self.radioButton_series_more.setText(QCoreApplication.translate("MDCx", u"\u5c3d\u91cf\u8865\u5168\u5b57\u6bb5", None))
        self.radioButton_series_none.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u5355\u72ec\u522e\u524a", None))
        self.label_254.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u8bbe\u7f6e\uff1a", None))
        self.groupBox_49.setTitle(QCoreApplication.translate("MDCx", u"\u53d1\u884c\u5546", None))
        self.label_223.setText(QCoreApplication.translate("MDCx", u"\u6392\u9664\u7f51\u7ad9\uff1a", None))
        self.label_222.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.radioButton_publisher_listed.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u5217\u51fa\u7684\u7f51\u7ad9", None))
        self.radioButton_publisher_more.setText(QCoreApplication.translate("MDCx", u"\u5c3d\u91cf\u8865\u5168\u5b57\u6bb5", None))
        self.radioButton_publisher_none.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u5355\u72ec\u522e\u524a", None))
        self.label_258.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u8bbe\u7f6e\uff1a", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MDCx", u"\u7f51\u7ad9\u504f\u597d", None))
        self.radioButton_scrape_single.setText(QCoreApplication.translate("MDCx", u"\u6307\u5b9a\u7f51\u7ad9", None))
        self.label_32.setText(QCoreApplication.translate("MDCx", u"\u6309\u5404\u4e2a\u5b57\u6bb5\u8bbe\u7f6e\u7684\u522e\u524a\u7f51\u7ad9\u8fdb\u884c\u522e\u524a\uff0c\u5b57\u6bb5\u6765\u81ea\u591a\u4e2a\u7f51\u7ad9\u3002\u5b57\u6bb5\u5168\u4e00\u4e9b\u3002", None))
        self.label_317.setText(QCoreApplication.translate("MDCx", u"\u5f53\u6307\u5b9a\u7f51\u7ad9\u65f6\uff0c\u6240\u6709\u756a\u53f7\u5c06\u53ea\u4f7f\u7528\u8be5\u7f51\u7ad9\u522e\u524a\uff01", None))
        self.radioButton_scrape_info.setText(QCoreApplication.translate("MDCx", u"\u5b57\u6bb5\u4f18\u5148", None))
        self.label_28.setText(QCoreApplication.translate("MDCx", u"\u6309\u756a\u53f7\u7c7b\u578b\u8bbe\u7f6e\u7684\u522e\u524a\u7f51\u7ad9\u8fdb\u884c\u522e\u524a\uff0c\u5b57\u6bb5\u6765\u81ea\u5355\u4e2a\u7f51\u7ad9\u3002\u901f\u5ea6\u5feb\u4e00\u4e9b\u3002", None))
        self.radioButton_scrape_speed.setText(QCoreApplication.translate("MDCx", u"\u901f\u5ea6\u4f18\u5148", None))
        self.comboBox_website_all.setItemText(0, QCoreApplication.translate("MDCx", u"airav_cc", None))
        self.comboBox_website_all.setItemText(1, QCoreApplication.translate("MDCx", u"airav", None))
        self.comboBox_website_all.setItemText(2, QCoreApplication.translate("MDCx", u"avsex", None))
        self.comboBox_website_all.setItemText(3, QCoreApplication.translate("MDCx", u"avsox", None))
        self.comboBox_website_all.setItemText(4, QCoreApplication.translate("MDCx", u"freejavbt", None))
        self.comboBox_website_all.setItemText(5, QCoreApplication.translate("MDCx", u"iqqtv", None))
        self.comboBox_website_all.setItemText(6, QCoreApplication.translate("MDCx", u"javdb", None))
        self.comboBox_website_all.setItemText(7, QCoreApplication.translate("MDCx", u"javbus", None))
        self.comboBox_website_all.setItemText(8, QCoreApplication.translate("MDCx", u"jav321", None))
        self.comboBox_website_all.setItemText(9, QCoreApplication.translate("MDCx", u"javlibrary", None))
        self.comboBox_website_all.setItemText(10, QCoreApplication.translate("MDCx", u"dmm", None))
        self.comboBox_website_all.setItemText(11, QCoreApplication.translate("MDCx", u"mgstage", None))
        self.comboBox_website_all.setItemText(12, QCoreApplication.translate("MDCx", u"getchu_dmm", None))
        self.comboBox_website_all.setItemText(13, QCoreApplication.translate("MDCx", u"getchu", None))
        self.comboBox_website_all.setItemText(14, QCoreApplication.translate("MDCx", u"hscangku", None))
        self.comboBox_website_all.setItemText(15, QCoreApplication.translate("MDCx", u"theporndb", None))
        self.comboBox_website_all.setItemText(16, QCoreApplication.translate("MDCx", u"kin8", None))
        self.comboBox_website_all.setItemText(17, QCoreApplication.translate("MDCx", u"xcity", None))
        self.comboBox_website_all.setItemText(18, QCoreApplication.translate("MDCx", u"7mmtv", None))
        self.comboBox_website_all.setItemText(19, QCoreApplication.translate("MDCx", u"mdtv", None))
        self.comboBox_website_all.setItemText(20, QCoreApplication.translate("MDCx", u"madouqu", None))
        self.comboBox_website_all.setItemText(21, QCoreApplication.translate("MDCx", u"cnmdb", None))
        self.comboBox_website_all.setItemText(22, QCoreApplication.translate("MDCx", u"lulubar", None))
        self.comboBox_website_all.setItemText(23, QCoreApplication.translate("MDCx", u"love6", None))
        self.comboBox_website_all.setItemText(24, QCoreApplication.translate("MDCx", u"fc2", None))
        self.comboBox_website_all.setItemText(25, QCoreApplication.translate("MDCx", u"fc2club", None))
        self.comboBox_website_all.setItemText(26, QCoreApplication.translate("MDCx", u"fc2hub", None))
        self.comboBox_website_all.setItemText(27, QCoreApplication.translate("MDCx", u"cableav", None))
        self.comboBox_website_all.setItemText(28, QCoreApplication.translate("MDCx", u"mywife", None))
        self.comboBox_website_all.setItemText(29, QCoreApplication.translate("MDCx", u"giga", None))
        self.comboBox_website_all.setItemText(30, QCoreApplication.translate("MDCx", u"fantastica", None))
        self.comboBox_website_all.setItemText(31, QCoreApplication.translate("MDCx", u"faleno", None))
        self.comboBox_website_all.setItemText(32, QCoreApplication.translate("MDCx", u"dahlia", None))
        self.comboBox_website_all.setItemText(33, QCoreApplication.translate("MDCx", u"prestige", None))
        self.comboBox_website_all.setItemText(34, QCoreApplication.translate("MDCx", u"javday", None))

        self.label_315.setText(QCoreApplication.translate("MDCx", u"\u26a0\ufe0f \u4e0b\u8f7d\u5267\u7167\u3001\u9884\u544a\u7247\uff0c\u8bf7\u9009\u62e9\u300c\u5b57\u6bb5\u4f18\u5148\u300d\u6216\u300c\u6307\u5b9a\u7f51\u7ad9\u300d\uff01\u300c\u901f\u5ea6\u4f18\u5148\u300d\u4fe1\u606f\u4e0d\u5168\uff01", None))
        self.pushButton_scrape_note.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u4e0d\u5230\uff1f\u770b\u8fd9\u91cc\uff01", None))
        self.groupBox_54.setTitle(QCoreApplication.translate("MDCx", u"\u5c01\u9762\u56fe", None))
        self.label_229.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.label_191.setText(QCoreApplication.translate("MDCx", u"\u6392\u9664\u7f51\u7ad9\uff1a", None))
        self.label_204.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u8bbe\u7f6e\uff1a", None))
        self.radioButton_poster_listed.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u5217\u51fa\u7684\u7f51\u7ad9", None))
        self.radioButton_poster_more.setText(QCoreApplication.translate("MDCx", u"\u5c3d\u91cf\u8865\u5168\u5b57\u6bb5", None))
        self.radioButton_poster_none.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u5355\u72ec\u522e\u524a", None))
        self.groupBox_60.setTitle(QCoreApplication.translate("MDCx", u"\u9884\u544a\u7247", None))
        self.label_207.setText(QCoreApplication.translate("MDCx", u"\u6392\u9664\u7f51\u7ad9\uff1a", None))
        self.label_206.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.radioButton_trailer_listed.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u5217\u51fa\u7684\u7f51\u7ad9", None))
        self.radioButton_trailer_more.setText(QCoreApplication.translate("MDCx", u"\u5c3d\u91cf\u8865\u5168\u5b57\u6bb5", None))
        self.radioButton_trailer_none.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u5355\u72ec\u522e\u524a", None))
        self.label_213.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u8bbe\u7f6e\uff1a", None))
        self.groupBox_56.setTitle(QCoreApplication.translate("MDCx", u"\u5267\u7167", None))
        self.label_193.setText(QCoreApplication.translate("MDCx", u"\u6392\u9664\u7f51\u7ad9\uff1a", None))
        self.label_180.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.label_212.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u8bbe\u7f6e\uff1a", None))
        self.radioButton_extrafanart_listed.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u5217\u51fa\u7684\u7f51\u7ad9", None))
        self.radioButton_extrafanart_more.setText(QCoreApplication.translate("MDCx", u"\u5c3d\u91cf\u8865\u5168\u5b57\u6bb5", None))
        self.radioButton_extrafanart_none.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u5355\u72ec\u522e\u524a", None))
        self.groupBox_55.setTitle(QCoreApplication.translate("MDCx", u"\u80cc\u666f\u56fe", None))
        self.label_192.setText(QCoreApplication.translate("MDCx", u"\u6392\u9664\u7f51\u7ad9\uff1a", None))
        self.label_185.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.label_203.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u8bbe\u7f6e\uff1a", None))
        self.radioButton_thumb_listed.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u5217\u51fa\u7684\u7f51\u7ad9", None))
        self.radioButton_thumb_more.setText(QCoreApplication.translate("MDCx", u"\u5c3d\u91cf\u8865\u5168\u5b57\u6bb5", None))
        self.radioButton_thumb_none.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u5355\u72ec\u522e\u524a", None))
        self.groupBox_59.setTitle(QCoreApplication.translate("MDCx", u"\u65f6\u957f", None))
        self.label_196.setText(QCoreApplication.translate("MDCx", u"\u6392\u9664\u7f51\u7ad9\uff1a", None))
        self.label_181.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.radioButton_runtime_listed.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u5217\u51fa\u7684\u7f51\u7ad9", None))
        self.radioButton_runtime_more.setText(QCoreApplication.translate("MDCx", u"\u5c3d\u91cf\u8865\u5168\u5b57\u6bb5", None))
        self.radioButton_runtime_none.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u5355\u72ec\u522e\u524a", None))
        self.label_225.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u8bbe\u7f6e\uff1a", None))
        self.groupBox_58.setTitle(QCoreApplication.translate("MDCx", u"\u53d1\u884c\u65e5\u671f", None))
        self.label_182.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.label_195.setText(QCoreApplication.translate("MDCx", u"\u6392\u9664\u7f51\u7ad9\uff1a", None))
        self.radioButton_release_listed.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u5217\u51fa\u7684\u7f51\u7ad9", None))
        self.radioButton_release_more.setText(QCoreApplication.translate("MDCx", u"\u5c3d\u91cf\u8865\u5168\u5b57\u6bb5", None))
        self.radioButton_release_none.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u5355\u72ec\u522e\u524a", None))
        self.label_224.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u8bbe\u7f6e\uff1a", None))
        self.groupBox_57.setTitle(QCoreApplication.translate("MDCx", u"\u8bc4\u5206", None))
        self.label_194.setText(QCoreApplication.translate("MDCx", u"\u6392\u9664\u7f51\u7ad9\uff1a", None))
        self.label_183.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.radioButton_score_listed.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u5217\u51fa\u7684\u7f51\u7ad9", None))
        self.radioButton_score_more.setText(QCoreApplication.translate("MDCx", u"\u5c3d\u91cf\u8865\u5168\u5b57\u6bb5", None))
        self.radioButton_score_none.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u5355\u72ec\u522e\u524a", None))
        self.label_226.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u8bbe\u7f6e\uff1a", None))
        self.groupBox_50.setTitle(QCoreApplication.translate("MDCx", u"\u5bfc\u6f14", None))
        self.label_227.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.label_228.setText(QCoreApplication.translate("MDCx", u"\u6392\u9664\u7f51\u7ad9\uff1a", None))
        self.radioButton_director_listed.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u5217\u51fa\u7684\u7f51\u7ad9", None))
        self.radioButton_director_more.setText(QCoreApplication.translate("MDCx", u"\u5c3d\u91cf\u8865\u5168\u5b57\u6bb5", None))
        self.radioButton_director_none.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u5355\u72ec\u522e\u524a", None))
        self.label_230.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u8bbe\u7f6e\uff1a", None))
        self.groupBox_63.setTitle(QCoreApplication.translate("MDCx", u"\u60f3\u770b\u4eba\u6570", None))
        self.radioButton_wanted_listed.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u5217\u51fa\u7684\u7f51\u7ad9", None))
        self.radioButton_wanted_none.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u5355\u72ec\u522e\u524a", None))
        self.label_274.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u8bbe\u7f6e\uff1a", None))
        self.label_307.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7f51\u7ad9\uff1a", None))
        self.label_300.setText(QCoreApplication.translate("MDCx", u"\u26a0\ufe0f \u6ce8\u610f\uff01\uff01\uff01\u9009\u62e9\u300c\u5b57\u6bb5\u4f18\u5148\u300d\u65f6\uff0c\u4ee5\u4e0b\u8bbe\u7f6e\u624d\u6709\u6548\uff01\uff01\uff01", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MDCx", u" \u522e\u524a\u7f51\u7ad9 ", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("MDCx", u"\u4e0b\u8f7d", None))
        self.checkBox_download_poster.setText(QCoreApplication.translate("MDCx", u"\u5c01\u9762\u56fe", None))
        self.checkBox_download_thumb.setText(QCoreApplication.translate("MDCx", u"\u7f29\u7565\u56fe", None))
        self.checkBox_download_fanart.setText(QCoreApplication.translate("MDCx", u"\u80cc\u666f\u56fe", None))
        self.checkBox_download_extrafanart.setText(QCoreApplication.translate("MDCx", u"\u5267\u7167", None))
        self.checkBox_download_trailer.setText(QCoreApplication.translate("MDCx", u"\u9884\u544a\u7247", None))
        self.checkBox_download_nfo.setText(QCoreApplication.translate("MDCx", u"nfo", None))
        self.checkBox_ignore_pic_fail.setText(QCoreApplication.translate("MDCx", u"\u56fe\u7247\u4e0b\u8f7d\u5931\u8d25\u65f6\uff0c\u4e0d\u89c6\u4e3a\u522e\u524a\u5931\u8d25", None))
        self.label_275.setText(QCoreApplication.translate("MDCx", u" \u6709\u65f6\u56fe\u7247\u5df2\u88ab\u6e90\u7f51\u7ad9\u5220\u9664\uff0c\u6b64\u65f6\u4f1a\u4e0b\u8f7d\u5931\u8d25", None))
        self.checkBox_ignore_youma.setText(QCoreApplication.translate("MDCx", u"\u6709\u7801\u5c01\u9762\u4e0d\u88c1\u526a\uff0c\u76f4\u63a5\u590d\u5236\u7f29\u7565\u56fe", None))
        self.label_326.setText(QCoreApplication.translate("MDCx", u" \u6709\u7801\u5c01\u9762\u53ef\u4ee5\u88c1\u526a\uff0c\u5982\u4e0d\u60f3\u88c1\u526a\u53ef\u4ee5\u52fe\u9009", None))
        self.checkBox_ignore_wuma.setText(QCoreApplication.translate("MDCx", u"\u65e0\u7801\uff08\u542b\u6b27\u7f8e\uff09\u5c01\u9762\u4e0d\u88c1\u526a\uff0c\u76f4\u63a5\u590d\u5236\u7f29\u7565\u56fe", None))
        self.label_273.setText(QCoreApplication.translate("MDCx", u" \u65e0\u7801\u5c01\u9762\u4eba\u8138\u4f4d\u7f6e\u4e0d\u56fa\u5b9a\uff0c\u5efa\u8bae\u624b\u52a8\u88c1\u526a\u6216\u76f4\u63a5\u590d\u5236", None))
        self.checkBox_ignore_fc2.setText(QCoreApplication.translate("MDCx", u"FC2 \u5c01\u9762\u4e0d\u88c1\u526a\uff0c\u76f4\u63a5\u590d\u5236\u7f29\u7565\u56fe", None))
        self.label_292.setText(QCoreApplication.translate("MDCx", u" FC2 \u5c01\u9762\u4eba\u8138\u4f4d\u7f6e\u4e0d\u56fa\u5b9a\uff0c\u5efa\u8bae\u624b\u52a8\u88c1\u526a\u6216\u76f4\u63a5\u590d\u5236", None))
        self.checkBox_ignore_guochan.setText(QCoreApplication.translate("MDCx", u"\u56fd\u4ea7\u5c01\u9762\u4e0d\u88c1\u526a\uff0c\u76f4\u63a5\u590d\u5236\u7f29\u7565\u56fe", None))
        self.label_305.setText(QCoreApplication.translate("MDCx", u" \u56fd\u4ea7\u5c01\u9762\u4eba\u8138\u4f4d\u7f6e\u4e0d\u56fa\u5b9a\uff0c\u5efa\u8bae\u624b\u52a8\u88c1\u526a\u6216\u76f4\u63a5\u590d\u5236", None))
        self.checkBox_ignore_size.setText(QCoreApplication.translate("MDCx", u"\u9884\u544a\u7247\u4e0b\u8f7d\u65f6\uff0c\u4e0d\u6821\u9a8c\u6587\u4ef6\u5927\u5c0f", None))
        self.label_272.setText(QCoreApplication.translate("MDCx", u" \u6709\u65f6\u7f51\u7edc\u8fd4\u56de\u503c\u4e0d\u5bf9\uff0c\u6821\u9a8c\u4f1a\u5bfc\u81f4\u9884\u544a\u7247\u4e0b\u8f7d\u5931\u8d25", None))
        self.label_85.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>\u5c01\u9762\u56fe\uff1aposter\uff0c\u5f53 Emby \u89c6\u56fe\u9009\u62e9\u5c01\u9762\u56fe\u65f6\uff0c\u5217\u8868\u9875\u4f1a\u4f7f\u7528 poster\uff08\u7ad6\u56fe\uff09\u663e\u793a\uff1b<br>\n"
"\u7f29\u7565\u56fe\uff1athumb\uff0c\u5f53 Emby \u89c6\u56fe\u9009\u62e9\u7f29\u7565\u56fe\u65f6\uff0c\u5217\u8868\u9875\u4f1a\u4f7f\u7528 Thumb\uff08\u6a2a\u56fe\uff09\u663e\u793a\uff1b<br>\n"
"\u80cc\u666f\u56fe\uff1afanart\uff0c\u5728 Emby \u8be6\u60c5\u9875\u4f5c\u4e3a\u80cc\u666f\u56fe\u663e\u793a\uff08\u590d\u5236\u7f29\u7565\u56fe\u5f97\u5230\u80cc\u666f\u56fe\uff09\uff1b<br>\n"
"\u5267\u7167\uff1aextrafanart\uff0c\u5728 Emby \u8be6\u60c5\u9875\u4f5c\u4e3a\u80cc\u666f\u8f6e\u64ad\u663e\u793a\uff08\u505c\u7559\u7ea6 50s \u540e\u8fdb\u5165\u8f6e\u64ad\u72b6\u6001\uff09\uff1b<br>\n"
"\u9884\u544a\u7247\uff1atrailer\uff0c\u5728 Emby \u8be6\u60c5\u9875\u53ef\u4ee5\u64ad\u653e\u9884\u544a\u7247\uff1b<br>\n"
"nfo\uff1a\u5305\u542b\u6807\u9898\u3001\u7b80\u4ecb\u3001\u6807\u7b7e\u7b49\u4fe1\u606f"
                        "\uff0c\u5728 Emby \u8be6\u60c5\u9875\u5c55\u793a\u3002</p>", None))
        self.label_310.setText(QCoreApplication.translate("MDCx", u"\u26a0\ufe0f \u4e0b\u8f7d\u5267\u7167\u3001\u9884\u544a\u7247\uff0c\u8bf7\u9009\u62e9\u300c\u5b57\u6bb5\u4f18\u5148\u300d\u6216\u300c\u6307\u5b9a\u7f51\u7ad9\u300d\uff01\u300c\u901f\u5ea6\u4f18\u5148\u300d\u4fe1\u606f\u4e0d\u5168\uff01", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("MDCx", u"\u4fdd\u7559\u65e7\u6587\u4ef6", None))
        self.checkBox_old_poster.setText(QCoreApplication.translate("MDCx", u"\u5c01\u9762\u56fe", None))
        self.checkBox_old_thumb.setText(QCoreApplication.translate("MDCx", u"\u7f29\u7565\u56fe", None))
        self.checkBox_old_fanart.setText(QCoreApplication.translate("MDCx", u"\u80cc\u666f\u56fe", None))
        self.checkBox_old_extrafanart.setText(QCoreApplication.translate("MDCx", u"\u5267\u7167", None))
        self.checkBox_old_trailer.setText(QCoreApplication.translate("MDCx", u"\u9884\u544a\u7247", None))
        self.checkBox_old_nfo.setText(QCoreApplication.translate("MDCx", u"nfo", None))
        self.checkBox_old_extrafanart_copy.setText(QCoreApplication.translate("MDCx", u"\u5267\u7167\u526f\u672c", None))
        self.checkBox_old_theme_videos.setText(QCoreApplication.translate("MDCx", u"\u4e3b\u9898\u89c6\u9891", None))
        self.label_79.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>\u52fe\u9009\u65f6\uff0c\u5c06\u4f7f\u7528\u672c\u5730\u6587\u4ef6\uff08\u5982\u6709\uff09\uff0c\u4e0d\u518d\u91cd\u65b0\u4e0b\u8f7d\u3002<br>\n"
"\u26a0\ufe0f \u6ce8\u610f\uff1a\u4e0d\u52fe\u9009\u65f6\uff0c\u672c\u5730\u65e7\u6587\u4ef6\u5c06\u88ab\u5220\u9664\uff01\u5e76\u6839\u636e\u4e0a\u65b9\u8bbe\u7f6e\u7684\u4e0b\u8f7d\u9879\u91cd\u65b0\u4e0b\u8f7d\uff01</p>", None))
        self.groupBox_51.setTitle(QCoreApplication.translate("MDCx", u"\u521b\u5efa\u4e3b\u9898\u89c6\u9891", None))
        self.label_87.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>\u590d\u5236\u9884\u544a\u7247\u5230\u89c6\u9891\u4e0b\u7684 backdrops \u76ee\u5f55\uff0c\u5f53\u5728 Emby \u6d4f\u89c8\u8be5\u756a\u53f7\u65f6\uff0c\u9884\u544a\u7247\u4f1a\u4f5c\u4e3a\u80cc\u666f\u89c6\u9891\u64ad\u653e\u3002<br>\n"
"\u5f00\u542f\u4e3b\u9898\u89c6\u9891\uff1aEmby \u8bbe\u7f6e-\u663e\u793a-\u4e3b\u9898\u89c6\u9891-\u5f00\uff08PC \u7aef\u53ef\u4ee5\u6253\u5f00\uff0c\u624b\u673a\u7aef\u4e0d\u5efa\u8bae\u6253\u5f00\uff0c\u4f1a\u53d8\u6210\u5168\u5c4f\u64ad\u653e...\uff09</p>", None))
        self.checkBox_theme_videos.setText(QCoreApplication.translate("MDCx", u"\u4f7f\u7528\u9884\u544a\u7247\u4f5c\u4e3a\u4e3b\u9898\u89c6\u9891", None))
        self.pushButton_add_all_theme_videos.setText(QCoreApplication.translate("MDCx", u"\u6dfb\u52a0\u6240\u6709\u4e3b\u9898\u89c6\u9891", None))
        self.pushButton_del_all_theme_videos.setText(QCoreApplication.translate("MDCx", u"\u5220\u9664\u6240\u6709\u4e3b\u9898\u89c6\u9891", None))
        self.groupBox_34.setTitle(QCoreApplication.translate("MDCx", u"\u521b\u5efa\u5267\u7167\u526f\u672c", None))
        self.checkBox_download_extrafanart_copy.setText(QCoreApplication.translate("MDCx", u"\u989d\u5916\u590d\u5236\u4e00\u4efd\u5267\u7167\u56fe\u5230\u6587\u4ef6\u5939", None))
        self.label_59.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>\u5728 Emby \u4e2d\uff0c\u5267\u7167\u56fe\u7247\u4f5c\u4e3a\u80cc\u666f\u663e\u793a\uff0c\u65e0\u6cd5\u624b\u52a8\u6d4f\u89c8\u3002<br>\n"
"\u5982\u9700\u5728 Emby \u4e2d\u624b\u52a8\u67e5\u770b\u5267\u7167\uff0c\u53ef\u590d\u5236\u5267\u7167\u56fe\u7247\u5230\u5355\u72ec\u76ee\u5f55\uff0c\u5e76\u4e14\u5a92\u4f53\u5e93\u7c7b\u578b\u9009\u62e9\u300c\u5bb6\u5ead\u89c6\u9891\u4e0e\u7167\u7247\u300d<br>\n"
"\u8bf7\u4f7f\u7528\u300cextrafanart\u300d\u4ee5\u5916\u7684\u5176\u4ed6\u540d\u5b57\u3002\u76ee\u5f55\u540d\u5b57\u4e3a\u7a7a\u6216\u300cextrafanart\u300d\u65f6\uff0c\u5c06\u4e0d\u4f1a\u521b\u5efa\u526f\u672c\u76ee\u5f55\u3002<br>\n"
"\u6ce8\u610f\uff1a\u6b64\u5904\u53ea\u9700\u586b\u5199\u76ee\u5f55\u540d\u5b57\uff0c\u8bf7\u4e0d\u8981\u586b\u5199\u5b8c\u6574\u8def\u5f84\uff01</p>", None))
        self.pushButton_add_all_extrafanart_copy.setText(QCoreApplication.translate("MDCx", u"\u6dfb\u52a0\u6240\u6709\u5267\u7167\u526f\u672c", None))
        self.pushButton_del_all_extrafanart_copy.setText(QCoreApplication.translate("MDCx", u"\u5220\u9664\u6240\u6709\u5267\u7167\u526f\u672c", None))
        self.groupBox_52.setTitle(QCoreApplication.translate("MDCx", u"\u4e0b\u8f7d\u9ad8\u6e05\u56fe", None))
        self.checkBox_hd_poster.setText(QCoreApplication.translate("MDCx", u"\u5c01\u9762\u56fe", None))
        self.checkBox_hd_thumb.setText(QCoreApplication.translate("MDCx", u"\u7f29\u7565\u56fe / \u80cc\u666f\u56fe", None))
        self.label_92.setText(QCoreApplication.translate("MDCx", u"\u5c06\u4ece\u7247\u5546\u5b98\u7f51\u548c\u5176\u4ed6\u4e00\u4e9b\u7f51\u7ad9\u67e5\u627e\u9ad8\u6e05\u56fe\uff0c\u5f53\u6709\u9ad8\u6e05\u56fe\u7247\u65f6\uff0c\u4e0b\u8f7d\u9ad8\u6e05\u56fe\u7247", None))
        self.checkBox_google_big_pic.setText(QCoreApplication.translate("MDCx", u"\u542f\u7528 Google \u4ee5\u56fe\u641c\u56fe\u67e5\u627e\u9ad8\u6e05\u56fe", None))
        self.label_399.setText(QCoreApplication.translate("MDCx", u"\u5c06\u4f7f\u7528\u56fe\u7247\u8bf7\u6c42 Google \u4ee5\u56fe\u641c\u56fe", None))
        self.label_311.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u4e0b\u8f7d\u7f51\u5740\u5305\u542b\u4ee5\u4e0b\u5173\u952e\u8bcd\u7684\u56fe\u7247", None))
        self.label_343.setText(QCoreApplication.translate("MDCx", u"\u591a\u4e2a\u4ee5\u9017\u53f7\u9694\u5f00\uff0c\u4f18\u5148\u7ea7\u6309\u7167\u987a\u5e8f\u4ece\u524d\u5f80\u540e", None))
        self.radioButton_google_first.setText(QCoreApplication.translate("MDCx", u"\u4f18\u5148\u4e0b\u8f7d\u7f51\u5740\u5305\u542b\u4ee5\u4e0b\u5173\u952e\u8bcd\u7684\u56fe\u7247", None))
        self.radioButton_google_only.setText(QCoreApplication.translate("MDCx", u"\u53ea\u4e0b\u8f7d\u7f51\u5740\u5305\u542b\u4ee5\u4e0b\u5173\u952e\u8bcd\u7684\u56fe\u7247", None))
        self.checkBox_amazon_big_pic.setText(QCoreApplication.translate("MDCx", u"\u542f\u7528 Amazon \u67e5\u627e\u9ad8\u6e05\u5c01\u9762\u56fe", None))
        self.label_397.setText(QCoreApplication.translate("MDCx", u"\u5c06\u4ece\u65e5\u4e9a\u5b98\u7f51\u641c\u7d22\u9ad8\u6e05\u56fe\uff0c\u5f53\u627e\u5230\u65f6\u76f4\u63a5\u4f7f\u7528\u65e5\u4e9a\u7ed3\u679c", None))
        self.checkBox_official_big_pic.setText(QCoreApplication.translate("MDCx", u"\u542f\u7528\u7247\u5546\u5b98\u7f51\u67e5\u627e\u9ad8\u6e05\u56fe", None))
        self.label_398.setText(QCoreApplication.translate("MDCx", u"\u5c06\u4ece\u7247\u5546\u5b98\u7f51\u641c\u7d22\u9ad8\u6e05\u56fe\uff0c\u5f53\u56fe\u7247\u4e0d\u9ad8\u6e05\u65f6\u4f1a\u7ee7\u7eed\u4f7f\u7528 Google \u641c\u56fe", None))
        self.groupBox_66.setTitle(QCoreApplication.translate("MDCx", u"\u663e\u793a\u5267\u7167", None))
        self.label_333.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>\u590d\u5236\u5267\u7167\u5230\u89c6\u9891\u4e0b\u7684 behind the scenes \u76ee\u5f55\uff0cEmby \u6d4f\u89c8\u65f6\uff0c\u5267\u7167\u4f1a\u4f5c\u4e3a\u9644\u52a0\u5185\u5bb9\u5728\u8be6\u60c5\u9875\u4e0b\u65b9\u663e\u793a\u3002<br></p>", None))
        self.checkBox_extras.setText(QCoreApplication.translate("MDCx", u"\u5267\u7167\u4f5c\u4e3a\u9644\u52a0\u5185\u5bb9\u663e\u793a", None))
        self.pushButton_add_all_extras.setText(QCoreApplication.translate("MDCx", u"\u4e3a\u6240\u6709\u89c6\u9891\u590d\u5236\u5267\u7167", None))
        self.pushButton_del_all_extras.setText(QCoreApplication.translate("MDCx", u"\u5220\u9664\u6240\u6709\u590d\u5236\u7684\u5267\u7167", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MDCx", u" \u4e0b\u8f7d ", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MDCx", u"\u89c6\u9891\u547d\u540d\u89c4\u5219", None))
        self.label_66.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>\u5f53\u522e\u524a\u6210\u529f\u65f6\uff0c\u5c06\u4e3a\u8be5\u89c6\u9891\u521b\u5efa\u4e00\u4e2a\u89c6\u9891\u76ee\u5f55\uff0c\u5e76\u79fb\u52a8\u8be5\u89c6\u9891\u76ee\u5f55\u5230\u6210\u529f\u8f93\u51fa\u76ee\u5f55\u3002<br>\n"
"\u76ee\u5f55\u540d\u5b57\u652f\u6301\u81ea\u5b9a\u4e49\u3002\u547d\u540d\u5b57\u6bb5\u6709\uff1a<br>\n"
"title \uff08\u6807\u9898\uff09, originaltitle \uff08\u539f\u6807\u9898\uff09, actor \uff08\u5973\u6f14\u5458\uff09, all_actor \uff08\u7537\u5973\u6f14\u5458\uff09,first_actor \uff08\u9996\u4f4d\u6f14\u5458\uff09,  number \uff08\u756a\u53f7\uff09, letters \uff08\u756a\u53f7\u524d\u7f00\uff09,  first_letter \uff08\u756a\u53f7\u9996\u5b57\u7b26\uff09, outline \uff08\u5267\u60c5\u7b80\u4ecb\uff09, director \uff08\u5bfc\u6f14\uff09, series \uff08\u7cfb\u5217\uff09,  studio \uff08\u7247\u5546\uff09, publisher \uff08\u53d1\u884c\u5546\uff09, release \uff08\u53d1\u884c\u65e5\u671f\uff09, year \uff08\u5e74\u4ee3\uff09,  runtime \uff08\u65f6\u957f\uff09, mosaic \uff08"
                        "\u6709\u7801/\u65e0\u7801\uff09, definition \uff08720P/1080P/4K\uff09, cnword \uff08\u81ea\u5b9a\u4e49\u7684\u5b57\u5e55\u6807\u8bc6\uff09, moword \uff08\u81ea\u5b9a\u4e49\u7684\u65e0\u7801\u6807\u8bc6\uff09, filename \uff08\u539f\u6587\u4ef6\u540d\uff09, wanted \uff08\u60f3\u770b\u4eba\u6570\uff09, score \uff08\u8bc4\u5206\uff09, 4K \uff084K\uff09<br>\n"
"\u6ce8\u610f\uff1a<br>\n"
"1\uff0c\u53ef\u4ee5\u6dfb\u52a0\u547d\u540d\u5b57\u6bb5\u4ee5\u5916\u7684\u5b57\u7b26\uff0c\u547d\u540d\u65f6\u4f1a\u539f\u6837\u4fdd\u7559\uff1b<br>\n"
"2\uff0c\u5f53\u7559\u7a7a\u65f6\uff0c\u8868\u793a\u4e0d\u521b\u5efa\u89c6\u9891\u76ee\u5f55\uff1b<br>\n"
"3\uff0c\u5f53\u52fe\u9009\u300c\u6210\u529f\u540e\u4e0d\u79fb\u52a8\u6587\u4ef6\u300d\u65f6\uff0c\u5c06\u4e0d\u4f1a\u521b\u5efa\u89c6\u9891\u76ee\u5f55</p>", None))
        self.label_63.setText(QCoreApplication.translate("MDCx", u"\u89c6\u9891\u6587\u4ef6\u540d\uff1a", None))
#if QT_CONFIG(accessibility)
        self.lineEdit_dir_name.setAccessibleDescription(QCoreApplication.translate("MDCx", u"\u6d4b\u8bd5", None))
#endif // QT_CONFIG(accessibility)
        self.label_43.setText(QCoreApplication.translate("MDCx", u"\u89c6\u9891\u76ee\u5f55\u540d\uff1a", None))
        self.label_240.setText(QCoreApplication.translate("MDCx", u"\u9632\u5c4f\u853d\u5b57\u7b26\uff1a", None))
        self.label_68.setText(QCoreApplication.translate("MDCx", u"\u6307\u5728 nfo \u6587\u4ef6\u4e2d\u7684\u6807\u9898\u683c\u5f0f\uff0c\u5728 Emby \u4e2d\u4f5c\u4e3a\u89c6\u9891\u6807\u9898\u663e\u793a\uff0c\u547d\u540d\u5b57\u6bb5\u540c\u4e0a", None))
        self.label_67.setText(QCoreApplication.translate("MDCx", u"Emby\u89c6\u9891\u6807\u9898\uff1a", None))
        self.label_61.setText(QCoreApplication.translate("MDCx", u"\u6307\u672c\u5730\u89c6\u9891\u6587\u4ef6\u7684\u6587\u4ef6\u540d\u683c\u5f0f\uff0c\u547d\u540d\u5b57\u6bb5\u540c\u4e0a", None))
        self.label_239.setText(QCoreApplication.translate("MDCx", u"\u89c6\u9891\u6587\u4ef6\u547d\u540d\u65f6\uff0c\u53ef\u63d2\u5165\u9632\u5c4f\u853d\u5b57\u7b26\u5230\u6587\u4ef6\u540d\u7684\u6bcf\u4e2a\u5b57\u7b26\u4e4b\u95f4", None))
        self.label_147.setText("")
        self.groupBox_38.setTitle(QCoreApplication.translate("MDCx", u"\u5206\u96c6\u547d\u540d\u89c4\u5219", None))
        self.label_98.setText(QCoreApplication.translate("MDCx", u"\u5927\u5199\uff0c-CD1\u3001-CD2", None))
        self.radioButton_cd_part_lower.setText(QCoreApplication.translate("MDCx", u"-cd1", None))
        self.label_97.setText(QCoreApplication.translate("MDCx", u"\u5c0f\u5199\uff0c-cd1\uff0c-cd2", None))
        self.radioButton_cd_part_upper.setText(QCoreApplication.translate("MDCx", u"-CD1", None))
        self.radioButton_cd_part_digital.setText(QCoreApplication.translate("MDCx", u"-1", None))
        self.label_349.setText(QCoreApplication.translate("MDCx", u"\u6570\u5b57\uff0c-1\u3001-2", None))
        self.label_99.setText(QCoreApplication.translate("MDCx", u"\u9ed8\u8ba4\u8bc6\u522b\u5206\u96c6\uff1a-CD1\uff5c-PART1\uff5c-HD1\uff5c-1.mp4 \uff08\u6587\u4ef6\u540d\u542b\u6709\u8fd9\u4e9b\u5b57\u7b26\u65f6\u5c06\u8bc6\u522b\u5176\u4e2d\u7684\u5206\u96c6\u4fe1\u606f\uff09", None))
        self.checkBox_cd_part_a.setText(QCoreApplication.translate("MDCx", u"-A.mp4\uff5c.A.mp4\uff5c12A.mp4 (\u5b57\u6bcd\u7ed3\u5c3e\u7684\u5206\u96c6\uff0c\u4e0d\u542b\u5b57\u6bcdC)", None))
        self.label_350.setText(QCoreApplication.translate("MDCx", u"\u5141\u8bb8\u8bc6\u522b\u5206\u96c6\uff1a", None))
        self.checkBox_cd_part_01.setText(QCoreApplication.translate("MDCx", u"-01.mp4(\u4e24\u4f4d\u6570\u5b57\u7ed3\u5c3e\u7684\u5206\u96c6)", None))
        self.checkBox_cd_part_1_xxx.setText(QCoreApplication.translate("MDCx", u"-1 abc.mp4 (\u6570\u5b57\u4e0d\u5728\u7ed3\u5c3e\u7684\u5206\u96c6)", None))
        self.label_408.setText(QCoreApplication.translate("MDCx", u"\u5141\u8bb8\u8bc6\u522b\u7684\u5206\u9694\u7b26\uff1a", None))
        self.checkBox_cd_part_space.setText(QCoreApplication.translate("MDCx", u"  \u7a7a\u683c", None))
        self.checkBox_cd_part_underline.setText(QCoreApplication.translate("MDCx", u"_ \u4e0b\u5212\u7ebf", None))
        self.checkBox_cd_part_point.setText(QCoreApplication.translate("MDCx", u". \u5c0f\u6570\u70b9", None))
        self.label_409.setText(QCoreApplication.translate("MDCx", u"\u9ed8\u8ba4\u8bc6\u522b\u7684\u5206\u96c6\u5206\u9694\u7b26\uff1a- \u77ed\u6a2a\u7ebf", None))
        self.checkBox_cd_part_c.setText(QCoreApplication.translate("MDCx", u"-C.mp4\uff5c.C.mp4\uff5c12C.mp4 (\u5b57\u6bcdC\u7ed3\u5c3e\u7684\u5206\u96c6\uff0c\u8bc6\u522b\u4e3aCD3)", None))
        self.label_430.setText(QCoreApplication.translate("MDCx", u"\u52fe\u9009\u540e\uff0c-C\u3001.C\u5c06\u8bc6\u522b\u4e3aCD3\uff0c\u4e0d\u518d\u8bc6\u522b\u4e3a\u5b57\u5e55", None))
        self.groupBox_77.setTitle(QCoreApplication.translate("MDCx", u"\u957f\u5ea6\u547d\u540d\u89c4\u5219", None))
        self.label_171.setText(QCoreApplication.translate("MDCx", u"\u76ee\u5f55\u540d\u6700\u5927\u957f\u5ea6\uff1a", None))
        self.label_167.setText(QCoreApplication.translate("MDCx", u"\u6f14\u5458\u540d\u6700\u5927\u6570\u91cf\uff1a", None))
        self.label_169.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>\u6307\u76ee\u5f55\u540d\u6700\u957f\u5b57\u7b26\u6570\uff08\u5efa\u8bae\u4e0d\u8981\u8d85\u8fc7 100\uff0c\u592a\u957f\u65f6 Windows \u53ef\u80fd\u62a5\u9519\uff09<br>\n"
"\u5f53\u8d85\u8fc7\u6700\u5927\u957f\u5ea6\u65f6\uff0c\u5c06\u901a\u8fc7\u622a\u77ed\u6807\u9898\u5b57\u6bb5\u5185\u5bb9\u6765\u7f29\u77ed\u957f\u5ea6</p>", None))
        self.label_170.setText(QCoreApplication.translate("MDCx", u"\u6587\u4ef6\u540d\u6700\u5927\u957f\u5ea6\uff1a", None))
        self.label_172.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>\u6307\u6587\u4ef6\u540d\u6700\u957f\u5b57\u7b26\u6570\uff08\u5efa\u8bae\u4e0d\u8981\u8d85\u8fc7 100\uff0c\u592a\u957f\u65f6 Windows \u53ef\u80fd\u62a5\u9519\uff09<br>\n"
"\u5f53\u8d85\u8fc7\u6700\u5927\u957f\u5ea6\u65f6\uff0c\u5c06\u901a\u8fc7\u622a\u77ed\u6807\u9898\u5b57\u6bb5\u5185\u5bb9\u6765\u7f29\u77ed\u957f\u5ea6</p>", None))
        self.label_168.setText(QCoreApplication.translate("MDCx", u"\u6307\u6709\u591a\u4f4d\u6f14\u5458\u65f6\uff0c\u547d\u540d\u65f6\u6700\u591a\u663e\u793a\u7684\u6f14\u5458\u6570\u91cf\u3002\u8d85\u51fa\u7684\u6f14\u5458\u5c06\u7528\u4ee5\u4e0b\u5b57\u7b26\u66ff\u4ee3\uff1a", None))
#if QT_CONFIG(accessibility)
        self.lineEdit_folder_name_max.setAccessibleDescription(QCoreApplication.translate("MDCx", u"\u6d4b\u8bd5", None))
#endif // QT_CONFIG(accessibility)
        self.label_288.setText("")
        self.label_287.setText("")
        self.label_289.setText("")
        self.label_290.setText("")
        self.groupBox_46.setTitle(QCoreApplication.translate("MDCx", u"\u9a6c\u8d5b\u514b\u547d\u540d\u89c4\u5219", None))
        self.label_285.setText("")
        self.label_281.setText("")
        self.label_189.setText(QCoreApplication.translate("MDCx", u"\u65e0\u7801\uff1a", None))
        self.label_117.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>\u6307\u65e0\u7801\u6d41\u51fa\u7248\u672c\uff0c\u5f53\u89c6\u9891\u6587\u4ef6\u8def\u5f84\u4e2d\u542b\u6709\u300c\u6d41\u51fa\u300d\u3001\u300cLEAKED\u300d\u5b57\u6837\u65f6\uff0c\u8be5\u6587\u4ef6\u8bc6\u522b\u4e3a\u65e0\u7801\u6d41\u51fa\u7248\u672c\u3002\u5728\u91cd\u547d\u540d\u6587\u4ef6\u540d\u53ca\u76ee\u5f55\u540d\u65f6\uff0c\u5728\u756a\u53f7\u540e\u663e\u793a\u8be5\u5b57\u7b26\u8868\u793a\u4e3a\u65e0\u7801\u6d41\u51fa\u7248\u672c</p>", None))
        self.label_282.setText("")
        self.label_175.setText(QCoreApplication.translate("MDCx", u"\u65e0\u7801\u6d41\u51fa\uff1a", None))
        self.label_284.setText("")
        self.label_190.setText(QCoreApplication.translate("MDCx", u"\u6709\u7801\uff1a", None))
        self.label_137.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>\u6307\u65e0\u7801\u7248\u672c\uff0c\u5f53\u89c6\u9891\u6587\u4ef6\u8def\u5f84\u4e2d\u542b\u6709\u300c\u65e0\u7801\u300d\u3001\u300c\u7121\u78bc\u300d\u3001\u300c\u7121\u4fee\u6b63\u300d\u3001\u300cuncensored\u300d\u5b57\u6837\u65f6\uff0c\u8be5\u6587\u4ef6\u8bc6\u522b\u4e3a\u65e0\u7801\u7248\u672c\u3002<br>\u5728\u91cd\u547d\u540d\u6587\u4ef6\u540d\u53ca\u76ee\u5f55\u540d\u65f6\uff0c\u5728\u756a\u53f7\u540e\u663e\u793a\u8be5\u5b57\u7b26\u8868\u793a\u4e3a\u65e0\u7801\u7248\u672c</p>", None))
        self.label_116.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>\u6307\u9a6c\u8d5b\u514b\u6709\u635f\u53bb\u9664\u7248\u672c\uff0c\u5f53\u89c6\u9891\u6587\u4ef6\u8def\u5f84\u4e2d\u542b\u6709\u300c-uncensored.\u300d\u3001\u300c\u7834\u89e3\u300d\u3001\u300c\u514b\u7834\u300d\u3001\u300cUMR.\u300d\u7b49\u5b57\u6837\u65f6\uff0c\u8be5\u6587\u4ef6\u8bc6\u522b\u4e3a\u65e0\u7801\u7834\u89e3\u7248\u672c\u3002<br>\n"
"\u5728\u91cd\u547d\u540d\u6587\u4ef6\u540d\u53ca\u76ee\u5f55\u540d\u65f6\uff0c\u5728\u756a\u53f7\u540e\u663e\u793a\u8be5\u5b57\u7b26\u8868\u793a\u4e3a\u65e0\u7801\u7834\u89e3\u7248\u672c</p>", None))
        self.label_283.setText("")
        self.label_174.setText(QCoreApplication.translate("MDCx", u"\u65e0\u7801\u7834\u89e3\uff1a", None))
        self.label_145.setText(QCoreApplication.translate("MDCx", u"\u6307\u6709\u7801\u7248\u672c\uff0c\u5f53\u89c6\u9891\u6587\u4ef6\u8def\u5f84\u4e2d\u542b\u6709\u300c\u6709\u7801\u300d\u3001\u300c\u6709\u78bc\u300d\u5b57\u6837\u65f6\uff0c\u8be5\u6587\u4ef6\u8bc6\u522b\u4e3a\n"
"\u6709\u7801\u7248\u672c\uff0c\u91cd\u547d\u540d\u6587\u4ef6\u540d\u53ca\u76ee\u5f55\u540d\u65f6\uff0c\u5728\u756a\u53f7\u540e\u663e\u793a\u8be5\u5b57\u7b26\u8868\u793a\u4e3a\u6709\u7801\u7248\u672c", None))
        self.label_235.setText(QCoreApplication.translate("MDCx", u"\u6307\u547d\u540d\u65f6\u5728\u756a\u53f7\u540e\u6dfb\u52a0\u7248\u672c\u547d\u540d\u5b57\u7b26\u3002\u4f60\u4e5f\u53ef\u4ee5\u4f7f\u7528 moword \u5b57\u6bb5\u6765\u8c03\u6574\u6dfb\u52a0\u4f4d\u7f6e", None))
        self.label_234.setText(QCoreApplication.translate("MDCx", u"\u6dfb\u52a0\u9a6c\u8d5b\u514b\u547d\u540d\u5b57\u7b26\uff1a", None))
        self.label_286.setText("")
        self.checkBox_foldername_mosaic.setText(QCoreApplication.translate("MDCx", u"\u89c6\u9891\u76ee\u5f55\u540d", None))
        self.checkBox_filename_mosaic.setText(QCoreApplication.translate("MDCx", u"\u89c6\u9891\u6587\u4ef6\u540d", None))
        self.groupBox_37.setTitle(QCoreApplication.translate("MDCx", u"\u56fe\u7247\u547d\u540d\u89c4\u5219", None))
        self.radioButton_pic_with_filename.setText(QCoreApplication.translate("MDCx", u"\u89c6\u9891\u6587\u4ef6\u540d-poster.jpg ", None))
        self.radioButton_pic_no_filename.setText(QCoreApplication.translate("MDCx", u"poster.jpg", None))
        self.label_95.setText(QCoreApplication.translate("MDCx", u"\u89c6\u9891\u6587\u4ef6\u540d-thumb.jpg\uff0c\u89c6\u9891\u6587\u4ef6\u540d-fanart.jpg", None))
        self.label_96.setText(QCoreApplication.translate("MDCx", u"thumb.jpg\uff0cfanart.jpg", None))
        self.groupBox_62.setTitle(QCoreApplication.translate("MDCx", u"\u9884\u544a\u7247\u547d\u540d\u89c4\u5219", None))
        self.radioButton_trailer_with_filename.setText(QCoreApplication.translate("MDCx", u"\u89c6\u9891\u6587\u4ef6\u540d-trailer.mp4 ", None))
        self.radioButton_trailer_no_filename.setText(QCoreApplication.translate("MDCx", u"trailer.mp4", None))
        self.label_115.setText(QCoreApplication.translate("MDCx", u"\u6bcf\u4e2a\u89c6\u9891\u521b\u5efa\u4e00\u4e2a\u300c\u89c6\u9891\u540d-trailer.mp4\u300d\uff0c\u591a\u5206\u96c6\u65f6\u4f1a\u521b\u5efa\u591a\u4e2a", None))
        self.label_122.setText(QCoreApplication.translate("MDCx", u"\u5728\u89c6\u9891\u76ee\u5f55\u521b\u5efa\u300ctrailers\u300d\u6587\u4ef6\u5939\uff0c\u591a\u5206\u96c6\u5171\u7528\u4e00\u4e2a\u300ctrailer.mp4\u300d", None))
        self.groupBox_40.setTitle(QCoreApplication.translate("MDCx", u"\u5b57\u6bb5\u547d\u540d\u89c4\u5219", None))
        self.label_407.setText(QCoreApplication.translate("MDCx", u"\u6f14\u5458\uff1a", None))
        self.label_146.setText(QCoreApplication.translate("MDCx", u"\u6bd4\u5982mosaic(\u9a6c\u8d5b\u514b),cnword(\u5b57\u5e55)\u5c06\u663e\u793a\u4e3a: \u756a\u53f7-\u6d41\u51fa-C", None))
        self.checkBox_number_del_num.setText(QCoreApplication.translate("MDCx", u"\u53bb\u9664\u7d20\u4eba\u756a\u53f7\u524d\u7f00\u6570\u5b57\uff08\u6bd4\u5982\uff1a259LUXU-1488 \u5c06\u4fee\u6539\u4e3a LUXU-1488\uff0c\u5efa\u8bae\u4fdd\u7559\uff09", None))
        self.checkBox_actor_del_char.setText(QCoreApplication.translate("MDCx", u"\u53bb\u9664\u6f14\u5458\u540d\u62ec\u53f7\u4e2d\u7684\u540d\u5b57\uff08\u6bd4\u5982\uff1aRio\uff08\u67da\u6728\u30c6\u30a3\u30ca\uff09\u5c06\u4fee\u6539\u4e3a Rio\uff09", None))
        self.label_319.setText(QCoreApplication.translate("MDCx", u"\u7d20\u4eba\u756a\u53f7\uff1a", None))
        self.label_197.setText(QCoreApplication.translate("MDCx", u"\u756a\u53f7\u540e\u7f00\u987a\u5e8f\uff1a", None))
        self.checkBox_title_del_actor.setText(QCoreApplication.translate("MDCx", u"\u53bb\u9664\u6807\u9898\u540e\u7684\u6f14\u5458\u540d\uff08\u4e2a\u522b\u7f51\u7ad9\u5728\u6807\u9898\u672b\u5c3e\u989d\u5916\u591a\u52a0\u4e86\u6f14\u5458\u540d\uff0c\u5efa\u8bae\u53bb\u9664\uff09", None))
        self.label_276.setText(QCoreApplication.translate("MDCx", u"\u53d1\u884c\u65e5\u671f\uff1a", None))
        self.label_302.setText(QCoreApplication.translate("MDCx", u"\u5e74: YYYY\u6216YY\uff0c\u6708: MM\uff0c\u65e5:DD\uff0c\u6bd4\u5982: YY.MM.DD \u5c06\u663e\u793a\u4e3a 22.03.20", None))
        self.label_100.setText(QCoreApplication.translate("MDCx", u"\u5f53\u6f14\u5458\u540d\u4e0d\u5b58\u5728\u65f6\uff0c\u5728\u4f7f\u7528\u6f14\u5458\u547d\u540d\u5b57\u6bb5\u547d\u540d\u65f6\uff0c\u4f7f\u7528\u4ee5\u4e0a\u5b57\u7b26\u66ff\u4ee3", None))
        self.label_320.setText(QCoreApplication.translate("MDCx", u"\u6807\u9898\uff1a", None))
        self.label_173.setText(QCoreApplication.translate("MDCx", u"\u672a\u77e5\u6f14\u5458\uff1a", None))
        self.checkBox_actor_fc2_seller.setText(QCoreApplication.translate("MDCx", u"FC2 \u65e0\u6f14\u5458\u65f6\uff0c\u4f7f\u7528\u5356\u5bb6\u540d\u5b57\u4f5c\u4e3a\u6f14\u5458\u540d\u5b57", None))
        self.groupBox_65.setTitle(QCoreApplication.translate("MDCx", u"\u753b\u8d28\u547d\u540d\u89c4\u5219", None))
        self.radioButton_definition_height.setText(QCoreApplication.translate("MDCx", u"720P\u30011080P\u30014K\u30018K", None))
        self.radioButton_definition_hd.setText(QCoreApplication.translate("MDCx", u"HD\u3001FHD\u3001QHD\u3001UHD", None))
        self.label_329.setText(QCoreApplication.translate("MDCx", u"\u4ee5\u89c6\u9891\u5206\u8fa8\u7387\u7684\u9ad8\u5ea6\u6570\u503c\u6765\u547d\u540d\u4e0d\u540c\u753b\u8d28", None))
        self.label_330.setText(QCoreApplication.translate("MDCx", u"\u4ee5\u89c6\u9891\u6e05\u6670\u5ea6\u7684\u82f1\u6587\u7f29\u5199\u6765\u547d\u540d\u4e0d\u540c\u753b\u8d28", None))
        self.label_331.setText(QCoreApplication.translate("MDCx", u"\u8bf4\u660e\uff1aqHD=540P\uff0cHD=720P/960P\uff0cFHD=1080P\uff0cQHD=1440P(2K)\uff0cUHD=4K/8K\u3002\u4f4e\u4e8e540P\u65f6\u9ed8\u8ba4\u4f7f\u7528\u9ad8\u5ea6\u503c\u547d\u540d", None))
        self.radioButton_videosize_video.setText(QCoreApplication.translate("MDCx", u"\u8bfb\u53d6\u89c6\u9891\u753b\u9762\u7684\u9ad8\u5ea6", None))
        self.radioButton_videosize_path.setText(QCoreApplication.translate("MDCx", u"\u4f7f\u7528\u8def\u5f84\u4e2d\u5305\u542b\u7684\u753b\u8d28\u4fe1\u606f", None))
        self.radioButton_videosize_none.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u83b7\u53d6\u5206\u8fa8\u7387", None))
        self.label_332.setText(QCoreApplication.translate("MDCx", u"\u5206\u8fa8\u7387\u83b7\u53d6\u65b9\u5f0f\uff1a", None))
        self.label_357.setText(QCoreApplication.translate("MDCx", u"\u6dfb\u52a0 4K \u5b57\u7b26\uff1a", None))
        self.checkBox_filename_4k.setText(QCoreApplication.translate("MDCx", u"\u89c6\u9891\u6587\u4ef6\u540d", None))
        self.label_358.setText(QCoreApplication.translate("MDCx", u"\u6307\u547d\u540d\u65f6\u5728\u756a\u53f7\u540e\u6dfb\u52a0 4K\uff08\u4ec54K\uff09\u3002\u4f60\u4e5f\u53ef\u4ee5\u4f7f\u7528 4K \u5b57\u6bb5\u6765\u8c03\u6574\u6dfb\u52a0\u4f4d\u7f6e", None))
        self.checkBox_foldername_4k.setText(QCoreApplication.translate("MDCx", u"\u89c6\u9891\u76ee\u5f55\u540d", None))
        self.groupBox_67.setTitle(QCoreApplication.translate("MDCx", u"\u5176\u4ed6\u8bf4\u660e", None))
        self.label_353.setText(QCoreApplication.translate("MDCx", u"1\uff0c\u591a\u7248\u672c\u663e\u793a\uff1a", None))
        self.label_352.setText(QCoreApplication.translate("MDCx", u"<html><head/><body><p>1\uff09Emby \u652f\u6301\u591a\u7248\u672c\u663e\u793a\uff08\u7c7b\u4f3c\u9009\u96c6\uff09\uff0c \u9700\u8981\uff1a</p><p>\u89c6\u9891\u6587\u4ef6\u540d\u7684\u5f00\u5934\u90e8\u5206\u5fc5\u987b\u5305\u542b\u89c6\u9891\u76ee\u5f55\u540d\u3002\uff08\u6bd4\u5982\uff1aSSIS-111/SSIS-111-4K.mp4\uff09 </p><p>\u67e5\u770b\u89c4\u5219\uff1a<a href=\"https://support.emby.media/support/solutions/articles/44001159102-movie-naming\"><span style=\" text-decoration: underline; color:#094fd1;\">https://support.emby.media/support/solutions/articles/44001159102-movie-naming</span></a></p><p>2\uff09\u5206\u96c6\u89c6\u9891\u9ed8\u8ba4\u4f1a\u663e\u793a\u4e3a\u9644\u52a0\u89c6\u9891\uff0c\u5982\u679c\u8981\u4ee5\u591a\u7248\u672c\u6837\u5f0f\u663e\u793a\uff0c\u5206\u96c6\u547d\u540d\u89c4\u5219\u8fd8\u9700\u8981\u9009\u62e9\u300c-1\u300d</p></body></html>", None))
        self.label_351.setText(QCoreApplication.translate("MDCx", u"Emby \u5206\u96c6\u5c01\u9762\u9700\u8981\u6bcf\u4e2a\u5206\u96c6\u90fd\u63d0\u4f9b\u56fe\u7247\uff0c\u56fe\u7247\u547d\u540d\u89c4\u5219\u9700\u8981\u9009\u62e9\u300c\u89c6\u9891\u6587\u4ef6\u540d-poster.jpg\u300d", None))
        self.label_354.setText(QCoreApplication.translate("MDCx", u"2\uff0c\u5206\u96c6\u5c01\u9762\u663e\u793a\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MDCx", u" \u547d\u540d ", None))
        self.groupBox_79.setTitle(QCoreApplication.translate("MDCx", u"\u7ffb\u8bd1\u5f15\u64ce", None))
        self.label_81.setText(QCoreApplication.translate("MDCx", u"\u7ffb\u8bd1\u5f15\u64ce\uff1a", None))
        self.label_60.setText(QCoreApplication.translate("MDCx", u"\u586b\u5199\u514d\u8d39\u6216\u4ed8\u8d39 key \u65f6\uff0c\u5c06\u4f7f\u7528 API \u7ffb\u8bd1 \uff1b\u4e0d\u586b\u5199\u65f6\uff0c\u5c06\u4f7f\u7528\u7f51\u9875\u7aef\u63a5\u53e3\u7ffb\u8bd1\u3002", None))
        self.checkBox_youdao.setText(QCoreApplication.translate("MDCx", u"\u6709\u9053", None))
        self.checkBox_google.setText(QCoreApplication.translate("MDCx", u"Google", None))
        self.checkBox_deepl.setText(QCoreApplication.translate("MDCx", u"DeepL", None))
        self.label_80.setText(QCoreApplication.translate("MDCx", u"DeepL API key\uff1a", None))
        self.label_164.setText(QCoreApplication.translate("MDCx", u"\u5f53\u52fe\u9009\u591a\u4e2a\u65f6\uff0c\u5c06\u968f\u673a\u4f7f\u7528\u6240\u52fe\u9009\u7684\u5176\u4e2d\u4efb\u4e00\u7ffb\u8bd1\u5f15\u64ce\uff0c\u53ef\u964d\u4f4e\u88ab\u5c01\u51e0\u7387", None))
        self.groupBox_82.setTitle(QCoreApplication.translate("MDCx", u"\u6807\u9898", None))
        self.checkBox_title_sehua.setText(QCoreApplication.translate("MDCx", u"\u4f7f\u7528\u8272\u82b1\u4e2d\u6587\u6807\u9898", None))
        self.checkBox_title_yesjav.setText(QCoreApplication.translate("MDCx", u"\u4f7f\u7528yesjav\u4e2d\u6587\u6807\u9898", None))
        self.checkBox_title_translate.setText(QCoreApplication.translate("MDCx", u"\u4f7f\u7528\u7ffb\u8bd1\u5f15\u64ce\u7ffb\u8bd1\u6807\u9898", None))
        self.label_242.setText(QCoreApplication.translate("MDCx", u"\u6807\u9898\u8bed\u8a00\uff1a", None))
        self.label_74.setText(QCoreApplication.translate("MDCx", u"\u5c06\u4f18\u5148\u4f7f\u7528\u522e\u524a\u7f51\u7ad9\u7684\u4e2d\u6587\u7ffb\u8bd1\uff0c\u5f53\u522e\u524a\u9875\u9762\u65e0\u4e2d\u6587\u65f6\uff0c\u624d\u4f7f\u7528\u4ee5\u4e0b\u7ffb\u8bd1\u65b9\u5f0f\u3002", None))
        self.radioButton_title_zh_cn.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u7b80\u4f53", None))
        self.radioButton_title_zh_tw.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u7e41\u4f53", None))
        self.radioButton_title_jp.setText(QCoreApplication.translate("MDCx", u"\u65e5\u8bed", None))
        self.label_236.setText(QCoreApplication.translate("MDCx", u"\u5f53\u5b58\u5728\u8272\u82b1\u4e2d\u6587\u6807\u9898\u65f6\uff0c\u5373\u4f7f\u522e\u524a\u7f51\u7ad9\u6709\u4e2d\u6587\u7ffb\u8bd1\uff0c\u4e5f\u4f1a\u4f7f\u7528\u8272\u82b1\u4e2d\u6587\u6807\u9898", None))
        self.label_160.setText(QCoreApplication.translate("MDCx", u"\u7ffb\u8bd1\u4f18\u5148\u7ea7\uff1a\u8272\u82b1\uff08\u5185\u7f6e\u6807\u9898\u6570\u636e\uff09 > yesjav\uff08\u5728\u7ebf\u8272\u82b1\u6570\u636e\uff09 > \u7ffb\u8bd1\u5f15\u64ce", None))
        self.checkBox_title_sehua_2.setText(QCoreApplication.translate("MDCx", u"\u4f18\u5148\u4f7f\u7528\u8272\u82b1\u4e2d\u6587\u6807\u9898", None))
        self.label_244.setText(QCoreApplication.translate("MDCx", u"\u7ffb\u8bd1\u65b9\u5f0f\uff1a", None))
        self.groupBox_83.setTitle(QCoreApplication.translate("MDCx", u"\u7b80\u4ecb", None))
        self.label_133.setText(QCoreApplication.translate("MDCx", u"\u7b80\u4ecb\u8bed\u8a00\uff1a", None))
        self.label_176.setText(QCoreApplication.translate("MDCx", u"\u5f53\u5b57\u6bb5\u8bed\u8a00\u9009\u62e9\u4e2d\u6587\uff0c\u4f46\u53ea\u522e\u524a\u5230\u65e5\u8bed\u65f6\uff0c\u53ef\u4f7f\u7528\u7ffb\u8bd1\u5f15\u64ce\u8fdb\u884c\u7ffb\u8bd1", None))
        self.label_166.setText(QCoreApplication.translate("MDCx", u"\u7ffb\u8bd1\u65b9\u5f0f\uff1a", None))
        self.radioButton_outline_zh_cn.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u7b80\u4f53", None))
        self.radioButton_outline_zh_tw.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u7e41\u4f53", None))
        self.radioButton_outline_jp.setText(QCoreApplication.translate("MDCx", u"\u65e5\u8bed", None))
        self.checkBox_outline_translate.setText(QCoreApplication.translate("MDCx", u"\u4f7f\u7528\u7ffb\u8bd1\u5f15\u64ce\u7ffb\u8bd1\u7b80\u4ecb", None))
        self.checkBox_show_translate_from.setText(QCoreApplication.translate("MDCx", u"\u663e\u793a\u7ffb\u8bd1\u6765\u6e90", None))
        self.radioButton_trans_show_zh_jp.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587+\u65e5\u8bed", None))
        self.radioButton_trans_show_jp_zh.setText(QCoreApplication.translate("MDCx", u"\u65e5\u8bed+\u4e2d\u6587", None))
        self.radioButton_trans_show_one.setText(QCoreApplication.translate("MDCx", u"\u5173\u95ed", None))
        self.label_328.setText(QCoreApplication.translate("MDCx", u"\u53cc\u8bed\u663e\u793a\uff1a", None))
        self.groupBox_84.setTitle(QCoreApplication.translate("MDCx", u"\u6f14\u5458", None))
        self.label_250.setText(QCoreApplication.translate("MDCx", u"\u7ffb\u8bd1\u65b9\u5f0f\uff1a", None))
        self.radioButton_actor_zh_cn.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u7b80\u4f53", None))
        self.radioButton_actor_zh_tw.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u7e41\u4f53", None))
        self.radioButton_actor_jp.setText(QCoreApplication.translate("MDCx", u"\u65e5\u8bed", None))
        self.label_249.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>\n"
"\u7d20\u4eba\u548c FC2 \u756a\u53f7\u6f14\u5458\u53ef\u80fd\u662f\u300c\u7d20\u4eba\u300d\u4e4b\u7c7b\u5047\u540d\u5b57\uff0c\u52fe\u9009\u300c\u4f7f\u7528AV-wiki\u83b7\u53d6\u6f14\u5458\u771f\u5b9e\u540d\u5b57\u300d\uff0c\u53ef\u4ee5\u8bf7\u6c42 AV-wiki \u83b7\u53d6\u6f14\u5458\u771f\u5b9e\u65e5\u6587\u540d\uff0c\u4e4b\u540e\u53ef\u4f7f\u7528\u6620\u5c04\u8868\u7ffb\u8bd1\u4e3a\u4e2d\u6587\uff01<br>\n"
"\u6f14\u5458\u540d\u6bd4\u8f83\u590d\u6742\uff0c\u4e0d\u80fd\u7b80\u5355\u4f7f\u7528\u7ffb\u8bd1\u5f15\u64ce\u7ffb\u8bd1\u3002\u4e3b\u8981\u7684\u95ee\u9898\uff1a\u6f14\u5458\u540d\u7ffb\u8bd1\u4e0d\u51c6\u786e\u3001\u6f14\u5458\u6709\u591a\u4e2a\u540d\u5b57\u3001\u540c\u4e00\u6f14\u5458\u4e0d\u540c\u756a\u53f7\u6f14\u5458\u540d\u4e0d\u7edf\u4e00\u3001\u5404\u7f51\u7ad9\u4f7f\u7528\u7684\u6f14\u5458\u540d\u4e0d\u7edf\u4e00\u7b49\u3002<br>\n"
"\u4e0d\u8fc7\uff0c\u901a\u8fc7\u6f14\u5458\u540d\u6620\u5c04\u7ffb\u8bd1\u8868\u53ef\u4ee5\u89e3\u51b3\u8fd9\u4e9b\u95ee\u9898\uff0c\u4f7f"
                        "\u522e\u524a\u540e\u7684\u6f14\u5458\u540d\u6574\u9f50\u7edf\u4e00\u3002<br>\n"
"\u5b9e\u73b0\u903b\u8f91\uff1a\u522e\u524a\u7f51\u7ad9\u83b7\u53d6\u6f14\u5458\u540d\u540e\uff0c\u901a\u8fc7\u67e5\u8be2\u6620\u5c04\u8868\u4e2d\u7684\u5339\u914d\u8bcd\u6765\u6620\u5c04\u5bf9\u5e94\u8f93\u51fa\u8bcd\u3002\n"
"<br>\n"
"\u6f14\u5458\u540d\u6620\u5c04\u7ffb\u8bd1\u8868\u6587\u4ef6\u540d\u4e3a\uff1amapping_actor.xml<br>\n"
"   \u00b7 Windows\u4f4d\u7f6e\uff1a\\\u914d\u7f6e\u6587\u4ef6\u76ee\u5f55\\userdata\\mapping_actor.xml\uff08\u914d\u7f6e\u6587\u4ef6\u76ee\u5f55\u5728\u300c\u8bbe\u7f6e\u300d-\u300c\u5176\u4ed6\u300d\u4e2d\u8bbe\u7f6e\uff09<br>\n"
"   \u00b7 Mac\u4f4d\u7f6e\uff1a/\u914d\u7f6e\u6587\u4ef6\u76ee\u5f55/userdata/mapping_actor.xml<br>\n"
"\u4f60\u53ef\u4f7f\u7528\u6587\u4ef6\u7f16\u8f91\u5de5\u5177\u6253\u5f00\u8be5\u6587\u4ef6\u81ea\u5b9a\u4e49\u4fee\u6539\u6dfb\u52a0\u3002\u6620\u5c04\u8868\u4e2d\u7684\u5b57\u6bb5\u542b\u4e49\u5982\u4e0b\uff1a<br>\n"
"1\u3001keyword\uff1a\u5339\u914d\u8bcd\uff08\u6bcf"
                        "\u4e2a\u540d\u5b57\u524d\u540e\u90fd\u8981\u6709\u9017\u53f7\uff09\u3002\u522e\u524a\u7f51\u7ad9\u83b7\u53d6\u6f14\u5458\u540d\u540e\uff0c\u4f1a\u5728 keyword \u7684\u540d\u5b57\u4e2d\u8fdb\u884c\u5339\u914d\u3002<br>\n"
"2\u3001zh_cn/zh_tw/jp\uff1a\u8f93\u51fa\u8bcd\u3002\u5f53 keyword \u5339\u914d\u5230\u6f14\u5458\u540d\u65f6\uff0c\u53ef\u8f93\u51fa\u5bf9\u5e94\u8bed\u8a00\u7684\u540d\u5b57\u3002</p>", None))
        self.checkBox_actor_realname.setText(QCoreApplication.translate("MDCx", u"\u4f7f\u7528AV-wiki\u83b7\u53d6\u6f14\u5458\u771f\u5b9e\u540d\u5b57", None))
        self.checkBox_actor_translate.setText(QCoreApplication.translate("MDCx", u"\u4f7f\u7528\u6f14\u5458\u6620\u5c04\u8868\u7ffb\u8bd1\u6f14\u5458", None))
        self.label_248.setText(QCoreApplication.translate("MDCx", u"\u6f14\u5458\u8bed\u8a00\uff1a", None))
        self.groupBox_85.setTitle(QCoreApplication.translate("MDCx", u"\u6807\u7b7e", None))
        self.radioButton_tag_zh_cn.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u7b80\u4f53", None))
        self.radioButton_tag_zh_tw.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u7e41\u4f53", None))
        self.radioButton_tag_jp.setText(QCoreApplication.translate("MDCx", u"\u65e5\u8bed", None))
        self.label_165.setText(QCoreApplication.translate("MDCx", u"\u6620\u5c04\u8868\u6587\u4ef6\u540d\uff1amapping_info.xml\u3002\u4f5c\u7528\u548c\u6f14\u5458\u6620\u5c04\u8868\u7c7b\u4f3c\uff0c\u8bf4\u660e\u53ef\u53c2\u8003\u6f14\u5458\u6620\u5c04\u8868\u3002", None))
        self.checkBox_tag_translate.setText(QCoreApplication.translate("MDCx", u"\u4f7f\u7528\u4fe1\u606f\u6620\u5c04\u8868\u7ffb\u8bd1\u6807\u7b7e", None))
        self.label_251.setText(QCoreApplication.translate("MDCx", u"\u6807\u7b7e\u8bed\u8a00\uff1a", None))
        self.label_253.setText(QCoreApplication.translate("MDCx", u"\u7ffb\u8bd1\u65b9\u5f0f\uff1a", None))
        self.groupBox_86.setTitle(QCoreApplication.translate("MDCx", u"\u7cfb\u5217", None))
        self.label_255.setText(QCoreApplication.translate("MDCx", u"\u7cfb\u5217\u8bed\u8a00\uff1a", None))
        self.label_256.setText(QCoreApplication.translate("MDCx", u"\u7ffb\u8bd1\u65b9\u5f0f\uff1a", None))
        self.label_245.setText(QCoreApplication.translate("MDCx", u"\u6620\u5c04\u8868\u6587\u4ef6\u540d\uff1amapping_info.xml\u3002\u4f5c\u7528\u548c\u6f14\u5458\u6620\u5c04\u8868\u7c7b\u4f3c\uff0c\u8bf4\u660e\u53ef\u53c2\u8003\u6f14\u5458\u6620\u5c04\u8868\u3002", None))
        self.radioButton_series_zh_cn.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u7b80\u4f53", None))
        self.radioButton_series_zh_tw.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u7e41\u4f53", None))
        self.radioButton_series_jp.setText(QCoreApplication.translate("MDCx", u"\u65e5\u8bed", None))
        self.checkBox_series_translate.setText(QCoreApplication.translate("MDCx", u"\u4f7f\u7528\u4fe1\u606f\u6620\u5c04\u8868\u7ffb\u8bd1\u7cfb\u5217", None))
        self.groupBox_87.setTitle(QCoreApplication.translate("MDCx", u"\u7247\u5546", None))
        self.label_259.setText(QCoreApplication.translate("MDCx", u"\u7247\u5546\u8bed\u8a00\uff1a", None))
        self.label_260.setText(QCoreApplication.translate("MDCx", u"\u7ffb\u8bd1\u65b9\u5f0f\uff1a", None))
        self.label_247.setText(QCoreApplication.translate("MDCx", u"\u6620\u5c04\u8868\u6587\u4ef6\u540d\uff1amapping_info.xml\u3002\u4f5c\u7528\u548c\u6f14\u5458\u6620\u5c04\u8868\u7c7b\u4f3c\uff0c\u8bf4\u660e\u53ef\u53c2\u8003\u6f14\u5458\u6620\u5c04\u8868\u3002", None))
        self.radioButton_studio_zh_cn.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u7b80\u4f53", None))
        self.radioButton_studio_zh_tw.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u7e41\u4f53", None))
        self.radioButton_studio_jp.setText(QCoreApplication.translate("MDCx", u"\u65e5\u8bed", None))
        self.checkBox_studio_translate.setText(QCoreApplication.translate("MDCx", u"\u4f7f\u7528\u4fe1\u606f\u6620\u5c04\u8868\u7ffb\u8bd1\u7247\u5546", None))
        self.groupBox_88.setTitle(QCoreApplication.translate("MDCx", u"\u53d1\u884c\u5546", None))
        self.label_264.setText(QCoreApplication.translate("MDCx", u"\u53d1\u884c\u5546\u8bed\u8a00\uff1a", None))
        self.label_265.setText(QCoreApplication.translate("MDCx", u"\u7ffb\u8bd1\u65b9\u5f0f\uff1a", None))
        self.label_266.setText(QCoreApplication.translate("MDCx", u"\u6620\u5c04\u8868\u6587\u4ef6\u540d\uff1amapping_info.xml\u3002\u4f5c\u7528\u548c\u6f14\u5458\u6620\u5c04\u8868\u7c7b\u4f3c\uff0c\u8bf4\u660e\u53ef\u53c2\u8003\u6f14\u5458\u6620\u5c04\u8868\u3002", None))
        self.radioButton_publisher_zh_cn.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u7b80\u4f53", None))
        self.radioButton_publisher_zh_tw.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u7e41\u4f53", None))
        self.radioButton_publisher_jp.setText(QCoreApplication.translate("MDCx", u"\u65e5\u8bed", None))
        self.checkBox_publisher_translate.setText(QCoreApplication.translate("MDCx", u"\u4f7f\u7528\u4fe1\u606f\u6620\u5c04\u8868\u7ffb\u8bd1\u53d1\u884c\u5546", None))
        self.groupBox_89.setTitle(QCoreApplication.translate("MDCx", u"\u5bfc\u6f14", None))
        self.label_267.setText(QCoreApplication.translate("MDCx", u"\u53d1\u884c\u5546\u8bed\u8a00\uff1a", None))
        self.label_268.setText(QCoreApplication.translate("MDCx", u"\u7ffb\u8bd1\u65b9\u5f0f\uff1a", None))
        self.label_269.setText(QCoreApplication.translate("MDCx", u"\u6620\u5c04\u8868\u6587\u4ef6\u540d\uff1amapping_info.xml\u3002\u4f5c\u7528\u548c\u6f14\u5458\u6620\u5c04\u8868\u7c7b\u4f3c\uff0c\u8bf4\u660e\u53ef\u53c2\u8003\u6f14\u5458\u6620\u5c04\u8868\u3002", None))
        self.checkBox_director_translate.setText(QCoreApplication.translate("MDCx", u"\u4f7f\u7528\u4fe1\u606f\u6620\u5c04\u8868\u7ffb\u8bd1\u5bfc\u6f14", None))
        self.radioButton_director_zh_cn.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u7b80\u4f53", None))
        self.radioButton_director_zh_tw.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u7e41\u4f53", None))
        self.radioButton_director_jp.setText(QCoreApplication.translate("MDCx", u"\u65e5\u8bed", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MDCx", u" \u7ffb\u8bd1 ", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u5b57\u5e55\u5b57\u7b26\u89c4\u5219", None))
        self.label_89.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u5b57\u5e55\u5224\u65ad\u5b57\u7b26\uff1a", None))
        self.label_90.setText(QCoreApplication.translate("MDCx", u"\u6307\u89c6\u9891\u6709\u4e2d\u6587\u5b57\u5e55\u65f6\uff0c\u5728\u91cd\u547d\u540d\u6587\u4ef6\u540d\u53ca\u76ee\u5f55\u540d\u65f6\u5728\u756a\u53f7\u540e\u6dfb\u52a0\u8be5\u5b57\u7b26\u8868\u793a\u6709\u4e2d\u6587\u5b57\u5e55", None))
        self.label_91.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>\u6307\u89c6\u9891\u6587\u4ef6\u8def\u5f84\u4e2d\u542b\u6709\u4ee5\u4e0a\u5b57\u7b26\u65f6\uff0c\u89c6\u4e3a\u8be5\u6587\u4ef6\u6709\u4e2d\u6587\u5b57\u5e55\uff0c\u591a\u4e2a\u4ee5\u9017\u53f7\u5206\u5272<br>\n"
"\u6b64\u5916\uff0c\u8fd8\u4f1a\u67e5\u627e\u540c\u76ee\u5f55\u662f\u5426\u5b58\u5728\u540c\u540d\u5b57\u5e55\u6587\u4ef6\u3001nfo \u7684\u6807\u7b7e\u662f\u5426\u6709\u4e2d\u6587\u5b57\u5e55\u5b57\u6837</p>", None))
        self.label_69.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u5b57\u5e55\u547d\u540d\u5b57\u7b26\uff1a", None))
        self.label_119.setText(QCoreApplication.translate("MDCx", u"\u6307\u547d\u540d\u65f6\u5728\u756a\u53f7\u540e\u6dfb\u52a0\u4e2d\u6587\u5b57\u5e55\u547d\u540d\u5b57\u7b26\u3002\u4f60\u4e5f\u53ef\u4ee5\u4f7f\u7528 cnword \u5b57\u6bb5\u6765\u8c03\u6574\u6dfb\u52a0\u4f4d\u7f6e", None))
        self.checkBox_foldername.setText(QCoreApplication.translate("MDCx", u"\u89c6\u9891\u76ee\u5f55\u540d", None))
        self.checkBox_filename.setText(QCoreApplication.translate("MDCx", u"\u89c6\u9891\u6587\u4ef6\u540d", None))
        self.label_120.setText(QCoreApplication.translate("MDCx", u"\u6dfb\u52a0\u4e2d\u6587\u5b57\u5e55\u5b57\u7b26\uff1a", None))
        self.groupBox_45.setTitle(QCoreApplication.translate("MDCx", u"\u6dfb\u52a0\u5916\u6302\u5b57\u5e55", None))
        self.label_113.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u65f6\uff0c\u5982\u679c\u89c6\u9891\u65e0\u5185\u5d4c\u5b57\u5e55\u4e14\u540c\u76ee\u5f55\u65e0\u5b57\u5e55\u6587\u4ef6\uff0c\u5219\u4ece\u5b57\u5e55\u6587\u4ef6\u76ee\u5f55\u67e5\u627e\u5e76\u590d\u5236\u5b57\u5e55", None))
        self.label_124.setText("")
        self.label_102.setText(QCoreApplication.translate("MDCx", u"\u4e0b\u8f7d\u5b57\u5e55\u5305\u89e3\u538b\uff0c\u586b\u5199\u5b57\u5e55\u6587\u4ef6\u76ee\u5f55\u7684\u8def\u5f84", None))
        self.label_download_sub_zip.setText(QCoreApplication.translate("MDCx", u"\u70b9\u51fb\u4e0b\u8f7d\u5b57\u5e55\u5305", None))
        self.label_111.setText(QCoreApplication.translate("MDCx", u"\u5b57\u5e55\u6587\u4ef6\u76ee\u5f55\uff1a", None))
        self.label_112.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u65f6\u81ea\u52a8\u6dfb\u52a0\u5b57\u5e55\uff1a", None))
        self.radioButton_add_sub_on.setText(QCoreApplication.translate("MDCx", u"\u5f00", None))
        self.radioButton_add_sub_off.setText(QCoreApplication.translate("MDCx", u"\u5173", None))
        self.pushButton_select_subtitle_folder.setText(QCoreApplication.translate("MDCx", u"\u9009\u62e9\u76ee\u5f55", None))
        self.pushButton_add_sub_for_all_video.setText(QCoreApplication.translate("MDCx", u"\u70b9\u51fb\u68c0\u67e5\u6240\u6709\u89c6\u9891\u7684\u5b57\u5e55\u60c5\u51b5\u5e76\u4e3a\u65e0\u5b57\u5e55\u89c6\u9891\u6dfb\u52a0\u5b57\u5e55", None))
        self.label_125.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>\u5f53\u5b57\u5e55\u6587\u4ef6\u76ee\u5f55\u4e3a\u7a7a\u65f6\uff0c\u5c06\u53ea\u68c0\u67e5\u5e76\u7edf\u8ba1\u65e0\u5b57\u5e55\u7684\u89c6\u9891\u5217\u8868<br>\n"
"\u5f53\u89c6\u9891\u5df2\u8bc6\u522b\u4e3a\u6709\u5b57\u5e55\u72b6\u6001\u65f6\uff08\u5df2\u6709\u5b57\u5e55\u6216\u5305\u542b\u4e2d\u6587\u5b57\u5e55\u5b57\u7b26\u7b49\uff09\uff0c\u4e0d\u4f1a\u91cd\u590d\u6dfb\u52a0\u5b57\u5e55<br>\n"
"\u5f53\u89c6\u9891\u6dfb\u52a0\u65b0\u7684\u5916\u6302\u5b57\u5e55\u540e\uff0c\u5982\u52fe\u9009\u91cd\u65b0\u522e\u524a\uff0c\u5c06\u5728\u6dfb\u52a0\u7ed3\u675f\u540e\u81ea\u52a8\u522e\u524a<br>\n"
"\u5f53\u89c6\u9891\u4e4b\u524d\u6dfb\u52a0\u4e86\u5916\u6302\u5b57\u5e55\uff0c\u4f46\u662f\u8fd8\u6ca1\u6709\u91cd\u65b0\u522e\u524a\u65f6\uff0c\u8fd9\u65f6\u4e5f\u4f1a\u81ea\u52a8\u522e\u524a<br>\n"
"\u5f53\u52fe\u9009\u6dfb\u52a0.chs\u540e\u7f00\u65f6\uff0c\u5b57\u5e55\u6587\u4ef6\u4f1a\u88ab\u7edf\u4e00\u547d\u540d\u4e3a\uff1a\u89c6\u9891\u6587\u4ef6\u540d.chs.srt</p>", None))
        self.checkBox_sub_add_chs.setText(QCoreApplication.translate("MDCx", u"\u5b57\u5e55\u6587\u4ef6\u540d\u6dfb\u52a0.chs\u540e\u7f00", None))
        self.checkBox_sub_rescrape.setText(QCoreApplication.translate("MDCx", u"\u65b0\u6dfb\u52a0\u5b57\u5e55\u7684\u89c6\u9891\u5728\u7ed3\u675f\u540e\u91cd\u65b0\u522e\u524a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MDCx", u" \u5b57\u5e55 ", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("MDCx", u"\u81ea\u5b9a\u4e49\u6c34\u5370\u6837\u5f0f", None))
        self.label_118.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>1\u3001\u4e0b\u8f7d\u6c34\u5370\u56fe\u7247\u5305\u5e76\u89e3\u538b\uff08\u4e5f\u53ef\u4ee5\u4f7f\u7528\u81ea\u5df1\u7684\u56fe\u7247\uff09\uff0c\u6c34\u5370\u56fe\u7247\u7684\u4fdd\u5b58\u8def\u5f84\u4e3a\uff1a<br>\n"
"   \u00b7 Windows\u4f4d\u7f6e\uff1a\uff08\u914d\u7f6e\u6587\u4ef6\u76ee\u5f55\u5728\u300c\u8bbe\u7f6e\u300d-\u300c\u9ad8\u7ea7\u300d\u4e2d\u8bbe\u7f6e\uff09<br>\n"
"       \u5b57\u5e55\u6c34\u5370\uff1a\\\u914d\u7f6e\u6587\u4ef6\u76ee\u5f55\\userdata\\watermark\\sub.png<br>\n"
"       \u6709\u7801\u6c34\u5370\uff1a\\\u914d\u7f6e\u6587\u4ef6\u76ee\u5f55\\userdata\\watermark\\youma.png<br>\n"
"       \u7834\u89e3\u6c34\u5370\uff1a\\\u914d\u7f6e\u6587\u4ef6\u76ee\u5f55\\userdata\\watermark\\umr.png<br>\n"
"       \u6d41\u51fa\u6c34\u5370\uff1a\\\u914d\u7f6e\u6587\u4ef6\u76ee\u5f55\\userdata\\watermark\\leak.png<br>\n"
"       \u65e0\u7801\u6c34\u5370\uff1a\\\u914d\u7f6e\u6587\u4ef6\u76ee\u5f55\\userdata\\watermark\\wuma.png<br>\n"
"       4K\u6c34\u5370\uff1a\\\u914d\u7f6e"
                        "\u6587\u4ef6\u76ee\u5f55\\userdata\\watermark\\4k.png<br>\n"
"       8K\u6c34\u5370\uff1a\\\u914d\u7f6e\u6587\u4ef6\u76ee\u5f55\\userdata\\watermark\\8k.png<br>\n"
"   \u00b7 Mac\u4f4d\u7f6e\uff1a\uff08\u914d\u7f6e\u6587\u4ef6\u76ee\u5f55\u5728\u300c\u8bbe\u7f6e\u300d-\u300c\u9ad8\u7ea7\u300d\u4e2d\u8bbe\u7f6e\uff09<br>\n"
"       \u5b57\u5e55\u6c34\u5370\uff1a/\u914d\u7f6e\u6587\u4ef6\u76ee\u5f55/userdata/watermark/sub.png<br>\n"
"       \u6709\u7801\u6c34\u5370\uff1a/\u914d\u7f6e\u6587\u4ef6\u76ee\u5f55/userdata/watermark/youma.png<br>\n"
"       \u7834\u89e3\u6c34\u5370\uff1a/\u914d\u7f6e\u6587\u4ef6\u76ee\u5f55/userdata/watermark/umr.png<br>\n"
"       \u6d41\u51fa\u6c34\u5370\uff1a/\u914d\u7f6e\u6587\u4ef6\u76ee\u5f55/userdata/watermark/leak.png<br>\n"
"       \u65e0\u7801\u6c34\u5370\uff1a/\u914d\u7f6e\u6587\u4ef6\u76ee\u5f55/userdata/watermark/wuma.png<br>\n"
"       4K\u6c34\u5370\uff1a/\u914d\u7f6e\u6587\u4ef6\u76ee\u5f55/userdata/watermark/4k.png<br>\n"
"       8K\u6c34\u5370\uff1a/\u914d\u7f6e\u6587"
                        "\u4ef6\u76ee\u5f55/userdata/watermark/8k.png<br>\n"
"<br>\n"
"2\u3001\u6c34\u5370\u56fe\u7247\u663e\u793a\u7684\u903b\u8f91\uff1a<br>\n"
"   \u00b7 \u9996\u5148\u8ba1\u7b97\u6c34\u5370\u56fe\u7247\u7684\u663e\u793a\u9ad8\u5ea6 = \u5c01\u9762\u56fe\u9ad8\u5ea6 * \u8bbe\u7f6e\u7684\u6c34\u5370\u5927\u5c0f / 40<br>\n"
"       \u6bd4\u5982\u6c34\u5370\u5927\u5c0f\u8bbe\u7f6e\u4e3a 5\uff0c\u5219\u6c34\u5370\u56fe\u7247\u7684\u9ad8\u5ea6\u4f1a\u7f29\u653e\u4e3a\u5c01\u9762\u56fe\u9ad8\u5ea6\u7684 5/40<br>\n"
"   \u00b7 \u7136\u540e\u6839\u636e\u6c34\u5370\u56fe\u7247\u7684\u663e\u793a\u9ad8\u5ea6\uff0c\u548c\u6c34\u5370\u56fe\u7247\u7684\u5bbd\u9ad8\u6bd4\uff0c\u8ba1\u7b97\u6c34\u5370\u56fe\u7247\u7684\u663e\u793a\u5bbd\u5ea6<br>\n"
"   \u00b7 \u6700\u540e\u6839\u636e\u8bbe\u7f6e\u7684\u8981\u6dfb\u52a0\u7684\u6c34\u5370\u7c7b\u578b\u548c\u9996\u4e2a\u6c34\u5370\u4f4d\u7f6e\uff0c\u987a\u65f6\u9488\u4f9d\u6b21\u663e\u793a\u5728\u5c01\u9762\u56fe\u7684\u56db\u4e2a\u89d2\u4e0a</p>", None))
        self.label_download_mark_zip.setText(QCoreApplication.translate("MDCx", u"\u70b9\u51fb\u4e0b\u8f7d\u6c34\u5370\u56fe\u7247\u5305", None))
        self.groupBox_31.setTitle(QCoreApplication.translate("MDCx", u"\u6c34\u5370\u8bbe\u7f6e", None))
        self.radioButton_not_fixed_position.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u56fa\u5b9a\u4f4d\u7f6e", None))
        self.radioButton_fixed_corner.setText(QCoreApplication.translate("MDCx", u"\u56fa\u5b9a\u4e00\u4e2a\u4f4d\u7f6e", None))
        self.radioButton_fixed_position.setText(QCoreApplication.translate("MDCx", u"\u56fa\u5b9a\u4e0d\u540c\u4f4d\u7f6e", None))
        self.label_138.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>\u6c34\u5370\u5206\u4e3a\u5b57\u5e55\u6c34\u5370\u3001\u9a6c\u8d5b\u514b\u6c34\u5370\u30014K/8K\u6c34\u5370\u3002<br>\n"
"\u9a6c\u8d5b\u514b\u6c34\u5370\u6709\u56db\u4e2a\uff1a\u6709\u7801\u3001\u7834\u89e3\u3001\u6d41\u51fa\u3001\u65e0\u7801\uff0c\u5c06\u6309\u4f18\u5148\u7ea7\u663e\u793a\u5176\u4e2d\u4e00\u79cd\u72b6\u6001<br>\n"
"\u9a6c\u8d5b\u514b\u6c34\u5370\u4f18\u5148\u7ea7\uff1a\u6709\u7801 > \u7834\u89e3 > \u6d41\u51fa > \u65e0\u7801<br>\n"
"\u4e3e\u4f8b\uff1a\u5982\u679c\u89c6\u9891\u662f\u6d41\u51fa\u7248\u672c<br>\n"
"   \u00b7\u5f53\u6d41\u51fa\u548c\u65e0\u7801\u90fd\u52fe\u9009\u65f6\uff0c\u4f1a\u663e\u793a\u6d41\u51fa\u6c34\u5370<br>\n"
"   \u00b7\u5f53\u6d41\u51fa\u672a\u52fe\u9009\uff0c\u65e0\u7801\u5df2\u52fe\u9009\u65f6\uff0c\u4f1a\u663e\u793a\u65e0\u7801\u6c34\u5370<br>\n"
"   \u00b7\u5f53\u6d41\u51fa\u548c\u65e0\u7801\u90fd\u4e0d\u52fe\u9009\u65f6\uff0c\u5219\u4e0d\u663e\u793a\u6c34\u5370\u5ba2</p>", None))
        self.label_135.setText(QCoreApplication.translate("MDCx", u"\u6c34\u5370\u7c7b\u578b\uff1a", None))
        self.label_128.setText(QCoreApplication.translate("MDCx", u"\u6dfb\u52a0\u6c34\u5370\u7684\u56fe\u7247\uff1a", None))
        self.checkBox_sub.setText(QCoreApplication.translate("MDCx", u"\u5b57\u5e55", None))
        self.checkBox_censored.setText(QCoreApplication.translate("MDCx", u"\u6709\u7801", None))
        self.checkBox_umr.setText(QCoreApplication.translate("MDCx", u"\u7834\u89e3", None))
        self.checkBox_leak.setText(QCoreApplication.translate("MDCx", u"\u6d41\u51fa", None))
        self.checkBox_uncensored.setText(QCoreApplication.translate("MDCx", u"\u65e0\u7801", None))
        self.checkBox_hd.setText(QCoreApplication.translate("MDCx", u"4K/8K", None))
        self.label_140.setText(QCoreApplication.translate("MDCx", u"\u6c34\u5370\u56fe\u7247\u7684\u663e\u793a\u9ad8\u5ea6 = \u8bbe\u7f6e\u7684\u6c34\u5370\u5927\u5c0f / 40 * \u5c01\u9762\u56fe\u9ad8\u5ea6", None))
        self.label_141.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>\u4e0d\u56fa\u5b9a\u4f4d\u7f6e\uff1a\u5c06\u4ece\u9996\u4e2a\u6c34\u5370\u4f4d\u7f6e\u5f00\u59cb\uff0c\u987a\u65f6\u9488\u65b9\u5411\u4f9d\u6b21\u6dfb\u52a0\u5176\u4ed6\u6c34\u5370<br>\n"
"\u56fa\u5b9a\u4e00\u4e2a\u4f4d\u7f6e\uff1a\u6c34\u5370\u5728\u6307\u5b9a\u4f4d\u7f6e\u4f9d\u6b21\u6a2a\u5411\u663e\u793a<br>\n"
"\u56fa\u5b9a\u591a\u4e2a\u4f4d\u7f6e\uff1a\u53ef\u5355\u72ec\u8bbe\u7f6e 4K/8K \u6c34\u5370\u3001\u5b57\u5e55\u6c34\u5370\u548c\u9a6c\u8d5b\u514b\u6c34\u5370\u7684\u4f4d\u7f6e<br>\n"
"\u6ce8\u610f\uff1a\u4e0d\u56fa\u5b9a\u4f4d\u7f6e\u65f6\uff0c4K/8K \u6c34\u5370\u4f1a\u4f7f\u7528\u56fa\u5b9a\u4f4d\u7f6e\u65b9\u5f0f\uff0c\u5e76\u81ea\u52a8\u6324\u5f00\u5176\u4ed6\u6c34\u5370</p>", None))
        self.checkBox_poster_mark.setText(QCoreApplication.translate("MDCx", u"poster", None))
        self.checkBox_thumb_mark.setText(QCoreApplication.translate("MDCx", u"thumb", None))
        self.checkBox_fanart_mark.setText(QCoreApplication.translate("MDCx", u"fanart", None))
        self.label_139.setText(QCoreApplication.translate("MDCx", u"\u6c34\u5370\u5927\u5c0f\uff1a", None))
        self.label_127.setText(QCoreApplication.translate("MDCx", u"\u6c34\u5370\u4f4d\u7f6e\uff1a", None))
        self.label_130.setText(QCoreApplication.translate("MDCx", u"Emby \u4e2d fanart \u4f5c\u4e3a\u80cc\u666f\u56fe\uff0c\u4e0d\u9700\u8981\u6dfb\u52a0\u6c34\u5370\u3002\u5176\u4ed6\u8f6f\u4ef6\u4f5c\u4e3a\u9884\u89c8\u56fe\u65f6\uff0c\u53ef\u6dfb\u52a0\u6c34\u5370", None))
        self.groupBox_36.setTitle(QCoreApplication.translate("MDCx", u"\u4e0d\u56fa\u5b9a\u4f4d\u7f6e", None))
        self.radioButton_top_left.setText(QCoreApplication.translate("MDCx", u"\u5de6\u4e0a", None))
        self.radioButton_top_right.setText(QCoreApplication.translate("MDCx", u"\u53f3\u4e0a", None))
        self.radioButton_bottom_right.setText(QCoreApplication.translate("MDCx", u"\u53f3\u4e0b", None))
        self.radioButton_bottom_left.setText(QCoreApplication.translate("MDCx", u"\u5de6\u4e0b", None))
        self.label_126.setText(QCoreApplication.translate("MDCx", u"\u9996\u4e2a\u6c34\u5370\u4f4d\u7f6e\uff1a", None))
        self.groupBox_42.setTitle(QCoreApplication.translate("MDCx", u"\u56fa\u5b9a\u4e0d\u540c\u4f4d\u7f6e", None))
        self.radioButton_top_left_sub.setText(QCoreApplication.translate("MDCx", u"\u5de6\u4e0a", None))
        self.radioButton_top_right_sub.setText(QCoreApplication.translate("MDCx", u"\u53f3\u4e0a", None))
        self.radioButton_bottom_right_sub.setText(QCoreApplication.translate("MDCx", u"\u53f3\u4e0b", None))
        self.radioButton_bottom_left_sub.setText(QCoreApplication.translate("MDCx", u"\u5de6\u4e0b", None))
        self.label_131.setText(QCoreApplication.translate("MDCx", u"\u5b57\u5e55\u6c34\u5370\u4f4d\u7f6e\uff1a", None))
        self.radioButton_top_left_mosaic.setText(QCoreApplication.translate("MDCx", u"\u5de6\u4e0a", None))
        self.radioButton_top_right_mosaic.setText(QCoreApplication.translate("MDCx", u"\u53f3\u4e0a", None))
        self.radioButton_bottom_right_mosaic.setText(QCoreApplication.translate("MDCx", u"\u53f3\u4e0b", None))
        self.radioButton_bottom_left_mosaic.setText(QCoreApplication.translate("MDCx", u"\u5de6\u4e0b", None))
        self.label_134.setText(QCoreApplication.translate("MDCx", u"\u9a6c\u8d5b\u514b\u6c34\u5370\u4f4d\u7f6e\uff1a", None))
        self.radioButton_top_left_hd.setText(QCoreApplication.translate("MDCx", u"\u5de6\u4e0a", None))
        self.radioButton_top_right_hd.setText(QCoreApplication.translate("MDCx", u"\u53f3\u4e0a", None))
        self.radioButton_bottom_right_hd.setText(QCoreApplication.translate("MDCx", u"\u53f3\u4e0b", None))
        self.radioButton_bottom_left_hd.setText(QCoreApplication.translate("MDCx", u"\u5de6\u4e0b", None))
        self.label_216.setText(QCoreApplication.translate("MDCx", u"4K/8K\u6c34\u5370\u4f4d\u7f6e\uff1a", None))
        self.groupBox_39.setTitle(QCoreApplication.translate("MDCx", u"\u56fa\u5b9a\u4e00\u4e2a\u4f4d\u7f6e", None))
        self.radioButton_top_left_corner.setText(QCoreApplication.translate("MDCx", u"\u5de6\u4e0a", None))
        self.radioButton_top_right_corner.setText(QCoreApplication.translate("MDCx", u"\u53f3\u4e0a", None))
        self.radioButton_bottom_right_corner.setText(QCoreApplication.translate("MDCx", u"\u53f3\u4e0b", None))
        self.radioButton_bottom_left_corner.setText(QCoreApplication.translate("MDCx", u"\u5de6\u4e0b", None))
        self.label_233.setText(QCoreApplication.translate("MDCx", u"\u6c34\u5370\u663e\u793a\u4f4d\u7f6e\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), QCoreApplication.translate("MDCx", u" \u6c34\u5370 ", None))
        self.groupBox_81.setTitle(QCoreApplication.translate("MDCx", u"\u5199\u5165 NFO \u7684\u5b57\u6bb5\uff1a", None))
        self.label_402.setText("")
        self.checkBox_nfo_all_actor.setText(QCoreApplication.translate("MDCx", u"\u5199\u5165\u7537\u5973\u6f14\u5458\uff08\u4e0d\u52fe\u9009\uff0c\u5219\u4ec5\u5199\u5165\u5973\u6f14\u5458\uff09", None))
        self.label_391.setText(QCoreApplication.translate("MDCx", u"\u5e74\u4efd/\u65f6\u957f/\u60f3\u770b\u4eba\u6570\uff1a", None))
        self.checkBox_tag_letters.setText(QCoreApplication.translate("MDCx", u"\u756a\u53f7\u524d\u7f00", None))
        self.checkBox_tag_actor.setText(QCoreApplication.translate("MDCx", u"\u6f14\u5458", None))
        self.checkBox_tag_definition.setText(QCoreApplication.translate("MDCx", u"\u5206\u8fa8\u7387", None))
        self.checkBox_tag_cnword.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u5b57\u5e55", None))
        self.label_413.setText("")
        self.label_396.setText(QCoreApplication.translate("MDCx", u"\u8bf7\u586b\u5199 Tagline \u683c\u5f0f\uff1a", None))
        self.lineEdit_nfo_tagline.setText(QCoreApplication.translate("MDCx", u"\u53d1\u884c\u65e5\u671f\uff1arelease", None))
        self.checkBox_nfo_sorttitle.setText(QCoreApplication.translate("MDCx", u"\u7c7b\u6807\u9898\uff08sorttitle\uff09", None))
        self.checkBox_nfo_originaltitle.setText(QCoreApplication.translate("MDCx", u"\u539f\u6807\u9898\uff08originaltitle\uff09", None))
        self.checkBox_nfo_genre.setText(QCoreApplication.translate("MDCx", u"\u98ce\u683c\uff08\u4f7f\u7528\u6807\u7b7e\u5b57\u6bb5\uff09", None))
        self.checkBox_nfo_actor_set.setText(QCoreApplication.translate("MDCx", u"\u5408\u96c6\uff08\u4f7f\u7528\u6f14\u5458\u5b57\u6bb5\uff09", None))
        self.checkBox_nfo_set.setText(QCoreApplication.translate("MDCx", u"\u5408\u96c6\uff08\u4f7f\u7528\u7cfb\u5217\u5b57\u6bb5\uff09", None))
        self.checkBox_nfo_poster.setText(QCoreApplication.translate("MDCx", u"\u5c01\u9762\uff08poster\uff09", None))
        self.checkBox_nfo_cover.setText(QCoreApplication.translate("MDCx", u"\u80cc\u666f\uff08cover\uff09", None))
        self.checkBox_nfo_trailer.setText(QCoreApplication.translate("MDCx", u"\u9884\u544a\u7247\uff08trilaer\uff09", None))
        self.checkBox_nfo_website.setText(QCoreApplication.translate("MDCx", u"\u7f51\u5740\uff08website\uff09", None))
        self.label_301.setText("")
        self.label_335.setText("")
        self.label_209.setText("")
        self.label_387.setText("")
        self.label_163.setText(QCoreApplication.translate("MDCx", u"\u6807\u9898\uff1a", None))
        self.label_388.setText(QCoreApplication.translate("MDCx", u"\u7247\u5546/\u53d1\u884c\u5546\uff1a", None))
        self.checkBox_nfo_outline.setText(QCoreApplication.translate("MDCx", u"\u7b80\u4ecb\uff08outline\uff09", None))
        self.checkBox_nfo_plot.setText(QCoreApplication.translate("MDCx", u"\u7b80\u4ecb\uff08plot\uff09", None))
        self.checkBox_nfo_originalplot.setText(QCoreApplication.translate("MDCx", u"\u539f\u7b80\u4ecb\uff08originalplot\uff09", None))
        self.label_412.setText(QCoreApplication.translate("MDCx", u"\u6807\u7b7e\u4e2d\u7cfb\u5217\u7684\u683c\u5f0f\uff1a", None))
        self.lineEdit_nfo_tag_series.setText(QCoreApplication.translate("MDCx", u"\u7cfb\u5217: series", None))
        self.label_416.setText(QCoreApplication.translate("MDCx", u"\u6807\u7b7e\u4e2d\u7247\u5546\u7684\u683c\u5f0f\uff1a", None))
        self.lineEdit_nfo_tag_studio.setText(QCoreApplication.translate("MDCx", u"\u7247\u5546: studio", None))
        self.label_394.setText("")
        self.checkBox_outline_cdata.setText(QCoreApplication.translate("MDCx", u"\u7b80\u4ecb\u4e0d\u5199\u5165 <![CDATA[*]]> \u6807\u8bb0", None))
        self.label_390.setText(QCoreApplication.translate("MDCx", u"\u8bc4\u5206\uff1a", None))
        self.checkBox_nfo_score.setText(QCoreApplication.translate("MDCx", u"\u516c\u4f17\u8bc4\u5206\uff08score\uff09", None))
        self.checkBox_nfo_criticrating.setText(QCoreApplication.translate("MDCx", u"\u5f71\u8bc4\u4eba\u8bc4\u5206\uff08criticrating\uff09", None))
        self.checkBox_nfo_studio.setText(QCoreApplication.translate("MDCx", u"\u7247\u5546\uff08studio\uff09", None))
        self.checkBox_nfo_maker.setText(QCoreApplication.translate("MDCx", u"\u7247\u5546\uff08maker\uff09", None))
        self.checkBox_nfo_publisher.setText(QCoreApplication.translate("MDCx", u"\u53d1\u884c\u5546\uff08publisher\uff09", None))
        self.checkBox_nfo_label.setText(QCoreApplication.translate("MDCx", u"\u53d1\u884c\u5546\uff08label\uff09", None))
        self.label_419.setText("")
        self.label_417.setText("")
        self.checkBox_tag_mosaic.setText(QCoreApplication.translate("MDCx", u"\u6709\u7801/\u65e0\u7801", None))
        self.checkBox_tag_series.setText(QCoreApplication.translate("MDCx", u"\u7cfb\u5217", None))
        self.checkBox_tag_studio.setText(QCoreApplication.translate("MDCx", u"\u7247\u5546", None))
        self.checkBox_tag_publisher.setText(QCoreApplication.translate("MDCx", u"\u53d1\u884c\u5546", None))
        self.checkBox_nfo_series.setText(QCoreApplication.translate("MDCx", u"\u7cfb\u5217\uff08series\uff09", None))
        self.checkBox_nfo_tag.setText(QCoreApplication.translate("MDCx", u"\u6807\u7b7e\uff08tag\uff09", None))
        self.label_384.setText(QCoreApplication.translate("MDCx", u"\u7b80\u4ecb\uff1a", None))
        self.label_208.setText(QCoreApplication.translate("MDCx", u"\u7cfb\u5217/\u6807\u7b7e\uff1a", None))
        self.label_161.setText("")
        self.label_418.setText(QCoreApplication.translate("MDCx", u"\u6807\u7b7e\u4e2d\u53d1\u884c\u7684\u683c\u5f0f\uff1a", None))
        self.lineEdit_nfo_tag_publisher.setText(QCoreApplication.translate("MDCx", u"\u53d1\u884c: publisher", None))
        self.checkBox_nfo_release.setText(QCoreApplication.translate("MDCx", u"\u53d1\u884c\u65e5\u671f\uff08release\uff09", None))
        self.checkBox_nfo_relasedate.setText(QCoreApplication.translate("MDCx", u"\u53d1\u884c\u65e5\u671f\uff08releasedate\uff09", None))
        self.checkBox_nfo_premiered.setText(QCoreApplication.translate("MDCx", u"\u53d1\u884c\u65e5\u671f\uff08premiered\uff09", None))
        self.label_334.setText(QCoreApplication.translate("MDCx", u"\u98ce\u683c/\u5408\u96c6\uff1a", None))
        self.label_385.setText(QCoreApplication.translate("MDCx", u"\u53d1\u884c\u65e5\u671f\uff1a", None))
        self.label_392.setText(QCoreApplication.translate("MDCx", u"\u56fd\u5bb6/\u5206\u7ea7\uff1a", None))
        self.checkBox_nfo_year.setText(QCoreApplication.translate("MDCx", u"\u5e74\u4efd\uff08year\uff09", None))
        self.checkBox_nfo_runtime.setText(QCoreApplication.translate("MDCx", u"\u65f6\u957f\uff08runtime\uff09", None))
        self.checkBox_nfo_wanted.setText(QCoreApplication.translate("MDCx", u"\u60f3\u770b\u4eba\u6570\uff08votes\uff09", None))
        self.label_403.setText("")
        self.label_393.setText("")
        self.checkBox_nfo_title_cd.setText(QCoreApplication.translate("MDCx", u"\u6807\u9898\u672b\u5c3e\u5199\u5165\u5206\u96c6\u4fe1\u606f", None))
        self.checkBox_nfo_country.setText(QCoreApplication.translate("MDCx", u"\u56fd\u5bb6\uff08country\uff09", None))
        self.checkBox_nfo_mpaa.setText(QCoreApplication.translate("MDCx", u"\u5206\u7ea7\u4fe1\u606f\uff08mpaa\uff09", None))
        self.checkBox_nfo_customrating.setText(QCoreApplication.translate("MDCx", u"\u81ea\u5b9a\u4e49\u5206\u7ea7\uff08customrating\uff09", None))
        self.label_386.setText(QCoreApplication.translate("MDCx", u"\u6f14\u5458/\u5bfc\u6f14\uff1a", None))
        self.checkBox_nfo_actor.setText(QCoreApplication.translate("MDCx", u"\u6f14\u5458\uff08actor\uff09", None))
        self.checkBox_nfo_director.setText(QCoreApplication.translate("MDCx", u"\u5bfc\u6f14\uff08director\uff09", None))
        self.label_395.setText(QCoreApplication.translate("MDCx", u"\u8bf7\u52fe\u9009\u5199\u5165\u6807\u7b7e\u7684\u4fe1\u606f\uff1a", None))
        self.label_150.setText(QCoreApplication.translate("MDCx", u"\u5c01\u9762/\u80cc\u666f/\u9884\u544a\u7247\uff1a", None))
        self.label_428.setText(QCoreApplication.translate("MDCx", u"\u6ce8\u610f\uff1a\u5982\u679c\u9700\u8981\u7e41\u4f53\uff0c\u8bf7\u5230\u300c\u8bbe\u7f6e\u300d-\u300c\u7ffb\u8bd1\u300d-\u300c\u6807\u7b7e\u300d\uff0c\u52fe\u9009\u4e3a\u7e41\u4f53\uff01", None))
        self.label_429.setText("")
        self.label_389.setText(QCoreApplication.translate("MDCx", u"\u6ce8\uff1a\u540c\u4e00\u5b57\u6bb5\u591a\u4e2a\u540d\u79f0\u53ef\u4ee5\u517c\u5bb9\u66f4\u591a\u7c7b\u578b\u7248\u672c\u7684\u5a92\u4f53\u5e93", None))
        self.pushButton_field_tips_nfo.setText(QCoreApplication.translate("MDCx", u"\u5b57\u6bb5\u8bf4\u660e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MDCx", u" NFO ", None))
        self.groupBox_43.setTitle(QCoreApplication.translate("MDCx", u"Emby/Jellyfin \u8bbe\u7f6e", None))
        self.label_104.setText(QCoreApplication.translate("MDCx", u"\u670d\u52a1\u5668\u5730\u5740\uff1a", None))
        self.label_105.setText(QCoreApplication.translate("MDCx", u"API \u5bc6\u94a5\u521b\u5efa\u65b9\u6cd5\uff1a\u63a7\u5236\u53f0->\u9ad8\u7ea7->API \u5bc6\u94a5->\u6dfb\u52a0\uff08APP \u540d\u79f0\u4efb\u610f\uff09", None))
        self.comboBox_pic_actor.setItemText(0, QCoreApplication.translate("MDCx", u"1 \u6240\u6709\u6f14\u5458", None))
        self.comboBox_pic_actor.setItemText(1, QCoreApplication.translate("MDCx", u"2 \u6709\u4fe1\u606f\uff0c\u6709\u5934\u50cf\u7684\u6f14\u5458", None))
        self.comboBox_pic_actor.setItemText(2, QCoreApplication.translate("MDCx", u"3 \u6709\u4fe1\u606f\uff0c\u6ca1\u5934\u50cf\u7684\u6f14\u5458", None))
        self.comboBox_pic_actor.setItemText(3, QCoreApplication.translate("MDCx", u"4 \u6ca1\u4fe1\u606f\uff0c\u6709\u5934\u50cf\u7684\u6f14\u5458", None))
        self.comboBox_pic_actor.setItemText(4, QCoreApplication.translate("MDCx", u"5 \u6ca1\u4fe1\u606f\uff0c\u6ca1\u5934\u50cf\u7684\u6f14\u5458", None))
        self.comboBox_pic_actor.setItemText(5, QCoreApplication.translate("MDCx", u"6 \u6709\u4fe1\u606f\u7684\u6f14\u5458", None))
        self.comboBox_pic_actor.setItemText(6, QCoreApplication.translate("MDCx", u"7 \u6ca1\u4fe1\u606f\u7684\u6f14\u5458", None))
        self.comboBox_pic_actor.setItemText(7, QCoreApplication.translate("MDCx", u"8 \u6709\u5934\u50cf\u7684\u6f14\u5458", None))
        self.comboBox_pic_actor.setItemText(8, QCoreApplication.translate("MDCx", u"9 \u6ca1\u5934\u50cf\u7684\u6f14\u5458", None))

        self.pushButton_show_pic_actor.setText(QCoreApplication.translate("MDCx", u"\u67e5\u770b", None))
        self.radioButton_server_emby.setText(QCoreApplication.translate("MDCx", u"Emby", None))
        self.radioButton_server_jellyfin.setText(QCoreApplication.translate("MDCx", u"Jellyfin", None))
        self.label_298.setText(QCoreApplication.translate("MDCx", u"\u67e5\u770b\u4fe1\u606f\uff1a", None))
        self.label_121.setText(QCoreApplication.translate("MDCx", u"\u6307\u4f60\u7684 Emby/Jellyfin \u670d\u52a1\u5668\u5730\u5740\uff0c\u6bd4\u5982\uff1ahttp://192.168.1.5:8096", None))
        self.label_306.setText(QCoreApplication.translate("MDCx", u"\u670d\u52a1\u5668\u7c7b\u578b\uff1a", None))
        self.label_108.setText(QCoreApplication.translate("MDCx", u"\u7528\u6237 ID\uff1a", None))
        self.label_107.setText(QCoreApplication.translate("MDCx", u"API \u5bc6\u94a5\uff1a", None))
        self.label_109.setText(QCoreApplication.translate("MDCx", u"\u5982\u679c\u8bbe\u7f6e\uff0c\u5c06\u4ec5\u83b7\u53d6\u6307\u5b9a Emby/Jellyfin \u7528\u6237\u5a92\u4f53\u5e93\u4e2d\u7684\u6f14\u5458", None))
        self.groupBox_41.setTitle(QCoreApplication.translate("MDCx", u"\u8865\u5168 Emby/Jellyfin \u6f14\u5458\u5934\u50cf", None))
        self.pushButton_add_actor_pic.setText(QCoreApplication.translate("MDCx", u"\u5f00\u59cb\u8865\u5168", None))
        self.label_297.setText(QCoreApplication.translate("MDCx", u"\u4f7f\u7528\u7f51\u7edc\u5934\u50cf\u5e93\u6216\u672c\u5730\u5934\u50cf\u5e93\uff0c\u8865\u5168 Emby/Jellyfin \u6f14\u5458\u5934\u50cf\u3002", None))
        self.checkBox_actor_photo_auto.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7ed3\u675f\u540e\u81ea\u52a8\u8865\u5168\u6f14\u5458\u5934\u50cf", None))
        self.radioButton_actor_photo_all.setText(QCoreApplication.translate("MDCx", u"\u6240\u6709\u5973\u4f18", None))
        self.radioButton_actor_photo_miss.setText(QCoreApplication.translate("MDCx", u"\u4ec5\u7f3a\u5c11\u5934\u50cf\u7684\u5973\u4f18", None))
        self.label_296.setText(QCoreApplication.translate("MDCx", u"\u8865\u5168\u8303\u56f4\uff1a", None))
        self.label_77.setText(QCoreApplication.translate("MDCx", u"\u4e0b\u8f7d\u5934\u50cf\u5305\u89e3\u538b\uff0c\u586b\u5199\u5934\u50cf\u56fe\u7247\u76ee\u5f55\u7684\u8def\u5f84", None))
        self.label_293.setText(QCoreApplication.translate("MDCx", u"\u5934\u50cf\u6765\u6e90\uff1a", None))
        self.label_101.setText(QCoreApplication.translate("MDCx", u"\u672c\u5730\u5934\u50cf\u5e93\uff1a", None))
        self.checkBox_actor_photo_ne_backdrop.setText(QCoreApplication.translate("MDCx", u"\u4f7f\u7528 Graphis \u80cc\u666f", None))
        self.checkBox_actor_photo_ne_face.setText(QCoreApplication.translate("MDCx", u"\u4f7f\u7528 Graphis \u5934\u50cf", None))
        self.checkBox_actor_photo_ne_new.setText(QCoreApplication.translate("MDCx", u"\u8bf7\u6c42 Graphis \u6700\u65b0\u56fe\u7247", None))
        self.label_327.setText("")
        self.radioButton_actor_photo_net.setText(QCoreApplication.translate("MDCx", u"\u7f51\u7edc\u5934\u50cf\u5e93\uff08Gfriends\uff09", None))
        self.radioButton_actor_photo_local.setText(QCoreApplication.translate("MDCx", u"\u672c\u5730\u5934\u50cf\u5e93", None))
        self.label_download_actor_zip.setText(QCoreApplication.translate("MDCx", u"\u70b9\u51fb\u4e0b\u8f7d\u5934\u50cf\u5305", None))
        self.pushButton_select_actor_photo_folder.setText(QCoreApplication.translate("MDCx", u"\u9009\u62e9\u76ee\u5f55", None))
        self.label_303.setText(QCoreApplication.translate("MDCx", u"\u7f51\u7edc\u5934\u50cf\u5e93\uff1a", None))
        self.label_123.setText(QCoreApplication.translate("MDCx", u"\u652f\u6301\u4f18\u5148\u4f7f\u7528 Graphis.ne.jp \u7684\u56fe\u7247\u4f5c\u4e3a\u6f14\u5458\u5934\u50cf\u548c\u6f14\u5458\u80cc\u666f\uff1b\n"
"Graphis.ne.jp \u63d0\u4f9b\u4e86\u6f14\u5458\u4e0d\u540c\u65f6\u671f\u7684\u56fe\u7247\uff0c\u9ed8\u8ba4\u8bf7\u6c42\u65e9\u671f\u7684\u56fe\u7247\u3002", None))
        self.label_159.setText(QCoreApplication.translate("MDCx", u"\u5efa\u8bae Fork \u8be5\u9879\u76ee\u5230\u4f60\u7684 Github\uff0c\u5f53\u9879\u76ee\u6545\u969c\u65f6\uff0c\u53ef\u586b\u5199\u4f60 Fork \u540e\u7684\u9879\u76ee\u5730\u5740", None))
        self.groupBox_64.setTitle(QCoreApplication.translate("MDCx", u"\u8865\u5168 Emby/Jellyfin \u6f14\u5458\u4fe1\u606f", None))
        self.radioButton_actor_info_zh_cn.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u7b80\u4f53", None))
        self.radioButton_actor_info_zh_tw.setText(QCoreApplication.translate("MDCx", u"\u4e2d\u6587\u7e41\u4f53", None))
        self.radioButton_actor_info_ja.setText(QCoreApplication.translate("MDCx", u"\u65e5\u8bed", None))
        self.radioButton_actor_info_all_2.setText(QCoreApplication.translate("MDCx", u"\u6240\u6709\u5973\u4f18", None))
        self.radioButton_actor_info_miss_2.setText(QCoreApplication.translate("MDCx", u"\u4ec5\u7f3a\u5c11\u4fe1\u606f\u7684\u5973\u4f18", None))
        self.label_431.setText(QCoreApplication.translate("MDCx", u"\u6f14\u5458\u4fe1\u606f\u6570\u636e\u5e93\uff1a", None))
        self.pushButton_select_actor_info_db.setText(QCoreApplication.translate("MDCx", u"\u9009\u62e9\u6587\u4ef6", None))
        self.radioButton_actor_info_all_3.setText(QCoreApplication.translate("MDCx", u"\u6240\u6709\u5973\u4f18", None))
        self.radioButton_actor_info_miss_3.setText(QCoreApplication.translate("MDCx", u"\u4ec5\u7f3a\u5c11\u4fe1\u606f\u7684\u5973\u4f18", None))
        self.checkBox_actor_db.setText(QCoreApplication.translate("MDCx", u"\u4f7f\u7528\u6570\u636e\u5e93\u8865\u5168\u6f14\u5458\u4fe1\u606f", None))
        self.label_download_actor_db.setText(QCoreApplication.translate("MDCx", u"\u70b9\u51fb\u4e0b\u8f7d\u6f14\u5458\u6570\u636e\u5e93", None))
        self.label_291.setText(QCoreApplication.translate("MDCx", u"\u8865\u5168\u8bed\u8a00\uff1a", None))
        self.label_280.setText("")
        self.checkBox_actor_info_translate.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u5b58\u5728\u4e2d\u6587\u65f6\uff0c\u7ffb\u8bd1\u65e5\u8bed\u4e3a\u4e2d\u6587", None))
        self.label_106.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u52fe\u9009\u5219\u65e0\u4e2d\u6587\u65f6\u4f7f\u7528\u65e5\u8bed", None))
        self.pushButton_add_actor_info.setText(QCoreApplication.translate("MDCx", u"\u5f00\u59cb\u8865\u5168", None))
        self.label_295.setText(QCoreApplication.translate("MDCx", u"\u4f7f\u7528\u7ef4\u57fa\u767e\u79d1\u8865\u5168 Emby/Jellyfin \u6f14\u5458\u4fe1\u606f\uff0c\u5305\u62ec\uff1a\u6f14\u5458\u4ecb\u7ecd\u3001\u8d44\u6599\u3001\u7b80\u5386\u3001\u751f\u5e73\u3001Imdb\u4e3b\u9875\u7b49\u3002", None))
        self.radioButton_actor_info_all.setText(QCoreApplication.translate("MDCx", u"\u6240\u6709\u5973\u4f18", None))
        self.radioButton_actor_info_miss.setText(QCoreApplication.translate("MDCx", u"\u4ec5\u7f3a\u5c11\u4fe1\u606f\u7684\u5973\u4f18", None))
        self.label_299.setText(QCoreApplication.translate("MDCx", u"\u8865\u5168\u8303\u56f4\uff1a", None))
        self.checkBox_actor_info_photo.setText(QCoreApplication.translate("MDCx", u"\u8865\u5168\u5b8c\u6210\u540e\u81ea\u52a8\u8865\u5168\u6f14\u5458\u5934\u50cf", None))
        self.groupBox_68.setTitle(QCoreApplication.translate("MDCx", u"\u8865\u5168 Kodi/Plex/Jvedio \u6f14\u5458\u5934\u50cf", None))
        self.pushButton_add_actor_pic_kodi.setText(QCoreApplication.translate("MDCx", u"\u5f00\u59cb\u8865\u5168", None))
        self.label_414.setText(QCoreApplication.translate("MDCx", u"\u5c06\u4e3a\u5f85\u522e\u524a\u76ee\u5f55\u7684\u6bcf\u4e2a\u89c6\u9891\u5728\u540c\u76ee\u5f55\u521b\u5efa\u4e00\u4e2a .actors \u6587\u4ef6\u5939\uff0c\u5e76\u5c06\u8be5\u89c6\u9891\u7684\u6f14\u5458\u56fe\u7247\u653e\u5728\u8be5\u6587\u4ef6\u5939\u4e2d", None))
        self.checkBox_actor_pic_replace.setText(QCoreApplication.translate("MDCx", u"\u8986\u76d6\u5df2\u5b58\u5728\u7684\u6f14\u5458\u56fe\u7247", None))
        self.label_415.setText(QCoreApplication.translate("MDCx", u"\u56fe\u7247\u5df2\u5b58\u5728\u65f6\uff1a", None))
        self.pushButton_del_actor_folder.setText(QCoreApplication.translate("MDCx", u"\u6e05\u9664\u6240\u6709 .actors \u6587\u4ef6\u5939", None))
        self.checkBox_actor_photo_kodi.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7ed3\u675f\u540e\u81ea\u52a8\u521b\u5efa", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MDCx", u" \u6f14\u5458 ", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MDCx", u"Cookie\u8bbe\u7f6e", None))
#if QT_CONFIG(accessibility)
        self.plainTextEdit_cookie_javbus.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.plainTextEdit_cookie_javbus.setPlaceholderText(QCoreApplication.translate("MDCx", u"\u7f8e\u56fd\u8282\u70b9\u9700\u8981\u586b\u5199\uff0c\u5176\u4ed6\u8282\u70b9\u4e00\u822c\u4e0d\u9700\u8981\u586b\u5199\uff0c\u9664\u975e\u63d0\u793a\u9700\u8981\u586b\u5199\u3002", None))
        self.plainTextEdit_cookie_javdb.setPlaceholderText(QCoreApplication.translate("MDCx", u"\u522e\u524aFC2\u9700\u8981\u586b\u5199", None))
        self.pushButton_check_javdb_cookie.setText(QCoreApplication.translate("MDCx", u"\u68c0\u67e5cookie", None))
        self.label_javdb_cookie_result.setText("")
        self.label_425.setText(QCoreApplication.translate("MDCx", u"javbus\uff1a\n"
"\uff08\u767b\u5f55\u72b6\u6001\uff09", None))
        self.label_45.setText(QCoreApplication.translate("MDCx", u"javdb\uff1a\n"
"\uff08\u767b\u5f55\u72b6\u6001\uff09", None))
        self.pushButton_check_javbus_cookie.setText(QCoreApplication.translate("MDCx", u"\u68c0\u67e5cookie", None))
        self.label_javbus_cookie_result.setText("")
        self.label_75.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:20px'>Cookie \u83b7\u53d6\u65b9\u6cd5\uff1a<br>\n"
"1\uff0c\u4f7f\u7528 Chrome \u6253\u5f00\u76ee\u6807\u7f51\u7ad9\u5e76\u767b\u5f55\uff0c\u5728\u9875\u9762\u7a7a\u767d\u4f4d\u7f6e\u70b9\u51fb\u9f20\u6807\u53f3\u952e\uff0c\u9009\u62e9 \u300c\u68c0\u67e5\u300d \uff1b<br>\n"
"2\uff0c\u53f3\u4fa7\u5f39\u7a97\u9876\u90e8\u9009\u62e9\uff1a\u300c\u7f51\u7edc\u300d -> \u300c\u5168\u90e8\u300d\uff0c\u7136\u540e\u5237\u65b0\u5f53\u524d\u9875\u9762\uff1b<br>\n"
"3\uff0c\u70b9\u51fb\u300c\u540d\u79f0\u300d\u680f\u65b0\u52a0\u8f7d\u51fa\u6765\u7684\u7b2c\u4e00\u4e2a\u5185\u5bb9 -> \u300c\u6807\u5934\u300d -> \u300c\u8bf7\u6c42\u8868\u5934\u300d -> \u300cCookie\u300d\uff1b<br>\n"
"4\uff0c\u590d\u5236 Cookie \u5bf9\u5e94\u7684\u5168\u90e8\u503c\u586b\u5165\u4e0a\u9762\u8f93\u5165\u6846\u3002\uff08\u4e0d\u8981\u76f4\u63a5\u53f3\u952e\u70b9\u300c\u590d\u5236\u503c\u300d\uff01\uff01\uff01\uff01\n"
"\u4e00\u5b9a\u8981\u5148\u7528\u9f20\u6807\u300c\u624b\u52a8\u6846\u9009\u300d\u8981\u590d\u5236\u7684\u5168"
                        "\u90e8\u6587\u5b57\uff0c\u7136\u540e\u518d\u53f3\u952e\u70b9\u300c\u590d\u5236\u300d\uff01\uff01\uff01\u4e0d\u662f\u300c\u590d\u5236\u503c\u300d\uff01\uff01\uff01\uff01\uff01\uff01\uff09<br>\n"
"\uff08\u6ce8\u610f\uff1aCookie \u5b58\u5728\u6709\u6548\u671f\uff0c\u8fc7\u671f\u65e0\u6548\u65f6\u8bf7\u91cd\u65b0\u83b7\u53d6\u3002\uff09</p>", None))
        self.label_get_cookie_url.setText(QCoreApplication.translate("MDCx", u"https://tieba.baidu.com/p/5492736764", None))
        self.label_7.setText(QCoreApplication.translate("MDCx", u"\u6f14\u793a\u52a8\u753b\uff1a", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("MDCx", u"\u4ee3\u7406\u8bbe\u7f6e", None))
        self.checkBox_net_ipv4_only.setText(QCoreApplication.translate("MDCx", u"\u5f3a\u5236\u4f7f\u7528 IPv4 \u8bf7\u6c42\u6570\u636e", None))
        self.label_64.setText(QCoreApplication.translate("MDCx", u"IP+\u7aef\u53e3\u53f7\uff1a", None))
        self.label_65.setText(QCoreApplication.translate("MDCx", u"\u91cd\u8bd5\u6b21\u6570\uff1a", None))
        self.label_103.setText(QCoreApplication.translate("MDCx", u"\u5e26\u7528\u6237\u540d\u548c\u5bc6\u7801\u65f6\uff0c\u586b\u5199\u683c\u5f0f: username:password@ip:port", None))
        self.radioButton_proxy_http.setText(QCoreApplication.translate("MDCx", u"http", None))
        self.radioButton_proxy_socks5.setText(QCoreApplication.translate("MDCx", u"socks5", None))
        self.radioButton_proxy_nouse.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u4f7f\u7528", None))
        self.label_410.setText(QCoreApplication.translate("MDCx", u"IPv4 only\uff1a", None))
        self.label_70.setText(QCoreApplication.translate("MDCx", u"\u4ee3\u7406\uff1a", None))
        self.label_73.setText(QCoreApplication.translate("MDCx", u"\u8d85\u65f6\u65f6\u95f4\uff1a", None))
        self.label_411.setText(QCoreApplication.translate("MDCx", u"\u4e00\u4e9b\u7f51\u7ad9\uff08Javbus\u3001Amazon\uff09\u4f7f\u7528 IPv6 \u8bf7\u6c42\u4f1a\u5931\u8d25\uff0c\u5efa\u8bae\u4f7f\u7528 IPv4\uff08\u91cd\u542f\u540e\u751f\u6548\uff09", None))
        self.groupBox_44.setTitle(QCoreApplication.translate("MDCx", u"\u7f51\u5740\u8bbe\u7f6e", None))
        self.label_110.setText(QCoreApplication.translate("MDCx", u"<p style='line-height:15px'>\u81ea\u5b9a\u4e49\u522e\u524a\u6307\u5b9a\u7f51\u7ad9\u65f6\u4f7f\u7528\u7684\u7f51\u5740\uff0c\u76ee\u524d\u652f\u6301\u4ee5\u4e0b\u7f51\u7ad9\uff1a<br>\n"
"    &nbsp;&nbsp;&nbsp;&nbsp;airavcc  avsex  hdouban  iqqtv  lulubar  mdtv  javbus  javdb  javlibrary* <br>\n"
"    &nbsp;&nbsp;&nbsp;&nbsp;* \u914d\u7f6e\u540e\u5c06\u76f4\u8fde\u8bbf\u95ee<br>\n"
"<br>\u6b22\u8fce pr \u5b9e\u73b0\u5176\u5b83\u7f51\u7ad9\u7684\u81ea\u5b9a\u4e49\u7f51\u5740\u529f\u80fd\uff0c\u53c2\u8003\uff1a<a href=\"https://github.com/sqzw-x/mdcx/wiki/\u81ea\u5b9a\u4e49\u7f51\u5740\"><span style=\"color:#094fd1;\" > Github wiki<span/><a/>\n"
"</p>", None))
        self.label_324.setText(QCoreApplication.translate("MDCx", u"\u26a0\ufe0f \u4fee\u6539\u540e\u5148\u70b9\u51fb\u4fdd\u5b58\u518d\u5207\u6362\uff0c\u5426\u5219\u4fee\u6539\u5c06\u4e22\u5931", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MDCx", u"API Token", None))
        self.label_355.setText(QCoreApplication.translate("MDCx", u"ThePornDB\uff1a", None))
        self.label_356.setText(QCoreApplication.translate("MDCx", u"<html><head/><body><p><a href=\"https://theporndb.net/\"><span style=\" text-decoration: underline; color:#094fd1;\">https://theporndb.net/</span></a> \u6ce8\u518c\u767b\u5f55\u540e\uff0c\u70b9\u5934\u50cf - API Tokens - CREATE\u3002\u590d\u5236\u751f\u6210\u7684 API Token \u586b\u5165\u6b64\u5904\u3002</p></body></html>", None))
        self.checkBox_theporndb_hash.setText(QCoreApplication.translate("MDCx", u"\u4e0d\u4f7f\u7528Hash\u503c\u5339\u914d\u6570\u636e", None))
        self.label_422.setText(QCoreApplication.translate("MDCx", u"<html><head/><body><p>\u8be5\u7f51\u7ad9\u7684Hash\u503c\u5339\u914d\u7ed3\u679c\u53ef\u80fd\u9519\u8bef</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), QCoreApplication.translate("MDCx", u" \u7f51\u7edc ", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MDCx", u"\u4fdd\u5b58\u65e5\u5fd7", None))
        self.radioButton_log_on.setText(QCoreApplication.translate("MDCx", u"\u5f00", None))
        self.radioButton_log_off.setText(QCoreApplication.translate("MDCx", u"\u5173", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MDCx", u"\u8c03\u8bd5\u6a21\u5f0f\uff08\u65e5\u5fd7\u9875\u9762\uff09", None))
        self.checkBox_show_web_log.setText(QCoreApplication.translate("MDCx", u"\u663e\u793a\u522e\u524a\u8fc7\u7a0b\u4fe1\u606f", None))
        self.checkBox_show_from_log.setText(QCoreApplication.translate("MDCx", u"\u663e\u793a\u5b57\u6bb5\u6765\u6e90\u4fe1\u606f", None))
        self.checkBox_show_data_log.setText(QCoreApplication.translate("MDCx", u"\u663e\u793a\u5b57\u6bb5\u5185\u5bb9\u4fe1\u606f", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MDCx", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.radioButton_update_on.setText(QCoreApplication.translate("MDCx", u"\u5f00", None))
        self.radioButton_update_off.setText(QCoreApplication.translate("MDCx", u"\u5173", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MDCx", u"\u9ad8\u7ea7\u529f\u80fd", None))
        self.checkBox_hide_window_title.setText(QCoreApplication.translate("MDCx", u"\u9690\u85cf\u8fb9\u6846\uff08\u7f8e\u89c2\u6837\u5f0f\uff09", None))
        self.checkBox_dark_mode.setText(QCoreApplication.translate("MDCx", u"\u6697\u9ed1\u6a21\u5f0f", None))
        self.checkBox_hide_dock_icon.setText(QCoreApplication.translate("MDCx", u"\u9690\u85cf Dock \u56fe\u6807\uff08Mac\uff09", None))
        self.label_42.setText(QCoreApplication.translate("MDCx", u"\u4fdd\u5b58\u540e\u91cd\u542f\u8f6f\u4ef6\u751f\u6548    ", None))
        self.checkBox_hide_menu_icon.setText(QCoreApplication.translate("MDCx", u"\u9690\u85cf\u83dc\u5355\u680f\u56fe\u6807\uff08Mac\uff09", None))
        self.label_321.setText(QCoreApplication.translate("MDCx", u"\u95f4\u6b47\u522e\u524a\uff1a", None))
        self.checkBox_auto_start.setText(QCoreApplication.translate("MDCx", u"\u542f\u52a8\u8f6f\u4ef6\u540e\u81ea\u52a8\u5f00\u59cb\u522e\u524a", None))
        self.checkBox_auto_exit.setText(QCoreApplication.translate("MDCx", u"\u522e\u524a\u7ed3\u675f\u540e\u81ea\u52a8\u9000\u51fa\u8f6f\u4ef6", None))
        self.checkBox_show_dialog_exit.setText(QCoreApplication.translate("MDCx", u"\u9000\u51fa\u8f6f\u4ef6\u65f6", None))
        self.checkBox_show_dialog_stop_scrape.setText(QCoreApplication.translate("MDCx", u"\u505c\u6b62\u522e\u524a\u65f6", None))
        self.checkBox_timed_scrape.setText(QCoreApplication.translate("MDCx", u"\u6bcf\u9694", None))
        self.label_84.setText(QCoreApplication.translate("MDCx", u"\uff08\u65f6:\u5206:\u79d2\uff09\uff0c\u81ea\u52a8\u5f00\u59cb\u522e\u524a\uff08\u8bfb\u53d6\u914d\u7f6e\u65f6\u5f00\u59cb\u8ba1\u65f6\uff09", None))
        self.label_308.setText(QCoreApplication.translate("MDCx", u"\u81ea\u52a8\u4efb\u52a1\uff1a", None))
        self.label_309.setText(QCoreApplication.translate("MDCx", u"\u81ea\u52a8\u522e\u524a\uff1a", None))
        self.label_277.setText(QCoreApplication.translate("MDCx", u"\u5f39\u7a97\u786e\u8ba4\uff1a", None))
        self.pushButton_select_config_folder.setText(QCoreApplication.translate("MDCx", u"\u9009\u62e9\u76ee\u5f55", None))
        self.checkBox_remain_task.setText(QCoreApplication.translate("MDCx", u"\u8bb0\u4f4f\u672a\u5b8c\u6210\u7684\u522e\u524a\u4efb\u52a1\uff0c\u5373\u4f7f\u9000\u51fa\u6216\u4e2d\u6b62\uff0c\u4e0b\u6b21\u4ecd\u53ef\u7ee7\u7eed\u522e\u524a\u672a\u5b8c\u6210\u4efb\u52a1", None))
        self.label_279.setText(QCoreApplication.translate("MDCx", u"\u4fdd\u7559\u4efb\u52a1\uff1a", None))
        self.label_40.setText(QCoreApplication.translate("MDCx", u"\u5c06\u8bfb\u53d6\u8be5\u76ee\u5f55\u4e2d\u7684\u914d\u7f6e\u6587\u4ef6\u3001\u6620\u5c04\u8868\u3001\u6c34\u5370\u56fe\u7247\u3001\u6f14\u5458\u5934\u50cf\u7b49\u6570\u636e\uff0c\u4fee\u6539\u540e\u91cd\u542f\u7a0b\u5e8f\u65b9\u53ef\u751f\u6548", None))
        self.checkBox_dialog_qt.setText(QCoreApplication.translate("MDCx", u"\u4f7f\u7528 QT \u9009\u62e9\u5bf9\u8bdd\u6846", None))
        self.label_421.setText(QCoreApplication.translate("MDCx", u"\u76ee\u5f55\u4e2d\u7684\u6587\u4ef6\u8f83\u591a\u65f6\uff0c\u53ef\u4ee5\u52fe\u9009\u6b64\u9879\u4ee5\u63d0\u9ad8\u6253\u5f00\u901f\u5ea6", None))
        self.label_314.setText(QCoreApplication.translate("MDCx", u"\u9690\u85cf\u56fe\u6807\uff1a", None))
        self.label_243.setText(QCoreApplication.translate("MDCx", u"\u914d\u7f6e\u6587\u4ef6\u76ee\u5f55\uff1a", None))
        self.radioButton_hide_close.setText(QCoreApplication.translate("MDCx", u"\u70b9\u5173\u95ed\u6309\u94ae", None))
        self.radioButton_hide_mini.setText(QCoreApplication.translate("MDCx", u"\u70b9\u6700\u5c0f\u5316\u6309\u94ae", None))
        self.radioButton_hide_none.setText(QCoreApplication.translate("MDCx", u"\u65e0", None))
        self.checkBox_rest_scrape.setText(QCoreApplication.translate("MDCx", u"\u8fde\u7eed\u522e\u524a", None))
        self.label_52.setText(QCoreApplication.translate("MDCx", u"\u4e2a\u6587\u4ef6\u540e\uff0c\u81ea\u52a8\u4f11\u606f", None))
        self.label_71.setText(QCoreApplication.translate("MDCx", u"\uff08\u65f6:\u5206:\u79d2\uff09", None))
        self.label_313.setText(QCoreApplication.translate("MDCx", u"\u9690\u85cf\u7a97\u53e3\uff1a", None))
        self.label_246.setText(QCoreApplication.translate("MDCx", u"\u754c\u9762\u5916\u89c2\uff1a", None))
        self.label_420.setText(QCoreApplication.translate("MDCx", u"\u9009\u62e9\u5bf9\u8bdd\u6846\uff1a", None))
        self.label_426.setText(QCoreApplication.translate("MDCx", u"\u9ad8\u5206\u5c4f\u7f29\u653e\uff1a", None))
        self.checkBox_highdpi_passthrough.setText(QCoreApplication.translate("MDCx", u"\u975e\u6574\u6570\u500d\u7f29\u653e", None))
        self.label_427.setText(QCoreApplication.translate("MDCx", u"\u4fdd\u5b58\u540e\u91cd\u542f\u8f6f\u4ef6\u751f\u6548\uff0c\u53ef\u80fd\u4f1a\u6709\u70b9\u6a21\u7cca", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), QCoreApplication.translate("MDCx", u" \u9ad8\u7ea7 ", None))
        self.label_config.setText("")
        self.pushButton_init_config.setText(QCoreApplication.translate("MDCx", u"\u6062\u590d\u9ed8\u8ba4", None))
        self.pushButton_save_config.setText(QCoreApplication.translate("MDCx", u"\u4fdd\u5b58", None))
        self.label_241.setText(QCoreApplication.translate("MDCx", u"\u5f53\u524d\u914d\u7f6e\uff1a", None))
        self.pushButton_save_new_config.setText(QCoreApplication.translate("MDCx", u"\u53e6\u5b58\u4e3a", None))
        self.textBrowser_show_success_list.setHtml(QCoreApplication.translate("MDCx", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        </p></body></html>", None))
        self.pushButton_success_list_close.setText(QCoreApplication.translate("MDCx", u"\u5173\u95ed", None))
        self.pushButton_success_list_clear.setText(QCoreApplication.translate("MDCx", u"\u6e05\u7a7a\u5217\u8868", None))
        self.pushButton_success_list_save.setText(QCoreApplication.translate("MDCx", u"\u4fdd\u5b58", None))
        self.label_success_title.setText(QCoreApplication.translate("MDCx", u"\u5df2\u522e\u524a\u6210\u529f\u6587\u4ef6\u5217\u8868", None))
        self.textBrowser_show_tips.setHtml(QCoreApplication.translate("MDCx", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        </p></body></html>", None))
        self.pushButton_show_tips_close.setText(QCoreApplication.translate("MDCx", u"\u5173\u95ed", None))
        self.label_show_tips_title.setText(QCoreApplication.translate("MDCx", u"\u8bf4\u660e", None))
        self.textBrowser_about.setHtml(QCoreApplication.translate("MDCx", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">\u00b7 Movie_Data_Capture \u9879\u76ee\u5730\u5740\uff1ahttps://github.com/yoshiko2/Movie_Data_Capture</span>           </p>\n"
"<p style=\" margin-top:0px; marg"
                        "in-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">\u00b7 AVDC-GUI \u9879\u76ee\u5730\u5740\uff1ahttps://github.com/moyy996/AVDC</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">\u00b7 MDCx-docker \u9879\u76ee\u5730\u5740\uff1ahttps://github.com/northsea4/mdcx-docker</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">\u4f7f\u7528\u8bf4\u660e \uff08\u5185\u5bb9\u6765"
                        "\u81ea AVDC-GUI \uff1ahttps://github.com/moyy996/AVDC \uff09</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">\u76ee\u5f55</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">\u4e00\u3001\u529f\u80fd\u7b80\u4ecb</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">\u4e8c\u3001\u9879\u76ee\u7b80\u4ecb</span>     "
                        "      </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">\u4e09\u3001\u5e38\u89c1\u756a\u53f7\u547d\u540d\u53c2\u8003</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">\u56db\u3001\u8bbe\u7f6e\u8bf4\u660e</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> </span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'"
                        "; font-size:13pt;\">\u4e00\u3001\u529f\u80fd\u7b80\u4ecb</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">           \u65e5\u672c\u7535\u5f71\u5143\u6570\u636e\u6293\u53d6\u5de5\u5177/\u522e\u524a\u5668\uff0c\u914d\u5408\u672c\u5730\u5f71\u7247\u7ba1\u7406\u8f6f\u4ef6EMBY,KODI\uff0cPLEX\u7b49\u7ba1\u7406\u672c\u5730\u5f71\u7247\uff0c\u8be5\u8f6f\u4ef6\u8d77\u5230\u5206\u7c7b\u4e0e\u5143\u6570\u636e\u6293\u53d6\u4f5c\u7528\uff0c\u5229\u7528\u5143\u6570\u636e\u4fe1\u606f\u6765\u5206\u7c7b\uff0c\u4f9b\u672c\u5730\u5f71\u7247\u5206\u7c7b\u6574\u7406\u4f7f\u7528\u3002</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> </span>           </p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">\u4e8c\u3001\u9879\u76ee\u7b80\u4ecb</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> Gui made by moyy996\uff0cCore made by yoshiko2</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> \u547d\u4ee4\u884c\u7248\u9879\u76ee\u5730\u5740\uff1ahttps://github.com/yoshiko2/Movie_Data_Capture</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                        "<span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> GUI\u7248\u9879\u76ee\u5730\u5740\uff1ahttps://github.com/moyy996/AVDC</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> GUI\u7248EXE\u4e0b\u8f7d\u5730\u5740\uff1ahttps://github.com/moyy996/AVDC/releases</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> </span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">\u4e09\u3001\u5e38\u89c1\u756a\u53f7\u547d\u540d\u53c2\u8003"
                        "</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">\u4e0d\u533a\u5206\u5927\u5c0f\u5199\u3001\u522e\u524a\u524d\u5c3d\u91cf\u547d\u540d\u89c4\u8303\uff01\uff01\uff01\uff01</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">3.1.\u6807\u51c6\u6709\u7801</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> Javdb\u3001Javbus:SSNI-111</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; t"
                        "ext-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> Dmm\uff1assni00111</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">3.2.\u65e0\u7801</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> Javdb\u3001Javbus\u3001Avsox:111111-1111\u3001111111_111\u3001HEYZO-1111\u3001n1111</span>           "
                        "</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">3.3.\u7d20\u4eba</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> Mgstage:259LUXU-1111</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-s"
                        "ize:13pt;\"> Javdb:LUXU-1111</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> Fc2club:FC2-111111\u3001FC2-PPV-111111\u3001FC2PPV-111111</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">3.4.\u6b27\u7f8e</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
                        "\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> Javdb\u3001Javbus:sexart.11.11.11(\u7cfb\u5217.\u5e74.\u6708.\u65e5)</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">3.5.\u81ea\u5e26\u5b57\u5e55\u5f71\u7247</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> \u53ef\u4ee5\u628a\u7535\u5f71\u547d\u540d"
                        "\u4e3a\u7c7b\u4f3cssni-xxx-c.mp4,ssni-xxx-C.mp4\uff0cabp-xxx-CD1-C.mp4 \u7684\u89c4\u5219\u3002</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">3.6.\u591a\u96c6\u5f71\u7247</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> \u53ef\u4ee5\u628a\u591a\u96c6\u7535\u5f71\u6309\u7167\u96c6\u6570\u540e\u7f00\u547d\u540d\u4e3a\u7c7b\u4f3cssni-xxx-cd1.mp"
                        "4, ssni-xxx-cd2.mp4,           abp-xxx-CD1-C.mp4\u7684\u89c4\u5219\uff0c\u53ea\u8981\u542b\u6709-CDn/-cdn\u7c7b\u4f3c\u547d\u540d\u89c4\u5219\uff0c\u5373\u53ef\u4f7f\u7528\u5206\u96c6\u529f\u80fd.**\u4e0d\u652f\u6301-A -B -1 -2,\u5bb9\u6613\u8ddf\u5b57\u5e55\u7684-C\u6df7\u6dc6**.</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">3.7.\u591a\u96c6\u3001\u5b57\u5e55\u987a\u5e8f</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style="
                        "\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> abp-xxx-CD1-C.mp4\uff0c\u5206\u96c6\u5728\u524d\uff0c\u5b57\u5e55\u5728\u540e\uff0c\u5b57\u5e55\u5fc5\u987b\u4e0e\u62d3\u5c55\u540d\u9760\u8fd1\uff0c-C.mp4.</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">3.8.\u5916\u6302\u5b57\u5e55\u6587\u4ef6</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft"
                        " YaHei UI'; font-size:13pt;\"> \u5b57\u5e55\u6587\u4ef6\u540d\u5fc5\u987b\u4e0e\u5f71\u7247\u6587\u4ef6\u540d\u4e00\u81f4\uff0c\u624d\u53ef\u4ee5\u4e00\u8d77\u79fb\u52a8\u5230\u65b0\u76ee\u5f55\uff0c\u76ee\u524d\u652f\u6301srt ass sub\u7c7b\u578b\u7684\u5b57\u5e55\u6587\u4ef6\u3002</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> </span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">\u56db\u3001\u8bbe\u7f6e\u8bf4\u660e</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; m"
                        "argin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">\u8be6\u7ec6\u7684\u8bf4\u660e\uff1a https://github.com/moyy996/AVDC/blob/master/README.md</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">4.1.\u522e\u524a\u6a21\u5f0f/\u6574\u7406\u6a21\u5f0f</span>           </p>\n"
"<p st"
                        "yle=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> 1\u3001\u522e\u524a\u6a21\u5f0f\uff1a\u901a\u8fc7\u756a\u53f7\u522e\u524a\u6570\u636e\uff0c\u5305\u62ec\u5143\u6570\u636e\u3001\u5c01\u9762\u56fe\u3001\u7f29\u7565\u56fe\u3001\u80cc\u666f\u56fe\u3002</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> 2\u3001\u6574\u7406\u6a21\u5f0f\uff1a\u4ec5\u6839\u636e\u5973\u4f18\u628a\u7535\u5f71\u547d\u540d\u4e3a\u756a\u53f7\u5e76\u5206\u7c7b\u5230\u5973\u4f18\u540d\u79f0\u7684\u6587\u4ef6\u5939\u4e0b\u3002</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<"
                        "p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">4.2.\u8f6f\u94fe\u63a5\u6a21\u5f0f\uff1a\u4f7f\u7528\u6b64\u6a21\u5f0f\uff0c\u8981\u4ee5\u7ba1\u7406\u5458\u8eab\u4efd\u8fd0\u884c\u3002</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> \u522e\u524a\u5b8c\u4e0d\u79fb\u52a8\u89c6\u9891\uff0c\u800c\u662f\u5728\u76f8\u5e94\u76ee\u5f55\u521b\u5efa\u8f6f\u94fe\u63a5\uff08\u7c7b\u4f3c\u4e8e\u5feb\u6377\u65b9\u5f0f\uff09\uff0c\u65b9\u4fbfPT\u4e0b\u8f7d\u5b8c\u65e2\u60f3\u522e\u524a\u53c8\u60f3\u7ee7\u7eed\u4e0a\u4f20\u7684\u4ed3"
                        "\u9f20\u515a\u540c\u5fd7\u3002</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> \u4f46\u662f\uff0c\u53ea\u80fd\u5728\u5a92\u4f53\u5e93\u5c55\u793a\uff0c\u4e0d\u80fd\u5728\u5a92\u4f53\u5e93\u64ad\u653e\u3002</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">4.3.\u8c03\u8bd5\u6a21\u5f0f</span>           </p>\n"
"<p style=\" margin-top:0px; margin-"
                        "bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> \u8f93\u51fa\u756a\u53f7\u7684\u5143\u6570\u636e\uff0c\u5305\u62ec\u5c01\u9762\uff0c\u5bfc\u6f14\uff0c\u6f14\u5458\uff0c\u7b80\u4ecb\u7b49\u3002</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">4.4.\u6392\u9664\u76ee\u5f55</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-in"
                        "dent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> \u5728\u591a\u5c42\u76ee\u5f55\u522e\u524a\u65f6\u6392\u9664\u6240\u586b\u76ee\u5f55\u3002</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">4.5.\u89c6\u9891\u76ee\u5f55</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> \u8981\u6574\u7406\u7684"
                        "\u89c6\u9891\u7684\u76ee\u5f55\uff0c\u4f1a\u904d\u5386\u6b64\u76ee\u5f55\u4e0b\u7684\u6240\u6709\u89c6\u9891\uff0c\u5305\u62ec\u5b50\u76ee\u5f55\u4e2d\u3002</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">4.6.\u547d\u540d\u89c4\u5219</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> 1\u3001\u76ee\u5f55\u547d\u540d\uff1a\u5b58\u653e\u89c6\u9891\u6570"
                        "\u636e\u7684\u76ee\u5f55\u540d\uff0c\u652f\u6301\u591a\u5c42\u76ee\u5f55\uff0c\u652f\u6301\u81ea\u5b9a\u4e49\u7b26\u53f7\uff0c\u4f8b\uff1a[actor]/studio/number-\u3010title\u3011\u3002</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> 2\u3001\u89c6\u9891\u6807\u9898\uff08\u5a92\u4f53\u5e93\u4e2d\uff09\uff1anfo\u4e2d\u7684\u6807\u9898\u547d\u540d\u3002\u4f8b\uff1anumber-[title]\u3002\u53ef\u4ee5\u81ea\u5b9a\u4e49\u7b26\u53f7\u3002</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> 3\u3001\u89c6\u9891\u6807\u9898\uff08\u672c\u5730\u6587\u4ef6\uff09\uff1a\u672c\u5730\u89c6\u9891\u3001\u56fe\u7247\u7684\u547d\u540d\u3002\u4f8b\uff1anumber-[tit"
                        "le]\u3002\u53ef\u4ee5\u81ea\u5b9a\u4e49\u7b26\u53f7\u3002</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">           4\u3001\u53ef\u9009\u9879\u4e3atitle\uff08\u7247\u540d\uff09\u3001actor\uff08\u6f14\u5458\uff09\u3001studio\uff08\u5236\u4f5c\u5546\uff09\u3001director\uff08\u5bfc\u6f14\uff09\u3001release\uff08\u53d1\u552e\u65e5\uff09\u3001year\uff08\u53d1\u884c\u5e74\u4efd\uff09\u3001number\uff08\u756a\u53f7\uff09\u3001runtime\uff08\u65f6\u957f\uff09\u3001series\uff08\u7cfb\u5217\uff09\u3001publisher\uff08\u53d1\u884c\u5546\uff09</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                        "<br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">4.7.\u4ee3\u7406\u8bbe\u7f6e</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> 1\u3001\u4ee3\u7406</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> proxy=127.0.0.1:1080</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;"
                        "\"> proxy\u884c\u8bbe\u7f6e\u672c\u5730\u4ee3\u7406\u5730\u5740\u548c\u7aef\u53e3\uff0c\u652f\u6301Shadowxxxx/X,V2XXX\u672c\u5730\u4ee3\u7406\u7aef\u53e3\uff0c\u4ee3\u7406\u8f6f\u4ef6\u5f00\u5168\u5c40\u6a21\u5f0f           ,\u5efa\u8bae\u4f7f\u7528\u65e5\u672c\u4ee3\u7406\u3002</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> \u5982\u679c\u4e00\u76f4\u62a5Connect Failed! Please check your Proxy or           Network!\u9519\u8bef\uff0c\u8bf7\u68c0\u67e5\u7aef\u53e3\u53f7\u662f\u5426\u6b63\u786e\uff0c\u6216\u8005\u628aproxy=\u540e\u9762\u7684\u5730\u5740\u548c\u7aef\u53e3\u5220\u9664\uff0c\u5e76\u5f00\u542f\u4ee3\u7406\u8f6f\u4ef6\u5168\u5c40\u6a21\u5f0f\uff0c\u6216\u8005\u91cd\u542f\u7535\u8111\uff0c\u4ee3\u7406\u8f6f\u4ef6\uff0c\u7f51\u5361\u3002</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; marg"
                        "in-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> 2\u3001\u8fde\u63a5\u8d85\u65f6\u91cd\u8bd5\u8bbe\u7f6e</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> timeout=10 </span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> 10\u4e3a\u8d85\u65f6\u91cd\u8bd5\u65f6\u95f4 \u5355\u4f4d\uff1a\u79d2\uff0c\u53ef\u9009\u8303\u56f43-10</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft "
                        "YaHei UI'; font-size:13pt;\"> 3\u3001\u8fde\u63a5\u91cd\u8bd5\u6b21\u6570\u8bbe\u7f6e</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> retry=3 </span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> 3\u5373\u4e3a\u91cd\u8bd5\u6b21\u6570\uff0c\u53ef\u9009\u8303\u56f42-5</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-l"
                        "eft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">4.8.\u5a92\u4f53\u5e93\u9009\u62e9</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> \u5982\u679c\u662fPLEX\uff0c\u8bf7\u5b89\u88c5\u63d2\u4ef6\uff1aXBMCnfoMoviesImporter</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsof"
                        "t YaHei UI'; font-size:13pt;\">4.9.\u6392\u9664\u6307\u5b9a\u5b57\u7b26\u548c\u76ee\u5f55\uff0c\u5b57\u7b26\u4e32</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> 1\u3001\u6392\u9664\u5b57\u7b26:\u6307\u5b9a\u5b57\u7b26\u5220\u9664\uff0c\u4f8b\u5982\u6392\u9664\u5b57\u7b26\uff1a \\()\uff0c\u5220\u9664\u521b\u5efa\u6587\u4ef6\u5939\u65f6\u7684\\()\u5b57\u7b26</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> 2\u3001\u6392\u9664\u76ee\u5f55:\u6307\u5b9a\u76ee\u5f55\uff0c\u4f8b\u5982\u6392\u9664\u76ee\u5f55\uff1a failed,JAV_output\uff0c\u591a\u76ee\u5f55\u522e\u524a\u65f6\u8df3\u8fc7failed,JAV_output</span>           </p>\n"
"<p style=\" m"
                        "argin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> 3\u3001\u6392\u9664\u5b57\u7b26\u4e32:\u63d0\u53d6\u756a\u53f7\u65f6\uff0c\u5148\u5220\u9664\u6307\u5b9a\u5b57\u7b26\u4e32\uff0c\u63d0\u9ad8\u6210\u529f\u7387\uff0c\u5b57\u7b26\u4e32\u4e4b\u95f4\u7528','\u9694\u5f00\u3002</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">4.10.\u7f51\u7ad9\u9009\u62e9</span>           </p>\n"
"<p style="
                        "\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> \u53ef\u4ee5\u4f7f\u7528\u6240\u6709\u7f51\u7ad9\uff0c\u6216\u8005\u6307\u5b9a\u7f51\u7ad9\uff08avsox,javbus,dmm,javdb,fc2club\uff0cmgstage\uff09\u8fdb\u884c\u522e\u524a\u3002</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> \u4ec5\u4f7f\u7528javdb\u8fdb\u884c\u522e\u524a\uff0c\u5c3d\u91cf\u4e0d\u8981\u7528\uff0c\u522e\u524a30\u5de6\u53f3\u4f1a\u88abJAVDB\u5c01IP\u4e00\u6bb5\u65f6\u95f4\u3002</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-le"
                        "ft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">4.11.\u4fdd\u5b58\u65e5\u5fd7</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> \u5f00\u542f\u540e\u65e5\u5fd7\u4fdd\u5b58\u5728\u7a0b\u5e8f\u76ee\u5f55\u7684Log\u76ee\u5f55\u4e0b\u7684txt\u6587\u4ef6\u5185\uff0c\u6bcf\u6b21\u8fd0\u884c\u4f1a\u4ea7\u751f\u4e00\u4e2atxt\u6587\u4ef6\uff0ctxt\u6587\u4ef6\u53ef\u4ee5\u5220\u9664\uff0c\u4e0d\u5f71\u54cd\u7a0b\u5e8f\u8fd0\u884c\u3002</span>           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><"
                        "br />           </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\">4.12.\u5931\u8d25\u540e\u79fb\u52a8\u6587\u4ef6</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> \u5982\u679c\u522e\u524a\u4e0d\u5230\u5f71\u7247\u4fe1\u606f\uff0c\u53ef\u9009\u62e9\u4e0d\u79fb\u52a8\u89c6\u9891\uff0c\u6216\u8005\u81ea\u52a8\u79fb\u52a8\u5230\u5931\u8d25\u8f93\u51fa\u76ee\u5f55\u4e2d\u3002</span>           </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent"
                        ":0px;\"><span style=\" font-family:'Consolas','PingFang SC','Microsoft YaHei UI'; font-size:13pt;\"> </span>       </p></body></html>", None))
        self.label_show_version.setText("")
        self.label_local_number.setText("")
        self.pushButton_main.setText(QCoreApplication.translate("MDCx", u" \u4e3b\u754c\u9762", None))
        self.pushButton_log.setText(QCoreApplication.translate("MDCx", u" \u65e5\u5fd7", None))
        self.pushButton_tool.setText(QCoreApplication.translate("MDCx", u" \u5de5\u5177", None))
        self.pushButton_setting.setText(QCoreApplication.translate("MDCx", u" \u8bbe\u7f6e", None))
        self.pushButton_net.setText(QCoreApplication.translate("MDCx", u" \u68c0\u6d4b\u7f51\u7edc", None))
        self.pushButton_about.setText(QCoreApplication.translate("MDCx", u" \u4f7f\u7528\u8bf4\u660e", None))
        self.pushButton_close.setText(QCoreApplication.translate("MDCx", u"\u00d7", None))
        self.pushButton_min.setText(QCoreApplication.translate("MDCx", u"-", None))
        self.label_19.setText(QCoreApplication.translate("MDCx", u"\u7b80\u4ecb\uff1a", None))
        self.label_359.setText(QCoreApplication.translate("MDCx", u"\u6f14\u5458\uff1a", None))
        self.label_360.setText(QCoreApplication.translate("MDCx", u"\u756a\u53f7\uff1a", None))
        self.label_361.setText(QCoreApplication.translate("MDCx", u"\u6807\u9898\uff1a", None))
        self.label_362.setText(QCoreApplication.translate("MDCx", u"\u6807\u7b7e\uff1a", None))
        self.label_363.setText(QCoreApplication.translate("MDCx", u"\u53d1\u884c\u65e5\u671f\uff1a", None))
        self.label_364.setText(QCoreApplication.translate("MDCx", u"\u65f6\u957f\uff1a", None))
        self.label_365.setText(QCoreApplication.translate("MDCx", u"\u7cfb\u5217\uff1a", None))
        self.label_366.setText(QCoreApplication.translate("MDCx", u"\u5bfc\u6f14\uff1a", None))
        self.label_367.setText(QCoreApplication.translate("MDCx", u"\u53d1\u884c\u5546\uff1a", None))
        self.label_368.setText(QCoreApplication.translate("MDCx", u"\u5236\u4f5c\u5546\uff1a", None))
        self.label_369.setText(QCoreApplication.translate("MDCx", u"\u56fd\u5bb6\uff1a", None))
        self.comboBox_nfo.setItemText(0, QCoreApplication.translate("MDCx", u"JP", None))
        self.comboBox_nfo.setItemText(1, QCoreApplication.translate("MDCx", u"US", None))
        self.comboBox_nfo.setItemText(2, QCoreApplication.translate("MDCx", u"CN", None))

        self.label_371.setText(QCoreApplication.translate("MDCx", u"\u539f\u7b80\u4ecb\uff1a", None))
        self.label_372.setText(QCoreApplication.translate("MDCx", u"\u539f\u6807\u9898\uff1a", None))
        self.label_375.setText(QCoreApplication.translate("MDCx", u"\u5c01\u9762\u56fe\u5730\u5740\uff1a", None))
        self.label_376.setText(QCoreApplication.translate("MDCx", u"\u80cc\u666f\u56fe\u5730\u5740\uff1a", None))
        self.label_377.setText(QCoreApplication.translate("MDCx", u"\u9884\u544a\u7247\u5730\u5740\uff1a", None))
        self.label_378.setText(QCoreApplication.translate("MDCx", u"\u7f51\u9875\u5730\u5740\uff1a", None))
        self.label_370.setText(QCoreApplication.translate("MDCx", u"\u591a\u4e2a\u4ee5\u9017\u53f7\u9694\u5f00", None))
        self.label_379.setText(QCoreApplication.translate("MDCx", u"\u591a\u4e2a\u4ee5\u9017\u53f7\u9694\u5f00", None))
        self.label_373.setText(QCoreApplication.translate("MDCx", u"\u8bc4\u5206\uff1a", None))
        self.label_374.setText(QCoreApplication.translate("MDCx", u"\u60f3\u770b\u4eba\u6570\uff1a", None))
        self.label_380.setText(QCoreApplication.translate("MDCx", u"\u5e74\u4ee3\uff1a", None))
        self.label_nfo.setText("")
        self.label_381.setText(QCoreApplication.translate("MDCx", u"\u6587\u4ef6\uff1a", None))
        self.pushButton_nfo_save.setText(QCoreApplication.translate("MDCx", u"\u4fdd\u5b58", None))
        self.pushButton_nfo_close.setText(QCoreApplication.translate("MDCx", u"\u5173\u95ed", None))
#if QT_CONFIG(shortcut)
        self.pushButton_nfo_close.setShortcut(QCoreApplication.translate("MDCx", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.label_4.setText(QCoreApplication.translate("MDCx", u"\u7f16\u8f91 NFO", None))
        self.label_save_tips.setText("")
    # retranslateUi

