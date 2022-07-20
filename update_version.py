import sys


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
    version = makefile_version

    if sys.argv[1] == '--patch':
        version = update_patch_version(version)
    elif sys.argv[1] == '--minor':
        version = update_minor_version(version)
    elif sys.argv[1] == '--major':
        version = update_major_version(version)
    else:
        raise ValueError('Invalid argument')


def validate_version(version):
    if len(version.split('.')) != 3:
        raise ValueError('Version must be in the format x.y.z')
    for part in version.split('.'):
        if not part.isdigit():
            raise ValueError('Version must be in the format x.y.z')


def validate_equivalence(version1, version2):
    if version1 != version2:
        raise ValueError('Versions must be equivalent')


def update_patch_version(version):
    parts = version.split('.')
    parts[2] = str(int(parts[2]) + 1)
    return '.'.join(parts)


def update_minor_version(version):
    parts = version.split('.')
    parts[1] = str(int(parts[1]) + 1)
    parts[2] = '0'
    return '.'.join(parts)


def update_major_version(version):
    parts = version.split('.')
    parts[0] = str(int(parts[0]) + 1)
    parts[1] = '0'
    parts[2] = '0'
    return '.'.join(parts)


if __name__ == '__main__':
    main()
    print('Version is valid')
    exit(0)
