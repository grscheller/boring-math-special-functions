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

from .gamma import gamma, gamma_real as rgamma

__all__ = ['beta', 'beta_real']


def beta(u: complex, v: complex) -> complex:
    """Beta function valid for all complex values of z.

    .. note::

        Initial naive implementation.

    """
    return gamma(u)*gamma(v)/gamma(u + v)


def beta_real(x: float, y: float) -> float:
    """Beta function valid for all real values of x.

    .. note::

        Initial naive implementation.

    """
    return rgamma(x)*rgamma(y)/rgamma(x + y)
