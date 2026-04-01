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

from cmath import exp as std_exp
from math import pi
from boring_math.special_functions.exponential.exp import cexp0
from boring_math.special_functions.trigonometry.trig0 import sin0, cos0

c0 = 1+0j
c1 = (3.0**(0.5))/2 + 1j/2
c2 = (1+1j)/(2**(0.5))
c3 = 1/2 + (3.0**(0.5))*1j/2
c4 = 0+1j
c5 = -1/2 + (3.0**(0.5))*1j/2
c6 = (-1+1j)/(2**(0.5))
c7 = -(3.0**(0.5))/2 + 1j/2
c8 = 0+1j
c9 = -(3.0**(0.5))/2 - 1j/2
c10 = (-1-1j)/(2**(0.5))
c11 = -1/2 - (3.0**(0.5))*1j/2
c12 = 0-1j
c13 = 1/2 - (3.0**(0.5))*1j/2
c14 = (1-1j)/(2**(0.5))
c15 = (3.0**(0.5))/2 - 1j/2

s1 = 0.831-0.479j
s2 = 0.411+0.672j
s3 = complex(cos0(0.613*pi), sin0(0.613*pi))
s4 = complex(cos0(-0.244*pi), sin0(-0.244*pi))
s5 = 0.0123-0.0432j

tolerance0 = 5.0e-16
tolerance1 = 1.0e-15
tolerance2 = 5.0e-15
tolerance3 = 1.0e-14
tolerance4 = 5.0e-14
tolerance5 = 1.0e-13
tolerance6 = 5.0e-13
tolerance7 = 1.0e-12
tolerance8 = 5.0e-12
tolerance9 = 1.0e-11
tolerance10 = 5.0e-11
tolerance11 = 1.0e-10
tolerance12 = 5.0e-10
tolerance13 = 1.0e-9
tolerance14 = 5.0e-9
tolerance15 = 1.0e-8
tolerance16 = 5.0e-8

