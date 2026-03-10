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
from cmath import log as clog, inf, infj, nan, isnan
from .exponential import cexp
from .gamma import gamma

__all__ = ['beta']

infinity = inf + infj


def beta(u: complex, v: complex) -> complex:
    """Beta function valid for all complex values of z.

    .. note::

        Using natural logs for more numerical stability.

    .. note::

        - B(u, v) = B(v, u) for ∀(u, v ∈ ℂ)
        - B(0, v) = Γ(0) = ∞ for ∀(v ∈ ℂ)
        - B(m, -n) = 0 ∀(m, n ∈ ℕ) where m > n > 0
        - B(m, -n) = Γ(m) * (Res[Γ, -n]/Res[Γ, m-n])

          - where ∀(n>=0) Res[Γ(z), z = -n] = (-1)**(n)/(n)!

    :param u: First argument to analytically continued beta function.
    :param v: Second argument to analytically continued beta function.
    :returns: Value of beta(u,v) where inf + infj is used to represent
              a single complex infinity.

    """
    u1 = int(u.real)
    v1 = int(v.real)
    if u1 == u and v1 == v:
        if u1 > 0 and v1 > 0:
            return complex(fac(u1-1) / fac(u1+v1 - 1) * fac(v1-1))
    else:
        if (int(sum := (u + v).real)) == u + v:
            if sum <= 0:
                return infinity

    if not isnan(abs((naive := cexp(clog(gamma(u)) + clog(gamma(v)) - clog (gamma(u + v)))))):
        if u == 0 or v == 0 or u == -v:
            return gamma(0)
        assert False # Need to consider other  cases with removable singularities.
    else:
        return naive
