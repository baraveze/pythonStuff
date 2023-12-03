import pyttsx3, PyPDF2

pdfReader = PyPDF2.PdfReader(open('ExamplePdf.pdf','rb'))
speaker = pyttsx3.init()

for page_num in range(len(pdfReader.pages)):
    text = pdfReader.pages[page_num].extract_text()
    cleanText = text.strip().replace('\n',' ')
    print(cleanText)
    
speaker.save_to_file(cleanText,'result.mp3')
speaker.runAndWait()
speaker.stop()