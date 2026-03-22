# CHANGELOG

PyPI boring-math-special-functions project.

## Semantic Versioning

Strict 3 digit semantic versioning.

- **MAJOR** version incremented for incompatible API changes
- **MINOR** version incremented for backward compatible added functionality
- **PATCH** version incremented for backward compatible bug fixes

See [Semantic Versioning 2.0.0](https://semver.org).

## Releases and Important Milestones

### PyPI Release 4.0.0 - TBD

Added the beta function

- implemented with gamma function
- correctly handles singularities and canceling poles
- using `inf + infj` to represent complex infinity
  - in complex analysis all of these are the same: `inf+infj`,
    `inf-infj`, `-inf+infj`, `-inf-infj`, `inf`, `-inf`
  - in Python all are distinct values, there is no concept of
    a single valued complex infinity
  
### PyPI Release 3.0.0 - 2026-03-03

Breaking API changes.

- improved trig function names leading to better docs

### PyPI Release 2.0.0 - 2026-03-02

Breaking API changes.

- broke out exponential functions to their own module
- added gamma function module

### PyPI Release 1.0.0 - 2026-02-25

Finished and tested:

- float0.exp0, float0.sin0, complex0.cos0, complex0.tan0
- float.exp, float.sin, complex.cos, complex.tan

### PyPI Release 0.2.0 - 2026-02-19

Added exp0 partially factored Taylor expansion about `x = 0.0`.

### Update - 2026-02-18

Added sin0, cos0 partially factored Taylor expansion about `x = 0.0`,
also `tan0(x) = sin0(x)/cos0(x)`.

### Update - 2025-10-04

Creating Sphinx based documentation for this "stub" project. Converted
this CHANGELOG file back to Markdown from reStructured text so it is in
agreement with the other Boring Math PyPI projects.

### Update - 2025-09-29

Broke boring-math-special-functions out to its own GitHub repo and future
PyPI project, like I did for pythonic-fp-gadgets. Project just a stub.

### Update - 2025-09-29

Redoing entire project's infrastructure along the lines of `pythonic-fp`.

- update code
  - no code changes needed for updated version of Pythonic FP
  - removed all `from __future__ import annotation` from the code
    - made the necessary typing changes to accomplish this
    - should not require a bump in major version
- created a Sphinx based homepage for the overall Boring Math effort
  - still need to update to Sphinx the individual Boring Math PyPI projects
  - still need to plumb in the old pdoc documentation

### Update - 2025-08-03

Decided to create a special functions project and put it in the base
boring-math repo.
