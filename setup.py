import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='cachier-common-library',
    version='0.1.0',
    author='apinanyogaratnam',
    author_email='apinanapinan@icloud.com',
    description='A python library for common classes and functions used to build cachier applications',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/apinanyogaratnam/cachier-common-library',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10.4',
    install_requires=[],
)
