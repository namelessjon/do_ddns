Digital Ocean Dynamic DNS
=========================

Simple python script to use the Digital Ocean DNS hosting and their API, along
with an IP lookup service, to act as a dynamic DNS for a home server.

Requirements
------------

Not much:

* python3
  * requests
  * click
* a domain hosted on Digital Ocean
* An API key

How to use
----------

``` shell
$ python do_ddns.py --domain your.domain.here --api-key ABCEDF01....
```

At the moment, it's pretty verbose and will let you know if things worked or not.

There's a `systemd` [service](do_ddns@.service), which tries to run in as locked down a manner as possible.

``` shell
# systemctl start do_ddns@your.domain.here
```
