﻿from __future__ import print_function
print('hello world')
aa = raw_input("I'm sorry, I don't understand. Choose your language :")
Say_hi = { 'Francais':"J'aime Git", 'English':"I <3 Git", 'Deutsch':'Ich liebe Git', 'Italiano':'Ti amo Git'}
Say_tu = { 'Francais':"Git t'aime aussi !", 'English':"And Git loves you back", 'Deutsch':'Git liebt dich auch', 'Italiano':'Git ti ama'}
print(Say_hi[aa].lower())
print(Say_tu[aa].lower())
