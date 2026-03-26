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

sqrt_pi = pi**0.5
euler = 0.57721566490153286060
jay = 0.0+1.0j
one = 1.0+0.0j
two = 2.0+0.0j
three = 3.0+0.0j
four = 4.0+0.0j
five = 5.0+0.0j
six = 6.0+0.0j

tolerance0 = 5.0e-16
tolerance1 = 5.0e-15
tolerance2 = 5.0e-14
tolerance3 = 5.0e-13
tolerance4 = 5.0e-12
tolerance5 = 5.0e-11


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
        assert abs(gamma_real(1.5) - sqrt_pi/2) < tolerance1
        assert abs(gamma_real(2.5) - 3*sqrt_pi/4) < tolerance1
        assert abs(gamma_real(1.0/3.0) - 2.67893853470774763365) < tolerance0
        assert abs(gamma_real(2.0/3.0) - 1.35411793942640041694) < tolerance0
        assert abs(gamma_real(0.75) - 1.22541670246517764512) < tolerance1
        assert abs(gamma_real(0.25) - 3.62560990822190831193) < tolerance1

    def test_gamma_complex(self) -> None:
        assert abs(gamma(one) - complex(fac(0))) < tolerance0
        assert abs(gamma(two) - complex(fac(1))) < tolerance0
        assert abs(gamma(three) - complex(fac(2))) < tolerance1
        assert abs(gamma(four) - complex(fac(3))) < tolerance2
        assert abs(gamma(five) - complex(fac(4))) < tolerance2
        assert abs(gamma(six) - complex(fac(5))) < tolerance3
        assert abs(gamma(21.0+0.0j) - complex(fac(20))) / fac(20) < tolerance1
        assert abs(gamma(0.5+0.0j) - sqrt_pi) < tolerance0
        assert abs(gamma(1.5+0.0j) - sqrt_pi/2) < tolerance1
        assert abs(gamma(2.5+0.0j) - 3*sqrt_pi/4) < tolerance1
        assert abs(gamma(jay) - (-0.1549498283018106-0.4980156681183560j)) < tolerance0
        assert abs(gamma(one + jay) - (0.4980156681183560-0.1549498283018106j)) < tolerance0
        assert abs(gamma(0.75+0.0j) - 1.22541670246517764512+0.0j) < tolerance1
        assert abs(gamma(0.25+0.0j) - 3.62560990822190831193+0.0j) < tolerance2
