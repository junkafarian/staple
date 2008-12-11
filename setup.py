from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='staple',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='junkafarian',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'jinja2',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
