from bs4 import BeautifulSoup
try:
    with open('html_text.txt', 'r') as file:
        file_content = file.read()
    print(file_content)
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")

html_soup = BeautifulSoup(file_content, 'html.parser')

print(html_soup.text)


print(html_soup.prettify(formatter='html', maxlevel=3))

