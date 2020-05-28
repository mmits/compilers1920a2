import re

def find_title():		#1
	rexp = re.compile('<title>(.+?)</title>')
	m = rexp.search(text)
	if m: print(m.group(1))
	print("\n")

def remove_comment():		#2
	rexp = re.compile(r'<!--.*?-->',re.DOTALL)
	m = rexp.sub("",text)
	return m

def remove_scrsty():		#3
	rexp = re.compile(r'(<script|<style)(>?).+?(</script>|</style>)',re.DOTALL)
	m = rexp.sub("",text)
	return m

def find_href():		#4
	rexp = re.compile('<a(.+?)</a>')
	for m in rexp.finditer(text):print(m.group(1))
	print("\n")
	
def remove_tags():		#5
	rexp = re.compile(r'<[^>]+>',re.DOTALL)
	m = rexp.sub("",text)
	return m
	
def cb(m):
	return '{}.{}'.format(m.group(2),m.group(1))

def replace_entities():		#6
	rexp = re.compile(r'(&amp;)(&)')
	m = rexp.sub(cb,text)
	return m

def replace_whitespace():		#7
	rexp = re.compile(r'\s+')
	m = rexp.sub(' ',text)
	return m

with open('testpage.txt','r',encoding='utf-8') as fp:

	text = fp.read()
	
	#------ 1 ------#
	print("Title")
	find_title()
	
	#------ 2 ------#
	text = remove_comment()
	
	#------ 3 ------#
	text = remove_scrsty()
	
	#------ 4 ------#
	print("HREFs")
	find_href()
	
	#------ 5 ------#
	text = remove_tags()
	
	#------ 6 ------#
	text = replace_entities()
	
	#------ 7 ------#
	text = replace_whitespace()
	
	#------ 8 ------#
	print("Final Text")
	print(text)
