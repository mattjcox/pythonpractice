pyg = 'ay'

def pyglatin():
  original = input('Enter a word:')
  if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print (new_word)
    pyglatin()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
  else:
    print ('empty or not a word')
    
pyglatin()