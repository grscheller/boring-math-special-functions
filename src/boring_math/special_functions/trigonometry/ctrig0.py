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

from math import factorial
from ..constants import infinity

__all__ = ['csin0', 'ccos0', 'ctan0']

depth = 20
maxdepth = 84

sin_factors: list[complex] = list()
cos_factors: list[complex] = list()

for ii in range(maxdepth):
    sin_factors.append(1 / factorial(2*ii + 1))
    cos_factors.append(1 / factorial(2*(ii + 1)))


def csin0(z: complex, /, n: int = depth) -> complex:
    """Partially factored Taylor expansion of sine about ``z = 0``.

    .. note::

        Best if ``|z| <= 2π`` and ``n >= 20``.

    :param z: independent variable
    :param n: terms in expansion, must have ``2 <= n <= 84``
    :returns: Taylor series expansion of sine(x) centered at ``z = 0``.

    """
    zsqr = z * z
    pos = n - 1
    accum = zsqr * sin_factors[pos]
    pos -= 1
    while pos > 0:
        accum = zsqr * (sin_factors[pos] - accum)
        pos -= 1
    return z * (1 - accum)


def ccos0(z: complex, /, n: int = depth) -> complex:
    """Partially factored Taylor expansion of cosine about ``z = 0``.

    .. note::

        Best if ``|z| <= 2π`` and ``n >= 22``.

    :param z: independent variable
    :param n: terms in expansion, must have ``2 <= n <= 84``
    :returns: Taylor series expansion of cosine(z) centered at ``z = 0``

    """
    zsqr = z * z
    pos = n - 1
    accum = zsqr * cos_factors[pos]
    pos -= 1
    while pos >= 0:
        accum = zsqr * (cos_factors[pos] - accum)
        pos -= 1
    return 1 - accum


def ctan0(z: complex, /, n: int = depth) -> complex:
    """Tangent centered about ``z = 0``.

    .. note::

        Best if ``|z| <= π`` and ``n >= 20``.

    :param z: Independent variable.
    :param n: Terms in expansion, must have ``2 <= n <= 84``.
    :returns: The value ``csin0(z)/ccos0(z)``.

    """
    try:
        return csin0(z, n=n)/ccos0(z, n=n)
    except ZeroDivisionError:
        return infinity
