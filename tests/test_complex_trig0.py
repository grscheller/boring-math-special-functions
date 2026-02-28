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
from boring_math.special_functions.trig0_complex import sin0, cos0, tan0

tolerance0 = 5.0e-16
tolerance1 = 5.0e-15
tolerance2 = 5.0e-14


class Test_sin0:
    def test_sin0(self) -> None:
        assert abs((sin0(0) - csin(0))) < tolerance0
        assert abs((sin0(0.023+0j) - csin(0.023+0j))) < tolerance0
        assert abs((sin0(0.35) - csin(0.35))) < tolerance0
        assert abs((sin0(pi/4.0) - csin(pi/4.0))) < tolerance0
        assert abs((sin0(-2.0*pi/3.0) - csin(-2.0*pi/3.0))) < tolerance0

class Test_cos0:
    def test_cos0(self) -> None:
        assert abs((cos0(0) - ccos(0))) < tolerance0
        assert abs((cos0(0.125+0j) - ccos(0.125+0j))) < tolerance0
        assert abs((cos0(0.125) - ccos(0.125))) < tolerance0
        assert abs((cos0(0.35) - ccos(0.35))) < tolerance0
        assert abs((cos0(pi/2.0) - ccos(pi/2.0))) < tolerance0
        assert abs((cos0(pi) - ccos(pi))) < tolerance0
        assert abs((cos0(1.5*pi) - ccos(1.5*pi))) < tolerance0

class Test_tan0:
    def test_cos0(self) -> None:
        assert abs(tan0(0) - ctan(0)) < tolerance0
        assert abs(tan0(0.023) - ctan(0.023)) < tolerance0
        assert abs(tan0(0.35) - ctan(0.35)) < tolerance0
        assert abs(tan0(pi/3.0) - ctan(pi/3.0)) < tolerance0
        assert abs(tan0(pi/5.0) - ctan(pi/5.0)) < tolerance0
        assert abs(tan0(3.0*pi/5.0) - ctan(3.0*pi/5.0)) < tolerance1
