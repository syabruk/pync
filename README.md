# pync

A simple Python wrapper around the [`terminal-notifier`][HOMEPAGE] command-line tool (version 2.0.0), which allows you to send User Notifications to the Notification Center on Mac OS X 10.10, or higher.

![Screenshot](http://f.cl.ly/items/1k051n3k0u0i101m1i0U/Screen%20Shot%202012-08-24%20at%2012.20.40%20PM.png)

### Installation

```bash
pip install pync
```
or
```bash
pip install git+https://github.com/SeTeM/pync.git
```
or
```bash
git clone git://github.com/SeTeM/pync.git
cd pync
python setup.py install
```

### Usage

For full information on all the options, see the tool’s [README][README].

#### Examples:

Using the notify function
```python
import pync

pync.notify('Hello World')
pync.notify('Hello World', title='Python')
pync.notify('Hello World', group=os.getpid())
pync.notify('Hello World', activate='com.apple.Safari')
pync.notify('Hello World', open='http://github.com/')
pync.notify('Hello World', execute='say "OMG"')

pync.remove_notifications(os.getpid())

pync.list_notifications(os.getpid())
```

Using the notifier object
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


### License

All the works are available under the MIT license. **Except** for ‘Terminal.icns’, which is a copy of Apple’s Terminal.app icon and as such is copyright of Apple.

See [LICENSE][LICENSE] for details.

[HOMEPAGE]: https://github.com/alloy/terminal-notifier
[README]: https://github.com/alloy/terminal-notifier/blob/master/README.markdown
[LICENSE]: https://github.com/setem/pync/blob/master/LICENSE
