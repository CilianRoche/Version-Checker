import csv
from distutils.version import LooseVersion

#Setup variables and functions
path = 'D:/development/projects/michael/installLog.txt'
mode = ('r+')
def open_file(path, mode):
    f = open(path, mode)
    return f
def close_file(file):
    file.close()

#grab each computer number from .txt
def get_comp_num():
    
    f = open_file(path, mode)
    
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
        
    close_file(f)
    return comp_num

#grab each version number from .txt
def get_comp_ver():

    f = open_file(path, mode)
    
    splitline = []
    for line in f:
        splitline.append(line.split())
    
    comp_ver = []
    for x in splitline:
        for y in x:
            if y.startswith('ProductVersion'):
                comp_ver.append(x[1])

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
    f = open_file(path, 'w')
    writer = csv.writer(f)
    for key, value in g.items():
        if LooseVersion(str(value)) >= LooseVersion("6.0.0.3051"):
            writer.writerow([key, value])
            print(key + ' - ' + value)

    close_file(f)
    print('Check out ' + path)

#the end
write_csv('D:/development/projects/michael/finale.csv')
