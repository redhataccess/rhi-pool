from setuptools import find_packages, setup

with open('requirements.txt') as f:
  requirements = f.read()

setup(
  name='rhi-pool',
  version='0.1.0',
  description='Red Hat Insights tests',
  author='Anisha Narang, Kanchan Katare',
  url='https://github.com/redhataccess/rhi-pool',
  packages=find_packages(exclude=['tests*']),
  package_data={'': ['LICENSE']},
  include_package_data=True,
  install_requires=requirements,
  license='GNU GPL v3.0',
)
