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
from math import pi
from cmath import sin as csin, cos as ccos, tan as ctan
from boring_math.special_functions.complex import sin, cos, tan

tolerance0 = 5.0e-16
tolerance1 = 5.0e-15
tolerance2 = 5.0e-14


class Test_sin0:
    def test_sin0(self) -> None:
        assert abs((sin(0) - csin(0))) < tolerance0
        assert abs((sin(0.023+0j) - csin(0.023+0j))) < tolerance0
        assert abs((sin(0.35) - csin(0.35))) < tolerance0
        assert abs((sin(pi/4.0) - csin(pi/4.0))) < tolerance0
        assert abs((sin(-2.0*pi/3.0) - csin(-2.0*pi/3.0))) < tolerance0

class Test_cos0:
    def test_cos0(self) -> None:
        assert abs((cos(0) - ccos(0))) < tolerance0
        assert abs((cos(0.125+0j) - ccos(0.125+0j))) < tolerance0
        assert abs((cos(0.125) - ccos(0.125))) < tolerance0
        assert abs((cos(0.35) - ccos(0.35))) < tolerance0
        assert abs((cos(pi/2.0) - ccos(pi/2.0))) < tolerance0
        assert abs((cos(pi) - ccos(pi))) < tolerance0
        assert abs((cos(1.5*pi) - ccos(1.5*pi))) < tolerance0

class Test_tan0:
    def test_cos0(self) -> None:
        assert abs(tan(0) - ctan(0)) < tolerance0
        assert abs(tan(0.023) - ctan(0.023)) < tolerance0
        assert abs(tan(0.35) - ctan(0.35)) < tolerance0
        assert abs(tan(pi/3.0) - ctan(pi/3.0)) < tolerance0
        assert abs(tan(2.0*pi/5.0) - ctan(2.0*pi/5.0)) < tolerance0
        assert abs(tan(3.0*pi/5.0) - ctan(3.0*pi/5.0)) < tolerance0
        assert abs(tan(42.0) - ctan(42.0)) < tolerance2
