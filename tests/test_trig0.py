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

from math import sin, cos, tan, pi
from boring_math.special_functions.float0 import sin0, cos0, tan0

tolerance = 7.0e-16


class Test_sin0:
    def test_sin0(self) -> None:
        assert (sin0(0) - sin(0)) < tolerance
        assert (sin0(0.023) - sin(0.023)) < tolerance
        assert (sin0(0.125) - sin(0.125)) < tolerance
        assert (sin0(0.35) - sin(0.35)) < tolerance
        assert (sin0(pi/4.0) - sin(pi/4.0)) < tolerance
        assert (sin0(pi/2.0) - sin(pi/2.0)) < tolerance
        assert (sin0(pi) - sin(pi)) < tolerance
        assert (sin0(4.0) - sin(4.0)) < tolerance
        assert (sin0(2.0*pi) - sin(2.0*pi)) < tolerance
        assert (sin0(-1.5*pi) - sin(-1.5*pi)) < tolerance
        assert (sin0(-2.0*pi/3.0) - sin(-2.0*pi/3.0)) < tolerance

class Test_cos0:
    def test_cos0(self) -> None:
        assert (cos0(0) - cos(0)) < tolerance
        assert (cos0(0.023) - cos(0.023)) < tolerance
        assert (cos0(0.125) - cos(0.125)) < tolerance
        assert (cos0(0.35) - cos(0.35)) < tolerance
        assert (cos0(pi/4.0) - cos(pi/4.0)) < tolerance
        assert (cos0(pi/2.0) - cos(pi/2.0)) < tolerance
        assert (cos0(pi) - cos(pi)) < tolerance
        assert (cos0(4.0) - cos(4.0)) < tolerance
        assert (cos0(1.5*pi) - cos(1.5*pi)) < tolerance
        assert (cos0(2.0*pi) - cos(2.0*pi)) < tolerance
        assert (cos0(-1.0*pi/3) - cos(-1.0*pi/3)) < tolerance

class Test_tan0:
    def test_cos0(self) -> None:
        assert (tan0(0) - tan(0)) < tolerance
        assert (tan0(0.023) - tan(0.023)) < tolerance
        assert (tan0(0.125) - tan(0.125)) < tolerance
        assert (tan0(0.35) - tan(0.35)) < tolerance
        assert (tan0(pi/4.0) - tan(pi/4.0)) < tolerance
        assert (tan0(pi/2.0) - tan(pi/2.0)) < tolerance
        assert (tan0(pi/3.0) - tan(pi/3.0)) < tolerance
        assert (tan0(2.0*pi/3.0) - tan(2.0*pi/3.0)) < tolerance
