print("Welcome to my book title counter!")
answer = input("Do you want me to count the characters of a book title for you? (yes/no) ").lower()
if answer =="yes":
  book = input("What is the title of the book?")
length = str(len(book))
print("There are " ,length, " symbols in the title " ,book, " including the spaces.")
else:
  input("Ok")
