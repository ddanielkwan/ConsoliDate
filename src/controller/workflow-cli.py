#This file will initiate the workflow process for analyzing and converting PDF information to ICS

from functions.rawDataFunctions import getText
from modules.RawData import RawData
from modules.ICS import ICS
from pdf2image.exceptions import PDFPageCountError
from functions.fileManagementFunctions import cleanExcess
import os

def runExtraction():
		
		run = True
		
		#Select path to print .ICS files to
		satisfactoryPath = False
		print("Welcome to ConsoliDate! This is where you can convert your pdf files (course outlines) into .ics files! Please input the directory you would like your .ics to be printed to.")
		while (satisfactoryPath == False):
				writeToPath = input()
				if writeToPath == "":
						writeToPath =  os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
						satisfactoryPath = True
				elif os.path.isdir(writeToPath) == False:
						print("That is not an existing directory, press enter to have ics files written onto desktop, or try to enter an existing directory")
				else:
						satisfactoryPath = True

		#Selection of pdf to extract assessments from
		while (run):
				basic = True   #basic specifies the mode the application is running in, in this case it will be set to true however in the future the user may specify the mode they wish to run the program in
				print("Now, please input a filepath to a PDF file, enter 0 to quit!")
				path = input()
				if path == "0":
					run = False
				elif path[-4:] != ".pdf":
					print("filepath does not point to a pdf file, make sure the filepath ends with '.pdf'!")
				else:
					try:
						text = getText(path)   #Return array with first index containing text and second index containing number of pages
					except FileNotFoundError:
						print("Invalid file path!")
					except PDFPageCountError:
						print("Invalid file path!")
					else:
						rawData = RawData(None,text[0],path)
						rawData.getTitlefromData()
						rawData.mineDueDates()
						ics = ICS(rawData.title,rawData.Events)
						icsPath = ics.writeICS(writeToPath)
						print("Your ICS file has been generated! It is located in this directory:\n " +icsPath)
						if (basic):
							  cleanExcess(text[1])
