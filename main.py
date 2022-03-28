import os
import re

initial_path = 'C:\\Users\\lepae\\Documents\\IGTI\\Programação\\Udemy - Complete Python 3 Bootcamp\\Complete-Python-3-Bootcamp-master\\Complete-Python-3-Bootcamp-master\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise\\extracted_content'

for dirpath, dirname, filesname in os.walk(initial_path):

    for f in filesname:

        if f.endswith('.txt'):
            # current path
            current_path = os.path.join(dirpath, f)
            # open
            o = open(current_path, 'r')
            # read
            text = o.read()
            # search
            phone = re.search(r'\d{3}-\d{3}-\d{4}', text)

            if phone:
                print(f'The phone number is: {phone.group()}')
