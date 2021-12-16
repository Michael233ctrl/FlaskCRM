import os
from setuptools import setup, find_packages


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name='Flask CRM',
    version='1.0',
    author='Mikhail Bessarabenko',
    author_email='mikhail.bessarabenko@gmail.com',
    description='A web application that allows you to manage '
                'your company and interact with customers.',
    long_description=read('README.md'),
    url='https://github.com/Michael233ctrl/FlaskCRM.git',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==2.0.2',
        'Flask-Migrate==3.1.0',
        'Flask-RESTful==0.3.9',
        'Flask-SQLAlchemy==2.5.1',
        'Flask-WTF==1.0.0',
        'marshmallow-sqlalchemy==0.25.0',
        'psycopg2-binary==2.9.2',
    ]
)
