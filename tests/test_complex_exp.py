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

from cmath import exp
from math import pi
from boring_math.special_functions.complex0 import exp0 as cexp
from boring_math.special_functions.float0 import sin0, cos0

tolerance = 5.0e-16

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


class Test_exp0:
    def test_exp0(self) -> None:
        assert abs(cexp(zero) - exp(zero)) < tolerance
        assert abs(cexp(one) - exp(one)) < tolerance
        assert abs(cexp(neg_one) - exp(neg_one)) < tolerance
        assert abs(cexp(eye) - exp(eye)) < tolerance
        assert abs(cexp(neg_eye) - exp(neg_eye)) < tolerance
        assert abs(cexp(eye_pi_div_2) - exp(eye_pi_div_2)) < tolerance
        assert abs(cexp(neg_eye_pi_div_2) - exp(neg_eye_pi_div_2)) < tolerance
        assert abs(cexp(eye_pi_div_4) - exp(eye_pi_div_4)) < tolerance
        assert abs(cexp(neg_eye_pi_div_4) - exp(neg_eye_pi_div_4)) < tolerance
        assert abs(cexp(neg_eye_pi_div_4) - exp(neg_eye_pi_div_4)) < tolerance
        assert abs(cexp(c1) - exp(c1)) < tolerance
        assert abs(cexp(c2) - exp(c2)) < tolerance
        assert abs(cexp(c3) - exp(c3)) < tolerance
        assert abs(cexp(c4) - exp(c4)) < tolerance
