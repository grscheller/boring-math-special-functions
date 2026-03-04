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
tolerance1 = 1.0e-15
tolerance2 = 5.0e-15
tolerance3 = 1.0e-14
tolerance4 = 5.0e-14
tolerance5 = 1.0e-13

class Test_gamma_shift_explore:
    def test_gamma_shift_real(self) -> None:
        assert abs(gamma_real(0.75) - 1.22541670246517764512) < tolerance1
        assert abs(gamma_real(1.75)/(0.75) - 1.22541670246517764512) < tolerance1
        assert abs(gamma_real(2.75)/(0.75*1.75) - 1.22541670246517764512) < tolerance2
        assert abs(gamma_real(3.75)/(0.75*1.75*2.75) - 1.22541670246517764512) < tolerance1
        assert abs(gamma_real(4.75)/(0.75*1.75*2.75*3.75) - 1.22541670246517764512) < tolerance2
        assert abs(gamma_real(5.75)/(0.75*1.75*2.75*3.75*4.75) - 1.22541670246517764512) < tolerance2
        assert abs(gamma_real(6.75)/(0.75*1.75*2.75*3.75*4.75*5.75) - 1.22541670246517764512) < tolerance2
        assert abs(gamma_real(7.75)/(0.75*1.75*2.75*3.75*4.75*5.75*6.75) - 1.22541670246517764512) < tolerance2
        assert abs(gamma_real(8.75)/(0.75*1.75*2.75*3.75*4.75*5.75*6.75*7.75) - 1.22541670246517764512) < tolerance2
        assert abs(gamma_real(9.75)/(0.75*1.75*2.75*3.75*4.75*5.75*6.75*7.75*8.75) - 1.22541670246517764512) < tolerance2

        assert abs(gamma_real(0.25) - 3.62560990822190831193) < tolerance2
        assert abs(gamma_real(1.25)/(0.25) - 3.62560990822190831193) < tolerance2
        assert abs(gamma_real(2.25)/(0.25*1.25) - 3.62560990822190831193) < tolerance2
        assert abs(gamma_real(3.25)/(0.25*1.25*2.25) - 3.62560990822190831193) < tolerance2
        assert abs(gamma_real(4.25)/(0.25*1.25*2.25*3.25) - 3.62560990822190831193) < tolerance3
        assert abs(gamma_real(5.25)/(0.25*1.25*2.25*3.25*4.25) - 3.62560990822190831193) < tolerance3
        assert abs(gamma_real(6.25)/(0.25*1.25*2.25*3.25*4.25*5.25) - 3.62560990822190831193) < tolerance3
        assert abs(gamma_real(7.25)/(0.25*1.25*2.25*3.25*4.25*5.25*6.25) - 3.62560990822190831193) < tolerance4
        assert abs(gamma_real(8.25)/(0.25*1.25*2.25*3.25*4.25*5.25*6.25*7.25) - 3.62560990822190831193) < tolerance4
        assert abs(gamma_real(9.25)/(0.25*1.25*2.25*3.25*4.25*5.25*6.25*7.25*8.25) - 3.62560990822190831193) < tolerance4

    def test_gamma_shift_complex(self) -> None:
        assert abs(gamma(0.75) - 1.22541670246517764512) < tolerance1
        assert abs(gamma(1.75)/(0.75) - 1.22541670246517764512) < tolerance1
        assert abs(gamma(2.75)/(0.75*1.75) - 1.22541670246517764512) < tolerance2
        assert abs(gamma(3.75)/(0.75*1.75*2.75) - 1.22541670246517764512) < tolerance1
        assert abs(gamma(4.75)/(0.75*1.75*2.75*3.75) - 1.22541670246517764512) < tolerance2
        assert abs(gamma(5.75)/(0.75*1.75*2.75*3.75*4.75) - 1.22541670246517764512) < tolerance2
        assert abs(gamma(6.75)/(0.75*1.75*2.75*3.75*4.75*5.75) - 1.22541670246517764512) < tolerance2
        assert abs(gamma(7.75)/(0.75*1.75*2.75*3.75*4.75*5.75*6.75) - 1.22541670246517764512) < tolerance2
        assert abs(gamma(8.75)/(0.75*1.75*2.75*3.75*4.75*5.75*6.75*7.75) - 1.22541670246517764512) < tolerance2
        assert abs(gamma(9.75)/(0.75*1.75*2.75*3.75*4.75*5.75*6.75*7.75*8.75) - 1.22541670246517764512) < tolerance2

        assert abs(gamma(0.25) - 3.62560990822190831193) < tolerance4
        assert abs(gamma(1.25)/(0.25) - 3.62560990822190831193) < tolerance2
        assert abs(gamma(2.25)/(0.25*1.25) - 3.62560990822190831193) < tolerance2
        assert abs(gamma(3.25)/(0.25*1.25*2.25) - 3.62560990822190831193) < tolerance2
        assert abs(gamma(4.25)/(0.25*1.25*2.25*3.25) - 3.62560990822190831193) < tolerance3
        assert abs(gamma(5.25)/(0.25*1.25*2.25*3.25*4.25) - 3.62560990822190831193) < tolerance3
        assert abs(gamma(6.25)/(0.25*1.25*2.25*3.25*4.25*5.25) - 3.62560990822190831193) < tolerance3
        assert abs(gamma(7.25)/(0.25*1.25*2.25*3.25*4.25*5.25*6.25) - 3.62560990822190831193) < tolerance4
        assert abs(gamma(8.25)/(0.25*1.25*2.25*3.25*4.25*5.25*6.25*7.25) - 3.62560990822190831193) < tolerance3
        assert abs(gamma(9.25)/(0.25*1.25*2.25*3.25*4.25*5.25*6.25*7.25*8.25) - 3.62560990822190831193) < tolerance4
