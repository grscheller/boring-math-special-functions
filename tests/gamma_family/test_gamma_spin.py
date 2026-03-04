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

from math import pi
from boring_math.special_functions.trig import cos, sin
from boring_math.special_functions.gamma import gamma

tolerance = 5.0e-14

jay = 0.0+1.0j
o_pt5 = 0.5+0.0j
o_one = 1.0+0.0j
o_1_j = 1.0+1.0j
r = 0.25
w = 2*pi/24

class Test_gamma_shift_explore:
    def test_gamma_spin_pt5(self) -> None:
        assert abs(
            gamma(o_pt5 + r*(cos(0.00*w) + jay*sin(0.00*w))) - (1.22541670246517764512+0.0j) # exact value
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(1.00*w) + jay*sin(1.00*w))) - (1.2271181171726913-0.08779977180512569j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(2.00*w) + jay*sin(2.00*w))) - (1.2330405110561171-0.1798441336242378j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(3.00*w) + jay*sin(3.00*w))) - (1.2457025092574627-0.2803188749547032j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(4.00*w) + jay*sin(4.00*w))) - (1.2696159881039049-0.3933623260432612j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(5.00*w) + jay*sin(6.00*w))) - (1.2963437653395615-0.5344343939266745j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(6.00*w) + jay*sin(6.00*w))) - (1.3851135919886597-0.6731815357596991j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(7.00*w) + jay*sin(7.00*w))) - (1.5088081612741266-0.8450869801594573j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(8.00*w) + jay*sin(8.00*w))) - (1.7174283214367463-1.0312868278533385j)
        ) < tolerance
        assert abs(
            gamma(o_pt5 + r*(cos(9.00*w) + jay*sin(9.00*w))) - (2.064856967154628-1.1952844351348146j)
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
