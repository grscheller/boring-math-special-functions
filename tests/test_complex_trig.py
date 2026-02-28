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
from cmath import sin as csin, cos as ccos, tan as ctan
from boring_math.special_functions.trig_complex import sin, cos, tan

tolerance0 = 5.0e-16
tolerance1 = 5.0e-15
tolerance2 = 5.0e-14
tolerance3 = 5.0e-13
tolerance4 = 5.0e-12
tolerance5 = 5.0e-11

jay = 0.0+1.0j


class Test_sin0:
    def test_sin0(self) -> None:
        assert abs((sin(0) - csin(0))) < tolerance0
        assert abs((sin(0.023+0j) - csin(0.023+0j))) < tolerance0
        assert abs((sin(0.0-0.032j) - csin(0.0-0.032j))) < tolerance0
        assert abs((sin(0.025+0.0125j) - csin(0.025+0.0125j))) < tolerance1
        assert abs((sin(0.35) - csin(0.35))) < tolerance1
        assert abs((sin(pi/4.0) - csin(pi/4.0))) < tolerance1
        assert abs((sin(-2.0*pi/3.0) - csin(-2.0*pi/3.0))) < tolerance2

class Test_cos0:
    def test_cos0(self) -> None:
        assert abs((cos(0) - ccos(0))) < tolerance0
        assert abs((cos(0.0+0.057j) - ccos(0.0+0.057j))) < tolerance0
        assert abs((cos(0.025-0.025j) - ccos(0.025-0.025j))) < tolerance1
        assert abs((cos(0.125+0j) - ccos(0.125+0j))) < tolerance1
        assert abs((cos(0.125) - ccos(0.125))) < tolerance1
        assert abs((cos(0.35) - ccos(0.35))) < tolerance1
        assert abs((cos(pi/2.0) - ccos(pi/2.0))) < tolerance0
        assert abs((cos(pi) - ccos(pi))) < tolerance4
        assert abs((cos(-1.5*pi) - ccos(-1.5*pi))) < tolerance0
        assert abs((cos(1.5*pi) - ccos(1.5*pi))) < tolerance0

class Test_tan0:
    def test_cos0(self) -> None:
        assert abs(tan(0) - ctan(0)) < tolerance0
        assert abs(tan(0.023) - ctan(0.023)) < tolerance0
        assert abs(tan(0.35) - ctan(0.35)) < tolerance1
        assert abs(tan(pi/3.0) - ctan(pi/3.0)) < tolerance2
        assert abs(tan(pi/2.0 - 0.1) - ctan(pi/2.0 - 0.1)) < tolerance3
        assert abs(tan(pi/2.0 - 0.01) - ctan(pi/2.0 - 0.01)) < tolerance5
        assert abs(tan(pi/2.0 - 0.01 + 0.02*jay) - ctan(pi/2.0 - 0.01 + 0.02*jay)) < tolerance4
        assert abs(tan(pi/2.0 - 0.02 + 0.03*jay) - ctan(pi/2.0 - 0.02 + 0.03*jay)) < tolerance4
        assert abs(tan(pi/2.0 + 0.02 - 0.03*jay) - ctan(pi/2.0 + 0.02 - 0.03*jay)) < tolerance4
        assert abs(tan(pi/2.0)) < 5.0e16 and abs(ctan(pi/2.0)) < 5.0e16
        assert abs(tan(pi/2.0 + 0.01) - ctan(pi/2.0 + 0.01)) < tolerance5
        assert abs(tan(pi/2.0 + 0.01 - 0.05*jay) - ctan(pi/2.0 + 0.01 - 0.05*jay)) < tolerance3
        assert abs(tan(2.0*pi/5.0) - ctan(2.0*pi/5.0)) < tolerance2
        assert abs(tan(2.0*pi*jay/5.0) - ctan(2.0*pi*jay/5.0)) < tolerance0
