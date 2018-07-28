from docx import Document

numbersdone = 0
numbersoffixes = 0
doc = Document('c:\temp\test.docx')

for para in doc.paragraphs:
    newtxt = ''
    for char in para.text:
        if char in '1234567890':
            numbersoffixes += 1
            if numbersdone == 0:
                newtxt += char
                numbersdone += 1
            else:
                newtxt = newtxt[:-1*numbersdone] + char + newtxt[-1*numbersdone:]
                numbersdone += 1
        else:
            newtxt += char
            numbersdone = 0

        para.text = newtxt

doc.save('c:\temp\fixed.test.docx')
print('in total fixed'. numbersoffixes)
