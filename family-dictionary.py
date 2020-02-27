family1 = {
  0: {
   'name':'matt',
    'age':43,
    'role':'father'
     }, 
  1: {
   'name':'doreen',
    'age':45,
    'role':'mother'    
  },
  2: {
   'name':'tyler',
    'age':9,
    'role':'son'    
  },
}
n = 1
o = 3
for n in range(n,o):
  new_name = raw_input ('Name?')
  new_age = raw_input ('Age?')
  new_role = raw_input ('Role?')
  family_count = len(family1)
  new_family_index = family_count + 1
  family1[new_family_index] ={'name':new_name,'age':new_age,'role':new_role}
  more = raw_input ('Add another? (Y,N)')    


for i in family1:
  print ('%s is %s years old') % (family1[i]['name'],str(family1[i]['age']))

print family1