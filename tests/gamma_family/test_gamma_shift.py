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

    def test_gamma_step_real(self) -> None:
        assert 1.22541670246517 < gamma_real(0.75) < 1.22541670246518  # Looking at trend,
        assert 1.29805533264755 < gamma_real(0.70) < 1.29805533264756  # no a priori knowledge
        assert 1.38479510202650 < gamma_real(0.65) < 1.38479510202652  # if most of these
        assert 1.48919224881281 < gamma_real(0.60) < 1.48919224881282  # are correct.
        assert 1.61612426873357 < gamma_real(0.55) < 1.61612426873358
        assert 1.77245385090551 < gamma_real(0.50) < 1.77245385090552
        assert 1.96813640060238 < gamma_real(0.45) < 1.96813640060239
        assert 2.21815954375768 < gamma_real(0.40) < 2.21815954375769
        assert 2.54614697721228 < gamma_real(0.35) < 2.54614697721229
        assert 2.99156898768758 < gamma_real(0.30) < 2.99156898768760
        assert 3.62560990822190 < gamma_real(0.25) < 3.62560990822191
        assert 4.59084371199880 < gamma_real(0.20) < 4.59084371199881
        assert 6.22027287404987 < gamma_real(0.15) < 6.22027287404988
        assert 9.51350769866872 < gamma_real(0.10) < 9.51350769866874
        assert 19.4700853112555 < gamma_real(0.05) < 19.4700853112556
        assert 24.4609550228560 < gamma_real(0.04) < 24.4609550228562
        assert 32.7849983517941 < gamma_real(0.03) < 32.7849983517942
        assert 49.4422101631956 < gamma_real(0.02) < 49.4422101631957
        assert 99.4325851191505 < gamma_real(0.01) < 99.4325851191506
        assert 199.427707050203 < gamma_real(0.005) < 199.427707050204
        assert -200.58218375519 < gamma_real(-0.005) < -200.58218375518
        assert -100.58719796442 < gamma_real(-0.01) < -100.58719796441
        assert -50.597367790626 < gamma_real(-0.02) < -50.597367790625

    def test_gamma_step_complex(self) -> None:
         assert 1.22541670246517 < gamma(0.75).real < 1.22541670246518
         assert 1.29805533264755 < gamma(0.70).real < 1.29805533264756
         assert 1.38479510202650 < gamma(0.65).real < 1.38479510202652
         assert 1.48919224881281 < gamma(0.60).real < 1.48919224881282
         assert 1.61612426873357 < gamma(0.55).real < 1.61612426873358
         assert 1.77245385090551 < gamma(0.50).real < 1.77245385090552
         assert 1.96813640060238 < gamma(0.45).real < 1.96813640060239
         assert 2.21815954375768 < gamma(0.40).real < 2.21815954375769
         assert 2.54614697721228 < gamma(0.35).real < 2.54614697721229
         assert 2.99156898768758 < gamma(0.30).real < 2.99156898768760
         assert 3.62560990822190 < gamma(0.25).real < 3.62560990822191
         assert 4.59084371199880 < gamma(0.20).real < 4.59084371199881
         assert 6.22027287404986 < gamma(0.15).real < 6.22027287404988
         assert 9.51350769866872 < gamma(0.10).real < 9.51350769866874
         assert 19.4700853112554 < gamma(0.05).real < 19.4700853112555
         assert 24.4609550228560 < gamma(0.04).real < 24.4609550228562
         assert 32.784998351793 < gamma(0.03).real < 32.784998351794
         assert 49.4422101631956 < gamma(0.02).real < 49.4422101631957
         assert 99.4325851191506 < gamma(0.01).real < 99.4325851191507
         assert 199.427707050202 < gamma(0.005).real < 199.427707050203
