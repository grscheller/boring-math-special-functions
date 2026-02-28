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

from math import exp
from boring_math.special_functions.trig0_float import exp0

tolerance0 = 5.0e-16
tolerance1 = 5.0e-15


class Test_exp0:
    def test_exp0(self) -> None:
        assert abs(exp0(0.00) - exp(0.00)) < tolerance0
        assert abs(exp0(0.01) - exp(0.01)) < tolerance0
        assert abs(exp0(0.05) - exp(0.05)) < tolerance0
        assert abs(exp0(0.10) - exp(0.10)) < tolerance0
        assert abs(exp0(0.15) - exp(0.15)) < tolerance0
        assert abs(exp0(0.20) - exp(0.20)) < tolerance0
        assert abs(exp0(0.25) - exp(0.25)) < tolerance0
        assert abs(exp0(0.30) - exp(0.30)) < tolerance0
        assert abs(exp0(0.35) - exp(0.35)) < tolerance0
        assert abs(exp0(0.40) - exp(0.40)) < tolerance0
        assert abs(exp0(0.45) - exp(0.45)) < tolerance0
        assert abs(exp0(0.50) - exp(0.50)) < tolerance0
        assert abs(exp0(0.55) - exp(0.55)) < tolerance0
        assert abs(exp0(0.60) - exp(0.60)) < tolerance0
        assert abs(exp0(0.65) - exp(0.65)) < tolerance0
        assert abs(exp0(0.70) - exp(0.70)) < tolerance0
        assert abs(exp0(0.75) - exp(0.75)) < tolerance0
        assert abs(exp0(0.80) - exp(0.80)) < tolerance0
        assert abs(exp0(0.85) - exp(0.85)) < tolerance0
        assert abs(exp0(0.90) - exp(0.90)) < tolerance0
        assert abs(exp0(0.95) - exp(0.95)) < tolerance0
        assert abs(exp0(1.00) - exp(1.00)) < tolerance0
        assert abs(exp0(1.10) - exp(1.10)) < tolerance0
        assert abs(exp0(1.20) - exp(1.20)) < tolerance0
        assert abs(exp0(1.30) - exp(1.30)) < tolerance0
        assert abs(exp0(1.40) - exp(1.40)) < tolerance0
        assert abs(exp0(1.50) - exp(1.50)) < tolerance0
        assert abs(exp0(1.60) - exp(1.60)) < tolerance0
        assert abs(exp0(1.70) - exp(1.70)) < tolerance0
        assert abs(exp0(1.80) - exp(1.80)) < tolerance1
        assert abs(exp0(1.90) - exp(1.90)) < tolerance1
        assert abs(exp0(2.00) - exp(2.00)) < tolerance1
        assert abs(exp0(-0.01) - exp(-0.01)) < tolerance0
        assert abs(exp0(-0.05) - exp(-0.05)) < tolerance0
        assert abs(exp0(-0.10) - exp(-0.10)) < tolerance0
        assert abs(exp0(-0.15) - exp(-0.15)) < tolerance0
        assert abs(exp0(-0.20) - exp(-0.20)) < tolerance0
        assert abs(exp0(-0.25) - exp(-0.25)) < tolerance0
        assert abs(exp0(-0.30) - exp(-0.30)) < tolerance0
        assert abs(exp0(-0.35) - exp(-0.35)) < tolerance0
        assert abs(exp0(-0.40) - exp(-0.40)) < tolerance0
        assert abs(exp0(-0.45) - exp(-0.45)) < tolerance0
        assert abs(exp0(-0.50) - exp(-0.50)) < tolerance0
        assert abs(exp0(-0.55) - exp(-0.55)) < tolerance0
        assert abs(exp0(-0.60) - exp(-0.60)) < tolerance0
        assert abs(exp0(-0.65) - exp(-0.65)) < tolerance0
        assert abs(exp0(-0.70) - exp(-0.70)) < tolerance0
        assert abs(exp0(-0.75) - exp(-0.75)) < tolerance0
        assert abs(exp0(-0.80) - exp(-0.80)) < tolerance0
        assert abs(exp0(-0.85) - exp(-0.85)) < tolerance0
        assert abs(exp0(-0.90) - exp(-0.90)) < tolerance0
        assert abs(exp0(-0.95) - exp(-0.95)) < tolerance0
        assert abs(exp0(-1.00) - exp(-1.00)) < tolerance0
        assert abs(exp0(-1.10) - exp(-1.10)) < tolerance0
        assert abs(exp0(-1.20) - exp(-1.20)) < tolerance0
        assert abs(exp0(-1.30) - exp(-1.30)) < tolerance0
        assert abs(exp0(-1.40) - exp(-1.40)) < tolerance0
        assert abs(exp0(-1.50) - exp(-1.50)) < tolerance0
        assert abs(exp0(-1.60) - exp(-1.60)) < tolerance0
        assert abs(exp0(-1.70) - exp(-1.70)) < tolerance0
        assert abs(exp0(-1.80) - exp(-1.80)) < tolerance0
        assert abs(exp0(-1.90) - exp(-1.90)) < tolerance0
        assert abs(exp0(-2.00) - exp(-2.00)) < tolerance0
