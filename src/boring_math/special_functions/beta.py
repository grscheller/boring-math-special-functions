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

"""Beta function."""

from math import factorial as fac
from cmath import log as clog, isnan, inf, infj, nan
from .exponential import cexp
from .gamma import gamma

__all__ = ['beta', 'infinity']

infinity = inf + infj
"""Used to represent a single complex infinity."""


def beta(u: complex, v: complex) -> complex:
    """Beta function valid for all complex values of z.

    .. note::

        For all u, v ∈ ℂ and m, n ∈ ℕ, we have

        - B(u, v) = B(v, u)
        - B(0, v) = Γ(0) = ∞
        - B(m, -n) = ∞ when m > n > 0
        - B(m, -n) = Γ(m) * (Res[Γ, -n]/Res[Γ, m-n]) when m <= n

          - where ∀(n>=0) Res[Γ(z), z = -n] = (-1)ⁿ/(n!)

    .. note::

        Using natural logs for more numerical stability.

    :param u: First argument to analytically continued beta function.
    :param v: Second argument to analytically continued beta function.
    :returns: Value of ``beta(u,v)`` where ``inf + infj`` is used to
              represent a single complex infinity.

    """
    if not isnan(naive := clog(gamma(u)) + clog(gamma(v)) - clog(gamma(u + v))):
        return cexp(naive)
    else:
        ui, vi = int(u.real), int(v.real)
        umax = max(ui, vi)
        vmin = min(ui, vi)

        if vmin <= umax <= 0:
            return nan

        if umax > 0 >= vmin:
            if umax <= -vmin:
                return (
                    ((-1.0)**(-vmin) / fac(-vmin))
                    / ((-1.0)**(-vmin - umax) / fac(-vmin - umax))
                    * (fac(umax - 1))
                )
            else:
                return infinity

        assert False
