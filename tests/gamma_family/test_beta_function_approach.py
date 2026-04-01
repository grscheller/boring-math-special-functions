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
from boring_math.special_functions.constants import pi
from boring_math.special_functions.gamma_family.beta import beta

tolerance1 = 1.0e-13
tolerance2 = 5.0e-13
tolerance3 = 1.0e-12
tolerance4 = 5.0e-12
tolerance5 = 1.0e-11
tolerance6 = 5.0e-11
tolerance7 = 1.0e-10
tolerance8 = 5.0e-10
tolerance9 = 1.0e-9
tolerance10 = 5.0e-9
tolerance11 = 1.0e-8


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
        assert abs(beta(1 - 1j/2, 1 - 1j/2) - (0.5216900572546433+0.764319155615944j)) < tolerance1
        assert abs(beta(1 - 1j/3, 1 - 1j/3) - (0.7626773805450787+0.5890143779152659j)) < tolerance1
        assert abs(beta(1 - 1j/4, 1 - 1j/4) - (0.8608423279235238+0.4658902194416702j)) < tolerance1
        assert abs(beta(1 - 1j/8, 1 - 1j/8) - (0.963725877908492+0.24555879049695992j)) < tolerance1
        assert abs(beta(1 - 1j/16, 1 - 1j/16) - (0.990833618033834+0.12443898981310324j)) < tolerance1
        assert abs(beta(1 - 1j/256, 1 - 1j/256) - (.9999640650525179+0.0078123625525104755j)) < tolerance1
        assert abs(beta(1, 1) - (1)) < tolerance1
        assert abs(beta(1 + 1j/256, 1 + 1j/256) - (.9999640650525179-0.0078123625525104755j)) < tolerance1
        assert abs(beta(1 + 1j/16, 1 + 1j/16) - (0.990833618033834-0.12443898981310324j)) < tolerance1
        assert abs(beta(1 + 1j/8, 1 + 1j/8) - (0.9637258779084817-0.24555879049696072j)) < tolerance1
        assert abs(beta(1 + 1j/4, 1 + 1j/4) - (0.8608423279235238-0.4658902194416702j)) < tolerance1
        assert abs(beta(1 + 1j/3, 1 + 1j/3) - (0.7626773805450787-0.5890143779152659j)) < tolerance1
        assert abs(beta(1 + 1j/2, 1 + 1j/2) - (0.5216900572546314-0.764319155615939j)) < tolerance1


class Test_beta_pos1_neg1:
    def test_beta_left_to_right(self) -> None:
        assert abs(beta(1 - 7/12, -1 - 7/12) - (0.8442222851283135)) < tolerance1
        assert abs(beta(1 - 13/24, -1 - 13/24) - (0.38238505517968213)) < tolerance1
        assert beta(1 - 1/2, -1 - 1/2) == 0
        assert abs(beta(1 - 11/24, -1 - 11/24) - (-0.3207299531745994)) < tolerance1
        assert abs(beta(1 - 5/12, -1 - 5/12) - (-0.5927126815301544)) < tolerance1
        assert abs(beta(1 - 1/3, -1 - 1/3) - (-1.0266951089695893)) < tolerance1
        assert abs(beta(1 - 1/4, -1 - 1/4) - (-1.355540935670367)) < tolerance1
        assert abs(beta(1 - 1/8, -1 - 1/8) - (-1.7225411407110252)) < tolerance1
        assert abs(beta(1 - 1/16, -1 - 1/16) - (-1.869078736112932)) < tolerance1
        assert abs(beta(1 - 1/256, -1 - 1/256) - (-1.9921676081459494)) < tolerance2
        assert beta(1, -1) == -1
        assert abs(beta(1 + 1/256, -1 + 1/256) - (-2.0077930275728715)) < tolerance2
        assert abs(beta(1 + 1/16, -1 + 1/16) - (-2.1208027766459008)) < tolerance1
        assert abs(beta(1 + 1/8, -1 + 1/8) - (-2.236481878750387)) < tolerance1
        assert abs(beta(1 + 1/4, -1 + 1/4) - (-2.472099569735163)) < tolerance1
        assert abs(beta(1 + 1/3, -1 + 1/3) - (-2.6499581254281717)) < tolerance1
        assert abs(beta(1 + 1/2, -1 + 1/2) - (-pi)) < tolerance1

    def test_beta_from_bottom_to_top(self) -> None:
        assert abs(beta(1 - 1j/2, -1 - 1j/2) - (-2.2517180192819937+0.6406008129183864j)) < tolerance1
        assert abs(beta(1 - 1j/3, -1 - 1j/3) - (-2.127974213010586+0.5481991558997743j)) < tolerance1
        assert abs(beta(1 - 1j/4, -1 - 1j/4) - (-2.0755853204975736+0.4479582191645817j)) < tolerance1
        assert abs(beta(1 - 1j/8, -1 - 1j/8) - (-2.0198281662231827+0.24322387873822485j)) < tolerance1
        assert abs(beta(1 - 1j/16, -1 - 1j/16) - (-2.005017980479562+0.1241440486622259j)) < tolerance1
        assert abs(beta(1 - 1j/256, -1 - 1j/256) - (-2.0000196815109663+0.007812290292326293j)) < tolerance1
        assert beta(1, -1) == -1
        assert abs(beta(1 + 1j/256, -1 + 1j/256) - (-2.000019681510964-0.007812290292326694j)) < tolerance1
        assert abs(beta(1 + 1j/16, -1 + 1j/16) - (-2.005017980479545-0.12414404866222331j)) < tolerance1
        assert abs(beta(1 + 1j/8, -1 + 1j/8) - (-2.0198281662231805-0.243223878738222j)) < tolerance1
        assert abs(beta(1 + 1j/4, -1 + 1j/4) - (-2.075585320497565-0.4479582191645744j)) < tolerance1
        assert abs(beta(1 + 1j/3, -1 + 1j/3) - (-2.1279742130105808-0.5481991558997661j)) < tolerance1
        assert abs(beta(1 + 1j/2, -1 + 1j/2) - (-2.2517180192819706-0.6406008129183801j)) < tolerance1

