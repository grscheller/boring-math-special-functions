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

from math import inf
from cmath import isinf
from boring_math.special_functions.constants import pi
from boring_math.special_functions.gamma_family.beta import beta_real

jay = 0.0 + 1.0j

tolerance1 = 1.0e-14
tolerance2 = 5.0e-14
tolerance3 = 1.0e-13
tolerance4 = 5.0e-13
tolerance5 = 1.0e-12


class Test_beta:
    def test_beta_with_exact_values(self) -> None:
        assert abs(beta_real(1, 1) - (1)) < tolerance1
        assert abs(beta_real(1, 2) - (1/2)) < tolerance1
        assert abs(beta_real(2, 3) - (1/12)) < tolerance1
        assert abs(beta_real(7, 3) - (1/252)) < tolerance1
        assert abs(beta_real(4, 4) - (1/140)) < tolerance1
        assert abs(beta_real(5, 4) - (1/280)) < tolerance1
        assert abs(beta_real(11, 17) - (1/143416845)) < tolerance1
        assert abs(beta_real(1/2, 1/1) - (2)) < tolerance1
        assert abs(beta_real(3/2, 1/2) - (pi/2)) < tolerance1
        assert abs(beta_real(5/2, 3/2) - (pi/16)) < tolerance1
        assert abs(beta_real(5/2, 7/2) - (3*pi/256)) < tolerance1
        assert abs(beta_real(5/2, 11/2) - (9*pi/2048)) < tolerance1
        assert abs(beta_real(1/6, 5/6) - (2*pi)) < tolerance2
        assert abs(beta_real(1/6, 2) - (36/7)) < tolerance2
        assert abs(beta_real(42, 11) - (1/664441017240)) < tolerance1


    def test_beta_with_approx_values(self) -> None:
        assert abs(beta_real(1.0023, 2.2123) - (0.4503795612154237)) < tolerance1
        assert abs(beta_real(1, pi/2) - (0.63661977236758134)) < tolerance1
        assert abs(beta_real(0.004, 0.007) - (392.83919317903175)) < tolerance5
        abs(beta_real(1, pi/2) - (-0.636619772367581343)) < tolerance1
        abs(beta_real(pi/2, pi/2) - (0.346628321041040863)) < tolerance1

    def test_beta_involving_singular_values(self) -> None:
        try:
            beta_real(0, 0) == 42
        except ValueError:
            assert True
        else:
            assert False

        try:
            isinf(beta_real(0, 0))
        except ValueError:
            assert True
        else:
            assert False

        try:
            beta_real(0, 0) == inf
        except ValueError:
            assert True
        else:
            assert False

        try:
            beta_real(1, 0) == inf
        except ValueError:
            assert True
        else:
            assert False

        try:
            isinf(beta_real(0, 1))
        except ValueError:
            assert True
        else:
            assert False

        try:
            isinf(beta_real(-1, 0))
        except ValueError:
            assert True
        else:
            assert False

    def test_beta_involving_nonpositive_args(self) -> None:
        try:
            isinf(beta_real(0, 1))
        except ValueError:
            assert True
        else:
            assert False

        try:
            isinf(beta_real(-1, 0))
        except ValueError:
            assert True
        else:
            assert False

        try:
            isinf(beta_real(1, -pi/2))
        except ValueError:
            assert True
        else:
            assert False

        try:
            beta_real(-7, 13) != 42
        except ValueError:
            assert True
        else:
            assert False

        try:
            abs(beta_real(1, -pi/2) - (-0.636619772367581343)) < tolerance1
        except ValueError:
            assert True
        else:
            assert False

        try:
            abs(beta_real(-pi/2, -pi/2) - (5.21953171495050934)) < tolerance1
        except ValueError:
            assert True
        else:
            assert False
