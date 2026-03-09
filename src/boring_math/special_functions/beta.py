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

from cmath import log as clog, nan, nanj
from .exponential import cexp
from .gamma import gamma

__all__ = ['beta']


def beta(u: complex, v: complex) -> complex:
    """Beta function valid for all complex values of z.

    .. note::

        Using natural logs for more numerical stability.

    .. note::

        - beta(u, v) = beta(v, u)
        - beta(0, z) = gamma(0) = ∞ ∀(z ∈ ℂ)
        - beta(-n, k) = 0 when k > n > 0
        - claim: beta(u. v) = 0 if it has a removable singularity,


    """
    if (naive := cexp(clog(gamma(u)) + clog(gamma(v)) - clog (gamma(u + v)))) == nan+nanj:
        if u == 0 or v == 0 or u == -v:
            return gamma(0)
        assert False # Need to consider other  cases with removable singularities.
    else:
        return naive
