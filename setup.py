from setuptools import setup, find_packages
import sys, os

version = '0.2.2'

setup(name='staple',
      version=version,
      description="A script for publishing static websites from Jinja templates",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='junkafarian',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      package_data = {'staple': ['*.sample', 'templates/*.*', 'templates/one/*.*'],},
      zip_safe=False,
      install_requires=[
          'jinja2',
          'nose',
      ],
      entry_points="""
      [console_scripts]
      staple = staple.scripts:main
      [paste.paster_create_template]
      staple = staple.paster:StapleSiteTemplate
      """,
      )
