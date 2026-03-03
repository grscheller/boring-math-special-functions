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

import cmath
from math import pi
from boring_math.special_functions.ctrig import csin, ccos, ctan

tolerance0 = 5.0e-16
tolerance1 = 5.0e-15
tolerance2 = 5.0e-14
tolerance3 = 5.0e-13
tolerance4 = 5.0e-12
tolerance5 = 5.0e-11

jay = 0.0+1.0j


class Test_ctrig:
    def test_sin(self) -> None:
        assert abs((csin(0) - cmath.sin(0))) < tolerance0
        assert abs((csin(0.023+0j) - cmath.sin(0.023+0j))) < tolerance0
        assert abs((csin(0.0-0.032j) - cmath.sin(0.0-0.032j))) < tolerance0
        assert abs((csin(0.025+0.0125j) - cmath.sin(0.025+0.0125j))) < tolerance1
        assert abs((csin(0.35) - cmath.sin(0.35))) < tolerance1
        assert abs((csin(pi/4.0) - cmath.sin(pi/4.0))) < tolerance1
        assert abs((csin(-2.0*pi/3.0) - cmath.sin(-2.0*pi/3.0))) < tolerance2

    def test_cos(self) -> None:
        assert abs((ccos(0) - cmath.cos(0))) < tolerance0
        assert abs((ccos(0.0+0.057j) - cmath.cos(0.0+0.057j))) < tolerance0
        assert abs((ccos(0.025-0.025j) - cmath.cos(0.025-0.025j))) < tolerance1
        assert abs((ccos(0.125+0j) - cmath.cos(0.125+0j))) < tolerance1
        assert abs((ccos(0.125) - cmath.cos(0.125))) < tolerance1
        assert abs((ccos(0.35) - cmath.cos(0.35))) < tolerance1
        assert abs((ccos(pi/2.0) - cmath.cos(pi/2.0))) < tolerance0
        assert abs((ccos(pi) - cmath.cos(pi))) < tolerance4
        assert abs((ccos(-1.5*pi) - cmath.cos(-1.5*pi))) < tolerance0
        assert abs((ccos(1.5*pi) - cmath.cos(1.5*pi))) < tolerance0

    def test_tan(self) -> None:
        assert abs(ctan(0) - cmath.tan(0)) < tolerance0
        assert abs(ctan(0.023) - cmath.tan(0.023)) < tolerance0
        assert abs(ctan(0.35) - cmath.tan(0.35)) < tolerance1
        assert abs(ctan(pi/3.0) - cmath.tan(pi/3.0)) < tolerance2
        assert abs(ctan(pi/2.0 - 0.1) - cmath.tan(pi/2.0 - 0.1)) < tolerance3
        assert abs(ctan(pi/2.0 - 0.01) - cmath.tan(pi/2.0 - 0.01)) < tolerance5
        assert abs(ctan(pi/2.0 - 0.01 + 0.02*jay) - cmath.tan(pi/2.0 - 0.01 + 0.02*jay)) < tolerance4
        assert abs(ctan(pi/2.0 - 0.02 + 0.03*jay) - cmath.tan(pi/2.0 - 0.02 + 0.03*jay)) < tolerance4
        assert abs(ctan(pi/2.0 + 0.02 - 0.03*jay) - cmath.tan(pi/2.0 + 0.02 - 0.03*jay)) < tolerance4
        assert abs(ctan(pi/2.0)) < 5.0e16 and abs(cmath.tan(pi/2.0)) < 5.0e16
        assert abs(ctan(pi/2.0 + 0.01) - cmath.tan(pi/2.0 + 0.01)) < tolerance5
        assert abs(ctan(pi/2.0 + 0.01 - 0.05*jay) - cmath.tan(pi/2.0 + 0.01 - 0.05*jay)) < tolerance3
        assert abs(ctan(2.0*pi/5.0) - cmath.tan(2.0*pi/5.0)) < tolerance2
        assert abs(ctan(2.0*pi*jay/5.0) - cmath.tan(2.0*pi*jay/5.0)) < tolerance0
