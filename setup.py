from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='aninfo',
    version='1.0.0',
    packages=find_packages(exclude=['tests*']),
    install_requires=requirements,
    author='adogecheems',
    author_email='adogecheems@outlook.com',
    description='A library for searching anime information from various sources',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/adogecheems/an-info',
    license='AGPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    keywords='search anime information anime-info anime-search anime-api api info bangumi bangumi-api',
)
