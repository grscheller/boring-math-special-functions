CHANGELOG
=========

PyPI boring-math-special-functions project.

Semantic Versioning
-------------------

Strict 3 digit semantic versioning.

- **MAJOR** version incremented for incompatible API changes
- **MINOR** version incremented for backward compatible added functionality
- **PATCH** version incremented for backward compatible bug fixes

See `Semantic Versioning 2.0.0 <https://semver.org>`_.

Releases and Important Milestones
---------------------------------

Update - 2025-09-29
~~~~~~~~~~~~~~~~~~~

Redoing entire project's infrastructure along the lines of ``pythonic-fp``.

- update code

  - no code changes needed for updated version of Pythonic FP
  - removed all ``from __future__ import annotation`` from the code

    - made the necessary typing changes to accomplish this
    - should not require a bump in major version

- created a Sphinx based homepage for the overall Boring Math effort

  - still need to update to Sphinx the individual Boring Math PyPI projects
  - still need to plumb in the old pdoc documentation

PyPI 1.1.3 - 2025-08-04
~~~~~~~~~~~~~~~~~~~~~~~

Created a second changelog, this one in Markdown, for the special
functions effort. So far it is just an `__init__.py` file with
documentation for things I have not yet written.

PyPI 1.1.0 - 2025-08-03
~~~~~~~~~~~~~~~~~~~~~~~

Decided to create a special functions project and put it in the base
boring-math repo. Its version number will mirror, if not drive, the
version number for the overall Boring Math effort.

