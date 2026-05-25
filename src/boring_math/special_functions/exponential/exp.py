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

"""
.. admonition:: Exponential function

    Complex and real valued implementations of the exponential function.

"""

from cmath import inf, isinf
from math import ceil, floor, nan
from ..constants import e, pi
from ..trigonometry.trig import sin, cos

__all__ = ['exp0', 'exp', 'cexp0', 'cexp']

two_pi = 2.0*pi

# Minimum depth required to agree with stdlib exp implementations.
min_depth: int = 22


def exp0(x: float, /, n: int = min_depth) -> float:
    """
    .. admonition:: Real exponential function about x = 0

        Best if -1 <= x <= 1 for n >= 22.

        :param x: Independent variable.
        :param n: Terms in expansion, must have n >= 2.
        :returns: Value of eˣ expanded about x = 0.

    """
    d = float(n)
    accum = x / d
    d -= 1.0
    while d >= 0.5:
        accum = x / d * (1 + accum)
        d -= 1.0
    return 1.0 + accum


def shift0(x: float) -> float:
    if x >= 0:
        shifted = x % 1.0
    else:
        shifted = x % -1.0
    return shifted


def exp(x: float, /, n: int = min_depth) -> float:
    """
    .. admonition:: Real exponential function about x = 0.

        Valid for extended value floating point arguments.

        :param x: Independent variable.
        :param n: Terms in expansion, must have n >= 2.
        :returns: Value of eˣ otherwise nan if x = nan.

    """
    try:
        if x >= 0.0:
            factor = e ** floor(x)
        else:
            factor = e ** ceil(x)
    except OverflowError:
        return inf if x == inf else 0.0
    except ValueError:
        return nan
    else:
        return exp0(shift0(x), n=n) * factor


def cexp0(z: complex, /, n: int = min_depth) -> complex:
    """
    .. admonition:: Complex exponential function about z = 0

        :param z: Independent variable.
        :param n: Terms in expansion, must have n >= 2.
        :returns: Value of eᶻ centered at z = 0

        .. tip::

            Best if |z| <= 1 and n >= 22.

    """
    d = float(n)
    accum = z / d
    d -= 1.0
    while d >= 0.5:
        accum = z / d * (1 + accum)
        d -= 1.0
    return 1.0 + accum


def cexp(z: complex, /, n: int = min_depth) -> complex:
    """
    .. admonition:: Exponential function for all complex z.

        :param z: Independent variable.
        :param n: Terms in expansion, must have n >= 2.
        :returns: Value of eᶻ.
        :raises ValueError: When z is infinite but re(z) is not.

        .. note::

            Complex exp(z) has an essential singularity at infinity.

            If given an infinite argument, phase information is given
            in the returned, possibly infinite, value consistent with
            Python's stdlib cmath.exp implementation.

    """
    x = z.real
    y = z.imag

    if not isinf(z):
        y %= two_pi
        return exp(x) * (cos(y) + 1j*sin(y))

    if isinf(y):
        if not isinf(x) or x == inf:
            msg = 'boring_math.special_functions.exponential.cexp: domain error'
            raise ValueError(msg)
        return 0+0j
    else:
        if (cos_y := cos(y)) == 0.0:
            return exp(x) * 1j*sin(y)
        if (sin_y := sin(y)) == 0.0:
            return exp(x) * cos(y)
        return exp(x) * (cos_y + 1j*sin_y)
