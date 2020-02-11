%global netease_ver     1.2.1
%global filename0       netease-cloud-music_%{netease_ver}_amd64_ubuntu_20190428.deb
%global deb0            http://d1.music.126.net/dmusic/%{filename0}
%global downloadcmd0    /usr/bin/curl -A 'Mozilla' -fLC - --retry 3 --retry-delay 3 -O %{deb0}

%global pkg_name        netease-cloud-music
%global packager    荒野無燈 <ttys3@outlook.com>

# need build with: QA_RPATHS=$(( 0x0004|0x0008 )) rpmbuild -ba -v ./netease-cloud-music.spec
# %%global _build_id_links none

Name:           %{pkg_name}
Version:        %{netease_ver}
Release:        1%{?dist}
Group:          Applications/Multimedia
Summary:        Netease Cloud Music

License:        Proprietary
URL:            https://music.163.com/#/download
Source0:        %{deb0}

BuildRequires:  curl coreutils
Requires:       libnsl

%description
Netease cloud music player.
Maintainer: zccrs <zhangjide@deepin.com>
Homepage: https://www.deepin.org
rpm package converted from .deb
thanks to https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=netease-cloud-music

%prep

%build

%install

%if 0%(test ! -f %{SOURCE0}) == 0
%{downloadcmd0}
mv %{_topdir}/BUILD/%{filename0} %{SOURCE0}
%endif

# Unpack the deb, correcting the lib directory and removing debian directories
ar p %{SOURCE0} data.tar.xz | tar -xJf- -C %{buildroot}

# fixup HiDPI problem
sed -i 's/Exec=.*/Exec=env QT_AUTO_SCREEN_SCALE_FACTOR=1 QT_SCALE_FACTOR=1 netease-cloud-music %U/' %{buildroot}/usr/share/applications/netease-cloud-music.desktop

%check


%files
%license
%doc
/opt/*
/usr/*


%changelog

* Tue Feb 11 2020 荒野無燈 <ttys3@outlook.com>
- converted from amd64_ubuntu_20190428.deb
