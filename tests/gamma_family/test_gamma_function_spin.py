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

jay = 0.0+1.0j
infinity = inf + jay*inf
o_pt5 = 0.5+0.0j
o_one = 1.0+0.0j
o_zero = 0.0+0.0j
o_1_j = 1.0+1.0j
o_1_nj = 1.0-1.0j
r0_25 = 0.25
r0_50 = 0.5
r1_00 = 1.0
w = 2.0*pi/24.0

tolerance = 2.0e-14

class Test_gamma_shift_explore:
    def test_gamma_spin_pt5(self) -> None:
        assert abs(
            gamma(o_pt5 + r0_25*(cos(0.0*w) + jay*sin(0.0*w))) - (1.22541670246518+0.0j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(1.0*w) + jay*sin(1.0*w))) - (1.22711811717269-0.08779977180513j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(2.0*w) + jay*sin(2.0*w))) - (1.23304051105612-0.17984413362424j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(3.0*w) + jay*sin(3.0*w))) - (1.24570250925746-0.28031887495470j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(4.0*w) + jay*sin(4.0*w))) - (1.26961598810390-0.39336232604326j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(5.0*w) + jay*sin(6.0*w))) - (1.29634376533956-0.53443439392667j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(6.0*w) + jay*sin(6.0*w))) - (1.38511359198866-0.67318153575970j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(7.0*w) + jay*sin(7.0*w))) - (1.50880816127413-0.84508698015946j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(8.0*w) + jay*sin(8.0*w))) - (1.71742832143675-1.03128682785334j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(9.0*w) + jay*sin(9.0*w))) - (2.06485696715463-1.19528443513481j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(10.0*w) + jay*sin(10.0*w))) - (2.60694178859814-1.22217884402920j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(11.0*w) + jay*sin(11.0*w))) - (3.27320760600414-0.86812895356317j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(12.0*w) + jay*sin(12.0*w))) - (3.62560990822191+0.0j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(12.0*w) + jay*sin(12.0*w))) - (3.62560990822191+1.07571729795641e-14j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(13.0*w) + jay*sin(13.0*w))) - (3.27320760600413+0.86812895356319j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(14.0*w) + jay*sin(14.0*w))) - (2.60694178859814+1.22217884402922j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(15.0*w) + jay*sin(15.0*w))) - (2.06485696715464+1.19528443513484j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(16.0*w) + jay*sin(16.0*w))) - (1.71742832143675+1.03128682785335j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(17.0*w) + jay*sin(17.0*w))) - (1.50880816127413+0.84508698015947j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(18.0*w) + jay*sin(18.0*w))) - (1.38511359198867+0.67318153575971j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(19.0*w) + jay*sin(19.0*w))) - (1.31210077398758+0.52308043123588j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(20.0*w) + jay*sin(20.0*w))) - (1.26961598810391+0.39336232604326j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(21.0*w) + jay*sin(21.0*w))) - (1.24570250925747+0.28031887495470j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(22.0*w) + jay*sin(22.0*w))) - (1.23304051105612+0.17984413362424j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(23.0*w) + jay*sin(23.0*w))) - (1.22711811717269+0.08779977180513j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r0_25*(cos(24.0*w) + jay*sin(24.0*w))) - (1.225416702465182+0.0j)
        ) < tolerance

    def test_gamma_spin_zero(self) -> None:
        assert abs(
            gamma(o_zero + r0_50*(cos(0.0*w) + jay*sin(0.0*w))) - pi**(0.5) # exact value
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(0.0*w) + jay*sin(0.0*w))) - (1.77245385090552)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(1.0*w) + jay*sin(1.0*w))) - (1.69904697012812-0.44988584324344j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(2.0*w) + jay*sin(2.0*w))) - (1.48401359389367-0.86597022187927j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(3.0*w) + jay*sin(3.0*w))) - (1.14215304043747-1.21581769241446j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(4.0*w) + jay*sin(4.0*w))) - (0.69586577337200-1.47012131722367j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(5.0*w) + jay*sin(6.0*w))) - (0.14678861522090-1.5394571214677j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(6.0*w) + jay*sin(6.0*w))) - (-0.39927947632919-1.60338819413943j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(7.0*w) + jay*sin(7.0*w))) - (-0.99266636075522-1.45897058446985j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(8.0*w) + jay*sin(8.0*w))) - (-1.58871742812200-1.17832670664320j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(9.0*w) + jay*sin(9.0*w))) - (-2.18118034234529-0.79136544763522j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(10.0*w) + jay*sin(10.0*w))) - (-2.77041463897469-0.37503633321176j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(11.0*w) + jay*sin(11.0*w))) - (-3.30160176216280-0.07794834036828j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(12.0*w) + jay*sin(12.0*w))) - (pi**(0.5)/(-0.5)) # exact value
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(12.0*w) + jay*sin(12.0*w))) - (-3.54490770181103)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(13.0*w) + jay*sin(13.0*w))) - (-3.30160176216282+0.07794834036828j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(14.0*w) + jay*sin(14.0*w))) - (-2.77041463897471+0.37503633321174j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(15.0*w) + jay*sin(15.0*w))) - (-2.18118034234531+0.79136544763521j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(16.0*w) + jay*sin(16.0*w))) - (-1.58871742812202+1.17832670664320j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(17.0*w) + jay*sin(17.0*w))) - (-0.99266636075523+1.45897058446985j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(18.0*w) + jay*sin(18.0*w))) - (-0.39927947632920+1.60338819413944j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(19.0*w) + jay*sin(19.0*w))) - (0.17241886223654+1.60483760884022j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(20.0*w) + jay*sin(20.0*w))) - (0.69586577337199+1.47012131722368j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(21.0*w) + jay*sin(21.0*w))) - (1.14215304043747+1.21581769241448j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(22.0*w) + jay*sin(22.0*w))) - (1.48401359389368+0.86597022187930j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(23.0*w) + jay*sin(23.0*w))) - (1.69904697012813+0.44988584324345j)
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(24.0*w) + jay*sin(24.0*w))) - pi**(0.5) # exact value
        ) < tolerance
        assert abs(
            gamma(o_zero + r0_50*(cos(24.0*w) + jay*sin(24.0*w))) - (1.77245385090552)
        ) < tolerance

    def test_gamma_spin_1(self) -> None:
        assert abs(
            gamma(o_one + r1_00*(cos(0.0*w) + jay*sin(0.0*w))) - (1.0+0.0j) # exact value
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(1.0*w) + jay*sin(1.0*w))) - (0.95933561872925+0.1009895965719j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(2.0*w) + jay*sin(2.0*w))) - (0.85843488703503+0.15261804612129j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(3.0*w) + jay*sin(3.0*w))) - (0.74060615483282+0.13797234921245j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(4.0*w) + jay*sin(4.0*w))) - (0.63787928688764+0.07028113503552j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(5.0*w) + jay*sin(6.0*w))) - (0.54268130214036-0.02576519283402j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(6.0*w) + jay*sin(6.0*w))) - (0.49801566811836-0.15494982830181j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(7.0*w) + jay*sin(7.0*w))) - (0.44281828265599-0.30837461808173j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(8.0*w) + jay*sin(8.0*w))) - (0.37980489179139-0.51727909947484j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(9.0*w) + jay*sin(9.0*w))) - (0.29237816287398-0.85293009936526j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(10.0*w) + jay*sin(10.0*w))) - (0.16374254765509-1.53288426210213j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(11.0*w) + jay*sin(11.0*w))) - (0.00647323271253-3.57105061212875j)
        ) < tolerance
        assert abs(gamma(o_one + r1_00*(cos(12.0*w) + jay*sin(12.0*w)))) > 1.0e+14
        assert abs(
            gamma(o_one + r1_00*(cos(13.0*w) + jay*sin(13.0*w))) - (0.00647323271252+3.57105061212876j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(14.0*w) + jay*sin(14.0*w))) - (0.16374254765508+1.53288426210213j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(15.0*w) + jay*sin(15.0*w))) - (0.29237816287397+0.85293009936527j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(16.0*w) + jay*sin(16.0*w))) - (0.37980489179139+0.51727909947484j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(17.0*w) + jay*sin(17.0*w))) - (0.44281828265599+0.30837461808173j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(18.0*w) + jay*sin(18.0*w))) - (0.49801566811836+0.15494982830181j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(19.0*w) + jay*sin(19.0*w))) - (0.55911874153787+0.03060625175708j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(20.0*w) + jay*sin(20.0*w))) - (0.63787928688764-0.07028113503552j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(21.0*w) + jay*sin(21.0*w))) - (0.74060615483283-0.13797234921245j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(22.0*w) + jay*sin(22.0*w))) - (0.85843488703503-0.15261804612129j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(23.0*w) + jay*sin(23.0*w))) - (0.95933561872926-0.10098959657192j)
        ) < tolerance
        assert abs(
            gamma(o_one + r1_00*(cos(24.0*w) + jay*sin(24.0*w))) - (1.0) # exact value
        ) < tolerance

    def test_gamma_spin_1_J(self) -> None:
        assert abs(
            gamma(o_1_j + r0_25*(cos(0.0*w) + jay*sin(0.0*w))) - (0.54140518348375-0.03000467718477j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(1.0*w) + jay*sin(1.0*w))) - (0.50929383555056-0.02441880098608j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(2.0*w) + jay*sin(2.0*w))) - (0.47726526471168-0.02665125669129j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(3.0*w) + jay*sin(3.0*w))) - (0.44715871932949-0.03620650021808j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(4.0*w) + jay*sin(4.0*w))) - (0.42043797707726-0.05215076121260j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(5.0*w) + jay*sin(5.0*w))) - (0.39810675992112-0.07339134160165j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(6.0*w) + jay*sin(6.0*w))) - (0.38081556472958-0.09892221417183j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(7.0*w) + jay*sin(7.0*w))) - (0.36908740056810-0.12793708659713j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(8.0*w) + jay*sin(8.0*w))) - (0.36357113327160-0.15977432399229j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(9.0*w) + jay*sin(9.0*w))) - (0.36523987938976-0.19368974591934j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(10.0*w) + jay*sin(10.0*w))) - (0.37543843153542-0.22846434655723j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(11.0*w) + jay*sin(11.0*w))) - (0.39563210847574-0.26190295364204j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(12.0*w) + jay*sin(12.0*w))) - (0.42668350976193-0.29044043221169j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(13.0*w) + jay*sin(13.0*w))) - (0.46766441981819-0.30933014741159j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(14.0*w) + jay*sin(14.0*w))) - (0.51476894721597-0.31394116008741j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(15.0*w) + jay*sin(15.0*w))) - (0.56149189212168-0.30198261646271j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(16.0*w) + jay*sin(16.0*w))) - (0.60075792877310-0.27515705301559j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(17.0*w) + jay*sin(17.0*w))) - (0.62779101773270-0.23855686371284j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(18.0*w) + jay*sin(18.0*w))) - (0.64142821631270-0.19814088308428j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(19.0*w) + jay*sin(19.0*w))) - (0.64316583678965-0.15846417860536j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(20.0*w) + jay*sin(20.0*w))) - (0.63533490317202-0.12207985729384j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(21.0*w) + jay*sin(21.0*w))) - (0.61990623699290-0.09021544333721j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(22.0*w) + jay*sin(22.0*w))) - (0.59828095176745-0.06367096853604j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(23.0*w) + jay*sin(23.0*w))) - (0.57164991633820-0.04330226671061j)
        ) < tolerance
        assert abs(
            gamma(o_1_j + r0_25*(cos(24.0*w) + jay*sin(24.0*w))) - (0.54140518348375-0.03000467718477j)
        ) < tolerance

    def test_gamma_spin_1_negJ(self) -> None:
        assert abs(
            gamma(o_1_nj + r0_25*(cos(0.0*w) + jay*sin(0.0*w))) - (0.54140518348375+0.03000467718477j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-1.0*w) + jay*sin(-1.0*w))) - (0.50929383555056+0.02441880098608j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-2.0*w) + jay*sin(-2.0*w))) - (0.47726526471168+0.02665125669129j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-3.0*w) + jay*sin(-3.0*w))) - (0.44715871932949+0.03620650021808j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-4.0*w) + jay*sin(-4.0*w))) - (0.42043797707726+0.05215076121260j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-5.0*w) + jay*sin(-5.0*w))) - (0.39810675992112+0.07339134160165j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-6.0*w) + jay*sin(-6.0*w))) - (0.38081556472958+0.09892221417183j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-7.0*w) + jay*sin(-7.0*w))) - (0.36908740056810+0.12793708659712j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-8.0*w) + jay*sin(-8.0*w))) - (0.36357113327160+0.15977432399229j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-9.0*w) + jay*sin(-9.0*w))) - (.36523987938976+0.19368974591934j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-10.0*w) + jay*sin(-10.0*w))) - (0.37543843153542+0.22846434655723j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-11.0*w) + jay*sin(-11.0*w))) - (0.39563210847574+0.26190295364204j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-12.0*w) + jay*sin(-12.0*w))) - (0.42668350976193+0.29044043221169j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-13.0*w) + jay*sin(-13.0*w))) - (0.46766441981819+0.30933014741159j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-14.0*w) + jay*sin(-14.0*w))) - (0.51476894721597+0.31394116008741j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-15.0*w) + jay*sin(-15.0*w))) - (0.56149189212168+0.30198261646271j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-16.0*w) + jay*sin(-16.0*w))) - (0.60075792877310+0.27515705301559j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-17.0*w) + jay*sin(-17.0*w))) - (0.62779101773270+0.23855686371284j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-18.0*w) + jay*sin(-18.0*w))) - (0.64142821631270+0.19814088308428j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-19.0*w) + jay*sin(-19.0*w))) - (0.64316583678965+0.15846417860535j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-20.0*w) + jay*sin(-20.0*w))) - (0.63533490317203+0.12207985729384j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-21.0*w) + jay*sin(-21.0*w))) - (0.61990623699290+0.09021544333720j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-22.0*w) + jay*sin(-22.0*w))) - (0.59828095176745+0.06367096853604j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-23.0*w) + jay*sin(-23.0*w))) - (0.57164991633820+0.04330226671061j)
        ) < tolerance
        assert abs(
            gamma(o_1_nj + r0_25*(cos(-24.0*w) + jay*sin(-24.0*w))) - (0.54140518348375+0.03000467718477j)
        ) < tolerance
