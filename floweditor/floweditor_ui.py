from PySide2 import QtCore, QtGui, QtWidgets

class Ui_FlowEditorWindow(object):
    def setupUi(self, FlowEditorWindow):
        FlowEditorWindow.setObjectName("FlowEditorWindow")
        FlowEditorWindow.resize(1009, 730)
        FlowEditorWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        FlowEditorWindow.setDockNestingEnabled(True)
        FlowEditorWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.ForceTabbedDocks|QtWidgets.QMainWindow.VerticalTabs)
        self.centralwidget = QtWidgets.QWidget(FlowEditorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_widget.sizePolicy().hasHeightForWidth())
        self.main_widget.setSizePolicy(sizePolicy)
        self.main_widget.setObjectName("main_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.main_widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.graph_name_lineedit = QtWidgets.QLineEdit(self.main_widget)
        self.graph_name_lineedit.setText("")
        self.graph_name_lineedit.setObjectName("graph_name_lineedit")
        self.verticalLayout_5.addWidget(self.graph_name_lineedit)
        self.graph_widget = QtWidgets.QWidget(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_widget.sizePolicy().hasHeightForWidth())
        self.graph_widget.setSizePolicy(sizePolicy)
        self.graph_widget.setObjectName("graph_widget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.graph_widget)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_5.addWidget(self.graph_widget)
        self.verticalLayout_6.addWidget(self.main_widget)
        self.bottom_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_widget.sizePolicy().hasHeightForWidth())
        self.bottom_widget.setSizePolicy(sizePolicy)
        self.bottom_widget.setObjectName("bottom_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressbar = QtWidgets.QProgressBar(self.bottom_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressbar.sizePolicy().hasHeightForWidth())
        self.progressbar.setSizePolicy(sizePolicy)
        self.progressbar.setProperty("value", 0)
        self.progressbar.setObjectName("progressbar")
        self.horizontalLayout_2.addWidget(self.progressbar)
        self.progress_label = QtWidgets.QLabel(self.bottom_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress_label.sizePolicy().hasHeightForWidth())
        self.progress_label.setSizePolicy(sizePolicy)
        self.progress_label.setText("")
        self.progress_label.setObjectName("progress_label")
        self.horizontalLayout_2.addWidget(self.progress_label)
        self.verticalLayout_6.addWidget(self.bottom_widget)
        FlowEditorWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FlowEditorWindow)
        self.statusbar.setObjectName("statusbar")
        FlowEditorWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(FlowEditorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuGraph = QtWidgets.QMenu(self.menubar)
        self.menuGraph.setObjectName("menuGraph")
        FlowEditorWindow.setMenuBar(self.menubar)
        self.nodes_dock = QtWidgets.QDockWidget(FlowEditorWindow)
        self.nodes_dock.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.nodes_dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.nodes_dock.setObjectName("nodes_dock")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nodes_splitter = QtWidgets.QSplitter(self.dockWidgetContents)
        self.nodes_splitter.setOrientation(QtCore.Qt.Vertical)
        self.nodes_splitter.setChildrenCollapsible(False)
        self.nodes_splitter.setObjectName("nodes_splitter")
        self.available_nodes_widget = QtWidgets.QWidget(self.nodes_splitter)
        self.available_nodes_widget.setObjectName("available_nodes_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.available_nodes_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.available_nodes_search = QtWidgets.QLineEdit(self.available_nodes_widget)
        self.available_nodes_search.setObjectName("available_nodes_search")
        self.verticalLayout_3.addWidget(self.available_nodes_search)
        self.available_nodes_view = AvailableNodesView(self.available_nodes_widget)
        self.available_nodes_view.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.available_nodes_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.available_nodes_view.setProperty("showDropIndicator", False)
        self.available_nodes_view.setDragEnabled(True)
        self.available_nodes_view.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.available_nodes_view.setAlternatingRowColors(True)
        self.available_nodes_view.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.available_nodes_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.available_nodes_view.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.available_nodes_view.setObjectName("available_nodes_view")
        self.verticalLayout_3.addWidget(self.available_nodes_view)
        self.node_details_widget = QtWidgets.QWidget(self.nodes_splitter)
        self.node_details_widget.setObjectName("node_details_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.node_details_widget)
        self.verticalLayout_4.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.nodes_details_text = QtWidgets.QTextEdit(self.node_details_widget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.nodes_details_text.setFont(font)
        self.nodes_details_text.setStyleSheet("background-color: palette(window)")
        self.nodes_details_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nodes_details_text.setFrameShadow(QtWidgets.QFrame.Plain)
        self.nodes_details_text.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.nodes_details_text.setObjectName("nodes_details_text")
        self.verticalLayout_4.addWidget(self.nodes_details_text)
        self.verticalLayout.addWidget(self.nodes_splitter)
        self.nodes_dock.setWidget(self.dockWidgetContents)
        FlowEditorWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.nodes_dock)
        self.logs_dock = QtWidgets.QDockWidget(FlowEditorWindow)
        self.logs_dock.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.logs_dock.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea)
        self.logs_dock.setObjectName("logs_dock")
        self.logs_tab = QtWidgets.QWidget()
        self.logs_tab.setObjectName("logs_tab")
        self.logs_layout = QtWidgets.QVBoxLayout(self.logs_tab)
        self.logs_layout.setObjectName("logs_layout")
        self.log_textedit = QtWidgets.QTextEdit(self.logs_tab)
        self.log_textedit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.log_textedit.setObjectName("log_textedit")
        self.logs_layout.addWidget(self.log_textedit)
        self.log_actions_layout = QtWidgets.QHBoxLayout()
        self.log_actions_layout.setContentsMargins(-1, 0, -1, -1)
        self.log_actions_layout.setObjectName("log_actions_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.log_actions_layout.addItem(spacerItem)
        self.clear_log_button = QtWidgets.QPushButton(self.logs_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_log_button.sizePolicy().hasHeightForWidth())
        self.clear_log_button.setSizePolicy(sizePolicy)
        self.clear_log_button.setObjectName("clear_log_button")
        self.log_actions_layout.addWidget(self.clear_log_button)
        self.logs_layout.addLayout(self.log_actions_layout)
        self.logs_dock.setWidget(self.logs_tab)
        FlowEditorWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.logs_dock)
        self.node_dock = QtWidgets.QDockWidget(FlowEditorWindow)
        self.node_dock.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.node_dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.node_dock.setObjectName("node_dock")
        self.node_name_widget = QtWidgets.QWidget()
        self.node_name_widget.setObjectName("node_name_widget")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.node_name_widget)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_lineedit = QtWidgets.QLineEdit(self.node_name_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.name_lineedit.setFont(font)
        self.name_lineedit.setStyleSheet("")
        self.name_lineedit.setObjectName("name_lineedit")
        self.horizontalLayout.addWidget(self.name_lineedit)
        self.node_state_label = QtWidgets.QLabel(self.node_name_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.node_state_label.setFont(font)
        self.node_state_label.setTextFormat(QtCore.Qt.RichText)
        self.node_state_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.node_state_label.setObjectName("node_state_label")
        self.horizontalLayout.addWidget(self.node_state_label)
        self.verticalLayout_14.addLayout(self.horizontalLayout)
        self.node_type_label = QtWidgets.QLabel(self.node_name_widget)
        self.node_type_label.setText("")
        self.node_type_label.setObjectName("node_type_label")
        self.verticalLayout_14.addWidget(self.node_type_label)
        self.description_textedit = QtWidgets.QTextEdit(self.node_name_widget)
        self.description_textedit.setMinimumSize(QtCore.QSize(0, 30))
        self.description_textedit.setStyleSheet("background-color: palette(window);")
        self.description_textedit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.description_textedit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.description_textedit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable)
        self.description_textedit.setObjectName("description_textedit")
        self.verticalLayout_14.addWidget(self.description_textedit)
        self.node_dock.setWidget(self.node_name_widget)
        FlowEditorWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.node_dock)
        self.inputs_dock = QtWidgets.QDockWidget(FlowEditorWindow)
        self.inputs_dock.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.inputs_dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.inputs_dock.setObjectName("inputs_dock")
        self.node_inputs_widget = AttributesWidget()
        self.node_inputs_widget.setMouseTracking(False)
        self.node_inputs_widget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.node_inputs_widget.setObjectName("node_inputs_widget")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.node_inputs_widget)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.inputs_dock.setWidget(self.node_inputs_widget)
        FlowEditorWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.inputs_dock)
        self.outputs_dock = QtWidgets.QDockWidget(FlowEditorWindow)
        self.outputs_dock.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.outputs_dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.outputs_dock.setObjectName("outputs_dock")
        self.node_outputs_widget = AttributesWidget()
        self.node_outputs_widget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.node_outputs_widget.setObjectName("node_outputs_widget")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.node_outputs_widget)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.outputs_dock.setWidget(self.node_outputs_widget)
        FlowEditorWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.outputs_dock)
        self.errors_dock = QtWidgets.QDockWidget(FlowEditorWindow)
        self.errors_dock.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.errors_dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.errors_dock.setObjectName("errors_dock")
        self.errors_widget = QtWidgets.QWidget()
        self.errors_widget.setObjectName("errors_widget")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.errors_widget)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.errors_textedit = QtWidgets.QTextEdit(self.errors_widget)
        self.errors_textedit.setReadOnly(True)
        self.errors_textedit.setObjectName("errors_textedit")
        self.verticalLayout_16.addWidget(self.errors_textedit)
        self.errors_dock.setWidget(self.errors_widget)
        FlowEditorWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.errors_dock)
        self.code_dock = QtWidgets.QDockWidget(FlowEditorWindow)
        self.code_dock.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.code_dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.code_dock.setObjectName("code_dock")
        self.code_widget = QtWidgets.QWidget()
        self.code_widget.setObjectName("code_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.code_widget)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.code_view = QtWidgets.QTextEdit(self.code_widget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.code_view.setFont(font)
        self.code_view.setStyleSheet("")
        self.code_view.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.code_view.setObjectName("code_view")
        self.verticalLayout_2.addWidget(self.code_view)
        self.open_code_button = QtWidgets.QPushButton(self.code_widget)
        self.open_code_button.setObjectName("open_code_button")
        self.verticalLayout_2.addWidget(self.open_code_button)
        self.code_dock.setWidget(self.code_widget)
        FlowEditorWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.code_dock)
        self.actionNew = QtWidgets.QAction(FlowEditorWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(FlowEditorWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(FlowEditorWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(FlowEditorWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionOpen_Recent = QtWidgets.QAction(FlowEditorWindow)
        self.actionOpen_Recent.setObjectName("actionOpen_Recent")
        self.actionQuit = QtWidgets.QAction(FlowEditorWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionDocumentation = QtWidgets.QAction(FlowEditorWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.evaluate_remotely_action = QtWidgets.QAction(FlowEditorWindow)
        self.evaluate_remotely_action.setObjectName("evaluate_remotely_action")
        self.actionThreaed = QtWidgets.QAction(FlowEditorWindow)
        self.actionThreaed.setObjectName("actionThreaed")
        self.actionNon_threaed = QtWidgets.QAction(FlowEditorWindow)
        self.actionNon_threaed.setObjectName("actionNon_threaed")
        self.evaluate_locally_action = QtWidgets.QAction(FlowEditorWindow)
        self.evaluate_locally_action.setObjectName("evaluate_locally_action")
        self.edit_mode_action = QtWidgets.QAction(FlowEditorWindow)
        self.edit_mode_action.setCheckable(True)
        self.edit_mode_action.setObjectName("edit_mode_action")
        self.project_action = QtWidgets.QAction(FlowEditorWindow)
        self.project_action.setObjectName("project_action")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionQuit)
        self.menuGraph.addAction(self.evaluate_locally_action)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuGraph.menuAction())

        self.retranslateUi(FlowEditorWindow)
        QtCore.QMetaObject.connectSlotsByName(FlowEditorWindow)

    def retranslateUi(self, FlowEditorWindow):
        FlowEditorWindow.setWindowTitle(QtWidgets.QApplication.translate("FlowEditorWindow", "Flow Editor", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("FlowEditorWindow", "File", None, -1))
        self.menuGraph.setTitle(QtWidgets.QApplication.translate("FlowEditorWindow", "Graph", None, -1))
        self.nodes_dock.setWindowTitle(QtWidgets.QApplication.translate("FlowEditorWindow", "Nodes", None, -1))
        self.logs_dock.setWindowTitle(QtWidgets.QApplication.translate("FlowEditorWindow", "Logs", None, -1))
        self.clear_log_button.setText(QtWidgets.QApplication.translate("FlowEditorWindow", "Clear", None, -1))
        self.node_dock.setWindowTitle(QtWidgets.QApplication.translate("FlowEditorWindow", "Node Info", None, -1))
        self.node_state_label.setText(QtWidgets.QApplication.translate("FlowEditorWindow", "clean", None, -1))
        self.inputs_dock.setWindowTitle(QtWidgets.QApplication.translate("FlowEditorWindow", "Input Plugs", None, -1))
        self.outputs_dock.setWindowTitle(QtWidgets.QApplication.translate("FlowEditorWindow", "Output Plugs", None, -1))
        self.errors_dock.setWindowTitle(QtWidgets.QApplication.translate("FlowEditorWindow", "Errors", None, -1))
        self.code_dock.setWindowTitle(QtWidgets.QApplication.translate("FlowEditorWindow", "Code", None, -1))
        self.open_code_button.setText(QtWidgets.QApplication.translate("FlowEditorWindow", "Open in Editor", None, -1))
        self.actionNew.setText(QtWidgets.QApplication.translate("FlowEditorWindow", "New", None, -1))
        self.actionNew.setShortcut(QtWidgets.QApplication.translate("FlowEditorWindow", "Ctrl+N", None, -1))
        self.actionOpen.setText(QtWidgets.QApplication.translate("FlowEditorWindow", "Open", None, -1))
        self.actionOpen.setShortcut(QtWidgets.QApplication.translate("FlowEditorWindow", "Ctrl+O", None, -1))
        self.actionSave.setText(QtWidgets.QApplication.translate("FlowEditorWindow", "Save", None, -1))
        self.actionSave.setShortcut(QtWidgets.QApplication.translate("FlowEditorWindow", "Ctrl+S", None, -1))
        self.actionSave_As.setText(QtWidgets.QApplication.translate("FlowEditorWindow", "Save As...", None, -1))
        self.actionSave_As.setShortcut(QtWidgets.QApplication.translate("FlowEditorWindow", "Ctrl+Shift+S", None, -1))
        self.actionOpen_Recent.setText(QtWidgets.QApplication.translate("FlowEditorWindow", "Open Recent", None, -1))
        self.actionQuit.setText(QtWidgets.QApplication.translate("FlowEditorWindow", "Quit", None, -1))
        self.actionQuit.setShortcut(QtWidgets.QApplication.translate("FlowEditorWindow", "Ctrl+Q", None, -1))
        self.actionDocumentation.setText(QtWidgets.QApplication.translate("FlowEditorWindow", "Documentation", None, -1))
        self.evaluate_remotely_action.setText(QtWidgets.QApplication.translate("FlowEditorWindow", "Send to Farm", None, -1))
        self.actionThreaed.setText(QtWidgets.QApplication.translate("FlowEditorWindow", "Threaded", None, -1))
        self.actionNon_threaed.setText(QtWidgets.QApplication.translate("FlowEditorWindow", "Non-threaded", None, -1))
        self.evaluate_locally_action.setText(QtWidgets.QApplication.translate("FlowEditorWindow", "Evaluate Locally", None, -1))
        self.edit_mode_action.setText(QtWidgets.QApplication.translate("FlowEditorWindow", "Edit Mode", None, -1))
        self.project_action.setText(QtWidgets.QApplication.translate("FlowEditorWindow", "Project...", None, -1))

from floweditor.widgets import AvailableNodesView
from floweditor.attributes.attributes_widget import AttributesWidget
