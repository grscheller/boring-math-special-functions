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
from cmath import log as clog, inf, infj, isnan, isinf
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
        - B(m, -n) = 0 ∀(m, n ∈ ℕ) when m > n > 0
        - B(m, -n) = Γ(m) * (Res[Γ, -n]/Res[Γ, m-n]) when m <= n

          - where ∀(n>=0) Res[Γ(z), z = -n] = (-1)**(n)/(n!)

    :param u: First argument to analytically continued beta function.
    :param v: Second argument to analytically continued beta function.
    :returns: Value of beta(u,v) where inf + infj is used to represent
              a single complex infinity.

    """
    if isnan(naive := cexp(clog(gamma(u)) + clog(gamma(v)) - clog(gamma(u + v)))):
        u1 = int(u.real)
        v1 = int(v.real)

        if u1 > 0 and v1 > 0:
            return complex(fac(u1-1) / fac(u1+v1-1) * fac(v1-1))
        if u1 <= 0 and v1 <= 0:
            return ((-1.0)**(-u1)/fac(-u1)) / ((-1.0)**(-u1-v1)/fac(-u1-v1)) * ((-1.0)**(-v1)/fac(-v1))
        if u1 > 0 and u1 > -v1 > 0:
            return 0+0j
        if u1 > 0 and u1 <= -v1:
            return (fac(u1-1)) / ((-1.0)**(u1-v1)/fac(u1-v1)) * ((-1.0)**(-v1)/fac(-v1))
        if v1 > 0 and v1 > -u1 > 0:
            return 0+0j
        if v1 > 0 and v1 <= -u1:
            return ((-1.0)**(-u1)/fac(v1)) / ((-1.0)**(v1-u1)/fac(v1-u1)) * (fac(v1-1))
        assert False
    else:
        if isinf(naive):
            return infinity
        return naive
