# key-tuner

password generator

```bash
$ tune
passphrase : <Enter your passphrase>
service : <Enter service name>
version : <Enter version>
mode (0: ex, 1: full, 2: short) : <Enter generate mode>
length : <Enter password length>
...(generation)
password : GENERATED-PASSWORD
```


###### Table of Contents

- [Requirements](#Requirements)
- [Usage](#Usage)
- [License](#License)

<a id="Requirements"></a>
## Requirements

- bash


<a id="Usage"></a>
## Usage

1. passphrase : your passphrase : e.g. "my passphrase"
1. service : service name : e.g. "amazon"
1. version : password version : e.g. "2018.06.03"
1. mode : generate mode
1. length : password length

use `"$passphrase" + "$service" + "$version"` as password seed

with same password seed, generate same password

### mode

- 0: ex : 0-9a-zA-Z-/:;()&@.,?!'[]{}#%^*+=_|<>$
- 1: full : 0-9a-zA-Z@#&*%!?
- 2: short : 0-9a-z

### Install for Linux

```bash
$ git clone https://github.com/getto-systems/key-tuner.git
$ PATH=$PATH:/path/to/key-tuner/bin
```

### Install for iOS

- install [OpenTerm](https://github.com/louisdh/openterm)
- copy `scripts/tune.cub` to scripts


<a id="License"></a>
## License

key-tuner is licensed under the [MIT](LICENSE) license.

Copyright &copy; since 2018 shun@getto.systems
