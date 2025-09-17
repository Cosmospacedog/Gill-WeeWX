from io import StringIO
import configobj

from weecfg.extension import ExtensionInstaller

def loader():
    return GillInstaller()

GILL_CONFIG = """
##############################################################################

[Gill]
    # This section is for the Gill MetConnect series of weather stations

    # Connection type: serial or ethernet
    # serial (via a com port or tty USB device)
    # ethernet (via a TCP connection i.e a MOXA or DIGI device port)
    type = ethernet

    # Internal IPV4 adress of the weather station
    eth_address = x.x.x.x

    # port your Gill device operates on - typically 4001 for a tcp connection
    eth_port = 4001

    gill_config = /x/x/config.mcf
    ###############################################################
    #  Advanced Config

    sample_rate = 1

    driver = user.gill
"""

gill_config_dict = configobj.ConfigObj(StringIO(GILL_CONFIG))

class GillInstaller(ExtensionInstaller):
    def __init__(self):
        super(GillInstaller,self).__init__(
            name='gill',
            version='1.3',
            description='WeewX driver for Gill MetConnect Stations.',
            author='Alex Burnett',
            author_email='support@siriusinsight.ai',
            files=[
                ('bin/user',[
                    'bin/user/gill.py',
                ])
            ],
            config=gill_config_dict
        )