%global netease_ver     1.2.1
%global filename0       netease-cloud-music_%{netease_ver}_amd64_ubuntu_20190428.deb
%global deb0            http://d1.music.126.net/dmusic/%{filename0}
%global downloadcmd0    /usr/bin/curl -A 'Mozilla' -fLC - --retry 3 --retry-delay 3 -O %{deb0}

%%global _build_id_links none

Name:           netease-cloud-music
Version:        %{netease_ver}
Release:        1%{?dist}
Summary:        Netease Cloud Music, converted from .deb package

License:        custom
URL:            https://music.163.com/#/download
Source0:        %{deb0}

BuildRequires:  curl coreutils
Requires:       libnsl

%description
Netease cloud music player.
thanks to https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=netease-cloud-music

%prep
%{downloadcmd0}
mv %{_topdir}/BUILD/%{filename0} %{_topdir}/SOURCES/%{filename0}

%build

ar -xv %{_topdir}/SOURCES/%{filename0}
rm -rf %{_topdir}/BUILD/opt
rm -rf %{_topdir}/BUILD/usr
rm -f debian-binary
rm -f control.tar.xz
tar --level=1 --xz -xvf data.tar.xz
rm -f data.tar.xz


%install

cp -rav . %{buildroot}/

%check


%files
%license
%doc
/opt/*
/usr/*


%changelog

* 2020-02-11 init release rpm package