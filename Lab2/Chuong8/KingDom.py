kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi','Animalia']
# bài 1
#câu a
print(kingdoms[0])
#câu b
print(kingdoms[5])
#câu c
print(kingdoms[:3])
#câu d
print(kingdoms[2:5])
#câu e
print(kingdoms[4:])
#câu f
print(kingdoms[1:0])



# bài 2
#câu a
print(kingdoms[-6])
#câu b
print(kingdoms[-1])
#câu c
print(kingdoms[-6:-3])
#câu d
print(kingdoms[-4:-1])
#câu e
print(kingdoms[-2:])
#câu f
print (kingdoms[-1:-2])



# bai 3
appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']
#câu a
appointments.append('16:30')
#câu b 
appointments += ['16:30']
#câu c  new list
my_list = []

         
  
# bài 4 
# câu a
horsemen =  [4353, 2314, 2956, 3382, 9362, 3900]
# câu b
horsemen.remove(3382)
print ("List duoc remove: ", horsemen)

#câu c
for i in horsemen: 
      if i == 9362:
          print ("i :" ,i )

#câu d
horsemen.append(5566)
horsemen.append(1830)

print(horsemen)

# câu e
horsemen.reverse()
print ("horsemen bi dao nguoc : ", horsemen)

# câu f 
horsemen.sort()
print ("horsemen duoc sap xep: ", horsemen)

# bài 6 
#câu a 
listCelsius =  [25.2,16.8, 31.4, 23.9, 28, 22.5, 19.6 ]
# câu b
listCelsius.sort()
print ("horsemen duoc sap xep: ", listCelsius)

# cau c
cool_temps =[]
warm_temps =[]
for i in listCelsius: 
      if i > 20:
          cool_temps.append(i)
print(cool_temps)
for i in listCelsius: 
      if i < 20:
          warm_temps.append(i)
print(warm_temps)

# bai 7
import stLasameFirst
print(stLasameFirst.st_lasame_first([3, 4, 2]))
# bai 8
import isLonger
print(isLonger.is_longer([1, 2, 3], [4, 5]))

# bai 9
values = [0, 1, 2]
values[1] = values
print(values)

# bai 10 
variable =  [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]
#cau a
lst2 = [item[0] for item in variable]
print(lst2)
# cau b
lst1 = [item[-1] for item in variable]
print(lst1)
# cau c
print(variable[0][0])

# cau d
print(variable[1][0])

# cau e
print(variable[0][1:])
#cau f
print(variable[1][0:2])

# bai 11


