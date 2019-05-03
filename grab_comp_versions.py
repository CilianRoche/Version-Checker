import csv
from distutils.version import LooseVersion
import codecs

#grab each computer number from .txt
def get_comp_num():
    
    f = codecs.open('path/to/ps1/script/output.txt', encoding='utf-16')
    
    
    splitline = []
    for line in f:
        splitline.append(line.split())

    comp_num = []
    for x in splitline:
        for y in x:
            if y.__len__() == 5 and y.startswith('L'):
                comp_num.append(y)
            elif y.__len__() == 5 and y.startswith('D'):
                comp_num.append(y)
        
    f.close()
    return comp_num

#grab each version number from .txt
def get_comp_ver():

    f = codecs.open('path/to/ps1/script/output.txt', encoding='utf-16')
    
    splitline = []
    for line in f:
        splitline.append(line.split())
    
    comp_ver = []
    for x in splitline:
        for y in x:
            if y.startswith('ProductVersion'):
                comp_ver.append(x[1])
    f.close()
    return comp_ver

#make dictionary from computer numbers and version numbers
def make_dictionary():
  
    p = get_comp_num()
    g = get_comp_ver()
    
    comp_num_ver = {key:value for key, value in zip(p, g)}
    return comp_num_ver

#Writing computers to CSV which have Trend version 6.0.0.3051 or greater
def write_csv(path):
    g = make_dictionary()
    f = open(path, 'r+')
    writer = csv.writer(f)
    for key, value in g.items():
        if LooseVersion(str(value)) <= LooseVersion("6.0.0.3051"):
            writer.writerow([key, value])
            print(key + ' - ' + value)

    print('Check out ' + path)

#the end
write_csv('path/to/final.csv')