class Test_beta_neg2_neg7:
    def test_beta_right_to_left(self) -> None:
    #   assert abs(beta(-2 + 1/2, -7 + 1/2) - (0)) < tolerance1
        assert abs(beta(-2 + 1/3, -7 + 1/3) - (77.004665527148142)) < tolerance1
        assert abs(beta(-2 + 1/4, -7 + 1/4) - (152.404386245326966)) < tolerance2
        assert abs(beta(-2 + 1/8, -7 + 1/8) - (448.66095912879820)) < tolerance4
        assert abs(beta(-2 + 1/16, -7 + 1/16) - (1030.97087443644088)) < tolerance6
        assert abs(beta(-2 + 1/256, -7 + 1/256) - (18318.72337057219)) < tolerance11
        assert isinf(beta(-2, -7))
        assert abs(beta(-2 - 1/256, -7 - 1/256) - (-18544.08473524038)) < tolerance11
        assert abs(beta(-2 - 1/16, -7 - 1/16) - (-1253.7545201376397)) < tolerance6
        assert abs(beta(-2 - 1/8, -7 - 1/8) - (-663.5417040997620)) < tolerance5
        assert abs(beta(-2 - 1/4, -7 - 1/4) - (-333.456837802792144)) < tolerance3
        assert abs(beta(-2 - 1/3, -7 - 1/3) - (-218.8288691843276)) < tolerance2
        assert abs(beta(-2 - 1/2, -7 - 1/2) - (0)) < tolerance1

    def test_beta_diagonally(self) -> None:
        assert abs(beta(-2 + (1+1j)/2, -7 + (1+1j)/2) - (-69.19100390654522-65.51108557215757j)) < tolerance1
        assert abs(beta(-2 + (1+1j)/3, -7 + (1+1j)/3) - (-37.58256399010684-112.89658546014992j)) < tolerance1
        assert abs(beta(-2 + (1+1j)/4, -7 + (1+1j)/4) - (1.761016743772245-153.01782524117849j)) < tolerance1
        assert abs(beta(-2 + (1+1j)/8, -7 + (1+1j)/8) - (157.55893367001724-298.36213298053826j)) < tolerance1
        assert abs(beta(-2 + (1+1j)/16, -7 + (1+1j)/16) - (453.96247669782167-583.1615282660869j)) < tolerance1
        assert abs(beta(-2 + (1+1j)/256, -7 + (1+1j)/256) - (9102.718413120123-9216.585908309606j)) < tolerance1
        assert isinf(beta(-2, -7))
        assert abs(beta(-2 - (1+1j)/256, -7 - (1+1j)/256) - (-9328.089842389212+9216.606035767285j)) < tolerance1
        assert abs(beta(-2 - (1+1j)/16, -7 - (1+1j)/16) - (-679.379617403794+588.3138413834292j)) < tolerance1
        assert abs(beta(-2 - (1+1j)/8, -7 - (1+1j)/8) - (-383.6611860983296+318.9524400831555j)) < tolerance1
        assert abs(beta(-2 - (1+1j)/4, -7 - (1+1j)/4) - (-238.68184705003927+234.1843079355342j)) < tolerance1
        assert abs(beta(-2 - (1+1j)/3, -7 - (1+1j)/3) - (-223.29129811565167+252.5134165941293j)) < tolerance1
        assert abs(beta(-2 - (1+1j)/2, -7 - (1+1j)/2) - (-311.4250423478645+328.26933802362237j)) < tolerance1


