## Report of assignment

### Deploy keys

Deploying keys was the first roadblock I encountered. After reading the theory it still didn't work immediately.
The first result I got was: *Error: Permission denied (publickey).*
Solved after the following:

* I had to move the private and public key to the deafault folder after generating them.
* Then adding them to the ssh-agent identity.

### Result
[![Test and deploy](https://github.com/dgdck/CD-project/actions/workflows/run-tests.yml/badge.svg)](https://github.com/dgdck/CD-project/actions/workflows/run-tests.yml)