# invenio-subjects-ddc

DDC subject terms for InvenioRDM

Install this extension to get the german [Dewey Decimal Classification](https://www.dnb.de/ddcuebersichten) into your instance.

## Installation

From your instance directory:

    pipenv install invenio-subjects-ddc-german

This will add it to your Pipfile.

### Versions

This repository follows [calendar versioning](https://calver.org/):

`2021.06.18` is both a valid semantic version and an indicator of the year-month corresponding to the loaded DDC terms.


## Usage

There are 2 types of users for this package. Maintainers of the package and instance administrators.

### Instance administrators

For instance administrators, after you have installed the extension as per the steps above, you are done. It should just work.

### TODO -- Maintainers

When a new list of DDC term comes out, this package should be updated. Here we show how.

0- Make sure you have cloned this package. Then install it locally with:

    make install

1- Update:

    make update

   This will

   1- Download the new list
   2- Convert terms to InvenioRDM subjects format
   3- Write those to `invenio_subjects_ddc_german/vocabularies/subjects_ddc_german.yaml` file

3- Run the tests just to make sure everything is still good:

    make test

4- When you are happy with the list, bump the version in `invenio_subjects_ddc_german/version.py` and release it.


## Future Ideas

- InvenioRDM doesn't have a way to update pre-existing subjects yet. Once there is one,
  this package should provide the functionality to update GND subject terms.
