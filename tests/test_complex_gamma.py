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
from boring_math.special_functions.trig_complex import gamma

sqrt_pi = pi**(0.5)
jay = 0.0+1.0j

tolerance0 = 5.0e-16
tolerance1 = 5.0e-15
tolerance2 = 5.0e-14
tolerance3 = 5.0e-13
tolerance4 = 5.0e-12

one = 1.0+0.0j
two = 2.0+0.0j
three = 3.0+0.0j
four = 4.0+0.0j
five = 5.0+0.0j
six = 6.0+0.0j
twenty_four = 24.0+0.0j
one_twenty = 120.0+0.0j
half = 0.5+0.0j


class Test_exp0:
    def test_exp0(self) -> None:
        assert abs(gamma(one) - one) < tolerance0
        assert abs(gamma(two) - one) < tolerance0
        assert abs(gamma(three) - two) < tolerance1
        assert abs(gamma(four) - six) < tolerance2
        assert abs(gamma(five) - twenty_four) < tolerance2
        assert abs(gamma(six) - one_twenty) < tolerance3
        assert abs(gamma(half) - sqrt_pi) < tolerance0
        assert abs(gamma(jay) - (-0.15494982830181067-0.49801566811835607j)) < tolerance0
