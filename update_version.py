with open('Makefile', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if 'VERSION' in line:
            version = line.split('=')[1].strip()
            break

print('makefile version', version)
