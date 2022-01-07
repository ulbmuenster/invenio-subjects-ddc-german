#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Northwestern University.
# Copyright (C) 2022 University of Münster.
#
# invenio-subjects-ddc-german is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.


# Quit on errors
set -o errexit

# Quit on unbound symbols
set -o nounset

python -m check_manifest
python -m pytest
tests_exit_code=$?
exit "$tests_exit_code"
