#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='music-collection-coursework',
    version='0.0.1',
    packages=["music_collection"],
    url='https://github.com/',
    license='Apache-2.0',
    author='Сутягина Дарья Денисовна',
    author_email='dsutiagina@gmail.com',
    description='Учебный пакет для управления музыкальной коллекцией.',
    include_package_data=True,
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "music-collection = music_collection.cli:main",
        ]
    },
)