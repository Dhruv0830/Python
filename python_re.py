#Python regular Expressions

import re
a = "charlie chaplin coa and the chocolate factory"
b = "nitish@gmail.com"
c = "hello"
d = "xyz,yz,xyzz,xyyz,xxzzy,zyz,xxyyzz,xyzxyz"

# \ -> escape character - used to escape special characters in regex patterns

match = re.search(r"\.", b)

# [] -> matches any one of the characters inside the brackets

match = re.search(r"[@]", b)
match = re.search(r"[i]", b)
match = re.search(r"[l]", c)
match = re.findall(r"[l]", c)#Returns a list of all occurrences of the pattern in the string (not the index but the actual character)

# ^ -> matches the start of a string

match = re.search(r"^c", b) #None because b starts with n
match = re.search(r"^nit", b) #Matches because b starts with nit
match = re.search(r"^c", a) #Matches because a starts with c

# $ -> matches the end of a string

match = re.search(r"y$", a) #Matches because a ends with y
match = re.search(r"y$", b) #None because b ends with m

# . -> matches any character except a newline

match = re.findall(r"c.a", a) #Matches because it finds "cha" in "charlie" "coa" and "cho" in "chocolate"

# | -> matches either the pattern before or the pattern after the operator

match = re.search(r"cha|fac", a) #Matches because it finds "charlie" in a and "factory" in a

# ? -> matches 0 or 1 occurrence of the preceding character or group

re.findall(r"xy?z", d) #Matches "xyz" and "xz" because y is optional in the pattern

# * -> matches 0 or more occurrences of the preceding character or group

re.findall(r"xy*z", d) #Matches "xyz", "xz", "xyyz", "xxyz" because y can occur 0 or more times in the pattern

# + -> matches 1 or more occurrences of the preceding character or group

re.findall(r"xy+z", d) #Matches "xyz", "xyyz", "xxyz" because y must occur at least once in the pattern

# {} -> matches exactly n occurrences of the preceding character or group

re.findall(r"xy{2}z", d) #Matches "xyyz" because y must occur exactly 2 times in the pattern
re.findall(r"x{2,4}z", d) #Matches "xxyyzz" because x must occur 2 to 4 times in the pattern

# () -> groups the enclosed pattern together
match = re.findall(r"(x|y)yz", d) #Matches because it finds "xyz" and "yyz" in d

##Special Sequences - do not match for the actual character in the string instead tells the specific location in the string where the match is to be found

#\A -> matches the start of the string

a = "harry Potter"

match = re.search(r'\Ahar',a)

#\b -> matches the empty string at the beginning or end of a word

match = re.search(r'\bPot', a) #Matches because it finds "Pot" at the beginning of the word "Potter"

match = re.search(r'\bhar', a) #Matches because "har" is at the beginning of a word in a

match = re.search(r'h\b', a) #None because "h" is not at the end of a word in a

match = re.search(r'er\b',a) #Matches because it finds "er" at the end of the word "Potter"

#\B -> matches the empty string not at the beginning or end of a word

match = re.search(r'\BPot', a) #None because "Pot" is at the beginning of a word in a

match = re.search(r'er\B') #None because "er" is at the end of a word in a

#\d -> matches any digit

match = re.search(r"\d", "abc123def456") #Matches "1",

match = re.findall(r"\d", "abc123def456") #Matches "1", "2", "3", "4", "5", "6"

#\D -> matches any non-digit character

match = re.findall(r"\D", "abc123def456") #Matches "a", "b", "c", "d", "e", "f"

#\s -> matches any whitespace character (spaces, tabs, newlines)

match = re.findall(r"\s", "Hello World! This is a test.") #Matches the spaces between the words

#\S -> matches any non-whitespace character

match = re.findall(r"\S", "Hello World! This is a test.") #Matches all the characters except the spaces like "H", "e", "l", "o", "W", "r", "d", "!", "T", "h", "i", "s", "a", "t", "e", "s", "t", "."

#\w -> matches any alphanumeric character (letters, digits, and underscores)

match = re.findall(r"\w", a) #Matches all the alphanumeric characters in a string

#\W -> matches any non-alphanumeric character

match = re.findall(r"\W", a) #Matches all the non-alphanumeric characters in a string like space and punctuation

#\Z -> matches the end of the string

match = re.search(r"ter\Z", a) #Matches because it finds "ter" at the end of a string in a


#Regex sets

#[atx] -> matches any one of the characters a, t, or x

#[^atx] -> matches any character that is not a, t, or x

#[a-z] -> matches any lowercase letter from a to z

#[1234] -> matches any one of the characters 1, 2, 3, or 4

#[0-9] -> matches any digit from 0 to 9

#[0-7][0-9] -> matches any two-digit number from 00 to 79

#[a-zA-Z] -> matches any uppercase or lowercase letter

#[+|$] -> matches any one of the characters +, |, or $


#Funtions in re module

#re.search() -> searches for the first occurrence of the pattern in the string and returns a match object if found, otherwise returns None

#re.findall() -> returns a list of all occurrences of the pattern in the string

#re.compile() -> compiles a regular expression pattern into a regex object, which can be used for matching using its match(), search(), and findall() methods

string = "The rain in Spain stays mainly in the plain."
pattern = re.compile(r"\b\w+ain\b") #Compiles a regex pattern to match words that end with "ain"
matches = pattern.findall(string) #Finds all occurrences of the pattern in the string using the compiled regex object
print(matches) #Output: ['rain', 'Spain', 'plain']

#re.sub() -> replaces occurrences of the pattern in the string with a specified replacement string

#re.split() -> splits the string into a list of substrings based on the occurrences of the pattern

#re.escape() -> escapes all special characters in the pattern, making it safe to use in a regex pattern without interpreting them as special characters

#re.subn() -> replaces occurrences of the pattern in the string with a specified replacement string, but also returns the number of substitutions made along with the modified string as a tuple (new_string, number_of_substitutions)

#Match Object Methods

#It contains all the infomation about the search and the result. If there is no match then it returns None

match = re.search(r"ain", string) #Searches for the first occurrence of "ain" in the string and returns a match object

print(match) #Output: <re.Match object; span=(4, 7), match='ain'> - it shows the span of the match in the string and the actual matched text

print(match.re) #Returns the regex pattern used for the search

print(match.string) #Returns the original string that was searched

print(match.group()) #Returns the actual matched text

print(match.start()) #Returns the starting index of the match in the string

print(match.end()) #Returns the ending index of the match in the string

print(match.span()) #Returns a tuple containing the starting and ending indices of the match in the string



#Phone number validation using regex

phone = "123-456-7890"
if re.search(r"\d{3}-\d{3}-\d{4}", phone):
    print("Valid phone number")
else:
    print("Invalid phone number")


#Email validation using regex
email = "john@gmail.com david.989@gmail.com john@.com"

print(re.findall(r"[\w._%]{0,20}@[\w-].[A-Za-z]{2,3}", email)) #Matches valid email addresses in the string and returns them as a list

