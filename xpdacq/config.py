#!/usr/bin/env python
#!/usr/bin/env python
##############################################################################
#
# xpdacq            by Billinge Group
#                   Simon J. L. Billinge sb2896@columbia.edu
#                   (c) 2016 trustees of Columbia University in the City of
#                        New York.
#                   All rights reserved
#
# File coded by:    Timothy Liu, Simon Billinge
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
##############################################################################
'''Constants and other global definitions.
'''

import os.path

#from xpdacq.main_config import main_config

WORKING_DIR = 'xpdUser'
CONFIG_DIR = 'xpdConfig'

class DataPath(object):
    '''Absolute paths to data folders in XPD experiment.
    '''
    def __init__(self, stem):
        self.stem = stem
    
    @property
    def base(self):
        ''' base dir of entire configuration '''
        if self.stem == '~':
            return os.path.expanduser('~/' + WORKING_DIR)
        return os.path.join( self.stem, WORKING_DIR)
    @property
    def raw_config(self): 
        ''' config dir of entire configuration''' 
        if self.stem == '~':
            return os.path.expanduser('~/'+ CONFIG_DIR)
        return os.path.join( self.stem, CONFIG_DIR)

    @property
    def import_dir(self):
        "Folder for user/beamline scientist import."
        return os.path.join(self.base, 'Import')

    @property
    def export_dir(self):
        "Folder for user output."
        return os.path.join(self.base, 'Export')

    @property
    def tif(self):
        "Folder for saving tiff files."
        return os.path.join(self.base, 'tif_base')

    @property
    def dark(self):
        "Folder for saving dark tiff files."
        return os.path.join(self.base, 'dark_base')

    @property
    def config(self):
        "Folder for calibration files."
        return os.path.join(self.base, 'config_base')

    @property
    def script(self):
        "Folder for saving script files for the experiment."
        return os.path.join(self.base, 'script_base')

    @property
    def allfolders(self):
        "Return a list of all data folder paths for XPD experiment."
        rv = [
                self.base, self.raw_config, self.tif, self.dark, self.config,
                self.script, self.export_dir, self.import_dir
            ]
        return rv

# class DataPath

# unique instance of the DataPath class.
#datapath = DataPath(STEM)