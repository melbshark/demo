# demo.binjit.su

Pwning in the browser! [Try it here!](http://demo.binjit.su)

This is just a mixture of Docker and Butterfly.py which lets people use Binjitsu in their browser.

It's probably crazy insecure and should only be run on a VM/Cloud VPS you don't care about and has nothing else on it.

## Setup

This is untested, but it's the general idea.

```sh
cd /
git init
git remote origin add git://github.com/binjitsu/demo.git
git fetch --all
git checkout --force -t origin/master
# git reset --hard origin/master # <-- If the above line doesn't work
cd /root
./setup.sh
```

