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

from cmath import exp as std_exp, inf, infj, isinf, pi
from boring_math.special_functions.exponential import cexp
from boring_math.special_functions.trig0 import sin0, cos0

c1 = complex(0.831, -0.479)
c2 = complex(0.411, 0.672)
c3 = complex(cos0(0.613*pi), sin0(0.613*pi))
c4 = complex(cos0(-0.244*pi), sin0(-0.244*pi))
c5 = -2.0+1.0j
c6 = 4.0-5.2j
c7 = 0.4-0.5j
c8 = -0.4+0.2j
c9 = -42.0+2.0j

tolerance0 = 5.0e-16
tolerance1 = 5.0e-15
tolerance2 = 5.0e-14
tolerance3 = 5.0e-13
tolerance4 = 5.0e-12


class Test_cexp:
    def test_cexp(self) -> None:
        assert abs(cexp(0.0) - std_exp(0.0)) < tolerance0
        assert abs(cexp(1.0) - std_exp(1.0)) < tolerance0
        assert abs(cexp(-1.0) - std_exp(-1.0)) < tolerance0
        assert abs(cexp(0+1j) - std_exp(0+1j)) < tolerance0
        assert abs(cexp(0-1j) - std_exp(0-1j)) < tolerance1
        assert abs(cexp(1j*pi/2) - std_exp(1j*pi/2)) < tolerance0
        assert abs(cexp(-1j*pi/2) - std_exp(-1j*pi/2)) < tolerance1
        assert abs(cexp(1j*pi/4) - std_exp(1j*pi/4)) < tolerance0
        assert abs(cexp(-1j*pi/4) - std_exp(-1j*pi/4)) < tolerance1
        assert abs(cexp(1 - 1j*pi/6) - std_exp(1 - 1j*pi/6)) < tolerance2
        assert abs(cexp(1/8 - 1j*pi/17) - std_exp(1/8 - 1j*pi/17)) < tolerance1
        assert abs(cexp(c1) - std_exp(c1)) < tolerance1
        assert abs(cexp(c2) - std_exp(c2)) < tolerance0
        assert abs(cexp(c3) - std_exp(c3)) < tolerance0
        assert abs(cexp(c4) - std_exp(c4)) < tolerance1
        assert abs(cexp(c5) - std_exp(c5)) < tolerance3
        assert abs(cexp(c5, n=23) - std_exp(c5)) < tolerance0
        assert abs(cexp(c6, n=34) - std_exp(c6)) < tolerance4
        assert abs(cexp(c6, n=80) - std_exp(c6)) < tolerance4
        assert abs(cexp(c7) - std_exp(c7)) < tolerance2
        assert abs(cexp(c8) - std_exp(c8)) < tolerance0
        assert abs(cexp(c9) - std_exp(c9)) < tolerance0

    def test_infinity(self) -> None:
        assert cexp(0.0+0.0j) == 1.0
        assert cexp(0.0) == 1.0
        assert isinf(cexp(inf))
        assert isinf(cexp(inf + 0j))
        assert isinf(cexp(inf + 42j))
        assert cexp(-inf + 0j) == 0.0
        assert cexp(-inf + 42j) == 0.0
        assert cexp(-inf - 42j) == 0.0
        assert cexp(-inf + infj) == 0.0
