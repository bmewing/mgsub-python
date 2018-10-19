# MIT License

# Copyright (c) 2018 Mark Ewing

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from setuptools import setup

SHORT_DESCRIPTION = """
A safe, multiple, simultaneous string substitution function
""".strip()

LONG_DESCRIPTION = """
You have a string you want to make substitutions on. You want to make many different substitutions at the same time and you want them done in a safe way.

For example, you want to shift each word in "hey, how are you?" to the left by replacing "hey" with "how", "how" with "are, etc.

This is a lightweight, pure python function with no dependencies to avoid package bloat when being used.
"""

VERSION = '1.0.0'

URL = 'https://github.com/bmewing/mgsub-python'

setup(name = 'mgsub',
    version = VERSION,
    description = SHORT_DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    url = URL,

    author = 'Mark Ewing',
    license = 'MIT License'
)
