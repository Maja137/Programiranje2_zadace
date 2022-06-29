from csv import reader
with open('rezultati.csv', 'r', encoding='utf8') as read_obj:
    csv_reader=reader(read_obj)
    studenti=list(map(tuple, csv_reader))
    #print(studenti)

for ime, prezime, bodovi in studenti:
    studenti.sort(key=lambda tup:tup[1])
print(studenti)

rjecnik={
    'izvrstan':0,
    'vrlo dobar':0,
    'dobar':0,
    'dovoljan':0,
    'nedovoljan':0
    }

for ime, prezime, bodovi in studenti:
    if int(bodovi)<50:
        rjecnik['nedovoljan']+=1
    elif int(bodovi)>49 and int(bodovi)<66:
        rjecnik['dovoljan']+=1
    elif int(bodovi)>65 and int(bodovi)<81:
        rjecnik['dobar']+=1
    elif int(bodovi)>80 and int(bodovi)<91:
        rjecnik['vrlo dobar']+=1
    else:
        rjecnik['izvrstan']+=1

print('-------Broj ostvarenih ocjena-------')
for element in rjecnik:
    print(element, rjecnik[element])
