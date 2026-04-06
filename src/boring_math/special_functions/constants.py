# Copyright 2026 Geoffrey R. Scheller
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
Mathematical constants
----------------------

.. admonition:: Mathematical constants

    All values derived internally by the
    boring_math.special_functions.constants module itself.

    - infinity
    - e
    - pi

"""

from cmath import inf, infj

__all__ = ['infinity', 'e', 'pi']

# Complex infinity

infinity: complex = inf + infj
"""
.. admonition:: Single complex infinity

    Used as a sentinel value to represent of a single complex infinity.

    .. note::

        Complex infinity is a mathematical concept. Python does not
        natively support ``inf + infj`` for this.

        .. tip::

            Use the ``cmath.isinf`` function to test for
            infinite values.

        .. note::

            Real valued functions will use +inf and -inf when a distinct
            two-sided infinity exists. Positive inf will be used when
            distinct one-sided infinite limits exist.

"""

# Calculate base of the natural logarithms.

def _exp0(x: float) -> float:
    d = 22.0
    accum = x / d
    d -= 1.0
    while d >= 0.5:
        accum = x / d * (1 + accum)
        d -= 1.0
    return 1.0 + accum

e: float = _exp0(1.0)
"""
.. admonition:: Base of the natural logarithms.

    Also the limit of ``(1 + 1/n)ⁿ`` as ``n → ∞``

"""

# Calculate π

def _pi(n:int) -> float:
    odds = [float(k) for k in range(3, 2*n+2, 2)]
    squares = [float(k*k) for k in range(1, len(odds)+1)]
    m = len(odds) - 1
    accum = squares[m]/odds[m]
    while m > 0:
        m -= 1
        accum = squares[m]/(odds[m] + accum)
    return 4/(1 + accum)

pi: float = _pi(21)
"""
.. admonition:: Ratio circle's circumference to diameter.

    π can also be defined as the smallest positive real
    value ``x`` where ``e²ˣⁱ = 1`` or ``sin(x/2) = 1``.

    .. note::

        This value for π is based on a continued fraction
        expansion due to Bill Gosper.

        ``π = 4/(1 + 1²/(3 + 2²/(5 + 3²/(7 + 4²/(9 + 5²/(11 + ...))))))``

"""
