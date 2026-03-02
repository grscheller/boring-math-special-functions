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

"""Floating point special functions about a point."""

from math import ceil, floor, pi
from .trig import sin as sinf, cos as cosf

__all__ = ['exp0', 'exp', 'cexp0', 'cexp']

mindepth = 22

two_pi = 2.0 * pi
jay = 0.0 + 1.0j


def exp0(x: float, /, n: int = mindepth) -> float:
    """Partially factored Taylor expansion of exp about ``x = 0``.

    .. note::

        Best if ``-1 <= x <= 1``.

    :param x: independent variable
    :param n: terms in expansion, must have ``n >= 22``
    :returns: Taylor series expansion of ``eˣ`` centered at ``x = 0``

    """
    d = float(max(n, mindepth))
    accum = x / d
    d -= 1.0
    while d >= 0.5:
        accum = x / d * (1 + accum)
        d -= 1
    return 1 + accum


e = exp0(1.0)


def shift0(x: float) -> float:
    if x >= 0:
        shifted = x % 1.0
    else:
        shifted = x % -1.0
    return shifted


def exp(x: float, /, n: int = mindepth) -> float:
    """Exponential function good for all floating point x.

    :param x: independent variable
    :param n: terms in expansion, must have ``n >= 20``
    :returns: Value of ``eˣ``

    """
    if x >= 0:
        factor = e ** floor(x)
    else:
        factor = e ** ceil(x)
    return exp0(shift0(x), n=n) * factor


def cexp0(z: complex, /, n: int = mindepth) -> complex:
    """Partially factored Taylor expansion of exp about z = 0.

    .. note::

        Best if ``|z| <= 1``.

    :param z: independent variable
    :param n: terms in expansion, must have n >= 20
    :returns: Taylor series expansion of eᶻ centered at z = 0

    """
    d = float(max(n, mindepth))
    accum = z / d
    d -= 1.0
    while d >= 0.5:
        accum = z / d * (1 + accum)
        d -= 1
    return 1 + accum


def shift1(x: float) -> float:
    return x % two_pi


def cexp(z: complex, /, n: int = mindepth) -> complex:
    """Exponential function good for all complex z.

    :param z: independent variable
    :param n: terms in expansion, must have n >= 20
    :returns: Value of ``eᶻ``

    """
    x = z.real
    y = z.imag
    return complex(exp(x), 0) * (cosf(shift1(y)) + jay * sinf(shift1(y)))
