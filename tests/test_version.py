#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of easy-drf.
# https://github.com/talp101/easy-drf.git

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Tal Peretz <13@1500.co.il>
from easy_drf import __version__
from unittest import TestCase



class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        self.assertEqual(__version__, '0.1.0')
