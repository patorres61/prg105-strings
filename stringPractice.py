# This program shows various ways to manipulate strings of data

# define colors and bold text parameters
class color:
    def __init__(self):
        pass
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Title
print color.BOLD + '                                                  STRING MANIPULATION\n\n' + color.END

# Print the first letter of the following string
school = "McHenry County College"
print('The variable, school, that will be used in the following demonstrations contains the following value: \n')
print color.PURPLE + school + color.END
print('\n\nThe following is a demonstration of printing the first letter from a variable.\n')
first_letter = school[0:1]
print color.BLUE + first_letter + color.END

# print the length of the school string
print('\n\nThe following displays determining the length of a variable and printing that length.\n')
length = len(school)
print 'The length of the variable, school, is ' + color.BOLD + str(length) + color.END

# Use a while loop to print each character (including spaces) in the school variable
print('\n\nThe following displays slicing a variable into different sections - single letters in this example.\n')
length = len(school)
index = 0
while index < length:
    print color.PURPLE + school[index:index+1] + color.END
    index += 1

# Slice school into three variables, print the variables
print('\n\nThe following display demonstrates slicing a variable into different sub-strings.\n')
print color.DARKCYAN + school[0:8] + color.END
print color.DARKCYAN + school[8:14] + color.END
print color.DARKCYAN + school[15:] + color.END

# use a while statement to search for the letter "e" in the contents of the school variable
# print the index of every location with the letter "e"
# remember, you should not use the same variable twice in the same program
# so if you used the variable index, use something else
print('\n\nThe following display demonstrates searching a variable for a specific letter and displaying the index when it is found.\n')
index2 = 0

while index2 < length:
    if school[index2] == 'e':
        print color.GREEN + 'The index for an identified letter e is ' + str(index2) + color.END
    index2 += 1

# Write the code to count the number of times the letter y appears in the school variable
# print the total
print('\n\nThe following display demonstrates searching a variable for a specific letter, counting how many times the letter is found, and displaying the total.\n')
index3 = 0
count = 0
while index3 < length:
    if school[index3] == 'y':
        count += 1
    index3 += 1
print color.YELLOW + 'The total times the letter y may be found in the variable, school, is: ' + str(count) + color.END

# create a variable named college and store the upper case version of the variable school in it
print('\n\nThe following display demonstrates creating a new variable from another and storing the upper case version of the old variable in that new variable.\n')
college = school.upper()
print color.BOLD + college + color.END

# check to see if Count is in the school variable
print('\n\nThe following display demonstrates looking for a sub-string in a variable and displaying a message if the sub-string is found or not found in the variable.\n')

def find(word, string):
    index4 = 0
    length2 = len(string)
    word_found = ''
    while index4 < len(word):
        if str(word[index4:index4+length2]) == str(string):
            word_found = 'True'
            index4 = len(word)
        else:
            word_found = 'False'
        index4 += 1
    if word_found == 'True':
        print color.CYAN + '\n The string ' + str(string) + ' is found in the variable school.' + color.END
    else:
        print color.RED + '\n The string ' + str(string) + ' is NOT found in the variable school.' + color.END

string = 'Count'
print 'The variable that will be used in the following demonstration is: ' + color.BOLD + school + color.END
print 'The search string used in this demonstration will be: ' + color.BOLD + str(string) + color.END
find(school, string)

# check to see if count is in the school variable
print('\n\nIn the previous demonstration, a sub-string was found in the variable. \nIn this demonstration, the same code is used to determine that a sub-string will not be found in the variable.\n')

def find(word, string):
    word_found = ''
    index4 = 0
    length2 = len(string)
    while index4 < len(word):
        if str(word[index4:index4+length2]) == str(string):
            word_found = 'True'
            index4 = len(word)
        else:
            word_found = 'False'
        index4 += 1
    if word_found == 'True':
        print color.CYAN + '\n The string ' + str(string) + ' IS found in the variable school.' + color.END
    else:
        print color.RED + '\n The string ' + str(string) + ' is NOT found in the variable school.' + color.END

string = 'count'
print 'The variable that will be used in the following demonstration is: ' + color.BOLD + school + color.END
print 'The search string used in this demonstration will be: ' + color.BOLD + str(string) + color.END

find(school, string)
