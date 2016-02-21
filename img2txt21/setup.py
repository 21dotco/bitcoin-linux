from setuptools import setup

setup(
    name='img2txt21',
    version='0.1',
    py_modules=['img2txt21'],
        install_requires=[
            'Click',
    ],
    entry_points='''
        [console_scripts]
        img2txt21=img2txt21:img2txt21
    ''',
)
