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
from boring_math.special_functions.gamma_family.gamma import gamma, gamma_real

sqrt_pi = pi**0.5
euler = 0.57721566490153286060
jay = 0.0+1.0j
one = 1.0+0.0j
two = 2.0+0.0j
three = 3.0+0.0j
four = 4.0+0.0j
five = 5.0+0.0j
six = 6.0+0.0j

tolerance1 = 2.0e-14
tolerance2 = 5.0e-14
tolerance3 = 1.0e-13
tolerance4 = 5.0e-13
tolerance5 = 1.0e-12
tolerance6 = 5.0e-12
tolerance7 = 1.0e-11
tolerance8 = 5.0e-11
tolerance9 = 1.0e-10
tolerance10 = 5.0e-10

class Test_gamma_shift_real:
    def test_gamma_shift_real(self) -> None:
        assert abs(gamma_real(-2.25) - (-3.25)*gamma_real(-3.25)) < tolerance1
        assert abs(gamma_real(-1.25) - (-2.25)*gamma_real(-2.25)) < tolerance1
        assert abs(gamma_real(-0.25) - (-1.25)*gamma_real(-1.25)) < tolerance1
        assert abs(gamma_real(0.75) - (-0.25)*gamma_real(-0.25)) < tolerance1
        assert abs(gamma_real(0.75) - 1.22541670246517764512) < tolerance1 # To 20 decimal places
        assert abs(gamma_real(1.75) - 0.75*gamma_real(0.75)) < tolerance1
        assert abs(gamma_real(2.75) - 1.75*gamma_real(1.75)) < tolerance1
        assert abs(gamma_real(3.75) - 2.75*gamma_real(2.75)) < tolerance1
        assert abs(gamma_real(4.75) - 3.75*gamma_real(3.75)) < tolerance1
        assert abs(gamma_real(5.75) - 4.75*gamma_real(4.75)) < tolerance4
        assert abs(gamma_real(6.75) - 5.75*gamma_real(5.75)) < tolerance4
        assert abs(gamma_real(7.75) - 6.75*gamma_real(6.75)) < tolerance4
        assert abs(gamma_real(8.75) - 7.75*gamma_real(7.75)) < tolerance8
        assert abs(gamma_real(9.75) - 8.75*gamma_real(8.75)) < tolerance10

        assert abs(gamma_real(-2.75) - (-3.75)*gamma_real(-3.75)) < tolerance1
        assert abs(gamma_real(-1.75) - (-2.75)*gamma_real(-2.75)) < tolerance1
        assert abs(gamma_real(-0.75) - (-1.75)*gamma_real(-1.75)) < tolerance1
        assert abs(gamma_real(0.25) - (-0.75)*gamma_real(-0.75)) < tolerance1
        assert abs(gamma_real(0.25) - 3.62560990822190831193) < tolerance1 # To 20 decimal places
        assert abs(gamma_real(1.25) - 0.25*gamma_real(0.25)) < tolerance1
        assert abs(gamma_real(2.25) - 1.25*gamma_real(1.25)) < tolerance1
        assert abs(gamma_real(3.25) - 2.25*gamma_real(2.25)) < tolerance1
        assert abs(gamma_real(4.25) - 3.25*gamma_real(3.25)) < tolerance1
        assert abs(gamma_real(5.25) - 4.25*gamma_real(4.25)) < tolerance4
        assert abs(gamma_real(6.25) - 5.25*gamma_real(5.25)) < tolerance4
        assert abs(gamma_real(7.25) - 6.25*gamma_real(6.25)) < tolerance6
        assert abs(gamma_real(8.25) - 7.25*gamma_real(7.25)) < tolerance8
        assert abs(gamma_real(9.25) - 8.25*gamma_real(8.25)) < tolerance10

    def test_gamma_shift_complex(self) -> None:
        assert abs(gamma(-2.25) - (-3.25)*gamma(-3.25)) < tolerance1
        assert abs(gamma(-1.25) - (-2.25)*gamma(-2.25)) < tolerance1
        assert abs(gamma(-0.25) - (-1.25)*gamma(-1.25)) < tolerance1
        assert abs(gamma(0.75) - (-0.25)*gamma(-0.25)) < tolerance1
        assert abs(gamma(0.75) - 1.22541670246517764512) < tolerance1 # To 20 decimal places
        assert abs(gamma(1.75) - 0.75*gamma(0.75)) < tolerance1
        assert abs(gamma(2.75) - 1.75*gamma(1.75)) < tolerance1
        assert abs(gamma(3.75) - 2.75*gamma(2.75)) < tolerance1
        assert abs(gamma(4.75) - 3.75*gamma(3.75)) < tolerance1
        assert abs(gamma(5.75) - 4.75*gamma(4.75)) < tolerance4
        assert abs(gamma(6.75) - 5.75*gamma(5.75)) < tolerance4
        assert abs(gamma(7.75) - 6.75*gamma(6.75)) < tolerance4
        assert abs(gamma(8.75) - 7.75*gamma(7.75)) < tolerance8
        assert abs(gamma(9.75) - 8.75*gamma(8.75)) < tolerance10

        assert abs(gamma(-2.75) - (-3.75)*gamma(-3.75)) < tolerance1
        assert abs(gamma(-1.75) - (-2.75)*gamma(-2.75)) < tolerance1
        assert abs(gamma(-0.75) - (-1.75)*gamma(-1.75)) < tolerance1
        assert abs(gamma(0.25) - (-0.75)*gamma(-0.75)) < tolerance1
        assert abs(gamma(0.25) - 3.62560990822190831193) < tolerance1 # To 20 decimal places
        assert abs(gamma(1.25) - 0.25*gamma(0.25)) < tolerance1
        assert abs(gamma(2.25) - 1.25*gamma(1.25)) < tolerance1
        assert abs(gamma(3.25) - 2.25*gamma(2.25)) < tolerance1
        assert abs(gamma(4.25) - 3.25*gamma(3.25)) < tolerance1
        assert abs(gamma(5.25) - 4.25*gamma(4.25)) < tolerance4
        assert abs(gamma(6.25) - 5.25*gamma(5.25)) < tolerance4
        assert abs(gamma(7.25) - 6.25*gamma(6.25)) < tolerance6
        assert abs(gamma(8.25) - 7.25*gamma(7.25)) < tolerance8
        assert abs(gamma(9.25) - 8.25*gamma(8.25)) < tolerance10

        assert abs(gamma(2.6+3j) - (1.6+3j)*gamma(1.6+3j)) < tolerance1

    def test_gamma_step_real(self) -> None:
        assert 1.22541670246517 < gamma_real(0.75) < 1.22541670246518  # Looking at trend,
        assert 1.29805533264755 < gamma_real(0.70) < 1.29805533264756  # no a priori knowledge
        assert 1.38479510202650 < gamma_real(0.65) < 1.38479510202652  # if most of these
        assert 1.48919224881281 < gamma_real(0.60) < 1.48919224881282  # are correct.
        assert abs(gamma_real(0.75) - 1.22541670246518) < tolerance1
        assert abs(gamma_real(0.70) - 1.29805533264756) < tolerance1
        assert abs(gamma_real(0.65) - 1.38479510202652) < tolerance1
        assert abs(gamma_real(0.60) - 1.48919224881282) < tolerance1
        assert abs(gamma_real(0.55) - 1.61612426873358) < tolerance1
        assert abs(gamma_real(0.50) - 1.77245385090552) < tolerance1
        assert abs(gamma_real(0.45) - 1.96813640060239) < tolerance1
        assert abs(gamma_real(0.40) - 2.21815954375769) < tolerance1
        assert abs(gamma_real(0.35) - 2.54614697721229) < tolerance1
        assert abs(gamma_real(0.30) - 2.99156898768760) < tolerance1
        assert abs(gamma_real(0.25) - 3.62560990822191) < tolerance1
        assert abs(gamma_real(0.20) - 4.59084371199881) < tolerance1
        assert abs(gamma_real(0.15) - 6.22027287404988) < tolerance1
        assert abs(gamma_real(0.10) - 9.51350769866874) < tolerance1
        assert abs(gamma_real(0.05) - 19.4700853112555) < tolerance1
        assert abs(gamma_real(0.04) - 24.4609550228561) < tolerance3
        assert abs(gamma_real(0.03) - 32.7849983517940) < tolerance4
        assert abs(gamma_real(0.02) - 49.4422101631957) < tolerance4
        assert abs(gamma_real(0.01) - 99.4325851191507) < tolerance4
        assert abs(gamma_real(0.005) - 199.427707050203) < tolerance6
        assert abs(gamma_real(-0.005) - (-200.58218375518)) < tolerance7
        assert abs(gamma_real(-0.01) - (-100.58719796441)) < tolerance6
        assert abs(gamma_real(-0.02) - (-50.597367790625)) < tolerance5

    def test_gamma_step_complex(self) -> None:
        assert abs(gamma(0.75).real - 1.22541670246518) < tolerance1
        assert abs(gamma(0.70).real - 1.29805533264756) < tolerance1
        assert abs(gamma(0.65).real - 1.38479510202652) < tolerance1
        assert abs(gamma(0.60).real - 1.48919224881282) < tolerance1
        assert abs(gamma(0.55).real - 1.61612426873358) < tolerance1
        assert abs(gamma(0.50).real - 1.77245385090552) < tolerance1
        assert abs(gamma(0.45).real - 1.96813640060239) < tolerance1
        assert abs(gamma(0.40).real - 2.21815954375769) < tolerance1
        assert abs(gamma(0.35).real - 2.54614697721229) < tolerance1
        assert abs(gamma(0.30).real - 2.99156898768760) < tolerance1
        assert abs(gamma(0.25).real - 3.62560990822191) < tolerance1
        assert abs(gamma(0.20).real - 4.59084371199881) < tolerance1
        assert abs(gamma(0.15).real - 6.22027287404988) < tolerance1
        assert abs(gamma(0.10).real - 9.51350769866874) < tolerance1
        assert abs(gamma(0.05).real - 19.4700853112555) < tolerance1
        assert abs(gamma(0.04).real - 24.4609550228561) < tolerance3
        assert abs(gamma(0.03).real - 32.7849983517940) < tolerance3
        assert abs(gamma(0.02).real - 49.4422101631957) < tolerance3
        assert abs(gamma(0.01).real - 99.4325851191507) < tolerance3
        assert abs(gamma(0.005).real - 199.427707050203) < tolerance6
        assert abs(gamma(-0.005).real - (-200.58218375518)) < tolerance7
        assert abs(gamma(-0.01).real - (-100.58719796441)) < tolerance6
        assert abs(gamma(-0.02).real - (-50.597367790625)) < tolerance5

    def test_gamma_step_down_0_5(self) -> None:
        assert abs(gamma(0.5+1.0j) - (0.30069461726065-0.42496787943312j)) <= tolerance1
        assert abs(gamma(0.5+0.9j) - (0.35699719770139-0.49294814036733j)) <= tolerance1
        assert abs(gamma(0.5+0.8j) - (0.43062970311350-0.56585745696284j)) <= tolerance1
        assert abs(gamma(0.5+0.7j) - (0.52741985731836-0.64044947484521j)) <= tolerance1
        assert abs(gamma(0.5+0.6j) - (0.65429287653185-0.71022181485669j)) <= tolerance1
        assert abs(gamma(0.5+0.5j) - (0.81816399954174-0.76331382871398j)) <= tolerance1
        assert abs(gamma(0.5+0.4j) - (1.02266900322137-0.78000232430956j)) <= tolerance1
        assert abs(gamma(0.5+0.3j) - (1.26099278639657-0.73175950569183j)) <= tolerance1
        assert abs(gamma(0.5+0.2j) - (1.50479796056852-0.58731576760504j)) <= tolerance1
        assert abs(gamma(0.5+0.1j) - (1.69761782638287-0.33284283907262j)) <= tolerance1
        assert abs(gamma(0.5+0.0j) - (pi**0.5)) <= tolerance1
        assert abs(gamma(0.5-0.1j) - (1.69761782638288+0.33284283907262j)) <= tolerance1
        assert abs(gamma(0.5-0.2j) - (1.50479796056852+0.58731576760504j)) <= tolerance1
        assert abs(gamma(0.5-0.3j) - (1.26099278639657+0.73175950569183j)) <= tolerance1
        assert abs(gamma(0.5-0.4j) - (1.02266900322137+0.78000232430956j)) <= tolerance1
        assert abs(gamma(0.5-0.5j) - (0.81816399954174+0.76331382871398j)) <= tolerance1
        assert abs(gamma(0.5-0.6j) - (0.65429287653185+0.71022181485669j)) <= tolerance1
        assert abs(gamma(0.5-0.7j) - (0.52741985731837+0.64044947484521j)) <= tolerance1
        assert abs(gamma(0.5-0.8j) - (0.43062970311350+0.56585745696284j)) <= tolerance1
        assert abs(gamma(0.5-0.9j) - (0.35699719770139+0.49294814036734j)) <= tolerance1
        assert abs(gamma(0.5-1.0j) - (0.30069461726065+0.42496787943312j)) <= tolerance1

    def test_gamma_step_down_1_0(self) -> None:
        assert abs(gamma(1.0+1.0j) - (0.49801566811835-0.15494982830181j)) <= tolerance1
        assert abs(gamma(1.0+0.9j) - (0.55232833292255-0.17514590718657j)) <= tolerance1
        assert abs(gamma(1.0+0.8j) - (0.61079898806795-0.19177395301476j)) <= tolerance1
        assert abs(gamma(1.0+0.7j) - (0.67282539316324-0.20285243648300j)) <= tolerance1
        assert abs(gamma(1.0+0.6j) - (0.73715642279989-0.20619323776345j)) <= tolerance1
        assert abs(gamma(1.0+0.5j) - (0.80169409706971-0.19963973816459j)) <= tolerance1
        assert abs(gamma(1.0+0.4j) - (0.86337911388526-0.18145712581519j)) <= tolerance1
        assert abs(gamma(1.0+0.3j) - (0.91827302339113-0.15084922588288j)) <= tolerance1
        assert abs(gamma(1.0+0.2j) - (0.96194742032062-0.10848528178474j)) <= tolerance1
        assert abs(gamma(1.0+0.1j) - (0.99020662958838-0.05682380875371j)) <= tolerance1
        assert abs(gamma(1.0+0.0j) - (1.0+0.0j)) <= tolerance1
        assert abs(gamma(1.0-0.1j) - (0.99020662958838+0.05682380875371j)) <= tolerance1
        assert abs(gamma(1.0-0.2j) - (0.96194742032062+0.10848528178473j)) <= tolerance1
        assert abs(gamma(1.0-0.3j) - (0.91827302339113+0.15084922588288j)) <= tolerance1
        assert abs(gamma(1.0-0.4j) - (0.86337911388526+0.18145712581519j)) <= tolerance1
        assert abs(gamma(1.0-0.5j) - (0.80169409706971+0.19963973816459j)) <= tolerance1
        assert abs(gamma(1.0-0.6j) - (0.73715642279989+0.20619323776345j)) <= tolerance1
        assert abs(gamma(1.0-0.7j) - (0.67282539316324+0.20285243648299j)) <= tolerance1
        assert abs(gamma(1.0-0.8j) - (0.61079898806795+0.19177395301476j)) <= tolerance1
        assert abs(gamma(1.0-0.9j) - (0.55232833292255+0.17514590718657j)) <= tolerance1
        assert abs(gamma(1.0-1.0j) - (0.49801566811835+0.15494982830181j)) <= tolerance1

    def test_gamma_step_down_1_5(self) -> None:
        assert abs(gamma(1.5+1.0j) - (0.57531518806345+0.08821067754409j)) <= tolerance1
        assert abs(gamma(1.5+0.9j) - (0.62215192518130+0.07482340774758j)) <= tolerance1
        assert abs(gamma(1.5+0.8j) - (0.66800081712702+0.06157503400938j)) <= tolerance1
        assert abs(gamma(1.5+0.7j) - (0.71202456105083+0.04896916270024j)) <= tolerance1
        assert abs(gamma(1.5+0.6j) - (0.75327952717994+0.03746481849076j)) <= tolerance1
        assert abs(gamma(1.5+0.5j) - (0.79073891412786+0.02742508541387j)) <= tolerance1
        assert abs(gamma(1.5+0.4j) - (0.82333543133451+0.01906643913376j)) <= tolerance1
        assert abs(gamma(1.5+0.3j) - (0.85002424490583+0.01241808307305j)) <= tolerance1
        assert abs(gamma(1.5+0.2j) - (0.86986213380527+0.00730170831118j)) <= tolerance1
        assert abs(gamma(1.5+0.1j) - (0.88209319709870+0.00334036310197j)) <= tolerance1
        assert abs(gamma(1.5+0.0j) - (pi**0.5 * 0.5)) <= tolerance1
        assert abs(gamma(1.5-0.1j) - (0.88209319709870-0.00334036310197j)) <= tolerance1
        assert abs(gamma(1.5-0.2j) - (0.86986213380527-0.00730170831118j)) <= tolerance1
        assert abs(gamma(1.5-0.3j) - (0.85002424490583-0.01241808307305j)) <= tolerance1
        assert abs(gamma(1.5-0.4j) - (0.82333543133451-0.01906643913376j)) <= tolerance1
        assert abs(gamma(1.5-0.5j) - (0.79073891412786-0.02742508541388j)) <= tolerance1
        assert abs(gamma(1.5-0.6j) - (0.75327952717994-0.03746481849076j)) <= tolerance1
        assert abs(gamma(1.5-0.7j) - (0.71202456105083-0.04896916270025j)) <= tolerance1
        assert abs(gamma(1.5-0.8j) - (0.66800081712702-0.06157503400938j)) <= tolerance1
        assert abs(gamma(1.5-0.9j) - (0.62215192518130-0.07482340774758j)) <= tolerance1
        assert abs(gamma(1.5-1.0j) - (0.57531518806345-0.08821067754409j)) <= tolerance1
