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
.. admonition:: Complex valued sine, cosine, tangent

    The named only argument ``n`` must be at least ``22``
    to agree with the ones from stdlib cmath.

    .. tip::

        For ``0 ≤ |z| < 1`` you can get away with smaller ``n``
        values to reduce the number of computations.

"""

from ..constants import infinity
from ..exponential.exp import cexp

__all__ = ['csin', 'ccos', 'ctan']

depth = 22


def csin(z: complex, /, n: int = depth) -> complex:
    """
    .. admonition:: Complex tangent

        Complex sine valid for all ``z∈ℂ``.

    :param z: Independent variable.
    :param n: Terms in expansion, must have ``2 ≤ n ≤ 84``.
    :returns: Value of ``sine(z)``.

    """
    x = z.real
    y = z.imag
    return (cexp(-y+(1j)*x, n=depth) - cexp(y-(1j)*x, n=depth))/2j


def ccos(z: complex, /, n: int = depth) -> complex:
    """
    .. admonition:: Complex cosine

        Complex cosine valid for all ``z∈ℂ``.

    :param z: Independent variable.
    :param n: Terms in expansion, must have ``2 ≤ n ≤ 84``.
    :returns: Value of ``cosine(z)``.

    """
    x = z.real
    y = z.imag
    return (cexp(-y+(1j)*x, n=depth) + cexp(y-(1j)*x, n=depth))/2


def ctan(z: complex, /, n: int = depth) -> complex:
    """
    .. admonition:: Complex tangent

        Complex tangent valid for all ``z∈ℂ``.

    :param z: Independent variable.
    :param n: Terms in expansion, must have ``2 ≤ n ≤ 84``.
    :returns: Value of ``tangent(z)`` via ``sine(z)/cosine(z)``.

    """
    try:
        return csin(z, n=depth)/ccos(z, n=depth)
    except ZeroDivisionError:
        return infinity
