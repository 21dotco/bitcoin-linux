from setuptools import setup

setup(
    name='pep8_21',
    version='0.1',
    py_modules=['pep8_21'],
        install_requires=[
            'Click',
    ],
    entry_points='''
        [console_scripts]
        pep8_21=pep8_21:pep8_21
    ''',
)