class Test_cexp0_default:
    def test_reasonable_values(self) -> None:
        assert abs(cexp0(0.0) - 1.0) < tolerance0
        assert abs(cexp0(1.0) - std_exp(1.0)) < tolerance0
        assert abs(cexp0(-1.0) - std_exp(-1.0)) < tolerance0
        assert abs(cexp0(1j) - std_exp(1j)) < tolerance0
        assert abs(cexp0(-1j) - std_exp(-1j)) < tolerance0
        assert abs(cexp0(pi*(1j)/2) - (1j)) < tolerance0
        assert abs(cexp0(-pi*(1j)/2) - (-1j)) < tolerance0
        assert abs(cexp0(pi*(1j)/4) - ((1+1j)/(2**(0.5)))) < tolerance0
        assert abs(cexp0(-pi*(1j)/4) - ((1-1j)/(2**(0.5)))) < tolerance0
        assert abs(cexp0(pi*(3j)/4) - ((-1+1j)/(2**(0.5)))) < tolerance4
        assert abs(cexp0(-pi*(3j)/4) - ((-1-1j)/(2**(0.5)))) < tolerance4
        assert abs(cexp0(c0) - std_exp(c0)) < tolerance0
        assert abs(cexp0(s1) - std_exp(s1)) < tolerance0
        assert abs(cexp0(s2) - std_exp(s2)) < tolerance0
        assert abs(cexp0(s3) - std_exp(s3)) < tolerance0
        assert abs(cexp0(s4) - std_exp(s4)) < tolerance0
        assert abs(cexp0(s5) - std_exp(s5)) < tolerance0

    def test_questionable_values(self) -> None:
        assert abs(cexp0(0.1*c0) - std_exp(0.1*c0)) < tolerance0
        assert abs(cexp0(0.5*c0) - std_exp(0.5*c0)) < tolerance0
        assert abs(cexp0(1.0*c0) - std_exp(1.0*c0)) < tolerance0
        assert abs(cexp0(1.5*c0) - std_exp(1.5*c0)) < tolerance0
        assert abs(cexp0(2.0*c0) - std_exp(2.0*c0)) < tolerance1
        assert abs(cexp0(2.5*c0) - std_exp(2.5*c0)) < tolerance5
        assert abs(cexp0(3.0*c0) - std_exp(3.0*c0)) < tolerance8
        assert abs(cexp0(3.5*c0) - std_exp(3.5*c0)) < tolerance12
        assert abs(cexp0(4.0*c0) - std_exp(4.0*c0)) < tolerance14

        assert abs(cexp0(0.1*c1) - std_exp(0.1*c1)) < tolerance0
        assert abs(cexp0(0.5*c1) - std_exp(0.5*c1)) < tolerance0
        assert abs(cexp0(1.0*c1) - std_exp(1.0*c1)) < tolerance0
        assert abs(cexp0(1.5*c1) - std_exp(1.5*c1)) < tolerance1
        assert abs(cexp0(2.0*c1) - std_exp(2.0*c1)) < tolerance2
        assert abs(cexp0(2.5*c1) - std_exp(2.5*c1)) < tolerance5
        assert abs(cexp0(3.0*c1) - std_exp(3.0*c1)) < tolerance8
        assert abs(cexp0(3.5*c1) - std_exp(3.5*c1)) < tolerance12
        assert abs(cexp0(4.0*c1) - std_exp(4.0*c1)) < tolerance14

        assert abs(cexp0(0.1*c2) - std_exp(0.1*c2)) < tolerance0
        assert abs(cexp0(0.5*c2) - std_exp(0.5*c2)) < tolerance0
        assert abs(cexp0(1.0*c2) - std_exp(1.0*c2)) < tolerance0
        assert abs(cexp0(1.5*c2) - std_exp(1.5*c2)) < tolerance0
        assert abs(cexp0(2.0*c2) - std_exp(2.0*c2)) < tolerance1
        assert abs(cexp0(2.5*c2) - std_exp(2.5*c2)) < tolerance5
        assert abs(cexp0(3.0*c2) - std_exp(3.0*c2)) < tolerance8
        assert abs(cexp0(3.5*c2) - std_exp(3.5*c2)) < tolerance12
        assert abs(cexp0(4.0*c2) - std_exp(4.0*c2)) < tolerance14

        assert abs(cexp0(0.1*c3) - std_exp(0.1*c3)) < tolerance0
        assert abs(cexp0(0.5*c3) - std_exp(0.5*c3)) < tolerance0
        assert abs(cexp0(1.0*c3) - std_exp(1.0*c3)) < tolerance0
        assert abs(cexp0(1.5*c3) - std_exp(1.5*c3)) < tolerance0
        assert abs(cexp0(2.0*c3) - std_exp(2.0*c3)) < tolerance1
        assert abs(cexp0(2.5*c3) - std_exp(2.5*c3)) < tolerance5
        assert abs(cexp0(3.0*c3) - std_exp(3.0*c3)) < tolerance8
        assert abs(cexp0(3.5*c3) - std_exp(3.5*c3)) < tolerance12
        assert abs(cexp0(4.0*c3) - std_exp(4.0*c3)) < tolerance14

        assert abs(cexp0(0.1*c4) - std_exp(0.1*c4)) < tolerance0
        assert abs(cexp0(0.5*c4) - std_exp(0.5*c4)) < tolerance0
        assert abs(cexp0(1.0*c4) - std_exp(1.0*c4)) < tolerance0
        assert abs(cexp0(1.5*c4) - std_exp(1.5*c4)) < tolerance0
        assert abs(cexp0(2.0*c4) - std_exp(2.0*c4)) < tolerance1
        assert abs(cexp0(2.5*c4) - std_exp(2.5*c4)) < tolerance5
        assert abs(cexp0(3.0*c4) - std_exp(3.0*c4)) < tolerance8
        assert abs(cexp0(3.5*c4) - std_exp(3.5*c4)) < tolerance12
        assert abs(cexp0(4.0*c4) - std_exp(4.0*c4)) < tolerance14

        assert abs(cexp0(0.1*c5) - std_exp(0.1*c5)) < tolerance0
        assert abs(cexp0(0.5*c5) - std_exp(0.5*c5)) < tolerance0
        assert abs(cexp0(1.0*c5) - std_exp(1.0*c5)) < tolerance0
        assert abs(cexp0(1.5*c5) - std_exp(1.5*c5)) < tolerance0
        assert abs(cexp0(2.0*c5) - std_exp(2.0*c5)) < tolerance1
        assert abs(cexp0(2.5*c5) - std_exp(2.5*c5)) < tolerance5
        assert abs(cexp0(3.0*c5) - std_exp(3.0*c5)) < tolerance8
        assert abs(cexp0(3.5*c5) - std_exp(3.5*c5)) < tolerance12
        assert abs(cexp0(4.0*c5) - std_exp(4.0*c5)) < tolerance14

        assert abs(cexp0(0.1*c6) - std_exp(0.1*c6)) < tolerance0
        assert abs(cexp0(0.5*c6) - std_exp(0.5*c6)) < tolerance0
        assert abs(cexp0(1.0*c6) - std_exp(1.0*c6)) < tolerance0
        assert abs(cexp0(1.5*c6) - std_exp(1.5*c6)) < tolerance0
        assert abs(cexp0(2.0*c6) - std_exp(2.0*c6)) < tolerance1
        assert abs(cexp0(2.5*c6) - std_exp(2.5*c6)) < tolerance5
        assert abs(cexp0(3.0*c6) - std_exp(3.0*c6)) < tolerance8
        assert abs(cexp0(3.5*c6) - std_exp(3.5*c6)) < tolerance12
        assert abs(cexp0(4.0*c6) - std_exp(4.0*c6)) < tolerance14

        assert abs(cexp0(0.1*c7) - std_exp(0.1*c7)) < tolerance0
        assert abs(cexp0(0.5*c7) - std_exp(0.5*c7)) < tolerance0
        assert abs(cexp0(1.0*c7) - std_exp(1.0*c7)) < tolerance0
        assert abs(cexp0(1.5*c7) - std_exp(1.5*c7)) < tolerance0
        assert abs(cexp0(2.0*c7) - std_exp(2.0*c7)) < tolerance1
        assert abs(cexp0(2.5*c7) - std_exp(2.5*c7)) < tolerance5
        assert abs(cexp0(3.0*c7) - std_exp(3.0*c7)) < tolerance8
        assert abs(cexp0(3.5*c7) - std_exp(3.5*c7)) < tolerance12
        assert abs(cexp0(4.0*c7) - std_exp(4.0*c7)) < tolerance14

        assert abs(cexp0(0.1*c8) - std_exp(0.1*c8)) < tolerance0
        assert abs(cexp0(0.5*c8) - std_exp(0.5*c8)) < tolerance0
        assert abs(cexp0(1.0*c8) - std_exp(1.0*c8)) < tolerance0
        assert abs(cexp0(1.5*c8) - std_exp(1.5*c8)) < tolerance0
        assert abs(cexp0(2.0*c8) - std_exp(2.0*c8)) < tolerance1
        assert abs(cexp0(2.5*c8) - std_exp(2.5*c8)) < tolerance5
        assert abs(cexp0(3.0*c8) - std_exp(3.0*c8)) < tolerance8
        assert abs(cexp0(3.5*c8) - std_exp(3.5*c8)) < tolerance12
        assert abs(cexp0(4.0*c8) - std_exp(4.0*c8)) < tolerance14

        assert abs(cexp0(0.1*c9) - std_exp(0.1*c9)) < tolerance0
        assert abs(cexp0(0.5*c9) - std_exp(0.5*c9)) < tolerance0
        assert abs(cexp0(1.0*c9) - std_exp(1.0*c9)) < tolerance0
        assert abs(cexp0(1.5*c9) - std_exp(1.5*c9)) < tolerance0
        assert abs(cexp0(2.0*c9) - std_exp(2.0*c9)) < tolerance1
        assert abs(cexp0(2.5*c9) - std_exp(2.5*c9)) < tolerance5
        assert abs(cexp0(3.0*c9) - std_exp(3.0*c9)) < tolerance8
        assert abs(cexp0(3.5*c9) - std_exp(3.5*c9)) < tolerance12
        assert abs(cexp0(4.0*c9) - std_exp(4.0*c9)) < tolerance14

        assert abs(cexp0(0.1*c10) - std_exp(0.1*c10)) < tolerance0
        assert abs(cexp0(0.5*c10) - std_exp(0.5*c10)) < tolerance0
        assert abs(cexp0(1.0*c10) - std_exp(1.0*c10)) < tolerance0
        assert abs(cexp0(1.5*c10) - std_exp(1.5*c10)) < tolerance0
        assert abs(cexp0(2.0*c10) - std_exp(2.0*c10)) < tolerance1
        assert abs(cexp0(2.5*c10) - std_exp(2.5*c10)) < tolerance5
        assert abs(cexp0(3.0*c10) - std_exp(3.0*c10)) < tolerance8
        assert abs(cexp0(3.5*c10) - std_exp(3.5*c10)) < tolerance12
        assert abs(cexp0(4.0*c10) - std_exp(4.0*c10)) < tolerance14

        assert abs(cexp0(0.1*c11) - std_exp(0.1*c11)) < tolerance0
        assert abs(cexp0(0.5*c11) - std_exp(0.5*c11)) < tolerance0
        assert abs(cexp0(1.0*c11) - std_exp(1.0*c11)) < tolerance0
        assert abs(cexp0(1.5*c11) - std_exp(1.5*c11)) < tolerance0
        assert abs(cexp0(2.0*c11) - std_exp(2.0*c11)) < tolerance1
        assert abs(cexp0(2.5*c11) - std_exp(2.5*c11)) < tolerance5
        assert abs(cexp0(3.0*c11) - std_exp(3.0*c11)) < tolerance8
        assert abs(cexp0(3.5*c11) - std_exp(3.5*c11)) < tolerance12
        assert abs(cexp0(4.0*c11) - std_exp(4.0*c11)) < tolerance14

        assert abs(cexp0(0.1*c12) - std_exp(0.1*c12)) < tolerance0
        assert abs(cexp0(0.5*c12) - std_exp(0.5*c12)) < tolerance0
        assert abs(cexp0(1.0*c12) - std_exp(1.0*c12)) < tolerance0
        assert abs(cexp0(1.5*c12) - std_exp(1.5*c12)) < tolerance0
        assert abs(cexp0(2.0*c12) - std_exp(2.0*c12)) < tolerance1
        assert abs(cexp0(2.5*c12) - std_exp(2.5*c12)) < tolerance5
        assert abs(cexp0(3.0*c12) - std_exp(3.0*c12)) < tolerance8
        assert abs(cexp0(3.5*c12) - std_exp(3.5*c12)) < tolerance12
        assert abs(cexp0(4.0*c12) - std_exp(4.0*c12)) < tolerance14

        assert abs(cexp0(0.1*c13) - std_exp(0.1*c13)) < tolerance0
        assert abs(cexp0(0.5*c13) - std_exp(0.5*c13)) < tolerance0
        assert abs(cexp0(1.0*c13) - std_exp(1.0*c13)) < tolerance0
        assert abs(cexp0(1.5*c13) - std_exp(1.5*c13)) < tolerance0
        assert abs(cexp0(2.0*c13) - std_exp(2.0*c13)) < tolerance1
        assert abs(cexp0(2.5*c13) - std_exp(2.5*c13)) < tolerance5
        assert abs(cexp0(3.0*c13) - std_exp(3.0*c13)) < tolerance8
        assert abs(cexp0(3.5*c13) - std_exp(3.5*c13)) < tolerance12
        assert abs(cexp0(4.0*c13) - std_exp(4.0*c13)) < tolerance14

        assert abs(cexp0(0.1*c14) - std_exp(0.1*c14)) < tolerance0
        assert abs(cexp0(0.5*c14) - std_exp(0.5*c14)) < tolerance0
        assert abs(cexp0(1.0*c14) - std_exp(1.0*c14)) < tolerance0
        assert abs(cexp0(1.5*c14) - std_exp(1.5*c14)) < tolerance0
        assert abs(cexp0(2.0*c14) - std_exp(2.0*c14)) < tolerance1
        assert abs(cexp0(2.5*c14) - std_exp(2.5*c14)) < tolerance5
        assert abs(cexp0(3.0*c14) - std_exp(3.0*c14)) < tolerance8
        assert abs(cexp0(3.5*c14) - std_exp(3.5*c14)) < tolerance12
        assert abs(cexp0(4.0*c14) - std_exp(4.0*c14)) < tolerance14

        assert abs(cexp0(0.1*c15) - std_exp(0.1*c15)) < tolerance0
        assert abs(cexp0(0.5*c15) - std_exp(0.5*c15)) < tolerance0
        assert abs(cexp0(1.0*c15) - std_exp(1.0*c15)) < tolerance0
        assert abs(cexp0(1.5*c15) - std_exp(1.5*c15)) < tolerance1
        assert abs(cexp0(2.0*c15) - std_exp(2.0*c15)) < tolerance2
        assert abs(cexp0(2.5*c15) - std_exp(2.5*c15)) < tolerance5
        assert abs(cexp0(3.0*c15) - std_exp(3.0*c15)) < tolerance8
        assert abs(cexp0(3.5*c15) - std_exp(3.5*c15)) < tolerance12
        assert abs(cexp0(4.0*c15) - std_exp(4.0*c15)) < tolerance14

