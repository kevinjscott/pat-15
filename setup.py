from setuptools import setup, find_packages

setup(
    name='golf_tournament_scraper',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'beautifulsoup4',
        'requests',
        'openai',
        'tenacity',
        'serpapi'
    ],
    entry_points='''
        [console_scripts]
        golf_tournament_scraper=src.main:main
    ''',
)