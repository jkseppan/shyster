# Release notes

<!-- do not remove -->

## 0.0.3

### New Features

- Find longest words in html document ([#6](https://github.com/jkseppan/shyster/issues/6))
  - To help build the exception list

- Specify exceptions with wildcards ([#4](https://github.com/jkseppan/shyster/issues/4))
  - Because of Finnish declension, the compound word `saippuakauppias` generates `saippuakauppiaan`, `saippuakauppiaiden`, `saippuakauppiainensa`, etc, and I would like to make all of them only break at the compound border. Almost all of the declension happens at the end of the word, so being able to specify `saippua-kaupp*` as an exception would cover the cases sufficiently.

### Bugs Squashed

- Should be case-insensitive ([#7](https://github.com/jkseppan/shyster/issues/7))
  - But retain case. Probably fine to not hyphenate CamelCase words but Titlecase ones should be hyphenated and the title-casing retained.


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

