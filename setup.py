from setuptools import setup, find_packages

setup(name='bidding',
      description='A bidding back-end for companies ',
      long_description='A bidding back-end for companies ',
      packages=find_packages(exclude=["*tests*"]),
      package_data={'': ['*.yaml']},
      version='0.0.1',
      install_requires=[
          'gunicorn==20.1.0',
          'django==4.0.4',
          'djangorestframework==3.13.1',
          'django-cors-headers==3.11.0',
          'django-environ==0.8.1',
          'drf-yasg>=1.20.0',
          'djangorestframework-simplejwt==5.1.0',
      ],
      extras_require={
          'dev': [
              'pycodestyle==2.8.0',
              'flake8==4.0.1',
              'pytest>=7.1.2',
              'pytest-cov>=3.0.0',
              'pytest-django==4.5.2',
          ],
      }
      )
