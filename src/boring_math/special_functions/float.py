# Copyright 2016-2025 Geoffrey R. Scheller
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Real valued

Real valued special functions.

"""

from math import pi, floor, ceil
from .float0 import exp0, sin0, cos0, tan0

__all__ = ['exp', 'sin', 'cos', 'tan']

maxdepth = 20
mindepth = 20

two_pi = 2.0*pi
pi_half = pi/2.0
e = exp0(1)

def shift0(x: float) -> float:
    shifted = x % (two_pi)
    if shifted > pi:
        shifted = -1.0*(shifted - pi)
    return shifted

def shift1(x: float) -> float:
    shifted = x % pi
    if shifted > pi_half:
        shifted = -1.0*(shifted - pi_half)
    return shifted

def shift2(x: float) -> float:
    if x > 0:
        shifted = x % 1.0
    elif x < 0:
        shifted = x % -1.0
    else:
        shifted = x
    return shifted


def exp(x: float, /, n: int = mindepth) -> float:
    """Partially factored Taylor expansion of exp about x = 0.

    :param x: independent variable
    :param n: terms in expansion, must have ``n >= 20``
    :returns: Value of ``eˣ``

    """
    if x > 0:
        factor = e**floor(x)
    elif x < 0:
        factor = e**ceil(x)
    else:
        factor = 1.0
    return exp0(shift2(x), n=n) * factor

def sin(x: float, /, n: int = maxdepth) -> float:
    """Partially factored Taylor expansion of sine about x = 0.

    :param x: angle in radians
    :param n: terms in expansion, must have 2 <= n <= 20
    :returns: Taylor series expansion of sine(x) centered at x = 0

    """
    return sin0(shift0(x), n=n)


def cos(x: float, /, n: int = maxdepth) -> float:
    """Partially factored Taylor expansion of cosine about x = 0.

    :param x: angle in radians
    :param n: terms in expansion, must have 2 <= n <= 20
    :returns: Taylor series expansion of cosine(x) centered at x = 0

    """
    return cos0(x % (two_pi), n=n)


def tan(x: float, /, n: int = maxdepth) -> float:
    """Tangent centered about x = 0.

    :param x: angle in radians
    :param n: terms in expansion, must have 2 <= n <= 20
    :returns: sin0(x)/cos0(x)

    """
    return tan0(shift1(x), n=n)
