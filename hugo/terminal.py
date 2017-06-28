import aiml
import os,sys
from modules.aiml.brain import Brain
from colorama import Fore, Style
class Terminal(object):

	def __init__(self):
		brain = Brain()
		self.clear()
		self.print_intro()
		print("Hugo: Hey! whats up?")
		stay = True
		
		while stay:
			try:
				text = str.upper(raw_input( "You: "))
			except:
				text = str.upper(input("You: "))
			
			if text == "Q":
				print("Thanks for talking to me")
				stay = False
			else:
				print("Hugo: "+brain.respond(text))
		pass

	def print_intro(self):
		print Fore.CYAN+Style.BRIGHT+ """
		\t    _    _                   
 		\t   | |  | |                  
 		\t   | |__| |_   _  __ _  ___  
 		\t   |  __  | | | |/ _` |/ _ \ 
 		\t   | |  | | |_| | (_| | (_) |
 		\t   |_|  |_|\__,_|\__, |\___/ 
        \t     		         __/ /      
        \t\t 	        |___/       
         """ + Style.RESET_ALL
		print "_"*80
		pass

	def clear(self):
		sys.stderr.write("\x1b[2J\x1b[H")
    	pass