pync
====

A simple Python wrapper around the [`terminal-notifier`][HOMEPAGE] command-line
tool, which allows you to send User Notifications to the Notification Center on
Mac OS X 10.8, or higher.


Installation
------------

```
$ pip install pync
```
or
```
$ git clone git@github.com:SeTeM/pync.git
$ cd pync
$ python setup.py install
```

Usage
-----

For full information on all the options, see the tool’s [README][README].

Examples are:

```python
from pync import Notifier

Notifier.notify('Hello World')
Notifier.notify('Hello World', title='Python')
Notifier.notify('Hello World', group=os.getpid())
Notifier.notify('Hello World', activate='com.apple.Safari')
Notifier.notify('Hello World', open='http://github.com/')
Notifier.notify('Hello World', execute='say "OMG"')

Notifier.remove(os.getpid())

Notifier.list(os.getpid())
```


License
-------

All the works are available under the MIT license. **Except** for
‘Terminal.icns’, which is a copy of Apple’s Terminal.app icon and as such is
copyright of Apple.

See [LICENSE][LICENSE] for details.

[HOMEPAGE]: https://github.com/alloy/terminal-notifier
[README]: https://github.com/alloy/terminal-notifier/blob/master/README.markdown
[LICENSE]: https://github.com/setem/pync/blob/master/LICENSE