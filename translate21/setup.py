from setuptools import setup

setup(
    name='translate21',
    version='0.1',
    py_modules=['translate21'],
        install_requires=[
            'Click',
    ],
    entry_points='''
        [console_scripts]
        translate21=translate21:cli
    ''',
)
