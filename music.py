# import pygame

# pygame.init()
# pygame.mixer.init()
# musicFile = '/home/macias/Muzyka/BEASTIE BOYS - Hot Sauce Committee(2011)/01.Make Some Noise.mp3'
# pygame.mixer.music.load(musicFile)
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy(): 
# 	print('Playing...')

from Tkinter import *
from tkFileDialog import askopenfilename
import pygame

class Song():
	def __init__(self, path):
		self.path = path
		self.name = self.path.split('/')[-1]

class Application(Frame):
	def say_hi(self):
		print "hi there, everyone!"

	def play(self):
		print(self.playlist)
		try:
			self.current_song = self.listbox.get(self.listbox.curselection())
		except:
			print('None of song is selected')
		else:
			pygame.mixer.music.load('./media/' + self.current_song)
			pygame.mixer.music.play()	

	def stop(self):
		pygame.mixer.music.stop()

	def chooseFile(self):
		musicFile = askopenfilename()
		self.playlist.append(musicFile)
		self.listbox.insert(END, musicFile.split('/')[-1])
		self.listbox.selection_set(first=musicFile)
		# print('list of songs =>', self.listbox.get(self.listbox.curselection()))

	def createWidgets(self):
		self.QUIT = Button(self)
		self.QUIT["text"] = "\xe2\x98\x93"
		self.QUIT["fg"]   = "red"
		self.QUIT["command"] =  self.quit

		self.QUIT.pack({"side": "left"})

		self.playButton = Button(self)
		self.playButton["text"] = "\xe2\x99\xaa"
		self.playButton["fg"] = "green"
		self.playButton["command"] = self.play

		self.playButton.pack({"side": "right"})

		self.stopButton = Button(self)
		self.stopButton["text"] = u"\u25A0"
		self.stopButton["fg"] = "black"
		self.stopButton["command"] = self.stop

		self.stopButton.pack({"side": "right"})

		self.stopButton = Button(self)
		self.stopButton["text"] = "Choose file"
		self.stopButton["fg"] = "blue"
		self.stopButton["command"] = self.chooseFile

		self.stopButton.pack({"side": "right"})

		self.listbox = Listbox(
			self.master,
			bg='#ffd89b',
			bd=0.5,
			font='DejaVuSerif-Bold'
		)
		# print(self.listbox[0])
		self.listbox.pack()

	def __init__(self, master=None):
		import sys
		mytext = u""
		mytext += unichr(247) 
		#check the codes for unicode chars here:  http://en.wikipedia.org/wiki/List_of_Unicode_characters
		print mytext.encode(sys.stdout.encoding, errors="replace")
		print('\xe2\x99\xa5')

		self.master = master
		pygame.init()
		pygame.mixer.init()

		self.current_song = None
		self.playlist = []

		master.minsize(width=600, height=300)
		master.configure(background='#ff9d00')
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

root = Tk()
root.wm_attributes('-type', 'splash')
app = Application(master=root)
app.mainloop()
root.destroy()