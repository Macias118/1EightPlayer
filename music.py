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

class Application(Frame):
	def say_hi(self):
		print "hi there, everyone!"

	def play(self):
		print(self.playlist)
		for file in self.playlist:
			pygame.mixer.music.load(file)
			pygame.mixer.music.play()
		# while pygame.mixer.music.get_busy(): 
		# 	print('Playing...') 	

	def stop(self):
		pygame.mixer.music.stop()

	def chooseFile(self):
		musicFile = askopenfilename()
		self.playlist.append(musicFile)

	def createWidgets(self):
		self.QUIT = Button(self)
		self.QUIT["text"] = "QUIT"
		self.QUIT["fg"]   = "red"
		self.QUIT["command"] =  self.quit

		self.QUIT.pack({"side": "left"})

		# self.hi_there = Button(self)
		# self.hi_there["text"] = "Hello",
		# self.hi_there["command"] = self.say_hi

		# self.hi_there.pack({"side": "left"})

		self.playButton = Button(self)
		self.playButton["text"] = "Play"
		self.playButton["fg"] = "green"
		self.playButton["command"] = self.play

		self.playButton.pack({"side": "right"})

		self.stopButton = Button(self)
		self.stopButton["text"] = "Stop"
		self.stopButton["fg"] = "red"
		self.stopButton["command"] = self.stop

		self.stopButton.pack({"side": "right"})

		self.stopButton = Button(self)
		self.stopButton["text"] = "Choose file"
		self.stopButton["fg"] = "blue"
		self.stopButton["command"] = self.chooseFile

		self.stopButton.pack({"side": "right"})

	def __init__(self, master=None):
		pygame.init()
		pygame.mixer.init()

		self.playlist = []

		master.minsize(width=400, height=200)
		master.configure(background='#CC5D2B')
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()