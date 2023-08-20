## Report of assignment

### Components
The site I made is running on Flask with Gunicorn. And Nginx serves it as a website to the user.
The site can be edited after a successful push, with Github actions testing and deploying it to the VPS.

### Some problems encountered

#### Deploy keys

Deploying keys was the first roadblock I encountered. After reading the theory it still didn't work immediately.
The first result I got was: *Error: Permission denied (publickey).*
Solved after the following:

* I had to move the private and public key to the default folder after generating them.
* Then adding them to the ssh-agent identity.

#### Github secrets

After reading some information on github I made the .yml-file.
To login the VPS trough Github actions I understood I needed to use secrets. I couldn't workout how to use the github secrets, I thought I could use only one.
So I searched on the marketplace to use a program to login the VPS with Github action. When I found [appleboy/ssh-action](https://github.com/appleboy/ssh-action) it became clear for me how to use the secrets. I followed that recommendation from appleboy to set it up and I could successfully login the VPS to execute the commands I wanted.

#### Final steps
I have tried making a virtual environment for the site. But I did not realise it kept conflicting with the previous assignments. After a lot of trial and error I got the site to work again using the steps from WINC, on how to setup Nginx and Gunicorn.


### Result
[![Test and deploy](https://github.com/dgdck/CD-project/actions/workflows/run-tests.yml/badge.svg?branch=main)](https://github.com/dgdck/CD-project/actions/workflows/run-tests.yml)