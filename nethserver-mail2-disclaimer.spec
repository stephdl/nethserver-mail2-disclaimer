Summary: nethserver-mail2-disclaimer  is a module to use altermime
%define name nethserver-mail2-disclaimer
Name: %{name}
%define version 0.0.1
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Requires: altermime
BuildRequires: nethserver-devtools
BuildArch: noarch

%description
nethserver-mail2-disclaimer is used to add disclaimer

%changelog
* Sat Feb 10 2018 stephane de Labrusse <stephdl@de-labrusse.fr>
- initial

%prep
%setup

%build
%{makedocs}
perl createlinks
%{__mkdir_p} root/var/spool/filter

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
%{genfilelist} \
--dir /var/spool/filter 'attr(0750,mail,mail)' \
$RPM_BUILD_ROOT > %{name}-%{version}-%{release}-filelist

%post
%postun

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING
