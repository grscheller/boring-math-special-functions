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
from boring_math.special_functions.float import exp0

tolerance = 5.0e-16


class Test_exp0:
    def test_exp0(self) -> None:
        assert abs(exp0(0.00) - exp(0.00)) < tolerance
        assert abs(exp0(0.05) - exp(0.05)) < tolerance
        assert abs(exp0(0.10) - exp(0.10)) < tolerance
        assert abs(exp0(0.15) - exp(0.15)) < tolerance
        assert abs(exp0(0.20) - exp(0.20)) < tolerance
        assert abs(exp0(0.25) - exp(0.25)) < tolerance
        assert abs(exp0(0.30) - exp(0.30)) < tolerance
        assert abs(exp0(0.35) - exp(0.35)) < tolerance
        assert abs(exp0(0.40) - exp(0.40)) < tolerance
        assert abs(exp0(0.45) - exp(0.45)) < tolerance
        assert abs(exp0(0.50) - exp(0.50)) < tolerance
        assert abs(exp0(0.55) - exp(0.55)) < tolerance
        assert abs(exp0(0.60) - exp(0.60)) < tolerance
        assert abs(exp0(0.65) - exp(0.65)) < tolerance
        assert abs(exp0(0.70) - exp(0.70)) < tolerance
        assert abs(exp0(0.75) - exp(0.75)) < tolerance
        assert abs(exp0(0.80) - exp(0.80)) < tolerance
        assert abs(exp0(0.85) - exp(0.85)) < tolerance
        assert abs(exp0(0.90) - exp(0.90)) < tolerance
        assert abs(exp0(0.95) - exp(0.95)) < tolerance
        assert abs(exp0(1.00) - exp(1.00)) < tolerance
        assert abs(exp0(-0.05) - exp(-0.05)) < tolerance
        assert abs(exp0(-0.10) - exp(-0.10)) < tolerance
        assert abs(exp0(-0.15) - exp(-0.15)) < tolerance
        assert abs(exp0(-0.20) - exp(-0.20)) < tolerance
        assert abs(exp0(-0.25) - exp(-0.25)) < tolerance
        assert abs(exp0(-0.30) - exp(-0.30)) < tolerance
        assert abs(exp0(-0.35) - exp(-0.35)) < tolerance
        assert abs(exp0(-0.40) - exp(-0.40)) < tolerance
        assert abs(exp0(-0.45) - exp(-0.45)) < tolerance
        assert abs(exp0(-0.50) - exp(-0.50)) < tolerance
        assert abs(exp0(-0.55) - exp(-0.55)) < tolerance
        assert abs(exp0(-0.60) - exp(-0.60)) < tolerance
        assert abs(exp0(-0.65) - exp(-0.65)) < tolerance
        assert abs(exp0(-0.70) - exp(-0.70)) < tolerance
        assert abs(exp0(-0.75) - exp(-0.75)) < tolerance
        assert abs(exp0(-0.80) - exp(-0.80)) < tolerance
        assert abs(exp0(-0.85) - exp(-0.85)) < tolerance
        assert abs(exp0(-0.90) - exp(-0.90)) < tolerance
        assert abs(exp0(-0.95) - exp(-0.95)) < tolerance
        assert abs(exp0(-1.00) - exp(-1.00)) < tolerance
