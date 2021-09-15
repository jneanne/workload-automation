#    Copyright 2017-2018 ARM Limited
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
#

from devlib import BaylibreAcmeNetworkInstrument as _Instrument

from wa import Instrument, Parameter, hostside
from wa.framework.instrument import fast, slow, very_fast, very_slow
from wa.utils.types import (list_of_strings, list_of_ints, list_or_string,
                            obj_dict, identifier, list_of_numbers)

import time

ACME_IP_ADDR = "baylibre-acme-ptec-jn.local"

class ADBconnect(Instrument):
    name = 'adb'

    description = """
    TBD
    """
    parameters = [
        Parameter('hostname', kind=str, default="baylibre-acme-ptec-jn.local",
                  description="""
                  The acme device network name.
                  """),
        Parameter('probe_names', kind=list_or_string, default=['1', '2', '3'],
                  description="""
                  The baud-rate to use when connecting to the serial connection.
                  """),
    ]

    def __init__(self, target, **kwargs):
        super(ADBconnect, self).__init__(target, **kwargs)
        self.instrument = _Instrument(target, self.hostname, self.probe_names)

    def adb_disconnect(self, context):
        self.instrument.probe_sw_off('3')

    def adb_connect(self, context):
        self.instrument.probe_sw_on('3')

    #def initialize(self, context):  # pylint: disable=unused-argument
        #self.instrument = _Instrument(self.target, hostname=ACME_IP_ADDR,
        #                                    probe_names=['1', '2', '3'])
        #self.context = '3'
        #self.instrument = _Instrument(self.target, hostname=ACME_IP_ADDR,
        #                                    probe_names=['battery', 'soc', 'usb'])

    #def get_instruments(self, target, hostname,
    #                    probe_names):

        #
        #

    #    ret = {}
    #    for probe in probe_names:
    #        ret[probe] = _Instrument(target, hostname=ACME_IP_ADDR, probe_names=['1', '2', '3'])
    #    return ret

    def setup(self, context):  # pylint: disable=unused-argument
        #pass
        self.instrument.reset()
        #self.instrument.probe_sw_on('3')

    @very_slow
    def start(self, context):  # pylint: disable=unused-argument
        pass
        #time.sleep(1)
        #self.before = self.instrument.probe_sw_off('3')
        #self.instrument.probe_sw_off('3')

    @very_slow
    #def on_run_start(self, context):  # pylint: disable=unused-argument
    def on_job_start(self, context):  # pylint: disable=unused-argument
        self.adb_disconnect(context)
        #time.sleep(1)
        #self.instrument.probe_sw_off('3')

    @very_fast
    def on_job_end(self, context):  # pylint: disable=unused-argument
        self.adb_connect(context)
        #time.sleep(1)
        #self.instrument.probe_sw_off('3')

    def before_processing_job_output(self, context):  # pylint: disable=unused-argument
        self.adb_connect(context)
    @very_fast
    def stop(self, context):  # pylint: disable=unused-argument
        #self.after = self.instrument.probe_sw_on('3')
        #self.instrument.probe_sw_on('3')
        self.adb_connect(context)

    def teardown(self, context):  # pylint: disable=unused-argument
        #self.instrument.probe_sw_on('3')
        self.adb_connect(context)
        self.instrument.teardown()

    #@hostside
    #def on_error(self, context):  # pylint: disable=unused-argument
    #    self.adb_connect(context)

