#changes ever vowel in the input word to: 'uwu' for small letter/ 'UWU' for capital letter
def translate(word):
    translated = ''
    
    # [' '+ c = c | c + uwu = cuwu | cuwu + t = cuwut]
    for letter in word:
        if letter in 'AEIOU':
            #capital vowel found
            translated += 'UWU'
        elif letter in 'aeiou':
            #small vowel found
            translated += 'uwu'
        else:
            #vowel not found
            translated += letter
    return translated

new_word = translate(input('enter your word: '))
print('your word is:', new_word)