from setuptools import setup

setup(
    name='FFW-HEY-AlarmPrediction',
    version='1.0',
    description='Einsatzvorhersage',
    author='Oliver Klengel',
    author_email='notset@example.com',
    packages=['FFW-HEY-AlarmPrediction'],
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn'
    ]
)