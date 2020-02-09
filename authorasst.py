# Type all other functions here

def print_menu(usrStr):

    print('MENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Fix capitalization\nr - Replace punctuation\ns - Shorten spaces\nq - Quit\n')
    menu_choice = input('Choose an option:\n')
    while (menu_choice != 'c' and menu_choice != 'w' and menu_choice != 'f' and menu_choice != 'r' and menu_choice != 's' and menu_choice != 'q'):
        menu_choice = input('Choose an option:\n')
    return menu_choice

def get_num_of_non_WS_characters(inputStr):

    white_space = 0
    for character in inputStr:
        if(character == ' ' or character == '\t'):
            white_space += 1
    return (len(inputStr) - white_space)

def get_num_of_words(inputStr):

    words = inputStr.split()
    return len(words)

def fix_capitalization(inputStr):

    capitalization = 0
    char_list = []
    for character in inputStr:
        char_list.append(character)
    
    if(char_list[0].islower()):
        char_list[0] = inputStr[0].upper()
        capitalization += 1
    
    x = 0
    keep_cappin = 'false'
    for character in char_list:
        if(keep_cappin == 'true' and character != ' ' and character != '\t'):
            char_list[x] = inputStr[x].upper()
            capitalization += 1
            keep_cappin = 'false'
        if(character == '.' or character == '!' or character == '?'):
            keep_cappin = 'true'
        x += 1

    revised_string = ''
    for character in char_list:
        revised_string = revised_string + character

    print('Number of letters capitalized:', capitalization, end = '\n')
    print('Edited text:', revised_string, end='\n\n')
    return revised_string, capitalization
  
def replace_punctuation(inputStr, exclamationCount, semicolonCount):

    exclamationCount = 0
    semicolonCount = 0
    questionCount = 0
    periodCount = 0
    char_list = []
    for character in inputStr:
        char_list.append(character)  
    x = 0
    for character in char_list:
        if(character == '!'):
            char_list[x] = '.'
            exclamationCount += 1
        elif(character == ';'):
            char_list[x] = ','
            semicolonCount += 1
        elif(character == '?'):
            char_list[x] = ';)'
            questionCount += 1
        elif(character == '.'):
            char_list[x] = '$$$'
            periodCount += 1
        x += 1
      
    revised_string = ''
    for character in char_list:
        revised_string = revised_string + character

    print('Punctuation replaced', end = '\n')
    print('Exclamation Point Count:', exclamationCount, end='\n')
    print('Semicolon Count:', semicolonCount, end='\n')
    print('Question Mark Count:', questionCount, end='\n')
    print('Period Count:', periodCount, end='\n')
    print('Edited text:', revised_string, end='\n\n')
    return revised_string
def shorten_space(inputStr):

    words = inputStr.split()
    revised_string = ''
    for word in words:
        if revised_string == '':
            revised_string = word;
        elif (revised_string != ''):
            revised_string = revised_string + ' ' + word
    print('Edited text:', revised_string, end='\n\n')
    return revised_string
if __name__ == '__main__':
    inputStr = str(input('Enter a sample text:\n'))
    print('\nYou entered:', inputStr, end='\n\n')
    chosen_option = ''
    while(chosen_option != 'q'):
        chosen_option = print_menu(inputStr)
        if (chosen_option == 'c'):
            print('Number of non-whitespace characters:',get_num_of_non_WS_characters(inputStr),end='\n\n')
        elif (chosen_option == 'w'):
            print('Number of words:', get_num_of_words(inputStr), end = '\n\n')
        elif (chosen_option == 'f'):
            fix_capitalization(inputStr)
        elif (chosen_option == 'r'):
            replace_punctuation(inputStr, 0, 0)
        elif (chosen_option == 's'):
            shorten_space(inputStr)
