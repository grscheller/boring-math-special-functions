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

"""
.. admonition:: Beta functions for real and complex values.

    Defined via the analytic continuation of the Gamma function.

"""

from math import factorial as fac, exp, log
from cmath import log as clog, isinf, isnan
from ..constants import infinity
from ..exponential.exp import cexp
from ..gamma_family.gamma import gamma, gamma_real

__all__ = ['beta', 'beta_real']


def beta(u: complex, v: complex) -> complex:
    """
    .. admonition:: Beta function for all complex ``u`` and ``v``.

        .. note::

            For all u, v ∈ ℂ and m, n ∈ ℕ, we have

            - B(u, v) = B(v, u)
            - B(0, v) = Γ(0) = ∞
            - B(m, -n) = ∞ when m > n > 0
            - B(m, -n) = Γ(m) * (Res[Γ, -n]/Res[Γ, m-n]) when m <= n

            - where ∀(n>=0) Res[Γ(z), z = -n] = (-1)ⁿ/(n!)

        .. note::

            Using natural logs in calculation for more numerical stability.

    :param u: First argument to analytically continued beta function.
    :param v: Second argument to analytically continued beta function.
    :returns: Value of ``beta(u,v)`` where ``inf+infj`` is returned to
              represent a single complex infinity.

    """
    if not isnan(naive := clog(gamma(u)) + clog(gamma(v)) - clog(gamma(u + v))):
        val = cexp(naive)
        return infinity if isinf(val) else val

    ui, vi = int(u.real), int(v.real)

    umax = max(ui, vi)
    vmin = min(ui, vi)

    if vmin <= umax <= 0:
        return infinity

    if umax > 0 >= vmin:
        if umax <= -vmin:
            val = (
                ((-1.0)**(-vmin)/fac(-vmin))
                / ((-1.0)**(-vmin - umax)/fac(-vmin - umax))
                * (fac(umax - 1))
            )
            return infinity if isinf(val) else val
        else:
            return 0.0

    assert False # should never happen


def beta_real(x: float, y: float) -> float:
    """Beta function valid for all real values of x, y > 1.

    .. note::

        Not valid for extended value reals.


    .. note::

        Using natural logs for more numerical stability.

    :param x: First argument to analytically continued beta function.
    :param y: Second argument to analytically continued beta function.
    :returns: Value of ``beta(x, y)`` where ``inf`` is returned.
              to denote singular points.
    :raises ValueError: If x <= 0 or y <= 0.

    """
    if x <= 0 or y <= 0 or isinf(x) or isinf(y):
        msg1 = 'Domain error: '
        msg2 = 'arguments to beta_real must be positive and finite'
        raise ValueError(msg1 + msg2)

    return exp(log(gamma_real(x)) + log(gamma_real(y)) - log(gamma_real(x + y)))
