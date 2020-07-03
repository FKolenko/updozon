#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
upd = form.getfirst("upd", "не задано")
order = form.getfirst("order", "не задано")
order_number = form.getfirst('order_number', 'не задано')
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")


#print("<p>TEXT_1: {}</p>".format(text1))
#print("<p>TEXT_2: {}</p>".format(text2))
l = [x for x in order.split()]
#print(l)

f = open('start.xml', 'w')
f.write(upd)
f.close()

#print("<h1>split ok</h1><br>")
from xml.etree import ElementTree

tree = ElementTree.parse('start.xml')
root = tree.getroot()

#print(root)
#print(root.tag, root.attrib)


for elem in root.iter('ГрузПолуч'):
    for el in elem.iter('СвЮЛУч'):
        el.set ('КПП', '504445002')
        print("<h1>гп ok</h1><br>")

root[1][0][2][1].remove(root[1][0][2][1][0])

root[1][0][2][1].append(root[1][0][2][1].makeelement('АдрРФ', {'КодРегион':'50', 'Индекс':'141533', 'Район':"Солнечногорский", 'НаселПункт':'Хоругвино', 'Дом':'32/2'}))

for elem in root.iter('ГрузПолуч'):
    for el in elem.iter('БанкРекв'):
        el.set ('НомерСчета', '40702810600014252743')
for elem in root.iter('ГрузПолуч'):
    for el in elem.iter('СвБанк'):
        el.set ('НаимБанк', 'ЗАО «Юникредит Банк')
        el.set('БИК', '044525545')
        el.set('КорСчет', '30101810300000000545')

for elem in root.iter('СвПокуп'):
    for el in elem.iter('СвЮЛУч'):
        el.set('НаимОрг','Общество с ограниченной ответственностью &quot;ИНТЕРНЕТ РЕШЕНИЯ&quot;')
        el.set('КПП','997750001')

root[1][0][3][1].remove(root[1][0][3][1][0])
root[1][0][3][1].append(root[1][0][3][1].makeelement('АдрРФ', {'КодРегион':"77", 'Индекс':"123112", 'Улица':"Пресненская наб.", 'Дом':"д. 10", 'Кварт':"Пом.I, эт.41, к.6"}))
for elem in root.iter('СвПокуп'):
    for el in elem.iter('БанкРекв'):
        el.set('НомерСчета','40702810600014252743')

for elem in root.iter('СвПокуп'):
    for el in elem.iter('СвБанк'):
        el.set('НаимБанк','ЗАО &quot;Юникредит Банк&quot;')
        el.set('БИК','044525545')
        el.set('КорСчет','30101810300000000545')
root[1][0].append(root[1][0].makeelement('ИнфПолФХЖ1',{}))
root[1][0][5].append(root[1][0][5].makeelement('ТекстИнф',{'Идентиф':'номер_заявки','Значен':order_number}))

for elem in root.iter('СвПер'):
        elem.set ('СодОпер', 'Товары переданы')


for elem in root.iter('ОснПер'):
        elem.set ('НаимОсн', 'Договор')
        elem.set('НомОсн', 'ИР-9922/19')
        elem.set('ДатаОсн', '17.06.2019')

id_ozon_list = ['178029785', '177847317', '177843701', '177843692', '177843395', '177764210', '177763877', '177763423', '177763178', '177848157', '177294976', '177131457', '177131268', '172215330', '170143982', '160825343', '154692745', '154672893', '154672887', '177132752', '177850724', '177864920', '177865339', '178029373', '178029318', '178029094', '178028669', '178028166', '178026831', '178026770', '178025440', '178025117', '178023347', '177872882', '177872713', '177872188', '177872161', '177871204', '177869166', '177868965', '177865868', '177865544', '154669606', '154669603']

i = 0
for elem in root.iter('СведТов'):
    root[1][1][i].append(root[1][1][i].makeelement('ИнфПолФХЖ2',{'Идентиф':'ID товара','Значен':id_ozon_list[i]}))
    i = i + 1
tree.write('proc.xml',encoding='utf-8')
print('<a href="../proc.xml">скачать упд</a>')

#print(tree)
#print('122')

print("""</body>
        </html>""")