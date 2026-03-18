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
from cmath import log as clog, isnan, nan, nanj
from .exponential import cexp
from .gamma import gamma

__all__ = ['beta']

infinity = nan + nanj # represents complex infinity


def beta(u: complex, v: complex) -> complex:
    """Beta function valid for all complex values of z.

    .. note::

        Using natural logs for more numerical stability.

    .. note::

        - B(u, v) = B(v, u) for ∀(u, v ∈ ℂ)
        - B(0, v) = Γ(0) = ∞ for ∀(v ∈ ℂ)
        - B(m, -n) = 0 ∀(m, n ∈ ℕ) when m > n > 0
        - B(m, -n) = Γ(m) * (Res[Γ, -n]/Res[Γ, m-n]) when m <= n

          - where ∀(n>=0) Res[Γ(z), z = -n] = (-1)**(n)/(n!)

    :param u: First argument to analytically continued beta function.
    :param v: Second argument to analytically continued beta function.
    :returns: Value of beta(u,v) where inf + infj is used to represent
              a single complex infinity.

    """
    if isnan(naive := clog(gamma(u)) + clog(gamma(v)) - clog(gamma(u + v))):
        if isnan(u) or isnan(v):
            return infinity
        ui, vi = int(u.real), int(v.real)
        umax = max(ui, vi)
        vmin = min(ui, vi)

        if vmin <= umax <= 0:
            return infinity

        if umax > 0 >= vmin:
            if umax < abs(vmin):
                return infinity
            elif umax == abs(vmin):
                return (fac(umax-1)) / ((-1.0)**(umax-vmin)/fac(umax-vmin)) * ((-1.0)**(-vmin)/fac(-vmin))
            else:
                assert False

        if umax >= vmin > 0:
            assert False

        assert False
    else:
        return cexp(naive)