class Test_cexp0_iteration:
    def test_25(self) -> None:
        assert abs(cexp0(0.0, n=25) - 1.0) < tolerance0

        assert abs(cexp0(0.1*c0, n=25) - (1.105170918075648)) < tolerance0
        assert abs(cexp0(0.5*c0, n=25) - (1.648721270700128)) < tolerance0
        assert abs(cexp0(1.0*c0, n=25) - (2.718281828459045)) < tolerance0
        assert abs(cexp0(1.5*c0, n=25) - (4.481689070338065)) < tolerance1
        assert abs(cexp0(2.0*c0, n=25) - (7.389056098930650)) < tolerance0
        assert abs(cexp0(2.5*c0, n=25) - (12.18249396070347)) < tolerance3
        assert abs(cexp0(3.0*c0, n=25) - (20.08553692318767)) < tolerance4
        assert abs(cexp0(3.5*c0, n=25) - (33.11545195869231)) < tolerance6
        assert abs(cexp0(4.0*c0, n=25) - (54.59815003314424)) < tolerance11

        assert abs(cexp0(0.1*c1, n=25) - (1.089100383470131+0.05450044378129976j)) < tolerance0
        assert abs(cexp0(0.5*c1, n=25) - (1.493961999000881+0.3814711270561049j)) < tolerance0
        assert abs(cexp0(1.0*c1, n=25) - (2.086402233681255+1.139806735075716j)) < tolerance0
        assert abs(cexp0(1.5*c1, n=25) - (2.682202291894879+2.498730159983147j)) < tolerance0
        assert abs(cexp0(2.0*c1, n=25) - (3.053914887386167+4.756190636053823j)) < tolerance1
        assert abs(cexp0(2.5*c1, n=25) - (2.748083387508846+8.270548424292862j)) < tolerance2
        assert abs(cexp0(3.0*c1, n=25) - (0.9505567222367386+13.40419952386731j)) < tolerance3
        assert abs(cexp0(3.5*c1, n=25) - (-3.693219478738045+20.38797465984588j)) < tolerance6
        assert abs(cexp0(4.0*c1, n=25) - (-13.29495322708720+29.05000278138290j)) < tolerance11

        assert abs(cexp0(0.1*c1, n=25) - std_exp(0.1*c1)) < tolerance0
        assert abs(cexp0(0.5*c1, n=25) - std_exp(0.5*c1)) < tolerance0
        assert abs(cexp0(1.0*c1, n=25) - std_exp(1.0*c1)) < tolerance0
        assert abs(cexp0(1.5*c1, n=25) - std_exp(1.5*c1)) < tolerance0
        assert abs(cexp0(2.0*c1, n=25) - std_exp(2.0*c1)) < tolerance0
        assert abs(cexp0(2.5*c1, n=25) - std_exp(2.5*c1)) < tolerance2
        assert abs(cexp0(3.0*c1, n=25) - std_exp(3.0*c1)) < tolerance3
        assert abs(cexp0(3.5*c1, n=25) - std_exp(3.5*c1)) < tolerance6
        assert abs(cexp0(4.0*c1, n=25) - std_exp(4.0*c1)) < tolerance11

        assert abs(cexp0(0.1*c8, n=25) - std_exp(0.1*c8)) < tolerance0
        assert abs(cexp0(0.5*c8, n=25) - std_exp(0.5*c8)) < tolerance0
        assert abs(cexp0(1.0*c8, n=25) - std_exp(1.0*c8)) < tolerance0
        assert abs(cexp0(1.5*c8, n=25) - std_exp(1.5*c8)) < tolerance0
        assert abs(cexp0(2.0*c8, n=25) - std_exp(2.0*c8)) < tolerance0
        assert abs(cexp0(2.5*c8, n=25) - std_exp(2.5*c8)) < tolerance2
        assert abs(cexp0(3.0*c8, n=25) - std_exp(3.0*c8)) < tolerance3
        assert abs(cexp0(3.5*c8, n=25) - std_exp(3.5*c8)) < tolerance6
        assert abs(cexp0(4.0*c8, n=25) - std_exp(4.0*c8)) < tolerance11

        assert abs(cexp0(0.1*c11, n=25) - std_exp(0.1*c11)) < tolerance0
        assert abs(cexp0(0.5*c11, n=25) - std_exp(0.5*c11)) < tolerance0
        assert abs(cexp0(1.0*c11, n=25) - std_exp(1.0*c11)) < tolerance0
        assert abs(cexp0(1.5*c11, n=25) - std_exp(1.5*c11)) < tolerance0
        assert abs(cexp0(2.0*c11, n=25) - std_exp(2.0*c11)) < tolerance0
        assert abs(cexp0(2.5*c11, n=25) - std_exp(2.5*c11)) < tolerance2
        assert abs(cexp0(3.0*c11, n=25) - std_exp(3.0*c11)) < tolerance3
        assert abs(cexp0(3.5*c11, n=25) - std_exp(3.5*c11)) < tolerance6
        assert abs(cexp0(4.0*c11, n=25) - std_exp(4.0*c11)) < tolerance11

    def test_30(self) -> None:
        assert abs(cexp0(0.0, n=30) - 1.0) < tolerance0

        assert abs(cexp0(0.1*c0, n=30) - (1.105170918075648)) < tolerance0
        assert abs(cexp0(0.5*c0, n=30) - (1.648721270700128)) < tolerance0
        assert abs(cexp0(1.0*c0, n=30) - (2.718281828459045)) < tolerance0
        assert abs(cexp0(1.5*c0, n=30) - (4.481689070338065)) < tolerance1
        assert abs(cexp0(2.0*c0, n=30) - (7.389056098930650)) < tolerance0
        assert abs(cexp0(2.5*c0, n=30) - (12.18249396070347)) < tolerance3
        assert abs(cexp0(3.0*c0, n=30) - (20.08553692318767)) < tolerance2
        assert abs(cexp0(3.5*c0, n=30) - (33.11545195869231)) < tolerance3
        assert abs(cexp0(4.0*c0, n=30) - (54.59815003314424)) < tolerance3

        assert abs(cexp0(0.1*c1, n=30) - (1.089100383470131+0.05450044378129976j)) < tolerance0
        assert abs(cexp0(0.5*c1, n=30) - (1.493961999000881+0.3814711270561049j)) < tolerance0
        assert abs(cexp0(1.0*c1, n=30) - (2.086402233681255+1.139806735075716j)) < tolerance0
        assert abs(cexp0(1.5*c1, n=30) - (2.682202291894879+2.498730159983147j)) < tolerance0
        assert abs(cexp0(2.0*c1, n=30) - (3.053914887386167+4.756190636053823j)) < tolerance1
        assert abs(cexp0(2.5*c1, n=30) - (2.748083387508846+8.270548424292862j)) < tolerance2
        assert abs(cexp0(3.0*c1, n=30) - (0.9505567222367386+13.40419952386731j)) < tolerance3
        assert abs(cexp0(3.5*c1, n=30) - (-3.693219478738045+20.38797465984588j)) < tolerance2
        assert abs(cexp0(4.0*c1, n=30) - (-13.29495322708720+29.05000278138290j)) < tolerance3
        assert abs(
          cexp0(4.0*c1, n=30)
          - (-13.294953227087199358226967988371017640050105071432297091+29.050002781382904736646704842355139971014070479969889431j)
        ) < tolerance3

        assert abs(cexp0(0.1*c1, n=30) - std_exp(0.1*c1)) < tolerance0
        assert abs(cexp0(0.5*c1, n=30) - std_exp(0.5*c1)) < tolerance0
        assert abs(cexp0(1.0*c1, n=30) - std_exp(1.0*c1)) < tolerance0
        assert abs(cexp0(1.5*c1, n=30) - std_exp(1.5*c1)) < tolerance0
        assert abs(cexp0(2.0*c1, n=30) - std_exp(2.0*c1)) < tolerance0
        assert abs(cexp0(2.5*c1, n=30) - std_exp(2.5*c1)) < tolerance2
        assert abs(cexp0(3.0*c1, n=30) - std_exp(3.0*c1)) < tolerance2
        assert abs(cexp0(3.5*c1, n=30) - std_exp(3.5*c1)) < tolerance2
        assert abs(cexp0(4.0*c1, n=30) - std_exp(4.0*c1)) < tolerance2

        assert abs(cexp0(0.1*c8, n=30) - std_exp(0.1*c8)) < tolerance0
        assert abs(cexp0(0.5*c8, n=30) - std_exp(0.5*c8)) < tolerance0
        assert abs(cexp0(1.0*c8, n=30) - std_exp(1.0*c8)) < tolerance0
        assert abs(cexp0(1.5*c8, n=30) - std_exp(1.5*c8)) < tolerance0
        assert abs(cexp0(2.0*c8, n=30) - std_exp(2.0*c8)) < tolerance0
        assert abs(cexp0(2.5*c8, n=30) - std_exp(2.5*c8)) < tolerance2
        assert abs(cexp0(3.0*c8, n=30) - std_exp(3.0*c8)) < tolerance2
        assert abs(cexp0(3.5*c8, n=30) - std_exp(3.5*c8)) < tolerance2
        assert abs(cexp0(4.0*c8, n=30) - std_exp(4.0*c8)) < tolerance2

        assert abs(cexp0(0.1*c11, n=30) - std_exp(0.1*c11)) < tolerance0
        assert abs(cexp0(0.5*c11, n=30) - std_exp(0.5*c11)) < tolerance0
        assert abs(cexp0(1.0*c11, n=30) - std_exp(1.0*c11)) < tolerance0
        assert abs(cexp0(1.5*c11, n=30) - std_exp(1.5*c11)) < tolerance0
        assert abs(cexp0(2.0*c11, n=30) - std_exp(2.0*c11)) < tolerance0
        assert abs(cexp0(2.5*c11, n=30) - std_exp(2.5*c11)) < tolerance2
        assert abs(cexp0(3.0*c11, n=30) - std_exp(3.0*c11)) < tolerance2
        assert abs(cexp0(3.5*c11, n=30) - std_exp(3.5*c11)) < tolerance2
        assert abs(cexp0(4.0*c11, n=30) - std_exp(4.0*c11)) < tolerance2

    def test_10(self) -> None:
        assert abs(cexp0(0.0, n=10) - 1.0) < tolerance0

        assert abs(cexp0(0.01*c1, n=10) - std_exp(0.01*c1)) < tolerance0
        assert abs(cexp0(0.05*c1, n=10) - std_exp(0.05*c1)) < tolerance0
        assert abs(cexp0(0.1*c1, n=10) - std_exp(0.1*c1)) < tolerance0
        assert abs(cexp0(0.2*c1, n=10) - std_exp(0.2*c1)) < tolerance1
        assert abs(cexp0(0.3*c1, n=10) - std_exp(0.3*c1)) < tolerance4
        assert abs(cexp0(0.4*c1, n=10) - std_exp(0.4*c1)) < tolerance8
        assert abs(cexp0(0.5*c1, n=10) - std_exp(0.5*c1)) < tolerance10

        assert abs(cexp0(0.1*c1, n=10) - (1.089100383470131+0.05450044378129976j)) < tolerance0
        assert abs(cexp0(0.5*c1, n=10) - (1.493961999000881+0.3814711270561049j)) < tolerance10
        assert abs(cexp0(1.0*c1, n=10) - (2.086402233681255+1.139806735075716j)) < tolerance16

    def test_18(self) -> None:
        assert abs(cexp0(0.0, n=15) - 1.0) < tolerance0

        assert abs(cexp0(0.01*c1, n=18) - std_exp(0.01*c1)) < tolerance0
        assert abs(cexp0(0.05*c1, n=18) - std_exp(0.05*c1)) < tolerance0
        assert abs(cexp0(0.1*c1, n=18) - std_exp(0.1*c1)) < tolerance0
        assert abs(cexp0(0.2*c1, n=18) - std_exp(0.2*c1)) < tolerance0
        assert abs(cexp0(0.3*c1, n=18) - std_exp(0.3*c1)) < tolerance0
        assert abs(cexp0(0.4*c1, n=18) - std_exp(0.4*c1)) < tolerance0
        assert abs(cexp0(0.5*c1, n=18) - std_exp(0.5*c1)) < tolerance0

        assert abs(cexp0(0.1*c1, n=18) - (1.089100383470131+0.05450044378129976j)) < tolerance0
        assert abs(cexp0(0.5*c1, n=18) - (1.493961999000881+0.3814711270561049j)) < tolerance0
        assert abs(cexp0(1.0*c1, n=18) - (2.086402233681255+1.139806735075716j)) < tolerance0
