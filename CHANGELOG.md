# Release notes

<!-- do not remove -->

## 0.0.2

### New Features

- Modify the TeX exception patterns with add_exception, rm_exception ([#2](https://github.com/jkseppan/shyster/issues/2))

### Bugs Squashed

- The regex idea didn't quite work, using tries instead ([#3](https://github.com/jkseppan/shyster/issues/3))
  - Given the rules `pu2t` and `5pute`, the hyphenator matched only one of them in the word `computer`.

- Exceptions always used `-` and not the specified hyphen character 
([#1](https://github.com/jkseppan/shyster/issues/1))


## 0.0.1

Initial release; trying out nbdev.

