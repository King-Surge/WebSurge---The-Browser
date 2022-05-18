from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

import os.path

class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)

		self.tabs = QTabWidget()
		# absolute path of resources/globe-solid.png as a variable
		self.iconPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resources', 'globe-solid.png'))
		#os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
		self.setWindowIcon(QIcon(self.iconPath))
		self.tabs.setDocumentMode(True)
		self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
		self.tabs.currentChanged.connect(self.current_tab_changed)
		self.tabs.setTabsClosable(True)
		self.tabs.tabCloseRequested.connect(self.close_current_tab)
		self.setCentralWidget(self.tabs)

		self.status = QStatusBar() 

		navtb = QToolBar("Navigation")
		navtb.setMovable( False );
		self.addToolBar(navtb)
  
		self.addToolBarBreak()
		bnavtb = QToolBar("Navigationa")
		bnavtb.setMovable( False );
		self.addToolBar(bnavtb)

		back_btn = QAction("⏪", self)
		back_btn.setStatusTip("Back to previous page")
		back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
		navtb.addAction(back_btn)

		navtb.addSeparator()

		next_btn = QAction("⏩", self)
		next_btn.setStatusTip("Forward to next page")
		next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
		navtb.addAction(next_btn)
  
		navtb.addSeparator()
  
		reload_btn = QAction("🔄", self)
		reload_btn.setStatusTip("Reload page")
		reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
		navtb.addAction(reload_btn)

		navtb.addSeparator()

		home_btn = QAction("🏡", self)
		home_btn.setStatusTip("Go home")
		home_btn.triggered.connect(self.navigate_home)
		navtb.addAction(home_btn)

		navtb.addSeparator()
  
		self.urlbar = QLineEdit()
		self.urlbar.returnPressed.connect(self.navigate_to_url)
		navtb.addWidget(self.urlbar)
  
		notice_btn = QAction("<<- Websites | Search ->>", self)
		navtb.addAction(notice_btn)
  
		self.search = QLineEdit()
		self.search.returnPressed.connect(self.navigate_to_search)
		navtb.addWidget(self.search)

		stop_btn = QAction("❌", self)
		stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
		navtb.addAction(stop_btn)
  
		bnavtb.addSeparator()

		booka_btn = QAction("Google", self)
		booka_btn.triggered.connect(self.navigate_homesurge)
		bnavtb.addAction(booka_btn)
  
		bnavtb.addSeparator()
  
		bookb_btn = QAction("🎬Youtube", self)
		bookb_btn.triggered.connect(self.navigate_homeson)
		bnavtb.addAction(bookb_btn)
		bnavtb.addSeparator()
  
		bookc_btn = QAction("📰Bing", self)
		bookc_btn.triggered.connect(self.navigate_homesonc)
		bnavtb.addAction(bookc_btn)
		bnavtb.addSeparator()
  
		bookd_btn = QAction("🖍Google Doodles", self)
		bookd_btn.triggered.connect(self.navigate_homesond)
		bnavtb.addAction(bookd_btn)
		bnavtb.addSeparator()
  
		booke_btn = QAction("📫Gmail", self)
		booke_btn.triggered.connect(self.navigate_homesone)
		bnavtb.addAction(booke_btn)
		bnavtb.addSeparator()
  
		bookf_btn = QAction("📑Google Docs", self)
		bookf_btn.triggered.connect(self.navigate_homesonf)
		bnavtb.addAction(bookf_btn)
		bnavtb.addSeparator()
  
		bookg_btn = QAction("📖Google Slides", self)
		bookg_btn.triggered.connect(self.navigate_homesong)
		bnavtb.addAction(bookg_btn)
		bnavtb.addSeparator()
  
		bookh_btn = QAction("🛒Amazon", self)
		bookh_btn.triggered.connect(self.navigate_homesonh)
		bnavtb.addAction(bookh_btn)
		bnavtb.addSeparator()
  
		booki_btn = QAction("💬Discord", self)
		booki_btn.triggered.connect(self.navigate_homesoni)
		bnavtb.addAction(booki_btn)
		bnavtb.addSeparator()
  
		bookj_btn = QAction("💾Discord Developer Portal", self)
		bookj_btn.triggered.connect(self.navigate_homesonj)
		bnavtb.addAction(bookj_btn)
		bnavtb.addSeparator()
  
		bookk_btn = QAction("🖼Pinterest", self)
		bookk_btn.triggered.connect(self.navigate_homesonk)
		bnavtb.addAction(bookk_btn)
		bnavtb.addSeparator()

		bookl_btn = QAction("📢Yahoo", self)
		bookl_btn.triggered.connect(self.navigate_homesonl)
		bnavtb.addAction(bookl_btn)
		bnavtb.addSeparator()
  
		bookm_btn = QAction("💡reddit", self)
		bookm_btn.triggered.connect(self.navigate_homesonm)
		bnavtb.addAction(bookm_btn)
		bnavtb.addSeparator()

		bookn_btn = QAction("📺CNN", self)
		bookn_btn.triggered.connect(self.navigate_homesonn)
		bnavtb.addAction(bookn_btn)
		bnavtb.addSeparator()

		booko_btn = QAction("🎮XBOX", self)
		booko_btn.triggered.connect(self.navigate_homesono)
		bnavtb.addAction(booko_btn)
		bnavtb.addSeparator()

		bookp_btn = QAction("💎Instagram", self)
		bookp_btn.triggered.connect(self.navigate_homesonp)
		bnavtb.addAction(bookp_btn)
		bnavtb.addSeparator()
  
		bookq_btn = QAction("🎶Spotify🔊", self)
		bookq_btn.triggered.connect(self.navigate_homesonq)
		bnavtb.addAction(bookq_btn)
		bnavtb.addSeparator()
  
		self.add_new_tab(QUrl('http://www.bing.com'), 'Homepage')
		self.show()
  
		self.setWindowTitle("WebSurge")
  
	
	def add_new_tab(self, qurl = None, label ="Blank"):

		if qurl is None:
			qurl = QUrl('http://www.bing.com')

		browser = QWebEngineView()

		browser.setUrl(qurl)

		i = self.tabs.addTab(browser, label)
		self.tabs.setCurrentIndex(i)

		browser.urlChanged.connect(lambda qurl, browser = browser:
								self.update_urlbar(qurl, browser))

		browser.loadFinished.connect(lambda _, i = i, browser = browser:
									self.tabs.setTabText(i, browser.page().title()))

	def tab_open_doubleclick(self, i):

		if i == -1:
			self.add_new_tab()


	def current_tab_changed(self, i):

		qurl = self.tabs.currentWidget().url()

		self.update_urlbar(qurl, self.tabs.currentWidget())

		self.update_title(self.tabs.currentWidget())

	def close_current_tab(self, i):

		if self.tabs.count() < 2:
			return

		self.tabs.removeTab(i)
  
	def update_title(self, browser):

		if browser != self.tabs.currentWidget():
			return

		title = self.tabs.currentWidget().page().title()

		self.setWindowTitle("% s - WebSurge" % title)

	def navigate_home(self):

		self.tabs.currentWidget().setUrl(QUrl("http://www.bing.com"))

	def navigate_to_url(self):

		q = QUrl(self.urlbar.text())

		if q.scheme() == "":
			q.setScheme("https")

		self.tabs.currentWidget().setUrl(q)
  
	def navigate_to_search(self):
		q = self.search.text()
  
		qur = QUrl("https://www.google.com/search?q=%s" % q)
		self.tabs.currentWidget().setUrl(qur)

	def update_urlbar(self, q, browser = None):

		if browser != self.tabs.currentWidget():

			return

		self.urlbar.setText(q.toString())

		self.urlbar.setCursorPosition(0)
  
	def navigate_homesurge(self):
    
		self.tabs.currentWidget().setUrl(QUrl("http://www.google.com"))
  
	def navigate_homeson(self):
    
		self.tabs.currentWidget().setUrl(QUrl("http://www.youtube.com"))
  
	def navigate_homesonc(self):
        
		self.tabs.currentWidget().setUrl(QUrl("http://www.bing.com"))

	def navigate_homesond(self):
        
		self.tabs.currentWidget().setUrl(QUrl("https://www.google.com/doodles"))
  
	def navigate_homesone(self):
        
		self.tabs.currentWidget().setUrl(QUrl("https://www.gmail.com"))
  
	def navigate_homesonf(self):
        
		self.tabs.currentWidget().setUrl(QUrl("https://docs.google.com/document"))
  
	def navigate_homesong(self):
        
		self.tabs.currentWidget().setUrl(QUrl("https://docs.google.com/presentation"))
  
	def navigate_homesonh(self):
        
		self.tabs.currentWidget().setUrl(QUrl("https://amazon.com"))
  
	def navigate_homesoni(self):
        
		self.tabs.currentWidget().setUrl(QUrl("https://discord.com"))
  
	def navigate_homesonj(self):
        
		self.tabs.currentWidget().setUrl(QUrl("https://discord.com/developers"))

	def navigate_homesonk(self):
        
		self.tabs.currentWidget().setUrl(QUrl("https://pinterest.com"))

	def navigate_homesonl(self):
        
		self.tabs.currentWidget().setUrl(QUrl("https://yahoo.com"))
  
	def navigate_homesonm(self):
        
		self.tabs.currentWidget().setUrl(QUrl("https://reddit.com"))
  
	def navigate_homesonn(self):
        
		self.tabs.currentWidget().setUrl(QUrl("https://edition.cnn.com/"))
  
	def navigate_homesono(self):
        
		self.tabs.currentWidget().setUrl(QUrl("https://xbox.com/"))
  
	def navigate_homesonp(self):
        
		self.tabs.currentWidget().setUrl(QUrl("https://instagram.com/"))
  
	def navigate_homesonq(self):
        
		self.tabs.currentWidget().setUrl(QUrl("https://spotify.com/"))