from docx import Document
from docx.shared import Inches
import os

#获取目录下的全部文件名，形成列表
itemPaths = []
for root, dir, items in os.walk(top='.\doc'):
    itemPaths.extend(
        [os.path.join(root, item) for item in items]
    )
print(itemPaths)

#打开一个word文档
document = Document('test.docx')
#遍历读取每一个文件，将文件内容添加到word文档
for i in itemPaths:
    f = open(i,'r',encoding = 'utf-8')
    for p in f.readlines():
        print(p)
        document.add_paragraph(p) 
    f.close()
#保存
document.save('test.docx')
