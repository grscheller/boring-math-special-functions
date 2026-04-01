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
from boring_math.special_functions.exponential.exp import exp

tolerance0 = 5.0e-16
tolerance1 = 5.0e-15
tolerance2 = 5.0e-12
tolerance3 = 5.0e-11


class Test_exp:
    def test_exp(self) -> None:
        assert abs(exp(0.00) - math.exp(0.00)) < tolerance0
        assert abs(exp(0.01) - math.exp(0.01)) < tolerance0
        assert abs(exp(-0.01) - math.exp(-0.01)) < tolerance0
        assert abs(exp(0.05) - math.exp(0.05)) < tolerance0
        assert abs(exp(-0.05) - math.exp(-0.05)) < tolerance0
        assert abs(exp(-0.25) - math.exp(-0.25)) < tolerance0
        assert abs(exp(0.15) - math.exp(0.15)) < tolerance0
        assert abs(exp(0.65) - math.exp(0.65)) < tolerance0
        assert abs(exp(0.95) - math.exp(0.95)) < tolerance0
        assert abs(exp(0.99) - math.exp(0.99)) < tolerance0
        assert abs(exp(1.00) - math.exp(1.00)) < tolerance0
        assert abs(exp(1.01) - math.exp(1.01)) < tolerance0
        assert abs(exp(1.10) - math.exp(1.10)) < tolerance0
        assert abs(exp(2.00) - math.exp(2.00)) < tolerance1
        assert abs(exp(2.70) - math.exp(2.70)) < tolerance1
        assert abs(exp(8.00) - math.exp(8.00)) < tolerance2
        assert abs(exp(9.00) - math.exp(9.00)) < tolerance2
        assert abs(exp(10.50) - math.exp(10.50)) < tolerance3
        assert abs(exp(-0.95) - math.exp(-0.95)) < tolerance0
        assert abs(exp(-1.00) - math.exp(-1.00)) < tolerance0
        assert abs(exp(-1.05) - math.exp(-1.05)) < tolerance0
        assert abs(exp(-2.75) - math.exp(-2.75)) < tolerance0
        assert abs(exp(-7.55) - math.exp(-7.55)) < tolerance0
        assert abs(exp(-42.3) - math.exp(-42.3)) < tolerance0
