import xml.etree.ElementTree as ET
mytree = ET.parse('cars.xml')
myroot = mytree.getroot()

for x in myroot.findall('Cars'):
    print(x.find('car').text)

sumIt = 0
count = 0
for x in myroot.findall('Cars'):
    sumIt = sumIt + int(x.find('cost').text)
    count = count + 1

avg = sumIt/count

print(avg)


mytree = ET.parse('characters.xml')
myroot = mytree.getroot()

heroes = myroot.find('Superheroes')
villains = myroot.find('Villains')

for x in heroes.findall('Superhero'):
    print(x.find('RealName').text)

for x in villains.findall('Villain'):
    print(x.find('RealName').text)
