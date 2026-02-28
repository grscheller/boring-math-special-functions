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

"""Complex valued special functions about a point."""

from math import factorial as fac

__all__ = ['exp0', 'sin0', 'cos0', 'tan0']

mindepth = 22
maxdepth = 22

s: list[complex] = list()
c: list[complex] = list()

for ii in range(maxdepth):
    s.append(1 / fac(2 * ii + 1))
    c.append(1 / fac(2 * (ii + 1)))


def exp0(z: complex, /, n: int = mindepth) -> complex:
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


def sin0(z: complex, /, n: int = maxdepth) -> complex:
    """Partially factored Taylor expansion of sine about z = 0.

    .. note::

        Best if ``|z| <= 2π``.

    :param z: independent variable
    :param n: terms in expansion, must have ``2 <= n <= 20``
    :returns: Taylor series expansion of sine(x) centered at ``z = 0``

    """
    zsqr = z * z
    pos = n - 1
    accum = zsqr * s[pos]
    pos -= 1
    while pos > 0:
        accum = zsqr * (s[pos] - accum)
        pos -= 1
    return z * (1 - accum)


def cos0(z: complex, /, n: int = maxdepth) -> complex:
    """Partially factored Taylor expansion of cosine about ``z = 0``.

    .. note::

        Best if ``|z| <= 2π``.

    :param z: independent variable
    :param n: terms in expansion, must have ``2 <= n <= 20``
    :returns: Taylor series expansion of cosine(z) centered at ``z = 0``

    """
    zsqr = z * z
    pos = n - 1
    accum = zsqr * c[pos]
    pos -= 1
    while pos >= 0:
        accum = zsqr * (c[pos] - accum)
        pos -= 1
    return 1 - accum


def tan0(z: complex, /, n: int = maxdepth) -> complex:
    """Tangent centered about ``z = 0``.

    .. note::

        Best if ``|z| <= π``.

    :param z: independent variable
    :param n: terms in expansion, must have ``2 <= n <= 20``
    :returns: ``sin0(z)/cos0(z)``

    """
    try:
        return sin0(z, n=n) / cos0(z, n=n)
    except ZeroDivisionError:
        absnum = abs(num := sin0(z, n=n))
        if absnum > 0:
            factor = num / absnum
        elif num.real >= 0:
            factor = complex(1.0, 0.0)
        else:
            factor = complex(-1.0, 0.0)
        return factor * 1.633123935319537e16
