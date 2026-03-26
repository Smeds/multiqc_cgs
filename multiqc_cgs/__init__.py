#!/usr/bin/env python

from importlib.metadata import version
from multiqc import config

__version__ = version("multiqc_cgs")
config.multiqc_cgs_version = __version__
