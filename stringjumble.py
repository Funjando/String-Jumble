"""
stringjumble.py
Author: Funjando
Credit: Russian who's name I cannot copy. Stack overflow.
        Heavy influence from other threads

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""

#Inputs
sen=input("Please enter a string of text (the bigger the better): ")
print('You entered "' + sen + '" ' + "Now jumble it: ")

#FullReverse
sen_dalt=(sen [::-1])
print(sen_dalt)


#WordReverse
sen_alt=sen.split(" ")
sen_alt.reverse()
print((" ").join(sen_alt))



#LetterReverse
sen_dalt_split=sen_dalt.split(" ")
sen_dalt_split.reverse()
print((" ").join(sen_dalt_split))



