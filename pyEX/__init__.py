# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from .common import (
    PyEXception,
    PyEXStopSSE,
    overrideUrl,
    setProxy,
)

from ._version import __version__
from .account import *
from .alternative import *
from .commodities import *
from .cryptocurrency import *
from .economic import *
from .files import *
from .fx import *
from .markets import *
from .metadata import *
from .mortgage import *
from .options import *
from .points import *
from .platform import *
from .premium import *
from .rates import *
from .refdata import *
from .rules import (
    createRule,
    deleteRule,
    lookupRule,
    ruleOutput,
    pauseRule,
    resumeRule,
    ruleInfo,
    rules,
)
from .stats import *
from .stocks import *
from .streaming.cryptocurrency import *
from .streaming.fx import *
from .streaming.news import *
from .streaming.sentiment import *
from .streaming.sse import *
from .streaming.stock import *
from .streaming.ws import *
from .timeseries import *
from .treasuries import *

from .client import *  # noqa: F403
from .studies import *  # noqa: F403

try:
    from .caching import *
except ImportError:
    pass

try:
    from .zipline import *
except ImportError:
    pass
