"""import os
with open('result.txt', 'a') as f:
    for current_dir, dirs, files in os.walk('adds'):
        if list(filter(lambda x: x.endswith('.txt'), files)):
            f.write('{}\n'.format(current_dir))
            f.write('{}\n'.format(files))"""
import os
for root, dirs, files in os.walk("adds"):
    for file in files:
        if file.endswith(".txt"):
             print(os.path.join(root, file))
             path = r"C:\\Users\\Виктория Иваненко\\Desktop\\project\\" + str(os.path.join(root, file))
             f = open(path, 'r')
             print(f.read())
            
