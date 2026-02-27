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

from cmath import exp as cexp
from math import pi
from boring_math.special_functions.complex import exp
from boring_math.special_functions.float0 import sin0, cos0

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


class Test_exp0:
    def test_exp0(self) -> None:
        assert abs(exp(zero) - cexp(zero)) < tolerance0
        assert abs(exp(one) - cexp(one)) < tolerance0
        assert abs(exp(neg_one) - cexp(neg_one)) < tolerance0
        assert abs(exp(eye) - cexp(eye)) < tolerance0
        assert abs(exp(neg_eye) - cexp(neg_eye)) < tolerance1
        assert abs(exp(eye_pi_div_2) - cexp(eye_pi_div_2)) < tolerance0
        assert abs(exp(neg_eye_pi_div_2) - cexp(neg_eye_pi_div_2)) < tolerance1
        assert abs(exp(eye_pi_div_4) - cexp(eye_pi_div_4)) < tolerance0
        assert abs(exp(neg_eye_pi_div_4) - cexp(neg_eye_pi_div_4)) < tolerance1
        assert abs(exp(neg_eye_pi_div_4) - cexp(neg_eye_pi_div_4)) < tolerance1
        assert abs(exp(c1) - cexp(c1)) < tolerance1
        assert abs(exp(c2) - cexp(c2)) < tolerance0
        assert abs(exp(c3) - cexp(c3)) < tolerance0
        assert abs(exp(c4) - cexp(c4)) < tolerance1
        assert abs(exp(c5) - cexp(c5)) < tolerance3
        assert abs(exp(c5, n=23) - cexp(c5)) < tolerance0
        assert abs(exp(c6, n=34) - cexp(c6)) < tolerance4
        assert abs(exp(c7) - cexp(c7)) < tolerance2
        assert abs(exp(c8) - cexp(c8)) < tolerance0
        assert abs(exp(c9) - cexp(c9)) < tolerance0
