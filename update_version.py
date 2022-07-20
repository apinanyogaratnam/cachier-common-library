def main():
    with open('Makefile', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if 'VERSION' in line:
                makefile_version = line.split('=')[1].strip()
                break

    print('makefile version', makefile_version)

    with open('setup.py', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if 'version' in line:
                setup_version = line.split('=')[1].strip().strip(',').strip("'")
                break

    print('setup.py version', setup_version)

    validate_version(makefile_version)
    validate_equivalence(makefile_version, setup_version)


def validate_version(version):
    if len(version.split('.')) != 3:
        raise ValueError('Version must be in the format x.y.z')
    for part in version.split('.'):
        if not part.isdigit():
            raise ValueError('Version must be in the format x.y.z')


def validate_equivalence(version1, version2):
    if version1 != version2:
        raise ValueError('Versions must be equivalent')


if __name__ == '__main__':
    main()
    print('Version is valid')
    exit(0)
