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

"""Complex valued.

Complex valued special functions.

"""

from .complex0 import exp0
from .float import exp as expf

__all__ = ['exp', 'sin', 'cos', 'tan']

maxdepth = 20
mindepth = 30

s: list[complex] = list()
c: list[complex] = list()


def exp(z: complex, /, n: int = mindepth) -> complex:
    """Partially factored Taylor expansion of exp about z = 0.

    :param z: independent variable
    :param n: terms in expansion, must have n >= 20
    :returns: Value of ``eᶻ``

    """
    eye = 0.0+1.0j
    return complex(expf(z.real), 0)*exp0(eye*z.imag)


def sin(z: complex, /, n: int = maxdepth) -> complex:
    """Partially factored Taylor expansion of sine about z = 0.

    :param z: independent variable
    :param n: terms in expansion, must have 2 <= n <= 20
    :returns: Value of ``sine(z)``.

    """
    x = z.real
    y = z.imag
    eye = 0.0+1.0j
    return 0.5*eye*(exp(y - eye*x) - exp(-y + eye*x))


def cos(z: complex, /, n: int = maxdepth) -> complex:
    """Partially factored Taylor expansion of cosine about z = 0.

    :param z: independent variable
    :param n: terms in expansion, must have 2 <= n <= 20
    :returns: Value of ``cosine(z)``.

    """
    x = z.real
    y = z.imag
    eye = 0.0+1.0j
    return 0.5*(exp(-y + eye*x) + exp(y - eye*x))


def tan(z: complex, /, n: int = maxdepth) -> complex:
    """Tangent centered about z = 0.

    :param z: independent variable
    :param n: terms in expansion, must have 2 <= n <= 20
    :returns: Value of ``tangent(z)`` via ``sin(z)/cos(z)``

    """
    try:
        return sin(z)/cos(z)
    except ZeroDivisionError:
        return complex(0, 0)
