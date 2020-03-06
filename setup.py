from setuptools import setup

setup(
    name='Deltek TS Entry',
    version='1.0',
    description=(
                 "Combined with a linux server and cron schedueler, this package "
                 "automatically fills out 8 hours M-F at 5pm to the first row of your TS."
                ),
    author='Jack Harmon',
    author_email='foo',
    packages=['Deltek TS Entry'],
    install_requires=['selenium', 'pyvirtualdisplay', 'pathlib'],
    scripts=[
            'cronExample/crontab.txt'
            ]
)

