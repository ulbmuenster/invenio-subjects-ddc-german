# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Northwestern University.
# Copyright (C) 2022 University of Münster.
#
# invenio-subjects-ddc-german is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""DDC term converter."""


class DDCConverter:
    """Convert DDC term into subject dict for YAML writing."""

    def __init__(self, reader):
        """Constructor."""
        self._reader = reader

    def generate_id(self, identifier):
        """Generate URI id."""
        return f"https://www.dnb.de/ddcuebersichten/{identifier}"

    def __iter__(self):
        """Iterate over converted entries."""
        for term in self._reader:
            yield {
                "id": self.generate_id(term['UI']),
                "scheme": "DDC",
                "subject": term['MH']
            }
