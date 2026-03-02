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

from cmath import exp as std_cexp
from math import pi
from boring_math.special_functions.exponential import cexp0
from boring_math.special_functions.trig0 import sin0, cos0

tolerance0 = 5.0e-16

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


class Test_cexp0:
    def test_cexp0(self) -> None:
        assert abs(cexp0(zero) - std_cexp(zero)) < tolerance0
        assert abs(cexp0(one) - std_cexp(one)) < tolerance0
        assert abs(cexp0(neg_one) - std_cexp(neg_one)) < tolerance0
        assert abs(cexp0(eye) - std_cexp(eye)) < tolerance0
        assert abs(cexp0(neg_eye) - std_cexp(neg_eye)) < tolerance0
        assert abs(cexp0(eye_pi_div_2) - std_cexp(eye_pi_div_2)) < tolerance0
        assert abs(cexp0(neg_eye_pi_div_2) - std_cexp(neg_eye_pi_div_2)) < tolerance0
        assert abs(cexp0(eye_pi_div_4) - std_cexp(eye_pi_div_4)) < tolerance0
        assert abs(cexp0(neg_eye_pi_div_4) - std_cexp(neg_eye_pi_div_4)) < tolerance0
        assert abs(cexp0(neg_eye_pi_div_4) - std_cexp(neg_eye_pi_div_4)) < tolerance0
        assert abs(cexp0(c1) - std_cexp(c1)) < tolerance0
        assert abs(cexp0(c2) - std_cexp(c2)) < tolerance0
        assert abs(cexp0(c3) - std_cexp(c3)) < tolerance0
        assert abs(cexp0(c4) - std_cexp(c4)) < tolerance0
