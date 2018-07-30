from setuptools import setup, find_packages


def get_version():
    return '0.1'


setup(
    name='flagon',
    version=get_version(),
    packages=find_packages(exclude=['tests', 'sample_api']),
    install_requires=[
        'flask==0.12.2',
        'Flask-Migrate==2.1.1',
        'flask-marshmallow==0.8.0',
        'Flask-SQLAlchemy==2.3.1',
        'marshmallow-sqlalchemy==0.13.2',
        'psycopg2==2.7.4',
        'structlog==18.1.0',
        'python-json-logger==0.1.8'
    ],
    entry_points={
    },
    test_suite="tests",
    description='Package for Flask wiring.'
)