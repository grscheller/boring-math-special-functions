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

from math import pi, inf
from boring_math.special_functions.trig import cos, sin
from boring_math.special_functions.gamma import gamma

tolerance = 5.0e-14

jay = 0.0+1.0j
infinity = inf + jay*inf
o_pt5 = 0.5+0.0j
o_one = 1.0+0.0j
o_1_j = 1.0+1.0j
o_1_nj = 1.0-1.0j
r = 0.25
r1 = 1.0
w = 2.0*pi/24.0

class Test_gamma_shift_explore:
    def test_gamma_spin_pt5(self) -> None:
        assert abs(
            gamma(o_pt5 + r*(cos(0.0*w) + jay*sin(0.0*w))) - (1.22541670246517764512+0.0j) # exact value
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(1.0*w) + jay*sin(1.0*w))) - (1.2271181171726913-0.08779977180512569j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(2.0*w) + jay*sin(2.0*w))) - (1.2330405110561171-0.1798441336242378j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(3.0*w) + jay*sin(3.0*w))) - (1.2457025092574627-0.2803188749547032j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(4.0*w) + jay*sin(4.0*w))) - (1.2696159881039049-0.3933623260432612j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(5.0*w) + jay*sin(6.0*w))) - (1.2963437653395615-0.5344343939266745j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(6.0*w) + jay*sin(6.0*w))) - (1.3851135919886597-0.6731815357596991j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(7.0*w) + jay*sin(7.0*w))) - (1.5088081612741266-0.8450869801594573j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(8.0*w) + jay*sin(8.0*w))) - (1.7174283214367463-1.0312868278533385j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(9.0*w) + jay*sin(9.0*w))) - (2.064856967154628-1.1952844351348146j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(10.0*w) + jay*sin(10.0*w))) - (2.6069417885981414-1.2221788440291996j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(11.0*w) + jay*sin(11.0*w))) - (3.273207606004141-0.8681289535631749j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(12.0*w) + jay*sin(12.0*w))) - (3.62560990822190831193+0.0j) # exact value
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(12.0*w) + jay*sin(12.0*w))) - (3.6256099082219064+1.0757172979564068e-14j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(13.0*w) + jay*sin(13.0*w))) - (3.273207606004129+0.8681289535631883j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(14.0*w) + jay*sin(14.0*w))) - (2.6069417885981445+1.2221788440292174j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(15.0*w) + jay*sin(15.0*w))) - (2.06485696715464+1.1952844351348377j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(16.0*w) + jay*sin(16.0*w))) - (1.717428321436748+1.0312868278533498j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(17.0*w) + jay*sin(17.0*w))) - (1.508808161274129+0.8450869801594673j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(18.0*w) + jay*sin(18.0*w))) - (1.3851135919886712+0.6731815357597052j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(19.0*w) + jay*sin(19.0*w))) - (1.3121007739875803+0.5230804312358839j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(20.0*w) + jay*sin(20.0*w))) - (1.2696159881039117+0.3933623260432626j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(21.0*w) + jay*sin(21.0*w))) - (1.2457025092574734+0.2803188749547047j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(22.0*w) + jay*sin(22.0*w))) - (1.2330405110561218+0.17984413362423818j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(23.0*w) + jay*sin(23.0*w))) - (1.2271181171726906+0.08779977180512617j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(24.0*w) + jay*sin(24.0*w))) - (1.22541670246517764512+0.0j) # exact value
        ) < tolerance

    def test_gamma_spin_1(self) -> None:
        assert abs(
            gamma(o_one + r1*(cos(0.0*w) + jay*sin(0.0*w))) - (1.0+0.0j) # exact value
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(1.0*w) + jay*sin(1.0*w))) - (0.9593356187292527+0.100989596571918j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(2.0*w) + jay*sin(2.0*w))) - (0.8584348870350261+0.15261804612128704j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(3.0*w) + jay*sin(3.0*w))) - (0.7406061548328244+0.13797234921244877j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(4.0*w) + jay*sin(4.0*w))) - (0.6378792868876431+0.07028113503552197j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(5.0*w) + jay*sin(6.0*w))) - (0.5426813021403584-0.025765192834020706j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(6.0*w) + jay*sin(6.0*w))) - (0.4980156681183563-0.15494982830181075j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(7.0*w) + jay*sin(7.0*w))) - (0.44281828265598744-0.3083746180817264j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(8.0*w) + jay*sin(8.0*w))) - (0.3798048917913885-0.51727909947484j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(9.0*w) + jay*sin(9.0*w))) - (0.2923781628739807-0.8529300993652641j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(10.0*w) + jay*sin(10.0*w))) - (0.16374254765509025-1.5328842621021321j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(11.0*w) + jay*sin(11.0*w))) - (0.006473232712530961-3.5710506121287473j)
        ) < tolerance
        assert abs(gamma(o_one + r1*(cos(12.0*w) + jay*sin(12.0*w)))) > 1.0e+14
        assert abs(
            gamma(o_one + r1*(cos(13.0*w) + jay*sin(13.0*w))) - (0.006473232712523238+3.5710506121287615j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(14.0*w) + jay*sin(14.0*w))) - (0.16374254765507829+1.532884262102134j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(15.0*w) + jay*sin(15.0*w))) - (0.29237816287397383+0.8529300993652651j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(16.0*w) + jay*sin(16.0*w))) - (0.3798048917913894+0.5172790994748437j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(17.0*w) + jay*sin(17.0*w))) - (0.44281828265598894+0.30837461808172656j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(18.0*w) + jay*sin(18.0*w))) - (0.49801566811835635+0.15494982830181075j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(19.0*w) + jay*sin(19.0*w))) - (0.5591187415378688+0.030606251757081843j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(20.0*w) + jay*sin(20.0*w))) - (0.6378792868876437-0.07028113503552219j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(21.0*w) + jay*sin(21.0*w))) - (0.740606154832826-0.13797234921244983j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(22.0*w) + jay*sin(22.0*w))) - (0.8584348870350293-0.15261804612128943j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(23.0*w) + jay*sin(23.0*w))) - (0.9593356187292551-0.10098959657191953j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1*(cos(24.0*w) + jay*sin(24.0*w))) - (1.0) # exact value
        ) < tolerance

    def test_gamma_spin_1_J(self) -> None:
        assert abs(
            gamma(o_1_j + r*(cos(0.0*w) + jay*sin(0.0*w))) - (0.5414051834837496-0.03000467718476757j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(1.0*w) + jay*sin(1.0*w))) - (0.5092938355505581-0.024418800986080264j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(2.0*w) + jay*sin(2.0*w))) - (0.4772652647116792-0.026651256691286804j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(3.0*w) + jay*sin(3.0*w))) - (0.447158719329485-0.03620650021808021j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(4.0*w) + jay*sin(4.0*w))) - (0.4204379770772642-0.05215076121259929j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(5.0*w) + jay*sin(5.0*w))) - (0.3981067599211152-0.07339134160164619j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(6.0*w) + jay*sin(6.0*w))) - (0.38081556472957556-0.09892221417183164j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(7.0*w) + jay*sin(7.0*w))) - (0.3690874005681015-0.12793708659712544j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(8.0*w) + jay*sin(8.0*w))) - (0.3635711332716032-0.1597743239922937j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(9.0*w) + jay*sin(9.0*w))) - (0.3652398793897562-0.1936897459193419j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(10.0*w) + jay*sin(10.0*w))) - (0.3754384315354163-0.2284643465572309j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(11.0*w) + jay*sin(11.0*w))) - (0.3956321084757357-0.26190295364203714j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(12.0*w) + jay*sin(12.0*w))) - (0.42668350976193165-0.290440432211691j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(13.0*w) + jay*sin(13.0*w))) - (0.4676644198181886-0.3093301474115857j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(14.0*w) + jay*sin(14.0*w))) - (0.5147689472159721-0.3139411600874066j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(15.0*w) + jay*sin(15.0*w))) - (0.5614918921216788-0.3019826164627133j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(16.0*w) + jay*sin(16.0*w))) - (0.6007579287730999-0.2751570530155896j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(17.0*w) + jay*sin(17.0*w))) - (0.6277910177326999-0.23855686371283677j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(18.0*w) + jay*sin(18.0*w))) - (0.6414282163127023-0.19814088308428426j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(19.0*w) + jay*sin(19.0*w))) - (0.6431658367896469-0.15846417860535536j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(20.0*w) + jay*sin(20.0*w))) - (0.6353349031720246-0.12207985729384158j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(21.0*w) + jay*sin(21.0*w))) - (0.6199062369928965-0.09021544333720546j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(22.0*w) + jay*sin(22.0*w))) - (0.598280951767445-0.06367096853604087j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(23.0*w) + jay*sin(23.0*w))) - (0.5716499163382027-0.0433022667106068j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r*(cos(24.0*w) + jay*sin(24.0*w))) - (0.5414051834837496-0.03000467718476757j)
        ) < tolerance

    def test_gamma_spin_1_negJ(self) -> None:
        assert abs(
            gamma(o_1_nj + r*(cos(0.0*w) + jay*sin(0.0*w))) - (0.5414051834837496+0.030004677184767486j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-1.0*w) + jay*sin(-1.0*w))) - (0.5092938355505584+0.024418800986078876j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-2.0*w) + jay*sin(-2.0*w))) - (0.47726526471167957+0.026651256691286j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-3.0*w) + jay*sin(-3.0*w))) - (0.44715871932948537+0.03620650021807981j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-4.0*w) + jay*sin(-4.0*w))) - (0.4204379770772649+0.052150761212598484j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-5.0*w) + jay*sin(-5.0*w))) - (0.3981067599211154+0.07339134160164563j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-6.0*w) + jay*sin(-6.0*w))) - (0.3808155647295759+0.09892221417183107j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-7.0*w) + jay*sin(-7.0*w))) - (0.3690874005681027+0.12793708659712444j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-8.0*w) + jay*sin(-8.0*w))) - (0.3635711332716044+0.1597743239922923j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-9.0*w) + jay*sin(-9.0*w))) - (.3652398793897574+0.19368974591934138j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-10.0*w) + jay*sin(-10.0*w))) - (0.37543843153541806+0.22846434655723047j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-11.0*w) + jay*sin(-11.0*w))) - (0.39563210847573776+0.26190295364203614j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-12.0*w) + jay*sin(-12.0*w))) - (0.42668350976193176+0.29044043221169097j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-13.0*w) + jay*sin(-13.0*w))) - (0.46766441981818957+0.3093301474115855j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-14.0*w) + jay*sin(-14.0*w))) - (0.5147689472159731+0.31394116008740586j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-15.0*w) + jay*sin(-15.0*w))) - (0.56149189212168+0.3019826164627124j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-16.0*w) + jay*sin(-16.0*w))) - (0.6007579287731007+0.2751570530155888j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-17.0*w) + jay*sin(-17.0*w))) - (0.6277910177327026+0.23855686371283522j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-18.0*w) + jay*sin(-18.0*w))) - (0.6414282163127025+0.1981408830842841j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-19.0*w) + jay*sin(-19.0*w))) - (0.6431658367896502+0.15846417860535345j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-20.0*w) + jay*sin(-20.0*w))) - (0.6353349031720252+0.12207985729384013j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-21.0*w) + jay*sin(-21.0*w))) - (0.6199062369928978+0.09021544333720322j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-22.0*w) + jay*sin(-22.0*w))) - (0.5982809517674468+0.06367096853603893j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-23.0*w) + jay*sin(-23.0*w))) - (0.5716499163382038+0.043302266710605414j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r*(cos(-24.0*w) + jay*sin(-24.0*w))) - (0.5414051834837496+0.030004677184767486j)
        ) < tolerance
