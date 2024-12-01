text=input(f'Paste the text half here (only letters please)')
numbers=input(f'Paste the number half here ( *NO* letters please)')

text=text.replaced(' ','')
numbers=numbers.replaced(' ','')

#remove spaces from the cipher so as to be able to aline them
if len(text) = len(numbers):
   print('Good to GO !')

#splice them 
merged_text=""
for index in range(len(text)):
   merge=f'{text[index]}{numbers[index]}'

#make it all one thing to work for dad's program to put it into plain text that prefers them the traditional polybius way with only one type of character
merged_text=merged_text.replace('a','1').replace('b','2').replace('c','3').replace('d','4').replace('e','5')
print (merged_text)
