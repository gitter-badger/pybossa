# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2014 SF Isle of Man Limited
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa.  If not, see <http://www.gnu.org/licenses/>.
"""This module tests the Uploader class."""

from base import web, model, Fixtures, db, redis_flushall
from pybossa.uploader import Uploader


class TestUploader:

    """Test PyBossa Uploader module."""

    def setUp(self):
        """SetUp method."""
        self.app = web.app.test_client()
        model.rebuild_db()
        redis_flushall()
        Fixtures.create()

    def tearDown(self):
        """Tear Down method."""
        db.session.remove()
        redis_flushall()

    @classmethod
    def teardown_class(cls):
        """Tear Down class."""
        model.rebuild_db()
        redis_flushall()

    def test_uploader_init(self):
        """Test UPLOADER init method works."""
        u = Uploader()
        new_extensions = set(['pdf', 'doe'])
        new_uploader = Uploader(new_extensions)
        expected_extensions = set.union(u.allowed_extensions, new_extensions)
        err_msg = "The new uploader should support two extra extensions"
        assert expected_extensions == new_uploader.allowed_extensions, err_msg
