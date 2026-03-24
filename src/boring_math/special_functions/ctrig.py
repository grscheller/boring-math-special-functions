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

"""Complex valued trig functions."""

from .constants import infinity, pi
from .exponential import cexp

__all__ = ['csin', 'ccos', 'ctan']

depth = 22
two_pi = 2.0*pi


def csin(z: complex, /, n: int = depth) -> complex:
    """Complex sine valid for all ``z∈ℂ``.

    :param z: Independent variable.
    :param n: Terms in expansion, must have 2 <= n <= 84.
    :returns: Value of ``sine(z)``.

    """
    x = z.real
    y = z.imag
    return (cexp(-y+(1j)*x) - cexp(y-(1j)*x))/2j


def ccos(z: complex, /, n: int = depth) -> complex:
    """Complex cosine valid for all ``z∈ℂ``.

    :param z: Independent variable.
    :param n: Terms in expansion, must have 2 <= n <= 84.
    :returns: Value of ``cosine(z)``.

    """
    x = z.real
    y = z.imag
    return (cexp(-y+(1j)*x) + cexp(y-(1j)*x))/2


def ctan(z: complex, /, n: int = depth) -> complex:
    """Complex tangent valid for all ``z∈ℂ``.

    :param z: Independent variable.
    :param n: Terms in expansion, must have 2 <= n <= 84.
    :returns: Value of ``tangent(z)`` via ``sin(z)/cos(z)``.

    """
    try:
        return csin(z)/ccos(z)
    except ZeroDivisionError:
        return infinity