class Test_beta_neg3_pos1:
    def test_beta_left_to_right(self) -> None:
        assert abs(beta(-3 - 1/3, 1 - 1/3) - (-0.5866829194111927)) < tolerance1
        assert abs(beta(-3 - 1/4, 1 - 1/4) - (-0.695149197779674)) < tolerance1
        assert abs(beta(-3 - 1/8, 1 - 1/8) - (-0.7295468360658462)) < tolerance1
        assert abs(beta(-3 - 1/20, 1 - 1/20) - (-0.7006018748883518)) < tolerance1
        assert abs(beta(-3 - 1/100, 1 - 1/100) - (-0.6742564516000351)) < tolerance1
        assert abs(beta(-3 - 1/256, 1 - 1/256) - (-0.6696764002044514)) < tolerance1
        assert abs(beta(-3, 1) - (-1/3)) < tolerance1
        assert abs(beta(-3 + 1/256, 1 + 1/256) - (-0.6636002949244252)) < tolerance1
        assert abs(beta(-3 + 1/100, 1 + 1/100) - (-0.6587056545925919)) < tolerance1
        assert abs(beta(-3 + 1/20, 1 + 1/20) - (-0.6234202673370612)) < tolerance1
        assert abs(beta(-3 + 1/8, 1 + 1/8) - (-0.5445347183044419)) < tolerance1
        assert abs(beta(-3 + 1/4, 1 + 1/4) - (-0.3852622706080775)) < tolerance1
        assert abs(beta(-3 + 1/3, 1 + 1/3) - (-0.2649958125428176)) < tolerance1

    def test_beta_one_side_left_to_right(self) -> None:
        assert abs(beta(-3 - 1/3, 1) - (-3/10)) < tolerance1
        assert abs(beta(-3 - 1/4, 1) - (-0.30769230769230704)) < tolerance1
        assert abs(beta(-3 - 1/8, 1) - (-0.31999999999999995)) < tolerance1
        assert abs(beta(-3 - 1/20, 1) - (-0.32786885245901715)) < tolerance1
        assert abs(beta(-3 - 1/100, 1) - (-0.33222591362125625)) < tolerance1
        assert abs(beta(-3 - 1/256, 1) - (-0.3328998699610047)) < tolerance1
        assert abs(beta(-3, 1) - (-1/3)) < tolerance1
        assert abs(beta(-3 + 1/256, 1) - (-0.33376792698828256)) < tolerance1
        assert abs(beta(-3 + 1/100, 1) - (-0.334448160535111)) < tolerance1
        assert abs(beta(-3 + 1/20, 1) - (-0.3389830508474576)) < tolerance1
        assert abs(beta(-3 + 1/8, 1) - (-0.3478260869565217)) < tolerance1
        assert abs(beta(-3 + 1/4, 1) - (-0.36363636363636354)) < tolerance1
        assert abs(beta(-3 + 1/3, 1) - (-3/8)) < tolerance1


    def test_beta_other_side_left_to_right(self) -> None:
        assert abs(beta(-1/2, 1) - (-2)) < tolerance1
        assert abs(beta(-1/3, 1) - (-3)) < tolerance1
        assert abs(beta(-1/4, 1) - (-4)) < tolerance1
        assert abs(beta(-1/8, 1) - (-8)) < tolerance1
        assert abs(beta(-1/20, 1) - (-20)) < tolerance2
        assert abs(beta(-1/100, 1) - (-100)) < tolerance6
        assert abs(beta(-1/256, 1) - (-256)) < tolerance7
        assert isinf(beta(0, 1))
        assert abs(beta(1/256, 1) - (256)) < tolerance7
        assert abs(beta(1/100, 1) - (100)) < tolerance6
        assert abs(beta(1/20, 1) - (20)) < tolerance2
        assert abs(beta(1/8, 1) - (8)) < tolerance1
        assert abs(beta(1/4, 1) - (4)) < tolerance1
        assert abs(beta(1/3, 1) - (3)) < tolerance1
        assert abs(beta(1/2, 1) - (2)) < tolerance1
