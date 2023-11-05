# SPDX-FileCopyrightText: 2023-present Bernard Cooke <bernard-cooke@hotmail.com>
#
# SPDX-License-Identifier: MIT

import pytest

from psr_692 import hello_world


def test_hello_world():
    hello_world()
