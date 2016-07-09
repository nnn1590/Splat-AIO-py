## Splat AIO ([Download](https://github.com/seresaa/Splat-AIO/blob/master/Splat-AIO.zip?raw=true))
A collection of easy python scripts to handle all python scripts, an attempt to try and put scripts from [Splatoon Modding Hub](https://gbatemp.net/threads/splatoon-modding-hub.425670/) or elsewhere in one tool for everyone to use, as well as a few other useful things. It also tries to support the Homebrew Launcher version of TCPGecko found in the downloads of [this thread](https://gbatemp.net/threads/post-your-wiiu-cheat-codes-here.395443/).

If there is something contained in here that shouldn't be, let me know and I'll remove it.

Splat AIO comes with rank/snail/level/money editors, All Gear and All Weapons, [a safe variant of Octohax](https://github.com/wiiudev/pyGecko/blob/master/octoling.py) which is essentially a model swap of the Inkling Girl, [Splatoon Colorizer](https://gbatemp.net/threads/splatoon-colorizer.406463/), [Splathax and Amiibohax](https://gbatemp.net/threads/splatoon-modding-hub.425670/page-47#post-6344607). It also comes with a few other tools (TCPGecko dotNET, Wireless Network Watcher, SARCTools, yamlconv..) to make life easier.

#### Prerequisites
[Python 2.7.11](https://www.python.org/downloads/). Python 3.5.1 will not work.
[Java](https://java.com/) for Colorizer.

#### Usage
Start "Splat-AIO.py" and the rest should be fairly self-explanatory.


#### Updating
I also wrote in a simple updater using urllib and urllib2 that will retrieve an update.zip from this repository, unzip it, and replace the contents of \Resources\run with it if the repository's ver.txt has a higher value than the locally stored \Resources\setup\ver.txt, and then update \Resources\setup\ver.txt as well. 

It's in the options menu, will show a sort of changelog from changes.txt, and will ask you to confirm. These updates should only contain fixes and changes to current TCPGecko scripts, additional scripts and possibly additional programs. Feel free to look through update.zip to make sure you're okay with everything it contains.
