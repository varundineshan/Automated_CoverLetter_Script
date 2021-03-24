from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from datetime import datetime


fileName = 'Demo_Coverletter.pdf'
documentTitle = 'Cover Letter'
title = 'Varun Dineshan '
subTitle = 'abcdefgh@gmail.com | https://www.linkedin.com/in/abcdefgh | 64x-7X7-XXXX'
now = datetime.now()
dateLine='{} {} {}'.format(now.strftime('%B'),now.strftime('%d'),now.strftime('%Y'))
thanksLine="Sincerely,"
my_name="Your Name"
textLines = [
    'Name Here',
    'HR Manager',
    'XYZA Corporation',
    '3X Sheppard Ave.', 'Suite Y0X'
    'Toronto ON', 'LXG 7X8'
]

respectLine="Dear"+" "+"Miss"+" "+textLines[0]+","

bodyPara1="Kindly consider my resume for the position of Junior xyz developer – \
Industrial IT ,which is advertised on indeed on {} \
I am a quick learner with a will and desire \
to undergo self-improvement for the growth of peers and the employer. My experience \
and knowledge in the technical skills would benefit the company helping them \
successfully complete the goals.".format(dateLine)

bodyPara2="Firstly, out of the many fields of strengths,\
the area in which I can excel is the knowledge in programming and as a xyz developer.\
I have worked as an systems engineer and I’m \
confident enough to work as a xyz developer and improve my skills consistently. My last \
work taught me how to work effectively in a team and how to support them in every \
situation. In addition, I’ve done many freelance works on automation which have polished \
my skills and heightened my confidence."

bodyPara3="I am eager to have an opportunity to get in contact with you to discuss how good \
I am in this field and eventually contribute to your organization. Please contact me at phone 64X \
XXX XXXX or by email abcdef@gmail.com. Also, you can check my skills at \
https://github.com/abcdefgh Thank you for your time and consideration."

# 0) Create document 
height_start=770


pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)

pdf.setFont('Times-Roman', 16)
pdf.drawCentredString(300, height_start, title)


pdf.setFont("Times-Roman",12 )
pdf.drawCentredString(290,height_start-20, subTitle)

pdfmetrics.registerFont(TTFont('abc', 'Arial.ttf'))
pdf.setFont('abc', 12)

pdf.drawString(50,height_start-50,dateLine)

text = pdf.beginText(50, height_start-70)
text.setFont("abc", 12)
for line in textLines:
    text.textLine(line)
pdf.drawText(text)
# ###################################Address Line
pdf.setFont('abc', 12)
pdf.drawString(50,height_start-180,respectLine)
# ###################################First message line
pdf.setFont('abc', 12)
text = pdf.beginText(50, height_start-210)
text.setFont("abc", 12)
# ###################################Body first paragraph
out = [(bodyPara1[i:i+91]) for i in range(0, len(bodyPara1),91)]
for line in out:
    text.textLine(line)
pdf.drawText(text)   
# ###################################Body second paragraph
text = pdf.beginText(50, height_start-300)
text.setFont("abc", 12)
out = [(bodyPara2[i:i+91]) for i in range(0, len(bodyPara2),91)]
for line in out:
    text.textLine(line)
pdf.drawText(text) 
# ###################################Body third paragraph
text = pdf.beginText(50, height_start-400)
text.setFont("abc", 12)
out = [(bodyPara3[i:i+91]) for i in range(0, len(bodyPara3),91)]
for line in out:
    text.textLine(line)
pdf.drawText(text) 
# ###################################Thanks line
pdf.drawString(50,height_start-490,thanksLine)
pdf.drawString(50,height_start-510,my_name)

pdf.save()
