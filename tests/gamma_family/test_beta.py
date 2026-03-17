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

from cmath import isinf
from math import pi, sinh, cosh
from boring_math.special_functions.beta import beta

jay = 0.0+1.0j

tolerance1 = 1.0e-14
tolerance2 = 5.0e-14
tolerance3 = 1.0e-13


class Test_beta:
    def test_beta_with_exact_values(self) -> None:
        assert abs(beta(1, 1) - (1)) < tolerance1
        assert abs(beta(1, 2) - (1/2)) < tolerance1
        assert abs(beta(2, 3) - (1/12)) < tolerance1
        assert abs(beta(7, 3) - (1/252)) < tolerance1
        assert abs(beta(4, 4) - (1/140)) < tolerance1
        assert abs(beta(5, 4) - (1/280)) < tolerance1
        assert abs(beta(1/2, 1/2) - (pi)) < tolerance1
        assert abs(beta(3/2, 1/2) - (pi/2)) < tolerance1
        assert abs(beta(5/2, 3/2) - (pi/16)) < tolerance1
        assert abs(beta(5/2, 7/2) - (3*pi/256)) < tolerance1
        assert abs(beta(3/2, -1/2) - (-pi)) < tolerance1
        assert abs(beta(-5/2, 7/2) - (-pi)) < tolerance1
        assert abs(beta(5/2, 11/2) - (9*pi/2048)) < tolerance1
        assert abs(beta(5/2, -11/2) - (0)) < tolerance1
        assert abs(beta(1/6, 5/6) - (2*pi)) < tolerance2
        assert abs(beta(1/6, 2) - (36/7)) < tolerance2
        assert abs(beta(42, 11) - (1/664441017240)) < tolerance1
        assert abs(beta(1, 1j) - (-1j)) < tolerance1
        assert abs(beta(1+42j, 1-42j) - (pi/sinh(pi*42))) < tolerance1
        assert abs(beta(1/2 - pi*(1j), 1/2 + pi*(1j)) - pi/cosh(pi*pi)) < tolerance1
        assert beta(1, -1) == -1.0
        assert beta(-3, 1) == -1/3
        assert beta(2, -3) == 1/6

    def test_beta_with_approx_values(self) -> None:
        assert abs(beta(1.0023, 2.2123) - (0.4503795612154237)) < tolerance1
        assert abs(beta(0+1j, 0+1j) - (-2.376146124821733-2.639568520278136j)) < tolerance1
        assert abs(beta(pi - 1j, 1+1j) - (0.036836170895854-0.1332437023662604j)) < tolerance1

    def test_beta_with_singular_values(self) -> None:
        assert isinf(beta(0, 0))
        assert isinf(beta(-2, -7))
