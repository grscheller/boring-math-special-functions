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
        assert abs(gamma(1.25) - 0.25*gamma(0.25)) < tolerance2
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

    def test_gamma_step_down_0_5(self) -> None:
        assert abs(gamma(0.5+1.0j) - (0.3006946172606561-0.42496787943312364j)) <= tolerance2
        assert abs(gamma(0.5+0.9j) - (0.3569971977013909-0.49294814036733847j)) <= tolerance2
        assert abs(gamma(0.5+0.8j) - (0.4306297031135052-0.56585745696284240j)) <= tolerance2
        assert abs(gamma(0.5+0.7j) - (0.5274198573183648-0.64044947484521810j)) <= tolerance2
        assert abs(gamma(0.5+0.6j) - (0.6542928765318525-0.71022181485669000j)) <= tolerance2
        assert abs(gamma(0.5+0.5j) - (0.8181639995417405-0.76331382871398120j)) <= tolerance2
        assert abs(gamma(0.5+0.4j) - (1.0226690032213737-0.78000232430956540j)) <= tolerance2
        assert abs(gamma(0.5+0.3j) - (1.2609927863965710-0.73175950569183290j)) <= tolerance2
        assert abs(gamma(0.5+0.2j) - (1.5047979605685253-0.58731576760504370j)) <= tolerance2
        assert abs(gamma(0.5+0.1j) - (1.6976178263828794-0.33284283907262086j)) <= tolerance2
        assert abs(gamma(0.5+0.0j) - (pi**0.5)) <= tolerance2
        assert abs(gamma(0.5-0.1j) - (1.6976178263828856+0.33284283907262147j)) <= tolerance2
        assert abs(gamma(0.5-0.2j) - (1.5047979605685264+0.5873157676050431j)) <= tolerance2
        assert abs(gamma(0.5-0.3j) - (1.2609927863965775+0.7317595056918342j)) <= tolerance2
        assert abs(gamma(0.5-0.4j) - (1.0226690032213754+0.7800023243095655j)) <= tolerance2
        assert abs(gamma(0.5-0.5j) - (0.8181639995417473+0.7633138287139827j)) <= tolerance2
        assert abs(gamma(0.5-0.6j) - (0.6542928765318525+0.7102218148566902j)) <= tolerance2
        assert abs(gamma(0.5-0.7j) - (0.5274198573183714+0.640449474845219j)) <= tolerance2
        assert abs(gamma(0.5-0.8j) - (0.4306297031135083+0.5658574569628427j)) <= tolerance2
        assert abs(gamma(0.5-0.9j) - (0.35699719770139293+0.4929481403673382j)) <= tolerance2
        assert abs(gamma(0.5-1.0j) - (0.3006946172606562+0.42496787943312364j)) <= tolerance2

    def test_gamma_step_down_1_0(self) -> None:
        assert abs(gamma(1.0+1.0j) - (0.4980156681183563-0.15494982830181075j)) <= tolerance2
        assert abs(gamma(1.0+0.9j) - (0.5523283329225556-0.17514590718657191j)) <= tolerance2
        assert abs(gamma(1.0+0.8j) - (0.6107989880679575-0.19177395301476516j)) <= tolerance2
        assert abs(gamma(1.0+0.7j) - (0.6728253931632413-0.20285243648300230j)) <= tolerance2
        assert abs(gamma(1.0+0.6j) - (0.7371564227998941-0.20619323776345633j)) <= tolerance2
        assert abs(gamma(1.0+0.5j) - (0.8016940970697127-0.19963973816459790j)) <= tolerance2
        assert abs(gamma(1.0+0.4j) - (0.8633791138852640-0.18145712581519724j)) <= tolerance2
        assert abs(gamma(1.0+0.3j) - (0.9182730233911345-0.15084922588288902j)) <= tolerance2
        assert abs(gamma(1.0+0.2j) - (0.9619474203206209-0.10848528178474010j)) <= tolerance2
        assert abs(gamma(1.0+0.1j) - (0.9902066295883810-0.05682380875371226j)) <= tolerance2
        assert abs(gamma(1.0+0.0j) - (1.0+0.0j)) <= tolerance2
        assert abs(gamma(1.0-0.1j) - (0.9902066295883846+0.05682380875371215j)) <= tolerance2
        assert abs(gamma(1.0-0.2j) - (0.9619474203206217+0.10848528178473960j)) <= tolerance2
        assert abs(gamma(1.0-0.3j) - (0.9182730233911386+0.15084922588288846j)) <= tolerance2
        assert abs(gamma(1.0-0.4j) - (0.8633791138852651+0.18145712581519668j)) <= tolerance2
        assert abs(gamma(1.0-0.5j) - (0.8016940970697176+0.19963973816459646j)) <= tolerance2
        assert abs(gamma(1.0-0.6j) - (0.7371564227998941+0.20619323776345650j)) <= tolerance2
        assert abs(gamma(1.0-0.7j) - (0.6728253931632462+0.20285243648299994j)) <= tolerance2
        assert abs(gamma(1.0-0.8j) - (0.6107989880679598+0.19177395301476366j)) <= tolerance2
        assert abs(gamma(1.0-0.9j) - (0.5523283329225570+0.17514590718657067j)) <= tolerance2
        assert abs(gamma(1.0-1.0j) - (0.4980156681183564+0.15494982830181060j)) <= tolerance2

    def test_gamma_step_down_1_5(self) -> None:
        assert abs(gamma(1.5+1.0j) - (0.5753151880634519+0.08821067754409376j)) <= tolerance2
        assert abs(gamma(1.5+0.9j) - (0.6221519251813004+0.07482340774758209j)) <= tolerance2
        assert abs(gamma(1.5+0.8j) - (0.6680008171270273+0.06157503400938330j)) <= tolerance2
        assert abs(gamma(1.5+0.7j) - (0.7120245610508359+0.04896916270024659j)) <= tolerance2
        assert abs(gamma(1.5+0.6j) - (0.7532795271799406+0.03746481849076683j)) <= tolerance2
        assert abs(gamma(1.5+0.5j) - (0.7907389141278611+0.027425085413879724j)) <= tolerance2
        assert abs(gamma(1.5+0.4j) - (0.8233354313345141+0.019066439133767377j)) <= tolerance2
        assert abs(gamma(1.5+0.3j) - (0.8500242449058351+0.012418083073055253j)) <= tolerance2
        assert abs(gamma(1.5+0.2j) - (0.8698621338052719+0.0073017083111836245j)) <= tolerance2
        assert abs(gamma(1.5+0.1j) - (0.8820931970987023+0.0033403631019776198j)) <= tolerance2
        assert abs(gamma(1.5+0.0j) - (pi**0.5 * 0.5)) <= tolerance2
        assert abs(gamma(1.5-0.1j) - (0.8820931970987054-0.003340363101977925j)) <= tolerance2
        assert abs(gamma(1.5-0.2j) - (0.8698621338052726-0.007301708311184041j)) <= tolerance2
        assert abs(gamma(1.5-0.3j) - (0.8500242449058388-0.012418083073056474j)) <= tolerance2
        assert abs(gamma(1.5-0.4j) - (0.8233354313345149-0.019066439133767932j)) <= tolerance2
        assert abs(gamma(1.5-0.5j) - (0.7907389141278653-0.0274250854138825j)) <= tolerance2
        assert abs(gamma(1.5-0.6j) - (0.7532795271799407-0.037464818490766716j)) <= tolerance2
        assert abs(gamma(1.5-0.7j) - (0.7120245610508398-0.0489691627002507j)) <= tolerance2
        assert abs(gamma(1.5-0.8j) - (0.6680008171270291-0.061575034009385576j)) <= tolerance2
        assert abs(gamma(1.5-0.9j) - (0.6221519251813011-0.07482340774758398j)) <= tolerance2
        assert abs(gamma(1.5-1.0j) - (0.5753151880634522-0.0882106775440939j)) <= tolerance2
