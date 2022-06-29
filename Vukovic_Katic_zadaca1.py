import random

imena=['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko', 'Dario', 'Mihael',
'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan', 'Ante', 'Ivan',
'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip', 'Tomislav', 'Luka', 'Ivan',
'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana', 'Emanuel',
'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan', 'Mario',
'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan', 'Freda', 'Kristina',
'Josip', 'Lucija']

rjecnik={}

for student in imena:
    rjecnik[student]=random.randint(1,5)

for student in imena:
    print(student, rjecnik[student])

print('-------uspjeh studenata-------')
odlican=0
vrlo_dobar=0
dobar=0
dovoljan=0
nedovoljan=0

for ime in rjecnik:
    if rjecnik[ime]==5:
        odlican+=1
    elif rjecnik[ime]==4:
        vrlo_dobar+=1
    elif rjecnik[ime]==3:
        dobar+=1
    elif rjecnik[ime]==2:
        dovoljan+=1
    else:
        nedovoljan+=1

print('Odličnih ocjena ima', odlican)
print('Vrlo dobrih ocjena ima', vrlo_dobar)
print('Dobrih ocjena ima', dobar)
print('Dovoljnih ocjena ima', dovoljan)
print('Nedovoljnih ocjena ima', nedovoljan)


prolazne=odlican+vrlo_dobar+dobar+dovoljan
ukupno=odlican+vrlo_dobar+dobar+dovoljan+nedovoljan

print('Postotak prolaznosti studenata je:', round((prolazne/ukupno)*100))


