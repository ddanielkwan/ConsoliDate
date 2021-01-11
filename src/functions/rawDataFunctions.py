
# Import libraries 
from PIL import Image 
from pdf2image import convert_from_path 
from functions.textAlgorithmSupportingFunctions import createArray, parseInt, RepresentsInt
from time import strptime
from modules.Event import Event
from datetime import datetime
import subprocess 
import os
#Constants
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
								  'August', 'September', 'October', 'November', 'December','Jan', 
								  'Feb', 'Mar', 'Apr', 'Jul', "Jun", "Aug", "Sep", "Sept", "Oct", "Nov", "Dec"]
ASSESSMENTS = ["Assignment", "Test", "quiz", "Quiz"]


def getText(filePath):

				
				# Store all the pages of the PDF in a variable 
				pages = convert_from_path(filePath, 500) 
				
				# Counter to store images of each page of PDF to image 
				image_counter = 1

				# Iterate through all the pages stored above 
				for page in pages: 
				
								filename = "page_"+str(image_counter)+".jpg".format(os.getpid())
								
								# Save the image of the page in system 
								page.save(filename, 'JPEG') 
				
								# Increment the counter to update filename 
								image_counter = image_counter + 1
				
				# Variable to get count of total number of pages 
				filelimit = image_counter-1
				outText = ""
				
				# Iterate from 1 to total number of pages 
				for i in range(1, filelimit + 1): 
				
								filename = "page_"+str(i)+".jpg".format(os.getpid())
																
								#Use tesseract from terminal to write a new file containing the text from image
								sumthin = subprocess.call('tesseract page_'+str(i)+'.jpg page_'+str(i) ,shell=True) 
								
								page = open('page_'+str(i)+'.txt', 'r') 
								
								text = page.read() 
										
								text = text.replace('-\n', '')	 
										
								# Finally, store the text in the appropriate output variable. 
								outText = outText + '\n' + text
								page.close()
										
				
				return [outText, filelimit]



def textAlgorithm(text):
				

				i = 0
				iDateUseful = []
				iAssessment = []
				assessmentsWithDate = []
				
				textArray = createArray(text)
				
				while i < len(textArray):
								if textArray[i] in MONTHS:
												intCandidate = parseInt(textArray[i+1])
												if RepresentsInt(intCandidate):
																iDateUseful.append(strptime(textArray[i][0:3],'%b').tm_mon)
																iDateUseful.append(int(intCandidate))
																if len(iAssessment) > 0:
																				assessmentsWithDate.append(Event(iAssessment[0],datetime(2020, iDateUseful[len(iDateUseful)-2], iDateUseful[len(iDateUseful)-1])))
																				iAssessment.pop(0)
																				iDateUseful.pop(len(iDateUseful)-2)
																				iDateUseful.pop(len(iDateUseful)-1)
								elif textArray[i] in ASSESSMENTS:
												intCandidate = parseInt(textArray[i+1])
												if RepresentsInt(intCandidate):
																iAssessment.append(textArray[i] + " " + textArray[i+1])  
																if len(iDateUseful) > 1:
																				assessmentsWithDate.append(Event(iAssessment[0],datetime(2020, iDateUseful[len(iDateUseful)-2], iDateUseful[len(iDateUseful)-1])))
																				iAssessment.pop(0)
																				iDateUseful.pop(len(iDateUseful)-2)
																				iDateUseful.pop(len(iDateUseful)-1)
								i = i + 1
								
				return assessmentsWithDate



def getTitle(text):
				textArray = createArray(text)
				title = textArray[0].partition('\n')[0]
				title = title[0:len(title)-1].replace(":","")
				icsTitle = title + ".ics"
				return icsTitle
