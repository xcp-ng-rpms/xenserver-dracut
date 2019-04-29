Summary: dracut configuration files for XenServer
Name: xenserver-dracut
Version: 9
Release: 1
License: GPL
Group: Xen
URL: http://www.citrix.com

Source0: https://code.citrite.net/rest/archive/latest/projects/XS/repos/xenserver-dracut/archive?at=v9&format=tar.gz&prefix=xenserver-dracut-9#/xenserver-dracut-9.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/xenserver-dracut/archive?at=v9&format=tar.gz&prefix=xenserver-dracut-9#/xenserver-dracut-9.tar.gz) = eddd14c7589b1302c68129fc65c7fdc871ca003d

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
* Tue Nov 25 2014  Ross Lagerwalll <ross.lagerwall@citrix.com>
- Update paths for newer dracut versions

* Thu Jan 30 2014  Frediano Ziglio <frediano.ziglio@citrix.com>
- First package version
