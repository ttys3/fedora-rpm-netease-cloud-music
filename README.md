# fedora rpm for netease-cloud-music (网易云音乐)

## how to build

```bash
# prepare tools
sudo dnf install -y gcc rpm-build rpm-devel rpmlint make python bash coreutils diffutils patch rpmdevtools

# prepare tree
rpmdev-setuptree

# build
QA_RPATHS=$(( 0x0004|0x0008 )) rpmbuild -ba -v ./netease-cloud-music.spec

# install
sudo dnf install -y $HOME/rpmbuild/RPMS/x86_64/netease-cloud-music-1.2.1-1.fc31.x86_64.rpm
```
