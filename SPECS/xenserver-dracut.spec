Summary: dracut configuration files for XenServer
Name: xenserver-dracut
Version: 10
Release: 1%{?dist}
License: GPL
Group: Xen
URL: http://www.citrix.com

Source0: https://code.citrite.net/rest/archive/latest/projects/XS/repos/xenserver-dracut/archive?at=v10&format=tar.gz&prefix=xenserver-dracut-10#/xenserver-dracut-10.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/xenserver-dracut/archive?at=v10&format=tar.gz&prefix=xenserver-dracut-10#/xenserver-dracut-10.tar.gz) = 342a2cecae12c7e477de8e28d4258fbfb41f3ddd

BuildArch: noarch
Requires: dracut

%description
dracut configuration files for XenServer.

%prep
%autosetup -p1

%build
# Do nothing

%install
mkdir -m 755 -p %{buildroot}/usr/lib/dracut/modules.d %{buildroot}/etc/dracut.conf.d
install -m 644 -t %{buildroot}/etc/dracut.conf.d config/*
cp -r modules/* %{buildroot}/usr/lib/dracut/modules.d

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/lib/dracut/modules.d/*
/etc/dracut.conf.d/*

%changelog
* Thu Jul 18 2019 Ross Lagerwall <ross.lagerwall@citrix.com> - 10-1
- Remove xenbuilder files
- CA-323402: Avoid 900s delay during iSCSI boot when path is down
- CA-323402: Don't wait for network interfaces to be setup

* Tue Nov 25 2014  Ross Lagerwalll <ross.lagerwall@citrix.com>
- Update paths for newer dracut versions

* Thu Jan 30 2014  Frediano Ziglio <frediano.ziglio@citrix.com>
- First package version
