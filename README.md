# handleBills

This application is intended for OCR, it uses a google api that expects an image, and return a json 
with the recognized text, its appear to be cnn (convolutional neural networks) to do the dirty job

so, it has two urls

/getBillAsJson     ------------>   recives a bill image and return total, date and bill number
/uploadImage       ------------>   upload an image, it will be in next realease an automated process that will proces all the images and save the text in a database
