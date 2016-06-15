## Splat AIO
A simple python script (key word "simple") to handle all python scripts, an attempt to try and put scripts from [Splatoon Modding Hub](https://gbatemp.net/threads/splatoon-modding-hub.425670/) or elsewhere in one tool for everyone to use, as well as a few other useful things. It also tries to support the Homebrew Launcher version of TCPGecko found in the downloads of [this thread](https://gbatemp.net/threads/5-5-1-5-4-0-5-3-2-self-hosting-package-everything-in-one-zip-file.424679/).

If there is something contained in here that shouldn't be, let me know and I'll remove it.

Splat AIO comes with default 'max this' scripts, a safe variant of Octohax which is essentially a model swap of the Inkling Girl (will add link when the original is back up), [Splatoon Colorizer](https://gbatemp.net/threads/splatoon-colorizer.406463/), [Splathax and Amiibohax](https://gbatemp.net/threads/splatoon-modding-hub.425670/page-47#post-6344607). It also comes with [TCP Gecko dotNET](https://github.com/Chadderz121/tcp-gecko-dotnet) if you want to get dirty, and [Wireless Network Watcher](http://www.nirsoft.net/utils/wireless_network_watcher.html) for keeping up with your IP addresses.

#### Prerequisites
[Python 2.7.11](https://www.python.org/downloads/). Python 3.5.1 will not work.
[Java](https://java.com/) for Colorizer.

#### Usage
Start "All In One Turbo.py" and the rest should be fairly self-explanatory.


#### Updating
I also wrote in a simple updater using urllib and urllib2 that will retrieve an update.zip from this repository, unzip it, and replace the contents of \Resources\run with it if the repository's ver.txt has a higher value than the locally stored \Resources\setup\ver.txt, and then update \Resources\setup\ver.txt as well. 

It's in the options menu, will show a sort of changelog from changes.txt, and will always ask you to confirm. These updates should only contain fixes and changes to current TCPGecko scripts, additional scripts and possibly additional programs. Feel free to look through update.zip to make sure you're okay with everything it contains.
