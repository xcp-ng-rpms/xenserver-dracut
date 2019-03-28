Summary: dracut configuration files for XenServer
Name: xenserver-dracut
Version: 9
Release: 1%{dist}
License: GPL
Group: Xen
URL: http://www.citrix.com
Source0: https://code.citrite.net/rest/archive/latest/projects/XS/repos/%{name}/archive?at=v%{version}&format=tar.gz&prefix=%{name}-%{version}#/%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: dracut

%description
dracut configuration files for XenServer.

%prep
%autosetup -p1 -n xenserver-dracut-9

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
