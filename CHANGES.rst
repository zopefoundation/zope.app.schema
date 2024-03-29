=========
 CHANGES
=========

5.1 (unreleased)
================

- Nothing changed yet.


5.0 (2023-02-07)
================

- Drop support for Python 2.7, 3.5, 3.6.

- Add support for Python 3.7, 3.8, 3.9, 3.10, 3.11.


4.1.0 (2017-05-10)
==================

- Replaced the local implementation of ``ZopeVocabularyRegistry`` with
  one imported from ``zope.vocabularyregistry``. Backwards
  compatibility imports remain.


4.0.1 (2017-05-10)
==================

- Packaging: Add the Python version and implementation classifiers.


4.0.0 (2017-04-17)
==================

- Support for Python 3.5, 3.6 and PyPy has been added.

- Added support for tox.

- Drop dependency on ``zope.app.testing``, since it was not needed.


3.6.0 (2017-04-17)
==================

- Package modernization including manifest.


3.5.0 (2008-12-16)
==================

- Remove deprecated ``vocabulary`` directive.
- Add test for component-based vocabulary registry.


3.4.0 (2007-10-27)
==================

- Initial release independent of the main Zope tree.
