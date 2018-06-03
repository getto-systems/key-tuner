# key-tuner

password generator

```bash
$ tune
passphrase : <Enter your passphrase>
service : <Enter service name>
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

1. passphrase : enter your passphrase for current session
1. service : enter service name
1. mode : select generate-mode
1. length : enter password length

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
