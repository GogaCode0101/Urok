
#Создаемсловарьснесколькимипарамиключ-значение
my_dict={'Alex':89238657482,'Roma':89132476571,'Oleg':89632417715}
print('Dict:',my_dict)

#Выводимзначениепосуществующемуключу
existing_value=my_dict.get('Oleg')
print("Existingvalue:",existing_value)

#Выводимзначениепоотсутствующемуключубезошибки
not_existing_value=my_dict.get('Masha')
print("Notexistingvalue:",not_existing_value)

#Добавляемещёдвепары
my_dict['Gleb']=89522175814
my_dict['Lena']=89028156417

#Удаляемоднупаруивыводимзначениеизэтойпары
deleted_value=my_dict.pop('Roma',None)
print("Deletedvalue:",deleted_value)

#Выводимизмененныйсловарь
print("Modifieddictionary:",my_dict)

print()

my_set={True,14,'Lake',13,14,True,'Lake'}
print('Set:',my_set)
my_set.add(5)
my_set.add(7)
my_set.discard(14)
print('Modifiedset:',my_set)




