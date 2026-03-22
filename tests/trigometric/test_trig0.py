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

import math
from math import inf, pi
from boring_math.special_functions.trig0 import sin0, cos0, tan0


class Test_trig0:
    def test_sin0(self) -> None:
        assert abs(sin0(0.0) - math.sin(0.0)) < 5.0e-16
        assert abs(sin0(0.023) - math.sin(0.023)) < 5.0e-16
        assert abs(sin0(0.125) - math.sin(0.125)) < 5.0e-16
        assert abs(sin0(0.35) - math.sin(0.35)) < 5.0e-16
        assert abs(sin0(pi/4.0) - math.sin(pi/4.0)) < 5.0e-16
        assert abs(sin0(pi/2.0) - math.sin(pi/2.0)) < 5.0e-16
        assert abs(sin0(pi) - math.sin(pi)) < 5.0e-16
        assert abs(sin0(4.0) - math.sin(4.0)) < 5.0e-15
        assert abs(sin0(2*pi) - math.sin(2*pi)) < 5.0e-16
        assert abs(sin0(-1.5*pi) - math.sin(-1.5*pi)) < 5.0e-16
        assert abs(sin0(-2.0*pi/3.0) - math.sin(-2.0*pi/3.0)) < 5.0e-16

    def test_cos0(self) -> None:
        assert abs(cos0(0.0) - math.cos(0.0)) < 5.0e-16
        assert abs(cos0(0.023) - math.cos(0.023)) < 5.0e-16
        assert abs(cos0(0.125) - math.cos(0.125)) < 5.0e-16
        assert abs(cos0(0.35) - math.cos(0.35)) < 5.0e-16
        assert abs(cos0(pi/4) - math.cos(pi/4)) < 5.0e-16
        assert abs(cos0(pi/2) - math.cos(pi/2)) < 5.0e-16
        assert abs(cos0(pi) - math.cos(pi)) < 5.0e-16
        assert abs(cos0(4.0) - math.cos(4.0)) < 5.0e-15
        assert abs(cos0(3*pi/2) - math.cos(3*pi/2)) < 5.0e-16
        assert abs(cos0(2*pi) - math.cos(2*pi)) < 5.0e-16
        assert abs(cos0(-pi/3) - math.cos(-pi/3)) < 5.0e-16

    def test_tan0(self) -> None:
        assert abs(tan0(0.0) - math.tan(0.0)) < 5.0e-16
        assert abs(tan0(0.023) - math.tan(0.023)) < 5.0e-16
        assert abs(tan0(0.125) - math.tan(0.125)) < 5.0e-16
        assert abs(tan0(0.35) - math.tan(0.35)) < 5.0e-16
        assert abs(tan0(pi/4) - math.tan(pi/4)) < 5.0e-16
        assert inf <= tan0(pi/2) <= inf
        assert abs(tan0(pi/3) - math.tan(pi/3)) < 5.0e-16
        assert abs(tan0(2*pi/3) - math.tan(2*pi/3)) < 5.0e-15

