from setuptools import setup

setup(
    name='Deltek_TS_Autofill',
    version='1.0',
    description=(
                 "Combined with a linux server and cron schedueler, this package "
                 "automatically fills out 8 hours M-F at 5pm to the first row of your TS."
                ),
    author='Jack Harmon',
    author_email='foo',
    packages=['Deltek_TS_Autofill'],
    install_requires=['selenium', 'pyvirtualdisplay', 'pathlib'],
    scripts=[
            'crontab.txt'
            ]
)

