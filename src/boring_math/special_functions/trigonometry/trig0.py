# Copyright 2025-2026 Geoffrey R. Scheller
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
.. admonition:: Floating point sine, cosine, tangent about θ = 0

    The named only argument n must be at least 22
    to agree with the ones from Python's stdlib math.

    .. tip::

        For ``0 ≤ |z| < 1`` you can get away with smaller ``n``
        values to reduce the number of computations.

"""

from math import factorial, inf

__all__ = ['sin0', 'cos0', 'tan0', 'maxdepth', 'mindepth']

maxdepth = 84
mindepth = 2
depth = 20

s: list[float] = list()
c: list[float] = list()

for ii in range(maxdepth):
    s.append(1.0/factorial(2 * ii + 1))
    c.append(1.0/factorial(2 * (ii + 1)))


def sin0(θ: float, /, n: int = depth) -> float:
    """
    .. admonition:: Sine centered at x = 0

        Partially factored Taylor series expansion of sine
        centered at x = 0.

        :param θ: Angle in radians.
        :param n: Terms in expansion, must have 2 <= n <= 84.
        :returns: The value of sine(θ).

        .. tip::

            Best n to use

            - n >= 20 when -2π <= θ <= 2π
            - n >= 15 when -π <= θ <= π
            - n >= 12 when -π/2 <= θ <= π/2

            The default is n=20.

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
    """
    .. admonition:: Cosine centered at x = 0

        Partially factored Taylor series expansion of cosine
        centered at x = 0.

        :param θ: Angle in radians.
        :param n: Terms in expansion, must have 2 <= n <= 84.
        :returns: The value of cosine(θ).

        .. tip::

            Best n to use

            - n >= 20 when -2π <= θ <= 2π
            - n >= 15 when -π <= θ <= π
            - n >= 12 when -π/2 <= θ <= π/2

            The default is n = 20.

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
    """
    .. admonition:: Tangent centered at θ = 0.

        Partially factored Taylor series expansion of tangent
        centered at ``θ = 0``.

        :param θ: Angle in radians.
        :param n: Terms in expansion, must have 2 <= n <= 84.
        :returns: The value sin0(θ)/cos0(θ).

        .. tip::

            Best n to use

            - n >= 20 when -2π <= θ <= 2π
            - n >= 15 when -π <= θ <= π
            - n >= 12 when -π/2 <= θ <= π/2

            The default is n=20.

    """
    try:
        return sin0(θ, n=n) / cos0(θ, n=n)
    except ZeroDivisionError:
        if sin0(θ, n=n) >= 0:
            return inf
        else:
            return -inf