class Test_trig_n_depth:
    def test_n2(self) -> None:
        assert sin0(0.0, n=2) == 0.0
        assert cos0(0.0, n=2) == 1.0
        assert tan0(0.0, n=2) == 0.0
        assert abs(sin0(0.001, n=2) - math.sin(0.001)) <= 5.0e-15
        assert abs(cos0(0.001, n=2) - math.cos(0.001)) <= 5.0e-15
        assert abs(tan0(0.001, n=2) - math.tan(0.001)) <= 5.0e-15
        assert abs(sin0(0.005, n=2) - math.sin(0.005)) <= 5.0e-14
        assert abs(cos0(0.005, n=2) - math.cos(0.005)) <= 5.0e-15
        assert abs(tan0(0.005, n=2) - math.tan(0.005)) <= 5.0e-14
        assert abs(sin0(0.025, n=2) - math.sin(0.025)) <= 5.0e-10
        assert abs(cos0(0.025, n=2) - math.cos(0.025)) <= 5.0e-13
        assert abs(tan0(0.025, n=2) - math.tan(0.025)) <= 5.0e-10
        assert abs(sin0(0.050, n=2) - math.sin(0.050)) <= 5.0e-9
        assert abs(cos0(0.050, n=2) - math.cos(0.050)) <= 5.0e-11
        assert abs(tan0(0.050, n=2) - math.tan(0.050)) <= 5.0e-9
        assert abs(sin0(0.100, n=2) - math.sin(0.100)) <= 5.0e-7
        assert abs(cos0(0.100, n=2) - math.cos(0.100)) <= 5.0e-9
        assert abs(tan0(0.100, n=2) - math.tan(0.100)) <= 5.0e-7
        assert abs(sin0(0.250, n=2) - math.sin(0.250)) <= 5.0e-5
        assert abs(cos0(0.250, n=2) - math.cos(0.250)) <= 5.0e-7
        assert abs(tan0(0.250, n=2) - math.tan(0.250)) <= 5.0e-5

    def test_n5(self) -> None:
        assert sin0(0.0, n=5) == 0.0
        assert cos0(0.0, n=5) == 1.0
        assert tan0(0.0, n=5) == 0.0
        assert abs(sin0(0.050, n=5) - math.sin(0.050)) <= 5.0e-17
        assert abs(cos0(0.050, n=5) - math.cos(0.050)) <= 5.0e-17
        assert abs(tan0(0.050, n=5) - math.tan(0.050)) <= 5.0e-17
        assert abs(sin0(0.100, n=5) - math.sin(0.100)) <= 5.0e-17
        assert abs(cos0(0.100, n=5) - math.cos(0.100)) <= 5.0e-16
        assert abs(tan0(0.100, n=5) - math.tan(0.100)) <= 5.0e-17
        assert abs(sin0(0.250, n=5) - math.sin(0.250)) <= 5.0e-14
        assert abs(cos0(0.250, n=5) - math.cos(0.250)) <= 5.0e-16
        assert abs(tan0(0.250, n=5) - math.tan(0.250)) <= 5.0e-14
        assert abs(sin0(0.500, n=5) - math.sin(0.500)) <= 5.0e-11
        assert abs(cos0(0.500, n=5) - math.cos(0.500)) <= 5.0e-12
        assert abs(tan0(0.500, n=5) - math.tan(0.500)) <= 5.0e-11
        assert abs(sin0(1.000, n=5) - math.sin(1.000)) <= 5.0e-8
        assert abs(cos0(1.000, n=5) - math.cos(1.000)) <= 5.0e-9
        assert abs(tan0(1.000, n=5) - math.tan(1.000)) <= 5.0e-7
        assert abs(sin0(pi/2,  n=5) - math.sin(pi/2))  <= 5.0e-6
        assert abs(cos0(pi/2,  n=5) - math.cos(pi/2))  <= 5.0e-7

    def test_n10(self) -> None:
        assert sin0(0.0, n=10) == 0.0
        assert cos0(0.0, n=10) == 1.0
        assert tan0(0.0, n=10) == 0.0
        assert abs(sin0(0.050, n=10) - math.sin(0.050)) <= 5.0e-17
        assert abs(cos0(0.050, n=10) - math.cos(0.050)) <= 5.0e-17
        assert abs(tan0(0.050, n=10) - math.tan(0.050)) <= 5.0e-17
        assert abs(sin0(0.100, n=10) - math.sin(0.100)) <= 5.0e-17
        assert abs(cos0(0.100, n=10) - math.cos(0.100)) <= 5.0e-16
        assert abs(tan0(0.100, n=10) - math.tan(0.100)) <= 5.0e-17
        assert abs(sin0(0.250, n=10) - math.sin(0.250)) <= 5.0e-14
        assert abs(cos0(0.250, n=10) - math.cos(0.250)) <= 5.0e-16
        assert abs(tan0(0.250, n=10) - math.tan(0.250)) <= 5.0e-14
        assert abs(sin0(0.500, n=10) - math.sin(0.500)) <= 5.0e-11
        assert abs(cos0(0.500, n=10) - math.cos(0.500)) <= 5.0e-12
        assert abs(tan0(0.500, n=10) - math.tan(0.500)) <= 5.0e-11
        assert abs(sin0(1.000, n=10) - math.sin(1.000)) <= 5.0e-8
        assert abs(cos0(1.000, n=10) - math.cos(1.000)) <= 5.0e-9
        assert abs(tan0(1.000, n=10) - math.tan(1.000)) <= 5.0e-7
        assert abs(sin0(pi/2,  n=10) - math.sin(pi/2))  <= 5.0e-6
        assert abs(cos0(pi/2,  n=10) - math.cos(pi/2))  <= 5.0e-7
        assert tan0(pi/2) > 1.0e+16 or tan0(pi/2) < -1.0e+16

    def test_n20(self) -> None:
        assert sin0(0.0, n=20) == 0.0
        assert cos0(0.0, n=20) == 1.0
        assert tan0(0.0, n=20) == 0.0
        assert abs(sin0(0.050, n=20) - math.sin(0.050)) <= 5.0e-17
        assert abs(cos0(0.050, n=20) - math.cos(0.050)) <= 5.0e-17
        assert abs(tan0(0.050, n=20) - math.tan(0.050)) <= 5.0e-17
        assert abs(sin0(0.100, n=20) - math.sin(0.100)) <= 5.0e-17
        assert abs(cos0(0.100, n=20) - math.cos(0.100)) <= 5.0e-16
        assert abs(tan0(0.100, n=20) - math.tan(0.100)) <= 5.0e-17
        assert abs(sin0(0.250, n=20) - math.sin(0.250)) <= 5.0e-17
        assert abs(cos0(0.250, n=20) - math.cos(0.250)) <= 5.0e-17
        assert abs(tan0(0.250, n=20) - math.tan(0.250)) <= 5.0e-17
        assert abs(sin0(0.500, n=20) - math.sin(0.500)) <= 5.0e-17
        assert abs(cos0(0.500, n=20) - math.cos(0.500)) <= 5.0e-17
        assert abs(tan0(0.500, n=20) - math.tan(0.500)) <= 5.0e-17
        assert abs(sin0(1.000, n=20) - math.sin(1.000)) <= 5.0e-17
        assert abs(cos0(1.000, n=20) - math.cos(1.000)) <= 5.0e-17
        assert abs(tan0(1.000, n=20) - math.tan(1.000)) <= 5.0e-16
        assert abs(sin0(pi/2,  n=20) - math.sin(pi/2))  <= 5.0e-16
        assert abs(cos0(pi/2,  n=20) - math.cos(pi/2))  <= 5.0e-16
        assert tan0(pi/2) > 1.0e+16 or tan0(pi/2) < -1.0e+16
        assert abs(sin0(3*pi/4, n=20) - math.sin(3*pi/4)) <= 5.0e-17
        assert abs(cos0(3*pi/4, n=20) - math.cos(3*pi/4)) <= 5.0e-17
        assert abs(tan0(3*pi/4, n=20) - math.tan(3*pi/4)) <= 5.0e-17
        assert abs(sin0(pi, n=20) - math.sin(pi)) <= 5.0e-16
        assert abs(cos0(pi, n=20) - math.cos(pi)) <= 5.0e-16
        assert abs(tan0(pi, n=20) - math.tan(pi)) <= 5.0e-16
        assert abs(tan0(-pi, n=20) - math.tan(-pi)) <= 5.0e-16
        assert abs(sin0(3*pi/2, n=20) - math.sin(3*pi/2)) <= 5.0e-16
        assert abs(cos0(3*pi/2, n=20) - math.cos(3*pi/2)) <= 5.0e-16
        assert tan0(3*pi/2) > 1.0e+15 or tan0(3*pi/2) < -1.0e+15
        assert tan0(-pi/2) > 1.0e+16 or tan0(-pi/2) < -1.0e+16
        assert abs(sin0(2*pi, n=20) - math.sin(2*pi)) <= 5.0e-16
        assert abs(cos0(2*pi, n=20) - math.cos(2*pi)) <= 5.0e-16
        assert abs(tan0(2*pi, n=20) - math.tan(2*pi)) <= 5.0e-16
        assert abs(sin0(-1.000, n=20) - math.sin(-1.000)) <= 5.0e-17
        assert abs(cos0(-1.000, n=20) - math.cos(-1.000)) <= 5.0e-17
        assert abs(tan0(-1.000, n=20) - math.tan(-1.000)) <= 5.0e-16

    def test_n22(self) -> None:
        assert sin0(0.0, n=22) == 0.0
        assert cos0(0.0, n=22) == 1.0
        assert tan0(0.0, n=22) == 0.0
        assert abs(sin0(0.050, n=22) - math.sin(0.050)) <= 5.0e-17
        assert abs(cos0(0.050, n=22) - math.cos(0.050)) <= 5.0e-17
        assert abs(tan0(0.050, n=22) - math.tan(0.050)) <= 5.0e-17
        assert abs(sin0(0.100, n=22) - math.sin(0.100)) <= 5.0e-17
        assert abs(cos0(0.100, n=22) - math.cos(0.100)) <= 5.0e-16
        assert abs(tan0(0.100, n=22) - math.tan(0.100)) <= 5.0e-17
        assert abs(sin0(0.250, n=22) - math.sin(0.250)) <= 5.0e-17
        assert abs(cos0(0.250, n=22) - math.cos(0.250)) <= 5.0e-17
        assert abs(tan0(0.250, n=22) - math.tan(0.250)) <= 5.0e-17
        assert abs(sin0(0.500, n=22) - math.sin(0.500)) <= 5.0e-17
        assert abs(cos0(0.500, n=22) - math.cos(0.500)) <= 5.0e-17
        assert abs(tan0(0.500, n=22) - math.tan(0.500)) <= 5.0e-17
        assert abs(sin0(1.000, n=22) - math.sin(1.000)) <= 5.0e-17
        assert abs(cos0(1.000, n=22) - math.cos(1.000)) <= 5.0e-17
        assert abs(tan0(1.000, n=22) - math.tan(1.000)) <= 5.0e-16
        assert abs(sin0(pi/2,  n=22) - math.sin(pi/2))  <= 5.0e-17
        assert abs(cos0(pi/2,  n=22) - math.cos(pi/2))  <= 5.0e-16
        assert tan0(pi/2) > 1.0e+16 or tan0(pi/2) < -1.0e+16
        assert abs(sin0(3*pi/4, n=22) - math.sin(3*pi/4)) <= 5.0e-17
        assert abs(cos0(3*pi/4, n=22) - math.cos(3*pi/4)) <= 5.0e-17
        assert abs(tan0(3*pi/4, n=22) - math.tan(3*pi/4)) <= 5.0e-17
        assert abs(sin0(pi, n=22) - math.sin(pi)) <= 5.0e-16
        assert abs(cos0(pi, n=22) - math.cos(pi)) <= 5.0e-17
        assert abs(tan0(pi, n=22) - math.tan(pi)) <= 5.0e-16
        assert abs(tan0(-pi, n=22) - math.tan(-pi)) <= 5.0e-16
        assert abs(sin0(3*pi/2, n=22) - math.sin(3*pi/2)) <= 5.0e-16
        assert abs(cos0(3*pi/2, n=22) - math.cos(3*pi/2)) <= 5.0e-16
        assert tan0(3*pi/2) > 1.0e+15 or tan0(3*pi/2) < -1.0e+15
        assert tan0(-pi/2) > 1.0e+16 or tan0(-pi/2) < -1.0e+16
        assert abs(sin0(2*pi, n=22) - math.sin(2*pi)) <= 5.0e-16
        assert abs(cos0(2*pi, n=22) - math.cos(2*pi)) <= 5.0e-17
        assert abs(tan0(2*pi, n=22) - math.tan(2*pi)) <= 5.0e-16
        assert abs(sin0(-1.000, n=22) - math.sin(-1.000)) <= 5.0e-17
        assert abs(cos0(-1.000, n=22) - math.cos(-1.000)) <= 5.0e-17
        assert abs(tan0(-1.000, n=22) - math.tan(-1.000)) <= 5.0e-16

    def test_n30(self) -> None:
        assert sin0(0.0, n=30) == 0.0
        assert cos0(0.0, n=30) == 1.0
        assert tan0(0.0, n=30) == 0.0
        assert abs(sin0(0.050, n=30) - math.sin(0.050)) <= 5.0e-17
        assert abs(cos0(0.050, n=30) - math.cos(0.050)) <= 5.0e-17
        assert abs(tan0(0.050, n=30) - math.tan(0.050)) <= 5.0e-17
        assert abs(sin0(0.100, n=30) - math.sin(0.100)) <= 5.0e-17
        assert abs(cos0(0.100, n=30) - math.cos(0.100)) <= 5.0e-16
        assert abs(tan0(0.100, n=30) - math.tan(0.100)) <= 5.0e-17
        assert abs(sin0(0.250, n=30) - math.sin(0.250)) <= 5.0e-17
        assert abs(cos0(0.250, n=30) - math.cos(0.250)) <= 5.0e-17
        assert abs(tan0(0.250, n=30) - math.tan(0.250)) <= 5.0e-17
        assert abs(sin0(0.500, n=30) - math.sin(0.500)) <= 5.0e-17
        assert abs(cos0(0.500, n=30) - math.cos(0.500)) <= 5.0e-17
        assert abs(tan0(0.500, n=30) - math.tan(0.500)) <= 5.0e-17
        assert abs(sin0(1.000, n=30) - math.sin(1.000)) <= 5.0e-17
        assert abs(cos0(1.000, n=30) - math.cos(1.000)) <= 5.0e-16
        assert abs(tan0(1.000, n=30) - math.tan(1.000)) <= 5.0e-16
        assert abs(sin0(pi/2,  n=30) - math.sin(pi/2))  <= 5.0e-17
        assert abs(cos0(pi/2,  n=30) - math.cos(pi/2))  <= 5.0e-16
        assert tan0(pi/2) > 1.0e+16 or tan0(pi/2) < -1.0e+16
        assert abs(sin0(3*pi/4, n=30) - math.sin(3*pi/4)) <= 5.0e-17
        assert abs(cos0(3*pi/4, n=30) - math.cos(3*pi/4)) <= 5.0e-17
        assert abs(tan0(3*pi/4, n=30) - math.tan(3*pi/4)) <= 5.0e-17
        assert abs(sin0(pi, n=30) - math.sin(pi)) <= 5.0e-16
        assert abs(cos0(pi, n=30) - math.cos(pi)) <= 5.0e-17
        assert abs(tan0(pi, n=30) - math.tan(pi)) <= 5.0e-16
        assert abs(tan0(-pi, n=30) - math.tan(-pi)) <= 5.0e-16
        assert abs(sin0(3*pi/2, n=30) - math.sin(3*pi/2)) <= 5.0e-16
        assert abs(cos0(3*pi/2, n=30) - math.cos(3*pi/2)) <= 5.0e-16
        assert tan0(3*pi/2) > 1.0e+15 or tan0(3*pi/2) < -1.0e+15
        assert tan0(-pi/2) > 1.0e+16 or tan0(-pi/2) < -1.0e+16
        assert abs(sin0(2*pi, n=30) - math.sin(2*pi)) <= 5.0e-16
        assert abs(cos0(2*pi, n=30) - math.cos(2*pi)) <= 5.0e-17
        assert abs(tan0(2*pi, n=30) - math.tan(2*pi)) <= 5.0e-16
        assert abs(sin0(-1.000, n=30) - math.sin(-1.000)) <= 5.0e-17
        assert abs(cos0(-1.000, n=30) - math.cos(-1.000)) <= 5.0e-17
        assert abs(tan0(-1.000, n=30) - math.tan(-1.000)) <= 5.0e-16

