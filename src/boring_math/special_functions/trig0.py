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

from math import factorial, inf

__all__ = ['sin0', 'cos0', 'tan0', 'maxdepth', 'mindepth']

maxdepth = 84
mindepth = 2
depth = 20

s: list[float] = list()
c: list[float] = list()

for ii in range(maxdepth):
    s.append(1 / factorial(2 * ii + 1))
    c.append(1 / factorial(2 * (ii + 1)))


def sin0(θ: float, /, n: int = depth) -> float:
    """Partially factored Taylor expansion of sine centered at ``x = 0``.

    .. note::

        Best n to use

        - ``n >= 20`` when ``-2π <= θ <= 2π``
        - ``n >= 15`` when ``-π <= θ <= π``
        - ``n >= 12`` when ``-π/2 <= θ <= π/2``

        The default is ``n=20``.

    :param x: angle in radians
    :param n: terms in expansion, must have ``2 <= n <= 84``
    :returns: Taylor series expansion of sine(x) centered at ``θ = 0``

    """
    θ_sqr = θ * θ
    pos = n - 1
    accum = θ_sqr * s[pos]
    pos -= 1
    while pos > 0:
        accum = θ_sqr * (s[pos] - accum)
        pos -= 1
    return θ * (1 - accum)


def cos0(θ: float, /, n: int = depth) -> float:
    """Partially factored Taylor expansion of cosine centered at ``x = 0``.

    .. note::

        Best n to use

        - ``n >= 20`` when ``-2π <= θ <= 2π``
        - ``n >= 15`` when ``-π <= θ <= π``
        - ``n >= 12`` when ``-π/2 <= θ <= π/2``

        The default is ``n=20``.

    :param x: angle in radians
    :param n: terms in expansion, must have ``2 <= n <= 84``
    :returns: Taylor series expansion of ``cosine(θ)`` centered at ``θ = 0``

    """
    θ_sqr = θ * θ
    pos = n - 1
    accum = θ_sqr * c[pos]
    pos -= 1
    while pos >= 0:
        accum = θ_sqr * (c[pos] - accum)
        pos -= 1
    return 1 - accum


def tan0(θ: float, /, n: int = depth) -> float:
    """Tangent centered about ``x = 0``.

    .. note::

        Best n to use

        - ``n >= 20`` when ``-2π <= θ <= 2π``
        - ``n >= 15`` when ``-π <= θ <= π``
        - ``n >= 12`` when ``-π/2 <= θ <= π/2``

    :param x: angle in radians
    :param n: terms in expansion, must have ``2 <= n <= 84``
    :returns: ``sin0(θ)/cos0(θ)``

    """
    try:
        return sin0(θ, n=n) / cos0(θ, n=n)
    except ZeroDivisionError:
        if sin0(θ, n=n) >= 0:
            return inf
        else:
            return -inf
