import io
import json
import os
import csv
import sys

directorio = sys.argv[1]
list_words = []
#Below Put Your Google Credentials in json format
#os.environ['GOOGLE_APPLICATION_CREDENTIALS']=os.path.abspath('My First Project-253ef37d6631.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=''

def detect_text(content):
	print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
	if os.environ['GOOGLE_APPLICATION_CREDENTIALS'] is '':
		print("configure your google api credentials")
		return ""
		
	from google.cloud import vision
	client = vision.ImageAnnotatorClient()

	# with io.open(path, 'rb') as image_file:
		# content = image_file.read()

	image = vision.types.Image(content=content.read())
	print("going to google clod")
	response = client.text_detection(image=image)
	response1 = client.document_text_detection(image=image)
	
	for page in response1.full_text_annotation.pages:
		for block in page.blocks:
			print('\n Block confidence: {}'.format(block.confidence))

			for paragraph in block.paragraphs:
				print('Paragraph confidence: {}'.format(paragraph.confidence))

				for word in paragraph.words:
					w={}
					position={}
					word_text = ''.join([symbol.text for symbol in word.symbols])
					print('Word text: {}(confidence: {})'.format(word_text, word.confidence))
					position['x'] = word.bounding_box.vertices[0].x
					position['y'] = word.bounding_box.vertices[0].y
					print(position)
					w['word'] = word_text
					w['confidence'] = word.confidence
					w['position'] = position

					list_words.append(w)
	words = {}
	words['words']= list_words		
	print(words)
	return words

# files = os.listdir(directorio)
# for file in files:
	# detect_text(file)
# words = {}
# words['worlds'] = list_words
# with open('data.json', 'w') as file:
	# json.dump(words, file, indent=4)

def get_invoice_number(words):
	# with open("data.json") as f:
		# data = json.load(f)
	if (words is ""):
		return ""
	data = words
	ls = []
	l = ["FACTURA", "Invoice"]
	l1 = ["#", "Number", "number", "VENTA"]
	for w in data['worlds']:
		ls.append(w["word"])

	j = 0
	invoicenum=[]
	for i in range(len(ls)):
		if (ls[i] in l) and (ls[i+1] in l1 or ls[i+2] in l1):
			j=i
			while (j<len(ls)):

				if ls[j].isnumeric():
					print(ls[i]+ls[i+1]+ls[i+2])
					print (ls[j])
					invoicenum.append(ls[j])
					break
				j+=1
	return invoicenum
	
# print("-----------------sigue los totales--------------------")


def get_invoice_total(words):
	if  words is '':
		return ''
	l = ["Total", "TOTAL"]
	l1 = ["Sub"]
	for w in data['worlds']:
		ls.append(w["word"])
	total=[]
	for i in range(len(ls)):
		if (ls[i] in l) and not(ls[i-1] in l1):
			j=i
			while (j<len(ls)):

				if (ls[j].replace('£', "")).isnumeric() and not (ls[j] in invoicenum):
					print(ls[i]+ls[i+1]+ls[i+2])
					print(ls[j].replace("£", ""))
					total.append(ls[j].replace("£", ""))
					break
				j+=1
	return total
	
# print("-----------------fechas------------------------")

def get_invoice_date(words):
	if words is '':
		return ''
	l=["/"]
	l1=["Invoice", "Date"]
	date=[]
	for i in range(len(ls)-4):
		if (ls[i-1] in l1) and (ls[i] in l1):
			#print(ls[i+1]+ls[i+2]+ls[i+4])
			date.append(ls[i+1]+ls[i+2]+ls[i+4])
		if (ls[i] in l) and (ls[i+2] in l):
			#print(ls[i-1]+ls[i]+ls[i+1]+ls[i+2]+ls[i+3])
			date.append(ls[i-1]+ls[i]+ls[i+1]+ls[i+2]+ls[i+3])
	return date
	
# myData=[]
# myFile = open('one.csv', 'w')
# p = ["Date", "Invoice Number", "Total Amount"]
# myData.append(p)
# for i in range (len(date)):
	# n=[]
	# n.append(date[i])
	# n.append(invoicenum[i])
	# n.append(total[i])
	# myData.append(n)

# with myFile:
	# writer = csv.writer(myFile)
	# writer.writerows(myData)

#set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\1456206\Downloads\My First Project-253ef37d6631.json


