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

Real valued special functions centered at ``x = 0``.

"""

from math import factorial as fac

__all__ = ['exp0', 'sin0', 'cos0', 'tan0']

mindepth = 22
maxdepth = 22

s: list[float] = list()
c: list[float] = list()

for ii in range(maxdepth):
    s.append(1/fac(2*ii + 1))
    c.append(1/fac(2*(ii + 1)))

def exp0(x: float, /, n: int = mindepth) -> float:
    """Partially factored Taylor expansion of exp about ``x = 0``.

    .. note::

        Best if ``-1 <= x <= 1``.

    :param x: independent variable
    :param n: terms in expansion, must have ``n >= 20``
    :returns: Taylor series expansion of ``eˣ`` centered at ``x = 0``

    """
    d = float(max(n, mindepth))
    accum = x/d
    d -= 1.0
    while d >= 0.5:
        accum = x/d*(1 + accum)
        d -= 1
    return 1 + accum

def sin0(x: float, /, n: int = maxdepth) -> float:
    """Partially factored Taylor expansion of sine about ``x = 0``.

    .. note::

        Best if ``-2π <= x <= 2π``.

    :param x: angle in radians
    :param n: terms in expansion, must have ``2 <= n <= 20``
    :returns: Taylor series expansion of sine(x) centered at ``x = 0``

    """
    xsqr = x * x
    pos = n - 1
    accum = xsqr * s[pos]
    pos -= 1
    while pos > 0:
        accum = xsqr * (s[pos] - accum)
        pos -= 1
    return x * (1 - accum)


def cos0(x: float, /, n: int = maxdepth) -> float:
    """Partially factored Taylor expansion of cosine about ``x = 0``.

    .. note::

        Best if ``-2π <= x <= 2π``.

    :param x: angle in radians
    :param n: terms in expansion, must have ``2 <= n <= 20``
    :returns: Taylor series expansion of ``cosine(x)`` centered at ``x = 0``

    """
    xsqr = x * x
    pos = n - 1
    accum = xsqr * c[pos]
    pos -= 1
    while pos >= 0:
        accum = xsqr * (c[pos] - accum)
        pos -= 1
    return 1 - accum


def tan0(x: float, /, n: int = maxdepth) -> float:
    """Tangent centered about x = 0.

    .. note::

        Best if ``-π <= x <= π``.

    :param x: angle in radians
    :param n: terms in expansion, must have ``2 <= n <= 20``
    :returns: ``sin0(x)/cos0(x)``

    """
    factor = 1.0
    try:
        return sin0(x, n=n)/cos0(x, n=n)
    except ZeroDivisionError:
        num = sin0(x, n=n)
        if num < 0:
            factor = -1.0
        return factor*1.633123935319537e16
