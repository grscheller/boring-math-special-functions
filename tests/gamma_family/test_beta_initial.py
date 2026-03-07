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

from math import pi
from boring_math.special_functions.beta import beta, beta_real

tolerance1 = 1.0e-14
tolerance2 = 2.0e-14
tolerance3 = 3.0e-14

jay = 0.0+1.0j
zero = 0.0+0.0j
half = 0.5+0.0j
one = 1.0+0.0j
two = 2.0+0.0j
three = 3.0+0.0j
four = 4.0+0.0j
five = 5.0+0.0j


class Test_gamma:
    def test_beta_real(self) -> None:
        assert abs(beta_real(1.0, 1.0) - 1.0) < tolerance1
        assert abs(beta_real(2.0, 3.0) - 1.0/12.0) < tolerance1
        assert abs(beta_real(4.0, 4.0) - 1.0/140) < tolerance1
        assert abs(beta_real(0.5, 0.5) - pi) < tolerance1
        assert abs(beta_real(2.5, 3.5) - 3.0*pi/256) < tolerance1
        assert abs(beta_real(1.5, 0.5) - pi/2.0) < tolerance1

    def test_beta_complex(self) -> None:
        assert abs(beta(one, one) - 1.0+0.0j) < tolerance1
        assert abs(beta(one, two) - 0.5+0.0j) < tolerance1
        assert abs(beta(five, four) - 0.0035714285714286+0.0j) < tolerance1
        assert abs(beta(two+half, one+half) - 1.5*0.5*0.5*pi/6.0) < tolerance1
        assert abs(beta(jay, one) - (-jay)) <tolerance1
