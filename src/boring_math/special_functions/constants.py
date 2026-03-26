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

"""Mathematical constants."""
"""Gamma function."""

from cmath import inf, infj

__all__ = ['infinity', 'e', 'pi']

# Complex infinity

infinity: complex = inf + infj
"""Representative of a single complex infinity.

Real valued functions will use +inf and -inf when two-sided limits
exist. The positive inf will be used for the case of distinct one-sided
extended real valued infinities.

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
"""Base of the natural logarithms."""

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
"""Ratio of a circle's circumference to its diameter.

Also, π can be defined as the smallest positive real
value ``x`` where ``e²ˣⁱ = 1`` or ``sin(x/2) = 1``.

This value for π is based on a continued fraction expansion
due to Bill Gosper.

    π = 4/(1 + 1²/(3 + 2²/(5 + 3²/(7 + 4²/(9 + 5²/(11 + ...))))))

"""
