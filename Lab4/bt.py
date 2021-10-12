# bài 1
def find_dups(L):
    elem_set = set()
    dups_set = set()
    for entry in L:
        len_initial = len(elem_set)
        elem_set.add(entry)
        len_after = len(elem_set)
        if len_initial == len_after:
            dups_set.add(entry)
    return(dups_set)
list_integers = [1,1,2,2,3,3,4,5,6,7,8,9]
print(find_dups(list_integers))

#bài 2
def read_molecule(reader):
    
    line = reader.readline()
    if not line:
        return None

    key, name = line.split()

    molecule = [name]
    line = reader.readline()
    
   
    while not line.startswith('END'):
        key, num, atom_type, x, y, z = line.split()
        molecule.append([atom_type, x, y, z])
        line = reader.readline()
    return molecule

def read_all_molecules(reader):
    result = []
    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule: 
            result.append(molecule)
        else:
            reading = False
    return result
if __name__ == "__main__":
    molecule_file = open('D:\\DEV\\Python-\\Lab4\\multimol.pdb','r')
    molecules = read_all_molecules(molecule_file)
    print(molecules)

#bài 3
def mating_pairs(males, females):
    try:
        pairs = set()
        num_gerbils = len(males)
        for i in range(num_gerbils):
            male = males.pop()
            female = females.pop()
            pairs.add((male, female),)
        return pairs
    except:
        return print("Số lượng Males và Females phải bằng nhau")
males = {'Nam1', 'Nam2', 'Nam3'}
females = {'Nu1', 'Nu2', 'Nu3'}
print(mating_pairs(males, females))

# bài 4
def get_authors(filenames):
    authors = set()
    for filename in filenames:
        for line in open(filename,'r'):
            if line.lower().startswith('author'):
                author = line[6:].strip()
                authors.add(author)
    return authors
if __name__ == "__main__":
    list_file = ['D:\\DEV\\Python-\\Lab4\\PDB_1.pdb','D:\\DEV\\Python-\\Lab4\\PDB_2.pdb']
    print(get_authors(list_file))

#Cau5 
from typing import Dict
def count_values(inDict: Dict) -> int:
    
    finalList = []

    for i in inDict.values():
        if i not in finalList:
            finalList.append(i)
    
    return len(finalList)



color = {'red':1,'green':1,'blue':2}

print(count_values(color))

#Cau6
from typing import Dict
def leastProbable(particleDict: Dict[str, float]) -> str:
    minValue = min(particleDict.values())
    printValue = ''
    for key,value in particleDict.items():
        if value == minValue:
            return key


values = { 'neutron ': 0.55,  'proton ': 0.21,  'meson ': 0.03,  'muon ': 0.07,  'neutrino ': 0.14}
print(leastProbable(values))

#Cau 7
def count_duplicates(inDict) -> int:

    lstAllValues = []
    lstAdditional = []
    lstFinal = []

    for i in inDict.values():
        lstAllValues.append(i)
        lstAdditional.append(i)
    
    lstFinal = set(lstAllValues).intersection(lstAdditional)

    return(len(lstAllValues) - len(lstFinal))


number = {'one' : 1, 'two' : 2, 'two1' : 2, 'three1' : 3,'three' : 3}

print(count_duplicates(number))

#Cau8
def is_balanced (inDict:[str, float]) -> bool:
    
    sumVar = 0.0

    for i in inDict.values():
        sumVar = sumVar + i 

    return sumVar == 1


RGB = {'R' : 0.2 , 'G' : 0.2, 'B' : 0.6}

print(is_balanced(RGB))

#Cau 9
def dict_intersect(inDict, inDict1) -> dict :
    
    return dict(inDict.items() & inDict1.items())



# How to use it :

Dictionary0 = {'one' : 1, 'two' : 2 }
Dictionary1 = {'one' : 1, 'three' : 2 }
print(dict_intersect(Dictionary0,Dictionary1))


#Cau 10 
def db_headings(inDict):
    
    keysInner = set()

    for key in inDict.keys():
        for inKey in inDict[key]:
            keysInner.add(inKey)
    
    return keysInner




#Cau11
def db_consistent(inDict):
    innerDictKeys = []

    for outerKey in inDict:
        tempKeys = list(inDict[outerKey].keys())
        tempKeys.sort()
        innerDictKeys.append(tempKeys)

    for i in range(1,len(innerDictKeys)):
        if len(innerDictKeys[0]) != len(innerDictKeys[i]):
            return False

        for j in range(len(innerDictKeys[0])):
            if innerDictKeys[0][j] != innerDictKeys[i][j]:
                return False

    return True
