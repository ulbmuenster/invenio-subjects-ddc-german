# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Northwestern University.
# Copyright (C) 2022 University of Münster.
#
# invenio-subjects-ddc-german is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Download DDC file."""

import shutil
from pathlib import Path

import requests


def download_ddc():
    """Download DDC file."""
    url = "https://www.dnb.de/ddcuebersichten"
    filename = url.rsplit('/', 1)[-1]
    filepath = Path(__file__).parent / filename

    with requests.get(url, stream=True) as req:
        with open(filepath, 'wb') as f:
            shutil.copyfileobj(req.raw, f)

    return filepath
