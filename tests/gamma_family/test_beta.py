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

from cmath import inf, infj
from math import pi, sinh, cosh
from boring_math.special_functions.beta import beta

jay = 0.0+1.0j

tolerance1 = 1.0e-14
tolerance2 = 2.0e-14
tolerance3 = 3.0e-14


class Test_gamma:
    def test_beta_with_real_args(self) -> None:
        assert abs(beta(1, 1).real - (1)) < tolerance1
        assert abs(beta(2, 3).real - (1/12)) < tolerance1
        assert abs(beta(4, 4).real - (1/140)) < tolerance1
        assert abs(beta(1/2, 1/2).real - (pi)) < tolerance1
        assert abs(beta(5/2, 7/2).real - (3*pi/256)) < tolerance1
        assert abs(beta(3/2, 1/2).real - (pi/2)) < tolerance1
        assert abs(beta(3/2, -1/2).real - (-pi)) < tolerance1
        assert abs(beta(-5/2, 7/2).real - (-pi)) < tolerance1
        assert abs(beta(1.0/6.0, 5.0/6.0).real - (2*pi)) < tolerance1

    def test_beta_with_complex_args(self) -> None:
        assert abs(beta(1, 1) - 1.0+0.0j) < tolerance1
        assert abs(beta(1, 2) - 0.5+0.0j) < tolerance1
        assert abs(beta(5, 4) - 0.0035714285714286+0.0j) < tolerance1
        assert abs(beta(2.5, 1.5) - 1.5*0.5*0.5*pi/6.0) < tolerance1
        assert abs(beta(1/2, 1/2) - (pi)) < tolerance1
        assert abs(beta(5/2, 7/2) - (3*pi/256)) < tolerance1
        assert abs(beta(3/2, 1/2) - (pi/2)) < tolerance1
        assert abs(beta(3/2, -1/2) - (-pi)) < tolerance1
        assert abs(beta(-5/2, 7/2) - (-pi)) < tolerance1
        assert abs(beta(1.0/6.0, 5.0/6.0).real - (2*pi)) < tolerance1
        assert abs(beta(0+1j, 1) - (0-1j)) < tolerance1
        assert abs(beta(1, 0+1j) - (0-1j)) < tolerance1
        assert abs(beta(1+1j, 1-1j) - pi/sinh(pi)) < tolerance1
        assert abs(beta(1/2 - pi*jay, 1/2 + pi*jay) - pi/cosh(pi*pi)) < tolerance1
        assert abs(beta(1+42j, 1-42j) - (pi/sinh(pi*42))) < tolerance1

    def test_beta_with_singular_values(self) -> None:
        assert beta(5/2, -7/2) == -inf-infj
        assert beta(-3, 1) == inf+infj
        assert beta(-2, -7) == inf+infj
        assert beta(0, 0) == inf+infj

    def test_beta_with_removable_singular_values(self) -> None:
        assert beta(1, -1) == 0
