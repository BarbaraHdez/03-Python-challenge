#Open file
file = '/Users/barbarahernandezrivero/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv'
with open(file,'r') as text:
    print(text)
    lines = text.read()
    print(lines)
    