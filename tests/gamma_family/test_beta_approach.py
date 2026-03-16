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

from cmath import pi, inf, infj
from boring_math.special_functions.beta import beta

jay = 0.0+1.0j

tolerance1 = 1.0e-13
tolerance2 = 2.0e-13


class Test_beta_pos1_pos1:
    def test_beta_left_to_right(self) -> None:
        assert abs(beta(1 - 1/2, 1 - 1/2) - (pi)) < tolerance1
        assert abs(beta(1 - 1/3, 1 - 1/3) - (2.0533902179391763)) < tolerance1
        assert abs(beta(1 - 1/4, 1 - 1/4) - (1.6944261695879586)) < tolerance1
        assert abs(beta(1 - 1/8, 1 - 1/8) - (1.2919058555332712)) < tolerance1
        assert abs(beta(1 - 1/16, 1 - 1/16) - (1.1347978040685676)) < tolerance1
        assert abs(beta(1 - 1/256, 1 - 1/256) - (1.0078485734124223)) < tolerance1
        assert abs(beta(1, 1) - (1)) < tolerance1
        assert abs(beta(1 + 1/256, 1 + 1/256) - (0.9922232985098526)) < tolerance1
        assert abs(beta(1 + 1/16, 1 + 1/16) - (0.883667823602458)) < tolerance1
        assert abs(beta(1 + 1/8, 1 + 1/8) - (0.7827686575626354)) < tolerance1
        assert abs(beta(1 + 1/4, 1 + 1/4) - (0.6180248924337906)) < tolerance1
        assert abs(beta(1 + 1/3, 1 + 1/3) - (0.5299916250856347)) < tolerance1
        assert abs(beta(1 + 1/2, 1 + 1/2) - (pi/8)) < tolerance1

    def test_beta_from_bottom_to_top(self) -> None:
        assert abs(beta(1 - jay/2, 1 - jay/2) - (0.5216900572546433+0.764319155615944j)) < tolerance1
        assert abs(beta(1 - jay/3, 1 - jay/3) - (0.7626773805450787+0.5890143779152659j)) < tolerance1
        assert abs(beta(1 - jay/4, 1 - jay/4) - (0.8608423279235238+0.4658902194416702j)) < tolerance1
        assert abs(beta(1 - jay/8, 1 - jay/8) - (0.963725877908492+0.24555879049695992j)) < tolerance1
        assert abs(beta(1 - jay/16, 1 - jay/16) - (0.990833618033834+0.12443898981310324j)) < tolerance1
        assert abs(beta(1 - jay/256, 1 - jay/256) - (.9999640650525179+0.0078123625525104755j)) < tolerance1
        assert abs(beta(1, 1) - (1)) < tolerance1
        assert abs(beta(1 + jay/256, 1 + jay/256) - (.9999640650525179-0.0078123625525104755j)) < tolerance1
        assert abs(beta(1 + jay/16, 1 + jay/16) - (0.990833618033834-0.12443898981310324j)) < tolerance1
        assert abs(beta(1 + jay/8, 1 + jay/8) - (0.9637258779084817-0.24555879049696072j)) < tolerance1
        assert abs(beta(1 + jay/4, 1 + jay/4) - (0.8608423279235238-0.4658902194416702j)) < tolerance1
        assert abs(beta(1 + jay/3, 1 + jay/3) - (0.7626773805450787-0.5890143779152659j)) < tolerance1
        assert abs(beta(1 + jay/2, 1 + jay/2) - (0.5216900572546314-0.764319155615939j)) < tolerance1


class Test_beta_pos1_neg1:
    def test_beta_left_to_right(self) -> None:
        assert abs(beta(1 - 7/12, -1 - 7/12) - (0.8442222851283135)) < tolerance1
        assert abs(beta(1 - 13/24, -1 - 13/24) - (0.38238505517968213)) < tolerance1
        assert abs(beta(1 - 1/2, -1 - 1/2) - (0)) < tolerance1
        assert abs(beta(1 - 11/24, -1 - 11/24) - (-0.3207299531745994)) < tolerance1
        assert abs(beta(1 - 5/12, -1 - 5/12) - (-0.5927126815301544)) < tolerance1
        assert abs(beta(1 - 1/3, -1 - 1/3) - (-1.0266951089695893)) < tolerance1
        assert abs(beta(1 - 1/4, -1 - 1/4) - (-1.355540935670367)) < tolerance1
        assert abs(beta(1 - 1/8, -1 - 1/8) - (-1.7225411407110252)) < tolerance1
        assert abs(beta(1 - 1/16, -1 - 1/16) - (-1.869078736112932)) < tolerance1
        assert abs(beta(1 - 1/256, -1 - 1/256) - (-1.9921676081459494)) < tolerance2
        assert abs(beta(1, -1) - (-2)) < tolerance1
        assert abs(beta(1 + 1/256, -1 + 1/256) - (-2.0077930275728715)) < tolerance2
        assert abs(beta(1 + 1/16, -1 + 1/16) - (-2.1208027766459008)) < tolerance1
        assert abs(beta(1 + 1/8, -1 + 1/8) - (-2.236481878750387)) < tolerance1
        assert abs(beta(1 + 1/4, -1 + 1/4) - (-2.472099569735163)) < tolerance1
        assert abs(beta(1 + 1/3, -1 + 1/3) - (-2.6499581254281717)) < tolerance1
        assert abs(beta(1 + 1/2, -1 + 1/2) - (-pi)) < tolerance1

    def test_beta_from_bottom_to_top(self) -> None:
        assert abs(beta(1 - jay/2, -1 - jay/2) - (-2.2517180192819937+0.6406008129183864j)) < tolerance1
        assert abs(beta(1 - jay/3, -1 - jay/3) - (-2.127974213010586+0.5481991558997743j)) < tolerance1
        assert abs(beta(1 - jay/4, -1 - jay/4) - (-2.0755853204975736+0.4479582191645817j)) < tolerance1
        assert abs(beta(1 - jay/8, -1 - jay/8) - (-2.0198281662231827+0.24322387873822485j)) < tolerance1
        assert abs(beta(1 - jay/16, -1 - jay/16) - (-2.005017980479562+0.1241440486622259j)) < tolerance1
        assert abs(beta(1 - jay/256, -1 - jay/256) - (-2.0000196815109663+0.007812290292326293j)) < tolerance1
        assert abs(beta(1, -1) - (-2)) < tolerance1
        assert abs(beta(1 + jay/256, -1 + jay/256) - (-2.000019681510964-0.007812290292326694j)) < tolerance1
        assert abs(beta(1 + jay/16, -1 + jay/16) - (-2.005017980479545-0.12414404866222331j)) < tolerance1
        assert abs(beta(1 + jay/8, -1 + jay/8) - (-2.0198281662231805-0.243223878738222j)) < tolerance1
        assert abs(beta(1 + jay/4, -1 + jay/4) - (-2.075585320497565-0.4479582191645744j)) < tolerance1
        assert abs(beta(1 + jay/3, -1 + jay/3) - (-2.1279742130105808-0.5481991558997661j)) < tolerance1
        assert abs(beta(1 + jay/2, -1 + jay/2) - (-2.2517180192819706-0.6406008129183801j)) < tolerance1
