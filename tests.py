#!/usr/local/bin/python3

# Copyright 2015-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE-examples file in the root directory of this source tree.

""" Test cases
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
import unittest

import nanog_demo_better


class TestCases(unittest.TestCase):
    SYSLOG_MSG_INTERFACE_REMOVED = (
        '2015 May 18 12:43:15 switch2 %ETHPORT-5-IF_DOWN_LINK_FAILURE: '
        'Interface Ethernet1/4 is down (Link failure)')

    def test_syslog_regex(self):
        matched = re.match(
            nanog_demo_better.SYSLOG_RE, self.SYSLOG_MSG_INTERFACE_REMOVED)
        assert bool(matched) is True, 'Regular expression matching failed!'


if __name__ == '__main__':
    unittest.main()
