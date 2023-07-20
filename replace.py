# Save the sentence "The!quick!brown!fox!jumped!over!the!lazy!dog!" as a string named "string"
# Reprint the string as "The quick brown fox jumped over the lazy dog" using the replace() function
# Reprint the string as "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG" using the upper() function
# Print the string in reverse

string = "The!quick!brown!fox!jumped!over!the!lazy!dog!"
print(string.replace("!", " "))
print(string.replace("!", " ").upper())
print(string[::-1])