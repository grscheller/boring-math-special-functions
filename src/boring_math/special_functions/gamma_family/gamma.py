# Copyright 2016-2026 Geoffrey R. Scheller
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
.. admonition:: Gamma functions for real and complex values.

    Defined via the analytic continuation of the Gamma function.

"""

from cmath import inf, isinf
from ..constants import infinity, pi
from ..exponential.exp import exp, cexp
from ..trigonometry.ctrig import csin
from ..trigonometry.trig import sin as rsin

__all__ = ['gamma', 'gamma_real']

two_pi = 2.0*pi
sqrt_two_pi = float(two_pi**0.5)
comp_sqrt_two_pi = complex(sqrt_two_pi)


def gamma(z: complex) -> complex:
    """
    .. admonition:: Gamma function

        Valid for all complex values of ``z``.

        .. note::

            Lanczos approximation of Gamma using g = 7 with n = 9 terms.

            The values of g and n were chosen to balance accuracy
            with speed. Typically accurate to 13 correct decimal places.

            Code modified from the `Wikipedia Lanczos approximate article
            <https://en.wikipedia.org/wiki/Lanczos_approximation>`_.

        :param z: Complex argument.
        :returns: Value of the analytic continuation of gamma(z). Uses
                  inf + infj to represent a single complex infinity.

    """
    g7 = 7.5 + 0.0j
    n = 9
    p = [
        0.99999999999980993+0.0j,
        676.5203681218851+0.0j,
        -1259.1392167224028+0.0j,
        771.32342877765313+0.0j,
        -176.61502916214059+0.0j,
        12.507343278686905+0.0j,
        -0.13857109526572012+0.0j,
        9.9843695780195716e-6+0.0j,
        1.5056327351493116e-7+0.0j,
    ]

    if z.real < 0.5:
        try:
            return pi / (csin(pi * z) * gamma(1.0 - z))  # Reflection formula
        except ZeroDivisionError:
            return inf
    else:
        z -= 1.0+0.0j
        y = p[0]
        for ii in range(1, n):
            y += p[ii] / (z + ii)
        t = z + g7
        z += 0.5+0.0j
        val = comp_sqrt_two_pi * t**z * cexp(-t) * y
        return infinity if isinf(val) else val


def gamma_real(x: float) -> float:
    """
    .. admonition:: Gamma function

        Valid for all finite real values of x.

        :param x: Floating point argument.
        :returns: Value of gamma(x).

    """
    g7 = 7.5
    n = 9
    p = [
        0.99999999999980993,
        676.5203681218851,
        -1259.1392167224028,
        771.32342877765313,
        -176.61502916214059,
        12.507343278686905,
        -0.13857109526572012,
        9.9843695780195716e-6,
        1.5056327351493116e-7,
    ]

    if x < 0.5:
        try:
            return pi / (rsin(pi*x) * gamma_real(1.0 - x))  # Reflection formula
        except ZeroDivisionError:
            return inf
    else:
        x -= 1.0
        y = p[0]
        for ii in range(1, n):
            y += p[ii] / (x + ii)
        t = x + g7
        x += 0.5
        t_to_x = float(t**x)
        return sqrt_two_pi * t_to_x * exp(-t) * y
