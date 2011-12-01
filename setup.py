from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='modifeatures',
      version=version,
      description="",
      long_description="",
      classifiers=[],
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'psycopg2',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
