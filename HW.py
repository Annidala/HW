from __future__ import print_function
aa = raw_input('Choose your language :')
Say_hi = { 'Francais':"J'aime Git", 'English':"I <3 Git", 'Deutsch':'Ich liebe Git', 'Italiano':'Ti amo Git}
Say_tu = { 'Francais':"Git t'aime", 'English':"And Git loves you back", 'Deutsch':'Git liebt dich', 'Italiano':'Git ti ama'}
print(Say_hi[aa].lower())
print(Say_tu[aa].lower())
