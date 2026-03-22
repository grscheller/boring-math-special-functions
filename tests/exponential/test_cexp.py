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

from cmath import exp as std_cexp, inf, infj, isnan
from math import pi
from boring_math.special_functions.exponential import cexp, infinity
from boring_math.special_functions.trig0 import sin0, cos0

tolerance0 = 5.0e-16
tolerance1 = 5.0e-15
tolerance2 = 5.0e-14
tolerance3 = 5.0e-13
tolerance4 = 5.0e-12

zero = complex(0, 0)
one = complex(1, 0)
neg_one = complex(-1, 0)
eye = complex(0, 1)
neg_eye = complex(0, -1)
eye_pi_div_2 = complex(0, pi/2.0)
neg_eye_pi_div_2 = complex(0, pi/(-2.0))
eye_pi_div_4 = complex(0, pi/4.0)
neg_eye_pi_div_4 = complex(0, pi/(-4.0))
c1 = complex(0.831, -0.479)
c2 = complex(0.411, 0.672)
c3 = complex(cos0(0.613*pi), sin0(0.613*pi))
c4 = complex(cos0(-0.244*pi), sin0(-0.244*pi))
c5 = -2.0+1.0j
c6 = 4.0-5.2j
c7 = 0.4-0.5j
c8 = -0.4+0.2j
c9 = -42.0+2.0j


class Test_cexp:
    def test_cexp(self) -> None:
        assert abs(cexp(zero) - std_cexp(zero)) < tolerance0
        assert abs(cexp(one) - std_cexp(one)) < tolerance0
        assert abs(cexp(neg_one) - std_cexp(neg_one)) < tolerance0
        assert abs(cexp(eye) - std_cexp(eye)) < tolerance0
        assert abs(cexp(neg_eye) - std_cexp(neg_eye)) < tolerance1
        assert abs(cexp(eye_pi_div_2) - std_cexp(eye_pi_div_2)) < tolerance0
        assert abs(cexp(neg_eye_pi_div_2) - std_cexp(neg_eye_pi_div_2)) < tolerance1
        assert abs(cexp(eye_pi_div_4) - std_cexp(eye_pi_div_4)) < tolerance0
        assert abs(cexp(neg_eye_pi_div_4) - std_cexp(neg_eye_pi_div_4)) < tolerance1
        assert abs(cexp(neg_eye_pi_div_4) - std_cexp(neg_eye_pi_div_4)) < tolerance1
        assert abs(cexp(c1) - std_cexp(c1)) < tolerance1
        assert abs(cexp(c2) - std_cexp(c2)) < tolerance0
        assert abs(cexp(c3) - std_cexp(c3)) < tolerance0
        assert abs(cexp(c4) - std_cexp(c4)) < tolerance1
        assert abs(cexp(c5) - std_cexp(c5)) < tolerance3
        assert abs(cexp(c5, n=23) - std_cexp(c5)) < tolerance0
        assert abs(cexp(c6, n=34) - std_cexp(c6)) < tolerance4
        assert abs(cexp(c7) - std_cexp(c7)) < tolerance2
        assert abs(cexp(c8) - std_cexp(c8)) < tolerance0
        assert abs(cexp(c9) - std_cexp(c9)) < tolerance0

    def test_infinity(self) -> None:
        assert cexp(0.0+0.0j) == 1.0
        assert cexp(0.0) == 1.0
        assert isnan(cexp(inf))
        assert isnan(cexp(inf + 0j))
        assert isnan(cexp(infj))
        assert isnan(cexp(inf+infj))
        assert isnan(cexp(inf+infj))
        assert isnan(cexp(42 + infj))
        assert isnan(cexp(inf + 42j))
        assert isnan(cexp(-inf + 0j))
