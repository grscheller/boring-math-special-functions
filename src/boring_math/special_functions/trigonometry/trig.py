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
.. admonition:: Floating point trigonometric functions.

    Valid for all extended real value ``θ``.

"""

from ..constants import pi
from ..trigonometry.trig0 import sin0, cos0, tan0

__all__ = ['sin', 'cos', 'tan']

mindepth = 20

two_pi = 2.0 * pi
pi_half = pi / 2.0


def shift0(θ: float) -> float:
    shifted = θ % (two_pi)
    if shifted > pi:
        shifted = -1.0 * (shifted - pi)
    return shifted


def sin(θ: float) -> float:
    """
    .. admonition:: Sine for all real θ

        :param θ: Angle in radians.
        :returns: Sine of angle θ.

    """
    return sin0(shift0(θ), n=mindepth)


def shift1(θ: float) -> float:
    return θ % two_pi


def cos(θ: float) -> float:
    """
    .. admonition:: Cosine for all real ``θ``

        :param θ: Angle in radians.
        :returns: Cosine of angle θ.

    """
    return cos0(shift1(θ), n=mindepth)


def shift2(θ: float) -> float:
    shifted = θ % pi
    if shifted > pi_half:
        shifted = -1.0 * (shifted - pi_half)
    return shifted


def tan(θ: float) -> float:
    """
    .. admonition:: Tangent for all real ``θ``

        :param θ: Angle in radians.
        :returns: Tangent of angle θ.

    """
    return tan0(shift2(θ), n=mindepth)
