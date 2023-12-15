<!-- Header -->
<div id="top" align="center">
  <br />

  <!-- Logo -->
  <img src="https://git.zakscode.com/repo-avatars/002f97340c2781ccfa5d09fde97403fd499c39a9ad5675dc0edf05a8396e9ac5" alt="Logo" width="200" height="200">

  <!-- Title -->
  ### py-bar

  <!-- Description -->
  Python ASCII Progress Bar

  <!-- Repo badges -->
  [![Version](https://img.shields.io/badge/dynamic/json.svg?label=Version&style=for-the-badge&url=https://git.zakscode.com/api/v1/repos/ztimson/py-bar/tags&query=$[0].name)](https://git.zakscode.com/ztimson/py-bar/tags)
  [![Pull Requests](https://img.shields.io/badge/dynamic/json.svg?label=Pull%20Requests&style=for-the-badge&url=https://git.zakscode.com/api/v1/repos/ztimson/py-bar&query=open_pr_counter)](https://git.zakscode.com/ztimson/py-bar/pulls)
  [![Issues](https://img.shields.io/badge/dynamic/json.svg?label=Issues&style=for-the-badge&url=https://git.zakscode.com/api/v1/repos/ztimson/py-bar&query=open_issues_count)](https://git.zakscode.com/ztimson/py-bar/issues)

  <!-- Links -->

  ---
  <div>
    <a href="https://git.zakscode.com/ztimson/py-bar/releases" target="_blank">Release Notes</a>
    • <a href="https://git.zakscode.com/ztimson/py-bar/issues/new?template=.github%2fissue_template%2fbug.md" target="_blank">Report a Bug</a>
    • <a href="https://git.zakscode.com/ztimson/py-bar/issues/new?template=.github%2fissue_template%2fenhancement.md" target="_blank">Request a Feature</a>
  </div>

  ---
</div>

## Table of Contents
- [py-bar](#top)
    - [About](#about)
       - [Built With](#built-with)
    - [Setup](#setup)
       - [Production](#production)
    - [Documentation](#documentation)
    - [License](#license)

## About

Python CLI Progress bar. This module is an iterator that can not only, iterate, but display its self as a progressbar along with some other usefull iformation such as iterations a second, estimated time, elapsed time, etc.

`00:25 100% [====================] [100/100] 3.99/s 00:00`

### Built With
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python)](https://www.python.org/)

## Setup

<details>
<summary>
  <h3 id="production" style="display: inline">
    Production
  </h3>
</summary>

#### Prerequisites
- [Python](https://www.python.org/downloads/)

#### Instructions
1. Download and add script to project: `curl https://git.zakscode.com/ztimson/py-bar/raw/branch/develop/progressbar.py`
2. Use in python script:

```python
from progressbar import Progressbar

for i in Progressbar(100):
    ...

# OR

progress = Progressbar(100, display=False) # Output manually
for i in progress:
    print(str(progress)) # Print progress bar
    ...
```

</details>

## Documentation

### Progressbar

#### Constructor Arguments
| Name       | Description                                 |
|------------|---------------------------------------------|
| start      | Iterator starting position                  |
| end        | Iterator ending position                    |
| current    | Current iteration position                  |
| step       | Added to current index after each iteration |
| length     | ASCII progress bar string length            |
| units      | Unit to append to progress rate             |
| color      | ANSI escape code to color progress bar      |
| display    | Automatically output to sdtout              |
| bar_format | Custom progress bar format string           |

#### Properties
| Name       | Description                                        |
|------------|----------------------------------------------------|
| elapsed    | Time ellapsed since first iteration: mm:ss         |
| percentage | Percentage of completion: 50%                      |
| bar        | ASCII progress bar:                 \|==========\| |
| fraction   | Position as a fraction: \[index/total\]            |
| rate       | Iterations per second: 2.00/s                      |
| eta        | Estimated time until complete: mm:ss               |

#### Methods
| Name                 | Description                                  |
|----------------------|----------------------------------------------|
| elapsed(self)        | Elapsed time in seconds                      |
| estimated_time(self) | Estimated time until completion in seconds   |
| fraction(self)       | Create fraction string                       |
| generate_bar         | Progress bar ASCII string                    |
| per_second           | Calculate iteration rate per second as float |
| percentage           | Percentage as a floating point               |

## License
Copyright © 2023 Zakary Timson | Available under the GNU General Public License

See the [license](./LICENSE) for more information.
