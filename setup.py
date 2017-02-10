#!/usr/bin/env python

from setuptools import setup

setup(name='tap-marketo',
      version='0.1.1',
      description='Taps Marketo data',
      author='Stitch',
      url='https://github.com/stitchstreams/tap-marketo',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_marketo'],
      install_requires=['stitchstream-python==0.6.0'
                        'requests==2.12.4',
                        'backoff==1.3.2',
                        'python-dateutil==2.6.0',
                        'arrow==0.10.0'],
      entry_points='''
          [console_scripts]
          tap-marketo=tap_marketo:main
      ''',
      packages=['tap_marketo'],
      package_data = {
          'tap_marketo': [
            'lead_activities.json',
            'lead_activity_types.json'
          ]
      }
)