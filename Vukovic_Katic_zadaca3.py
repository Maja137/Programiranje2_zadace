import re

em='^[a-z]+\.[a-z]+@fpmoz.sum.ba$'
ed='^[a-z]+\d*@sum.ba$'

while True:
    mail=input('Unesite svoju elektroničku adresu: ')
    rez1=re.match(em, mail)
    eduid=input('Unesite svoj elektronički identitet: ')
    rez2=re.match(ed, eduid)

    if rez1 and rez2:
        break
print('Uspjesan unos!')
