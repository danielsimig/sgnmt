"""Redirect to cam.sgnmt.blocks.align """

import sys
import os
import inspect

sys.path.insert(0, "%s/cam/sgnmt/blocks"
   % os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

import cam.sgnmt.blocks.align
