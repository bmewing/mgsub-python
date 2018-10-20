from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

version = {}
with open("mgsub/version.py") as f:
    exec(f.read(), version)

setup(name='mgsub',
      version=version['__version__'],
      description='A safe, multiple, simultaneous string substitution function',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author = 'Mark Ewing',
      author_email='b.mark@ewingsonline.com',
      url='https://github.com/bmewing/mgsub-python',
      packages=['mgsub'],
      tests_require=['pytest'],
      keywords=['string', 'substitution', 'regex', 'regular expression'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ]
)
