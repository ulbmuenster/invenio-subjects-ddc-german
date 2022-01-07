# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Northwestern University.
# Copyright (C) 2022 University of Münster.
#
# invenio-subjects-ddc-german is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Command line tool."""

import click

from .converter import DDCConverter
from .download import download_ddc
from .reader import DDCReader
from .writer import write_yaml


@click.command()
def main():
    """Generate new subjects_ddc.yaml file."""
    filepath = download_ddc()

    reader = DDCReader(filepath, filter='topics')

    converter = DDCConverter(reader)

    filepath = write_yaml(converter)

    print(f"DDC terms written here {filepath}")
