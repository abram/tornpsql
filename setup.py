from setuptools import setup

version = '0.0.3'

setup(name='tornpsql',
      version=version,
      description="PostgreSQL handler for tornado",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='tornado psql postgres postgresql sql',
      author='@iopeak',
      author_email='steve@stevepeak.net',
      url='https://github.com/stevepeak/tornpsql',
      license='Apache v2.0',
      packages=['tornpsql'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )