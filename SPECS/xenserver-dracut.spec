%global package_speccommit c6981959af0747deb651db1cbeb480444e3613ed
%global package_srccommit v10
Summary: dracut configuration files for XenServer
Name: xenserver-dracut
Version: 10
Release: 2%{?xsrel}%{?dist}
License: GPL
Group: Xen
URL: http://www.citrix.com
Source0: xenserver-dracut-10.tar.gz
BuildArch: noarch
Requires: dracut intel-microcode amd-microcode

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

echo "early_microcode=\"yes\"" > %{buildroot}/etc/dracut.conf.d/xs_early_microcode.conf

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/lib/dracut/modules.d/*
/etc/dracut.conf.d/*

%changelog
* Mon Apr 11 2022 Andrew Cooper <andrew.cooper3@citrix.com> - 10-2
- Pull in intel/amd-microcode packages automatically
- Add xs_early_microcode.conf

* Thu Jul 18 2019 Ross Lagerwall <ross.lagerwall@citrix.com> - 10-1
- Remove xenbuilder files
- CA-323402: Avoid 900s delay during iSCSI boot when path is down
- CA-323402: Don't wait for network interfaces to be setup

* Tue Nov 25 2014  Ross Lagerwalll <ross.lagerwall@citrix.com>
- Update paths for newer dracut versions

* Thu Jan 30 2014  Frediano Ziglio <frediano.ziglio@citrix.com>
- First package version
