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

from cmath import sin as csin, cos as ccos, tan as ctan
from math import pi
from boring_math.special_functions.float import sin, cos, tan

tolerance0 = 5.0e-16
tolerance1 = 5.0e-15
tolerance2 = 5.0e-14


class Test_sin0:
    def test_sin0(self) -> None:
        assert abs(sin(0) - csin(0)) < tolerance0
        assert abs(sin(0.023) - csin(0.023)) < tolerance0
        assert abs(sin(0.125) - csin(0.125)) < tolerance0
        assert abs(sin(0.35) - csin(0.35)) < tolerance0
        assert abs(sin(pi/4.0) - csin(pi/4.0)) < tolerance0
        assert abs(sin(pi/2.0) - csin(pi/2.0)) < tolerance0
        assert abs(sin(pi) - csin(pi)) < tolerance0
        assert abs(sin(4.0) - csin(4.0)) < tolerance0
        assert abs(sin(42.0) - csin(42.0)) < tolerance1
        assert abs(sin(2.0*pi) - csin(2.0*pi)) < tolerance0
        assert abs(sin(-1.5*pi) - csin(-1.5*pi)) < tolerance0
        assert abs(sin(-2.0*pi/3.0) - csin(-2.0*pi/3.0)) < tolerance0

class Test_cos0:
    def test_cos0(self) -> None:
        assert abs(cos(0) - ccos(0)) < tolerance0
        assert abs(cos(0.023) - ccos(0.023)) < tolerance0
        assert abs(cos(0.125) - ccos(0.125)) < tolerance0
        assert abs(cos(0.35) - ccos(0.35)) < tolerance0
        assert abs(cos(pi/4.0) - ccos(pi/4.0)) < tolerance0
        assert abs(cos(pi/2.0) - ccos(pi/2.0)) < tolerance0
        assert abs(cos(pi) - ccos(pi)) < tolerance0
        assert abs(cos(4.0) - ccos(4.0)) < tolerance1
        assert abs(cos(42.0) - ccos(42.0)) < tolerance1
        assert abs(cos(1.5*pi) - ccos(1.5*pi)) < tolerance0
        assert abs(cos(2.0*pi) - ccos(2.0*pi)) < tolerance0
        assert abs(cos(-1.0*pi/3) - ccos(-1.0*pi/3)) < tolerance1

class Test_tan0:
    def test_cos0(self) -> None:
        assert abs(tan(0) - ctan(0)) < tolerance0
        assert abs(tan(0.023) - ctan(0.023)) < tolerance0
        assert abs(tan(0.125) - ctan(0.125)) < tolerance0
        assert abs(tan(0.35) - ctan(0.35)) < tolerance0
        assert abs(tan(42.0) - ctan(42.0)) < tolerance2
        assert abs(tan(pi/4.0) - ctan(pi/4.0)) < tolerance0
        assert abs(tan(pi/2.0) - ctan(pi/2.0)) < tolerance0
        assert abs(tan(pi/3.0) - ctan(pi/3.0)) < tolerance0
        assert abs(tan(2.0*pi/5.0) - ctan(2.0*pi/5.0)) < tolerance1
