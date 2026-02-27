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

"""Complex valued special functions."""

from math import pi
from .float import exp as expf, sin as sinf, cos as cosf

__all__ = ['exp', 'sin', 'cos', 'tan', 'gamma']

mindepth = 22
maxdepth = 22

two_pi = 2.0 * pi
sqrt_two_pi = two_pi ** (0.5)

s: list[complex] = list()
c: list[complex] = list()

jay = 0.0 + 1.0j


def shift0(x: float) -> float:
    shifted = x % (two_pi)
    if shifted > pi:
        shifted = -1.0 * (shifted - pi)
    return shifted


def shift1(x: float) -> float:
    return x % two_pi


def exp(z: complex, /, n: int = mindepth) -> complex:
    """Partially factored Taylor expansion of exp about z = 0.

    :param z: independent variable
    :param n: terms in expansion, must have n >= 20
    :returns: Value of ``eᶻ``

    """
    x = z.real
    y = z.imag
    return complex(expf(x), 0) * (cosf(shift1(y)) + jay * sinf(shift0(y)))


def sin(z: complex, /, n: int = maxdepth) -> complex:
    """Partially factored Taylor expansion of sine about z = 0.

    :param z: independent variable
    :param n: terms in expansion, must have 2 <= n <= 20
    :returns: Value of ``sine(z)``.

    """
    x = z.real
    y = z.imag
    return 0.5 * jay * (exp(y - jay * x) - exp(-y + jay * x))


def cos(z: complex, /, n: int = maxdepth) -> complex:
    """Partially factored Taylor expansion of cosine about z = 0.

    :param z: independent variable
    :param n: terms in expansion, must have 2 <= n <= 20
    :returns: Value of ``cosine(z)``.

    """
    x = z.real
    y = z.imag
    return 0.5 * (exp(-y + jay * x) + exp(y - jay * x))


def tan(z: complex, /, n: int = maxdepth) -> complex:
    """Tangent centered about z = 0.

    :param z: independent variable
    :param n: terms in expansion, must have 2 <= n <= 20
    :returns: Value of ``tangent(z)`` via ``sin(z)/cos(z)``

    """
    try:
        return sin(z) / cos(z)
    except ZeroDivisionError:
        return 1.633123935319537e16 + 0j


def gamma(z: complex) -> complex:
    """Gamma function valid for all complex values of z.

    .. note::

        Lanczos approximation of Gamma using ``g = 7`` with ``n = 9``
        terms. The values of g and n were chosen to balance accuracy
        with speed. Typically accurate to 13 correct decimal places.

        Code modified from the `Wikipedia Lanczos appoximation article
        <https://en.wikipedia.org/wiki/Lanczos_approximation>`_.

    """
    g7 = 7.5 + 0.0j
    n = 9
    p = [
        0.99999999999980993 + 0.0j,
        676.5203681218851 + 0.0j,
        -1259.1392167224028 + 0.0j,
        771.32342877765313 + 0.0j,
        -176.61502916214059 + 0.0j,
        12.507343278686905 + 0.0j,
        -0.13857109526572012 + 0.0j,
        9.9843695780195716e-6 + 0.0j,
        1.5056327351493116e-7 + 0.0j,
    ]

    if z.real < 0.5:
        return pi / (sin(pi * z) * gamma(1.0 - z))  # Reflection formula
    else:
        z -= 1.0 + 0.0j
        x = p[0]
        for ii in range(1, n):
            x += p[ii] / (z + ii)
        t = z + g7
        return complex(sqrt_two_pi) * t ** (z + 0.5) * exp(-t) * x
