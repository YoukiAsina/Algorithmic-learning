name_list=['ren','wang','li']
print('Ren can not attend the party. ')
del name_list[0]
name_list.append('liu')
name_list.insert(0,'gao')
name_list.insert(2,'jiang')
name_list.append('zhao')
print(name_list)
print(f'I invite {len(name_list)} people. ')
name1=name_list.pop()
name2=name_list.pop()
name3=name_list.pop()
name4=name_list.pop()
print(f'{name1.title()}, I am sorry to tell you about the party. ')
print(f'{name2.title()}, I am sorry to tell you about the party. ')
print(f'{name3.title()}, I am sorry to tell you about the party. ')
print(f'{name4.title()}, I am sorry to tell you about the party. ')
print(f'{name_list[0].title()}, you can attend the party. ')
print(f'{name_list[1].title()}, you can attend the party. ')
del name_list[0]
del name_list[-1]
print(name_list)