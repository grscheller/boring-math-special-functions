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

"""Floating point special functions."""

from math import pi
from .trig0 import sin0, cos0, tan0

__all__ = ['sin', 'cos', 'tan']

mindepth = 22
maxdepth = 22

two_pi = 2.0 * pi
pi_half = pi / 2.0


def shift0(x: float) -> float:
    shifted = x % (two_pi)
    if shifted > pi:
        shifted = -1.0 * (shifted - pi)
    return shifted


def sin(x: float, /, n: int = maxdepth) -> float:
    """Partially factored Taylor expansion of sine about x = 0.

    :param x: angle in radians
    :param n: terms in expansion, must have 2 <= n <= 20
    :returns: Taylor series expansion of sine(x) centered at x = 0

    """
    return sin0(shift0(x), n=n)


def shift1(x: float) -> float:
    return x % two_pi


def cos(x: float, /, n: int = maxdepth) -> float:
    """Partially factored Taylor expansion of cosine about x = 0.

    :param x: angle in radians
    :param n: terms in expansion, must have 2 <= n <= 20
    :returns: Taylor series expansion of cosine(x) centered at x = 0

    """
    return cos0(shift1(x), n=n)


def shift2(x: float) -> float:
    shifted = x % pi
    if shifted > pi_half:
        shifted = -1.0 * (shifted - pi_half)
    return shifted


def tan(x: float, /, n: int = maxdepth) -> float:
    """Tangent centered about x = 0.

    :param x: angle in radians
    :param n: terms in expansion, must have 2 <= n <= 20
    :returns: sin0(x)/cos0(x)

    """
    return tan0(shift2(x), n=n)
