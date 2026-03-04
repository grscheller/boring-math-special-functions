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
from boring_math.special_functions.exponential import exp0

tolerance0 = 5.0e-16
tolerance1 = 5.0e-15


class Test_exp0:
    def test_exp0(self) -> None:
        assert abs(exp0(0.00) - math.exp(0.00)) < tolerance0
        assert abs(exp0(0.01) - math.exp(0.01)) < tolerance0
        assert abs(exp0(0.05) - math.exp(0.05)) < tolerance0
        assert abs(exp0(0.10) - math.exp(0.10)) < tolerance0
        assert abs(exp0(0.15) - math.exp(0.15)) < tolerance0
        assert abs(exp0(0.20) - math.exp(0.20)) < tolerance0
        assert abs(exp0(0.25) - math.exp(0.25)) < tolerance0
        assert abs(exp0(0.30) - math.exp(0.30)) < tolerance0
        assert abs(exp0(0.35) - math.exp(0.35)) < tolerance0
        assert abs(exp0(0.40) - math.exp(0.40)) < tolerance0
        assert abs(exp0(0.45) - math.exp(0.45)) < tolerance0
        assert abs(exp0(0.50) - math.exp(0.50)) < tolerance0
        assert abs(exp0(0.55) - math.exp(0.55)) < tolerance0
        assert abs(exp0(0.60) - math.exp(0.60)) < tolerance0
        assert abs(exp0(0.65) - math.exp(0.65)) < tolerance0
        assert abs(exp0(0.70) - math.exp(0.70)) < tolerance0
        assert abs(exp0(0.75) - math.exp(0.75)) < tolerance0
        assert abs(exp0(0.80) - math.exp(0.80)) < tolerance0
        assert abs(exp0(0.85) - math.exp(0.85)) < tolerance0
        assert abs(exp0(0.90) - math.exp(0.90)) < tolerance0
        assert abs(exp0(0.95) - math.exp(0.95)) < tolerance0
        assert abs(exp0(1.00) - math.exp(1.00)) < tolerance0
        assert abs(exp0(1.10) - math.exp(1.10)) < tolerance0
        assert abs(exp0(1.20) - math.exp(1.20)) < tolerance0
        assert abs(exp0(1.30) - math.exp(1.30)) < tolerance0
        assert abs(exp0(1.40) - math.exp(1.40)) < tolerance0
        assert abs(exp0(1.50) - math.exp(1.50)) < tolerance0
        assert abs(exp0(1.60) - math.exp(1.60)) < tolerance0
        assert abs(exp0(1.70) - math.exp(1.70)) < tolerance0
        assert abs(exp0(1.80) - math.exp(1.80)) < tolerance1
        assert abs(exp0(1.90) - math.exp(1.90)) < tolerance1
        assert abs(exp0(2.00) - math.exp(2.00)) < tolerance1
        assert abs(exp0(-0.01) - math.exp(-0.01)) < tolerance0
        assert abs(exp0(-0.05) - math.exp(-0.05)) < tolerance0
        assert abs(exp0(-0.10) - math.exp(-0.10)) < tolerance0
        assert abs(exp0(-0.15) - math.exp(-0.15)) < tolerance0
        assert abs(exp0(-0.20) - math.exp(-0.20)) < tolerance0
        assert abs(exp0(-0.25) - math.exp(-0.25)) < tolerance0
        assert abs(exp0(-0.30) - math.exp(-0.30)) < tolerance0
        assert abs(exp0(-0.35) - math.exp(-0.35)) < tolerance0
        assert abs(exp0(-0.40) - math.exp(-0.40)) < tolerance0
        assert abs(exp0(-0.45) - math.exp(-0.45)) < tolerance0
        assert abs(exp0(-0.50) - math.exp(-0.50)) < tolerance0
        assert abs(exp0(-0.55) - math.exp(-0.55)) < tolerance0
        assert abs(exp0(-0.60) - math.exp(-0.60)) < tolerance0
        assert abs(exp0(-0.65) - math.exp(-0.65)) < tolerance0
        assert abs(exp0(-0.70) - math.exp(-0.70)) < tolerance0
        assert abs(exp0(-0.75) - math.exp(-0.75)) < tolerance0
        assert abs(exp0(-0.80) - math.exp(-0.80)) < tolerance0
        assert abs(exp0(-0.85) - math.exp(-0.85)) < tolerance0
        assert abs(exp0(-0.90) - math.exp(-0.90)) < tolerance0
        assert abs(exp0(-0.95) - math.exp(-0.95)) < tolerance0
        assert abs(exp0(-1.00) - math.exp(-1.00)) < tolerance0
        assert abs(exp0(-1.10) - math.exp(-1.10)) < tolerance0
        assert abs(exp0(-1.20) - math.exp(-1.20)) < tolerance0
        assert abs(exp0(-1.30) - math.exp(-1.30)) < tolerance0
        assert abs(exp0(-1.40) - math.exp(-1.40)) < tolerance0
        assert abs(exp0(-1.50) - math.exp(-1.50)) < tolerance0
        assert abs(exp0(-1.60) - math.exp(-1.60)) < tolerance0
        assert abs(exp0(-1.70) - math.exp(-1.70)) < tolerance0
        assert abs(exp0(-1.80) - math.exp(-1.80)) < tolerance0
        assert abs(exp0(-1.90) - math.exp(-1.90)) < tolerance0
        assert abs(exp0(-2.00) - math.exp(-2.00)) < tolerance0
