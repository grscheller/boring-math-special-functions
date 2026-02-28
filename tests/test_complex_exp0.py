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
from boring_math.special_functions.trig0_complex import exp0
from boring_math.special_functions.trig0_float import sin0, cos0

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
        assert abs(exp0(zero) - cexp(zero)) < tolerance
        assert abs(exp0(one) - cexp(one)) < tolerance
        assert abs(exp0(neg_one) - cexp(neg_one)) < tolerance
        assert abs(exp0(eye) - cexp(eye)) < tolerance
        assert abs(exp0(neg_eye) - cexp(neg_eye)) < tolerance
        assert abs(exp0(eye_pi_div_2) - cexp(eye_pi_div_2)) < tolerance
        assert abs(exp0(neg_eye_pi_div_2) - cexp(neg_eye_pi_div_2)) < tolerance
        assert abs(exp0(eye_pi_div_4) - cexp(eye_pi_div_4)) < tolerance
        assert abs(exp0(neg_eye_pi_div_4) - cexp(neg_eye_pi_div_4)) < tolerance
        assert abs(exp0(neg_eye_pi_div_4) - cexp(neg_eye_pi_div_4)) < tolerance
        assert abs(exp0(c1) - cexp(c1)) < tolerance
        assert abs(exp0(c2) - cexp(c2)) < tolerance
        assert abs(exp0(c3) - cexp(c3)) < tolerance
        assert abs(exp0(c4) - cexp(c4)) < tolerance
