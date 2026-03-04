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

tolerance0 = 5.0e-16
tolerance1 = 5.0e-15
tolerance2 = 5.0e-14
tolerance3 = 5.0e-13
tolerance4 = 5.0e-12
tolerance5 = 5.0e-11

jay = 0.0+1.0j
zero = 0.0+0.0j
one = 1.0+0.0j
two = 2.0+0.0j
three = 3.0+0.0j
four = 4.0+0.0j
five = 5.0+0.0j


class Test_gamma:
    def test_beta_real(self) -> None:
        assert abs(beta_real(1.0, 1.0) - 1.0) < tolerance0
        assert abs(beta_real(2.0, 3.0) - 1.0/12.0) < tolerance0
        assert abs(beta_real(2.5, 3.5) - 3.0*pi/256) < tolerance0

    def test_beta_complex(self) -> None:
        assert abs(beta(one, one) - 1.0+0.0j) < tolerance0
        assert abs(beta(one, two) - 0.5+0.0j) < tolerance0
        assert abs(beta(five, four) - 0.0035714285714285713+0.0j) < tolerance0
