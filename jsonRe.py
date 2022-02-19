import re

f = open('./static/covidmap.js','r')
alllines = f.readlines()
f.close
f = open('./static/covidmap.js','w+')
for eachline in alllines:
    a=re.sub('\\','',eachline)
    f.writelines(a)
f.close