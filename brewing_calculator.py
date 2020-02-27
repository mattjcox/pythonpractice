#!/usr/bin/env python
fermentables = {
  'Acid Malt' : {
    'name' : 'Acid Malt', 
    'origin' : 'Germany', 
    'mash' : True, 
    'color-lovibond' : 3, 
    'power' : 0,
    'potential' : 1.027,
    'ppg' : 27,
    'max-percentage' : 10,
    'notes' : 'Acid malt contains acids from natural lactic acids. Used by German brewers to adjust malt PH without chemicals to adhere to German purity laws. Also enhances the head retention.'
  },
  'Acidulated Weyermann' : {
    'name' : 'Acidulated Weyermann', 
    'origin' : 'Germany', 
    'mash' : False, 
    'color-lovibond' : 1.8, 
    'power' : 0,
    'potential' : 1.03,
    'ppg' : 30,
    'max-percentage' : 10,
    'notes' : 'Used in Germany to lower PH levels without resorting to chemicals. Lowers mash pH levels, lightens color, improves flavor stability.'
  },
  'Pale Malt (2 Row) UK' : {
    'name' : 'Pale Malt (2 Row) UK', 
    'origin' : 'UK', 
    'mash' : True, 
    'color-lovibond' : 3, 
    'power' : 45,
    'potential' : 1.036,
    'ppg' : 36,
    'max-percentage' : 100,
    'notes' : 'Base malt for all English beer styles Lower diastatic power than American 2 Row Pale Malt.'
  }
}

total_grain_bill = 0
i = 0
fermentable_number = int(input('How many fermentables?: '))
while i < fermentable_number:
  fermentable_input = input('Enter fermentable %s: ' % fermentable_input)
  fermentable1_kg = float(input('How many kg?: '))
    a = 2
print (fermentable1)
print (fermentables[fermentable1])
#print ('Potential for %s = %s' % (fermentable1, fermentables[fermentable1]['potential']))
total_grain_bill += fermentable1_kg