from setuptools import setup, find_packages

setup(
    name='nfl-player-stats',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4==4.6.0',
        'requests'
    ],
)
