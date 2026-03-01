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

from math import pi, factorial as fac
from boring_math.special_functions.gamma import gamma, gamma_real

tolerance0 = 5.0e-16
tolerance1 = 5.0e-15
tolerance2 = 5.0e-14
tolerance3 = 5.0e-13
tolerance4 = 5.0e-12
tolerance5 = 5.0e-11

sqrt_pi = pi**0.5
jay = 0.0 + 1.0j


class Test_gamma:
    def test_gamma_real(self) -> None:
        assert abs(gamma_real(1.0) - float(fac(0))) < tolerance0
        assert abs(gamma_real(2.0) - float(fac(1))) < tolerance0
        assert abs(gamma_real(3.0) - float(fac(2))) < tolerance1
        assert abs(gamma_real(4.0) - float(fac(3))) < tolerance2
        assert abs(gamma_real(5.0) - float(fac(4))) < tolerance2
        assert abs(gamma_real(6.0) - float(fac(5))) < tolerance3
        assert abs(gamma_real(21.0) - float(fac(20)))/fac(20) < tolerance1
        assert abs(gamma_real(0.5) - sqrt_pi) < tolerance0

    def test_gamma_complex(self) -> None:
        assert abs(gamma(1.0+0.0j) - complex(fac(0), 0)) < tolerance0
        assert abs(gamma(2.0+0.0j) - complex(fac(1), 0)) < tolerance0
        assert abs(gamma(3.0+0.0j) - complex(fac(2), 0)) < tolerance1
        assert abs(gamma(4.0+0.0j) - complex(fac(3), 0)) < tolerance2
        assert abs(gamma(5.0+0.0j) - complex(fac(4), 0)) < tolerance2
        assert abs(gamma(6.0+0.0j) - complex(fac(5), 0)) < tolerance3
        assert abs(gamma(21.0+0.0j) - complex(fac(20), 0))/fac(20) < tolerance1
        assert abs(gamma(0.5+0.0j) - sqrt_pi) < tolerance0
