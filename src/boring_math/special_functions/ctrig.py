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
from .exponential import cexp as exp

__all__ = ['sin', 'cos', 'tan']

mindepth = 22
maxdepth = 22

two_pi = 2.0 * pi
jay = 0.0 + 1.0j


def shift0(x: float) -> float:
    shifted = x % (two_pi)
    if shifted > pi:
        shifted = -1.0 * (shifted - pi)
    return shifted


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