class Test_trig_angle_at_depths:
    def test_sin0_pi_over_two(self) -> None:
        assert sin0(pi/2, n=84) == 1.0
        assert sin0(pi/2, n=83) == 1.0
        assert sin0(pi/2, n=82) == 1.0
        assert sin0(pi/2, n=81) == 1.0
        assert sin0(pi/2, n=80) == 1.0
        assert sin0(pi/2, n=79) == 1.0
        assert sin0(pi/2, n=78) == 1.0
        assert sin0(pi/2, n=77) == 1.0
        assert sin0(pi/2, n=76) == 1.0
        assert sin0(pi/2, n=75) == 1.0
        assert sin0(pi/2, n=74) == 1.0
        assert sin0(pi/2, n=73) == 1.0
        assert sin0(pi/2, n=72) == 1.0
        assert sin0(pi/2, n=71) == 1.0
        assert sin0(pi/2, n=70) == 1.0
        assert sin0(pi/2, n=69) == 1.0
        assert sin0(pi/2, n=68) == 1.0
        assert sin0(pi/2, n=67) == 1.0
        assert sin0(pi/2, n=66) == 1.0
        assert sin0(pi/2, n=65) == 1.0
        assert sin0(pi/2, n=64) == 1.0
        assert sin0(pi/2, n=63) == 1.0
        assert sin0(pi/2, n=62) == 1.0
        assert sin0(pi/2, n=61) == 1.0
        assert sin0(pi/2, n=60) == 1.0
        assert sin0(pi/2, n=59) == 1.0
        assert sin0(pi/2, n=58) == 1.0
        assert sin0(pi/2, n=57) == 1.0
        assert sin0(pi/2, n=56) == 1.0
        assert sin0(pi/2, n=55) == 1.0
        assert sin0(pi/2, n=54) == 1.0
        assert sin0(pi/2, n=53) == 1.0
        assert sin0(pi/2, n=52) == 1.0
        assert sin0(pi/2, n=51) == 1.0
        assert sin0(pi/2, n=50) == 1.0
        assert sin0(pi/2, n=49) == 1.0
        assert sin0(pi/2, n=48) == 1.0
        assert sin0(pi/2, n=47) == 1.0
        assert sin0(pi/2, n=46) == 1.0
        assert sin0(pi/2, n=45) == 1.0
        assert sin0(pi/2, n=44) == 1.0
        assert sin0(pi/2, n=43) == 1.0
        assert sin0(pi/2, n=42) == 1.0
        assert sin0(pi/2, n=41) == 1.0
        assert sin0(pi/2, n=40) == 1.0
        assert sin0(pi/2, n=39) == 1.0
        assert sin0(pi/2, n=38) == 1.0
        assert sin0(pi/2, n=37) == 1.0
        assert sin0(pi/2, n=36) == 1.0
        assert sin0(pi/2, n=35) == 1.0
        assert sin0(pi/2, n=34) == 1.0
        assert sin0(pi/2, n=33) == 1.0
        assert sin0(pi/2, n=32) == 1.0
        assert sin0(pi/2, n=31) == 1.0
        assert sin0(pi/2, n=30) == 1.0
        assert sin0(pi/2, n=29) == 1.0
        assert sin0(pi/2, n=28) == 1.0
        assert sin0(pi/2, n=27) == 1.0
        assert sin0(pi/2, n=26) == 1.0
        assert sin0(pi/2, n=25) == 1.0
        assert sin0(pi/2, n=24) == 1.0
        assert sin0(pi/2, n=23) == 1.0
        assert sin0(pi/2, n=22) == 1.0
        assert sin0(pi/2, n=21) == 1.0
        assert sin0(pi/2, n=20) == 1.0
        assert sin0(pi/2, n=19) == 1.0
        assert sin0(pi/2, n=18) == 1.0
        assert sin0(pi/2, n=17) == 1.0
        assert sin0(pi/2, n=16) == 1.0
        assert sin0(pi/2, n=15) == 1.0
        assert sin0(pi/2, n=14) == 1.0
        assert sin0(pi/2, n=13) == 1.0
        assert sin0(pi/2, n=12) == 1.0
        assert sin0(pi/2, n=11) == 1.0
        assert abs(sin0(pi/2, n=10) - 1.0) < 5.0e-16
        assert abs(sin0(pi/2,  n=9) - 1.0) < 5.0e-14
        assert abs(sin0(pi/2,  n=8) - 1.0) < 5.0e-11
        assert abs(sin0(pi/2,  n=7) - 1.0) < 5.0e-9
        assert abs(sin0(pi/2,  n=6) - 1.0) < 5.0e-7
        assert abs(sin0(pi/2,  n=5) - 1.0) < 5.0e-6
        assert abs(sin0(pi/2,  n=4) - 1.0) < 5.0e-4
        assert abs(sin0(pi/2,  n=3) - 1.0) < 5.0e-3
        assert abs(sin0(pi/2,  n=2) - 1.0) < 5.0e-1

    def test_cos0_pi_over_two(self) -> None:
        assert cos0(pi/2, n=84) == 0.0
        assert cos0(pi/2, n=83) == 0.0
        assert cos0(pi/2, n=82) == 0.0
        assert cos0(pi/2, n=81) == 0.0
        assert cos0(pi/2, n=80) == 0.0
        assert cos0(pi/2, n=79) == 0.0
        assert cos0(pi/2, n=78) == 0.0
        assert cos0(pi/2, n=77) == 0.0
        assert cos0(pi/2, n=76) == 0.0
        assert cos0(pi/2, n=75) == 0.0
        assert cos0(pi/2, n=74) == 0.0
        assert cos0(pi/2, n=73) == 0.0
        assert cos0(pi/2, n=72) == 0.0
        assert cos0(pi/2, n=71) == 0.0
        assert cos0(pi/2, n=70) == 0.0
        assert cos0(pi/2, n=69) == 0.0
        assert cos0(pi/2, n=68) == 0.0
        assert cos0(pi/2, n=67) == 0.0
        assert cos0(pi/2, n=66) == 0.0
        assert cos0(pi/2, n=65) == 0.0
        assert cos0(pi/2, n=64) == 0.0
        assert cos0(pi/2, n=63) == 0.0
        assert cos0(pi/2, n=62) == 0.0
        assert cos0(pi/2, n=61) == 0.0
        assert cos0(pi/2, n=60) == 0.0
        assert cos0(pi/2, n=59) == 0.0
        assert cos0(pi/2, n=58) == 0.0
        assert cos0(pi/2, n=57) == 0.0
        assert cos0(pi/2, n=56) == 0.0
        assert cos0(pi/2, n=55) == 0.0
        assert cos0(pi/2, n=54) == 0.0
        assert cos0(pi/2, n=53) == 0.0
        assert cos0(pi/2, n=52) == 0.0
        assert cos0(pi/2, n=51) == 0.0
        assert cos0(pi/2, n=50) == 0.0
        assert cos0(pi/2, n=49) == 0.0
        assert cos0(pi/2, n=48) == 0.0
        assert cos0(pi/2, n=47) == 0.0
        assert cos0(pi/2, n=46) == 0.0
        assert cos0(pi/2, n=45) == 0.0
        assert cos0(pi/2, n=44) == 0.0
        assert cos0(pi/2, n=43) == 0.0
        assert cos0(pi/2, n=42) == 0.0
        assert cos0(pi/2, n=41) == 0.0
        assert cos0(pi/2, n=40) == 0.0
        assert cos0(pi/2, n=39) == 0.0
        assert cos0(pi/2, n=38) == 0.0
        assert cos0(pi/2, n=37) == 0.0
        assert cos0(pi/2, n=36) == 0.0
        assert cos0(pi/2, n=35) == 0.0
        assert cos0(pi/2, n=34) == 0.0
        assert cos0(pi/2, n=33) == 0.0
        assert cos0(pi/2, n=32) == 0.0
        assert cos0(pi/2, n=31) == 0.0
        assert cos0(pi/2, n=30) == 0.0
        assert cos0(pi/2, n=29) == 0.0
        assert cos0(pi/2, n=28) == 0.0
        assert cos0(pi/2, n=27) == 0.0
        assert cos0(pi/2, n=26) == 0.0
        assert cos0(pi/2, n=25) == 0.0
        assert cos0(pi/2, n=24) == 0.0
        assert cos0(pi/2, n=23) == 0.0
        assert cos0(pi/2, n=22) == 0.0
        assert cos0(pi/2, n=21) == 0.0
        assert cos0(pi/2, n=20) == 0.0
        assert cos0(pi/2, n=19) == 0.0
        assert cos0(pi/2, n=18) == 0.0
        assert cos0(pi/2, n=17) == 0.0
        assert cos0(pi/2, n=16) == 0.0
        assert cos0(pi/2, n=15) == 0.0
        assert cos0(pi/2, n=14) == 0.0
        assert cos0(pi/2, n=13) == 0.0
        assert cos0(pi/2, n=12) == 0.0
        assert cos0(pi/2, n=11) == 0.0
        assert abs(cos0(pi/2, n=10) - 0.0) < 5.0e-16
        assert abs(cos0(pi/2,  n=9) - 0.0) < 5.0e-14
        assert abs(cos0(pi/2,  n=8) - 0.0) < 5.0e-11
        assert abs(cos0(pi/2,  n=7) - 0.0) < 5.0e-9
        assert abs(cos0(pi/2,  n=6) - 0.0) < 5.0e-7
        assert abs(cos0(pi/2,  n=5) - 0.0) < 5.0e-6
        assert abs(cos0(pi/2,  n=4) - 0.0) < 5.0e-4
        assert abs(cos0(pi/2,  n=3) - 0.0) < 5.0e-3
        assert abs(cos0(pi/2,  n=2) - 0.0) < 5.0e-1

    def test_sin0_pi(self) -> None:
        assert abs(sin0(pi, n=84) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=83) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=82) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=81) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=80) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=79) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=78) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=77) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=76) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=75) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=74) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=73) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=72) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=71) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=70) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=69) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=68) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=67) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=66) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=65) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=64) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=63) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=62) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=61) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=60) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=59) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=58) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=57) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=56) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=55) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=54) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=53) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=52) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=51) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=50) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=49) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=48) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=47) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=46) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=45) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=44) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=43) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=42) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=41) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=40) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=39) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=38) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=37) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=36) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=35) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=34) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=33) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=32) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=31) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=30) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=29) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=28) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=27) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=26) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=25) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=24) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=23) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=22) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=21) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=20) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=19) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=18) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=17) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=16) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=15) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=14) - 0.0) < 5.0e-16
        assert abs(sin0(pi, n=13) - 0.0) < 5.0e-15
        assert abs(sin0(pi, n=12) - 0.0) < 5.0e-13
        assert abs(sin0(pi, n=11) - 0.0) < 5.0e-11
        assert abs(sin0(pi, n=10) - 0.0) < 5.0e-9
        assert abs(sin0(pi,  n=9) - 0.0) < 5.0e-8
        assert abs(sin0(pi,  n=8) - 0.0) < 5.0e-6
        assert abs(sin0(pi,  n=7) - 0.0) < 5.0e-5
        assert abs(sin0(pi,  n=6) - 0.0) < 5.0e-4
        assert abs(sin0(pi,  n=5) - 0.0) < 5.0e-2
        assert abs(sin0(pi,  n=4) - 0.0) < 5.0e-1
        assert abs(sin0(pi,  n=3) - 0.0) < 5.0e-0
        assert abs(sin0(pi,  n=2) - 0.0) < 5.0e-0

    def test_cos0_pi(self) -> None:
        assert abs(cos0(pi, n=84) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=83) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=82) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=81) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=80) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=79) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=78) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=77) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=76) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=75) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=74) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=73) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=72) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=71) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=70) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=69) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=68) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=67) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=66) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=65) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=64) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=63) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=62) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=61) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=60) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=59) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=58) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=57) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=56) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=55) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=54) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=53) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=52) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=51) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=50) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=49) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=48) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=47) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=46) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=45) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=44) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=43) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=42) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=41) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=40) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=39) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=38) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=37) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=36) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=35) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=34) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=33) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=32) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=31) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=30) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=29) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=28) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=27) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=26) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=25) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=24) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=23) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=22) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=21) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=20) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=19) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=18) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=17) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=16) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=15) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=14) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=13) - (-1.0)) < 5.0e-16
        assert abs(cos0(pi, n=12) - (-1.0)) < 5.0e-14
        assert abs(cos0(pi, n=11) - (-1.0)) < 5.0e-12
        assert abs(cos0(pi, n=10) - (-1.0)) < 5.0e-10
        assert abs(cos0(pi,  n=9) - (-1.0)) < 5.0e-9
        assert abs(cos0(pi,  n=8) - (-1.0)) < 5.0e-7
        assert abs(cos0(pi,  n=7) - (-1.0)) < 5.0e-6
        assert abs(cos0(pi,  n=6) - (-1.0)) < 5.0e-4
        assert abs(cos0(pi,  n=5) - (-1.0)) < 5.0e-3
        assert abs(cos0(pi,  n=4) - (-1.0)) < 5.0e-2
        assert abs(cos0(pi,  n=3) - (-1.0)) < 5.0e-1
        assert abs(cos0(pi,  n=2) - (-1.0)) < 2.0e-0

    def test_sin0_two_pi(self) -> None:
        assert abs(sin0(2*pi, n=84) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=83) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=82) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=81) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=80) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=79) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=78) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=77) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=76) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=75) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=74) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=73) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=72) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=71) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=70) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=69) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=68) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=67) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=66) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=65) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=64) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=63) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=62) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=61) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=60) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=59) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=58) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=57) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=56) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=55) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=54) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=53) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=52) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=51) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=50) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=49) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=48) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=47) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=46) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=45) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=44) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=43) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=42) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=41) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=40) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=39) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=38) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=37) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=36) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=35) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=34) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=33) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=32) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=31) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=30) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=29) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=28) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=27) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=26) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=25) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=24) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=23) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=22) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=21) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=20) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=19) - 0.0) < 5.0e-16
        assert abs(sin0(2*pi, n=18) - 0.0) < 5.0e-14
        assert abs(sin0(2*pi, n=17) - 0.0) < 5.0e-12
        assert abs(sin0(2*pi, n=16) - 0.0) < 5.0e-11
        assert abs(sin0(2*pi, n=15) - 0.0) < 5.0e-9
        assert abs(sin0(2*pi, n=14) - 0.0) < 5.0e-8
        assert abs(sin0(2*pi, n=13) - 0.0) < 5.0e-7
        assert abs(sin0(2*pi, n=12) - 0.0) < 5.0e-5
        assert abs(sin0(2*pi, n=11) - 0.0) < 5.0e-3
        assert abs(sin0(2*pi, n=10) - 0.0) < 5.0e-3
        assert abs(sin0(2*pi,  n=9) - 0.0) < 5.0e-2

    def test_cos0_two_pi(self) -> None:
        assert abs(cos0(2*pi, n=84) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=83) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=82) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=81) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=80) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=79) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=78) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=77) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=76) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=75) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=74) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=73) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=72) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=71) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=70) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=69) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=68) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=67) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=66) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=65) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=64) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=63) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=62) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=61) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=60) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=59) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=58) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=57) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=56) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=55) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=54) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=53) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=52) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=51) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=50) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=49) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=48) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=47) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=46) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=45) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=44) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=43) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=42) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=41) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=40) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=39) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=38) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=37) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=36) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=35) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=34) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=33) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=32) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=31) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=30) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=29) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=28) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=27) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=26) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=25) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=24) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=23) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=22) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=21) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=20) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=19) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=18) - (1.0)) < 5.0e-16
        assert abs(cos0(2*pi, n=17) - (1.0)) < 5.0e-13
        assert abs(cos0(2*pi, n=16) - (1.0)) < 5.0e-12
        assert abs(cos0(2*pi, n=15) - (1.0)) < 5.0e-10
        assert abs(cos0(2*pi, n=14) - (1.0)) < 5.0e-9
        assert abs(cos0(2*pi, n=13) - (1.0)) < 5.0e-7
        assert abs(cos0(2*pi, n=12) - (1.0)) < 5.0e-6
        assert abs(cos0(2*pi, n=11) - (1.0)) < 5.0e-4
        assert abs(cos0(2*pi, n=10) - (1.0)) < 5.0e-4
        assert abs(cos0(2*pi,  n=9) - (1.0)) < 5.0e-3
        assert abs(cos0(2*pi,  n=8) - (1.0)) < 5.0e-2
        assert abs(cos0(2*pi,  n=7) - (1.0)) < 5.0e-1
