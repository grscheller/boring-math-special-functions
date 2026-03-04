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
from cmath import sin as std_csin, cos as std_ccos, tan as std_ctan
from boring_math.special_functions.ctrig0 import csin0, ccos0, ctan0

tolerance0 = 5.0e-16
tolerance1 = 5.0e-15
tolerance2 = 5.0e-14


class Test_sin0:
    def test_sin0(self) -> None:
        assert abs((csin0(0) - std_csin(0))) < tolerance0
        assert abs((csin0(0.023+0j) - std_csin(0.023+0j))) < tolerance0
        assert abs((csin0(0.35) - std_csin(0.35))) < tolerance0
        assert abs((csin0(pi/4.0) - std_csin(pi/4.0))) < tolerance0
        assert abs((csin0(-2.0*pi/3.0) - std_csin(-2.0*pi/3.0))) < tolerance0

class Test_cos0:
    def test_cos0(self) -> None:
        assert abs((ccos0(0) - std_ccos(0))) < tolerance0
        assert abs((ccos0(0.125+0j) - std_ccos(0.125+0j))) < tolerance0
        assert abs((ccos0(0.125) - std_ccos(0.125))) < tolerance0
        assert abs((ccos0(0.35) - std_ccos(0.35))) < tolerance0
        assert abs((ccos0(pi/2.0) - std_ccos(pi/2.0))) < tolerance0
        assert abs((ccos0(pi) - std_ccos(pi))) < tolerance0
        assert abs((ccos0(1.5*pi) - std_ccos(1.5*pi))) < tolerance0

class Test_tan0:
    def test_cos0(self) -> None:
        assert abs(ctan0(0) - std_ctan(0)) < tolerance0
        assert abs(ctan0(0.023) - std_ctan(0.023)) < tolerance0
        assert abs(ctan0(0.35) - std_ctan(0.35)) < tolerance0
        assert abs(ctan0(pi/3.0) - std_ctan(pi/3.0)) < tolerance0
        assert abs(ctan0(pi/5.0) - std_ctan(pi/5.0)) < tolerance0
        assert abs(ctan0(3.0*pi/5.0) - std_ctan(3.0*pi/5.0)) < tolerance1
