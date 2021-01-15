#This file will initiate the workflow process for analyzing and converting PDF information to ICS

from functions.rawDataFunctions import getText
from modules.RawData import RawData
from modules.ICS import ICS
from pdf2image.exceptions import PDFPageCountError
from functions.fileManagementFunctions import cleanExcess
import os

def runExtraction():
		
		run = True	

		#Selection of pdf to extract assessments from
		while (run):
				basic = True   #basic specifies the mode the application is running in, in this case it will be set to true however in the future the user may specify the mode they wish to run the program in
				# print("Now, please input a filepath to a PDF file, enter 0 to quit!")
				path = input() #         <------------------------------------------------------- Gets User Input (comment for shernan)
				if path[-4:] != ".pdf":
					# print("filepath does not point to a pdf file, make sure the filepath ends with '.pdf'!")
				else:
					try:
						text = getText(path)   #Return array with first index containing text and second index containing number of pages
					except FileNotFoundError:
						# print("Invalid file path!")
					except PDFPageCountError:
						# print("Invalid file path!")
					else:
						rawData = RawData(None,text[0],path)
						rawData.getTitlefromData()
						rawData.mineDueDates()
						ics = ICS(rawData.title,rawData.Events)
						# icsPath = ics.writeICS(writeToPath) <--- Writes into Download Folder
						# print("Your ICS file has been generated! It is located in this directory:\n " +icsPath)
						if (basic):
							  cleanExcess(text[1])
