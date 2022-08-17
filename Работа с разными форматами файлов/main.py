import sys

import xml.etree.ElementTree as ET
# tree = ET.parse("files/newsafr.xml")

parser = ET.XMLParser(encoding="utf-8")
# # подставляем парсер при разборе xml
tree = ET.parse("files/newsafr.xml", parser)
print()
print()
print(tree)
root = tree.getroot()
print(root.tag)

title_list = root.findall("channel/item/title")
print(type(title_list))
title_first = root.find("channel/item/title")
print(type(title_first))
print(f"Всего {len(title_list)} новостей")
for title in title_list:
	print(title.text)

print()
print("Цикл, от которого мы избавились")
items_list = root.findall("channel/item")
for item in items_list:
	print(item.find("title").text)

# for descr in root.findall("channel/item/description"):
# 	print(descr.text)


sys.exit()

import json
from pprint import pprint

with open("files/newsafr.json") as f:
	json_data = json.load(f)

# print(json_data)
news_list = json_data["rss"]["channel"]["items"]
# print(f"Всего {len(news_list)} новостей")
# pprint(news_list[0])
# for news in news_list:
# 	# print(type(news))
# 	print(news["title"])

with open("files/newsafr2.json", "w") as f:
	# json.dump(json_data, f, ensure_ascii=False, indent=4)
	json_export = json.dumps(json_data,  ensure_ascii=False)
	print(type(json_export))
	print(json_export)

sys.exit()


import csv

# with open("files/newsafr.csv") as f:
# 	reader = csv.reader(f)
# 	news_count = 0
# 	print(type(reader))
# 	for row in reader:
# 		if news_count > 0:
# 			print(row[-1])
# 		news_count+= 1

# print(f"Всего {news_count-1} новостей")

with open("files/newsafr.csv") as f:
	reader = csv.reader(f)
	news_list = list(reader)
print(type(news_list))
header = news_list.pop(0)
# for row in news_list:
# 	print(row[-1])

csv.register_dialect("customcsv", delimiter=",", quoting=csv.QUOTE_NONE, escapechar="\\")
csv.register_dialect("customcsv2", delimiter=";", quoting=csv.QUOTE_ALL)

with open("files/newsafr2.csv", "a") as f:
	writer = csv.writer(f, "customcsv")
	# print(header)
	writer.writerow(header)
	# print(news_list[:2])
	writer.writerows(news_list)
	# на самом деле writerows делает вот это:
	# for row in news_list:
	# 	writer.writerow(row)

# print(f"Всего {len(news_list)} новостей")

# print()
# print(news_list[:3])

# with open("files/newsafr.csv") as f:
# 	reader = csv.DictReader(f)
# 	news_count = 0
# 	for row in reader:
# 		print(row["title"])
# 		news_count += 1

# print(f"Всего {news_count} новостей")