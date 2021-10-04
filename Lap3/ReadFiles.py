
#bài 2
alkaline_metals = []
for line in open('D:\\DEV\\Python-\\Lap3\\alkaline_metals.txt','r',encoding='UTF-8'):
 alkaline_metals.append(line.strip().split(' '))
 print(alkaline_metals)

 #bài 3
 content = []
for line in open('D:\\DEV\\Python-\\Lap3\\kiet.txt','r',encoding='UTF-8'):
    content.append(line)
print('Doc nguoc file :\n ',)
for line in reversed(content):
    print(line)

#bài 4
def skip_header(reader):
    line = reader.readline()    
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline() 
    
    return line

def process_file(reader):
    line = skip_header(reader).strip()
    print(line)
    for line in reader:
        line = line.strip()
        print(line)

input_file = open('D:\\DEV\\Python-\\Lap3\\kiet.txt', 'r',encoding='UTF-8')
process_file(input_file)
input_file.close()

#bài 5 
def smallest_value_skip(reader):
    line = skip_header(reader).strip()
    # Only execute this code, if there is data following the header.
    if line != '':
        smallest = line
    for line in reader:
        line = line.strip()
        if line != '-':
            value = line
            smallest = min(smallest, value)
    return smallest

input_file = open('D:\\DEV\\Python-\\Lap3\\kiet.txt', 'r')
print(smallest_value_skip(input_file))
input_file.close()

#bài 6
def smallest_value_skip2(reader):
    line = skip_header(reader).strip()
    smallest = line

    for line in reader: 
        line = line.strip()
        if line == '-':
            continue

    value = line
    smallest = min(smallest, value)

    return smallest

input_file = open('D:\\DEV\\Python-\\Lap3\\kiet.txt', 'r')
print(smallest_value_skip2(input_file))
input_file.close()

#bài 7 
def read_molecule(reader):
    content = []
    for line in reader:
        if not line.startswith('CMNT'):
            if not line.isspace():
                content.append(line.strip())
    for line in content:
        print(line)
    
input_file = open('D:\\DEV\\Python-\\Lap3\\kiet.pdb', 'r')
print(read_molecule(input_file))
input_file.close()