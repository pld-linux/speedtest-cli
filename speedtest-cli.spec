Summary:	speedtest
Name:		speedtest-cli
Version:	2.1.3
Release:	1
License:	Apache
Group:		Networking
Source0:	https://github.com/sivel/speedtest-cli/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	08c431f2f398880745c4f0564962b9e2
URL:		https://github.com/sivel/speedtest-cli
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python3-setuptools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command line interface for testing internet bandwidth using speedtest.net.

%prep
%setup -q

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -p speedtest-cli.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/speedtest
%attr(755,root,root) %{_bindir}/speedtest-cli
%{_mandir}/man1/speedtest-cli.1*
%{py3_sitescriptdir}/speedtest.py
%{py3_sitescriptdir}/__pycache__/speedtest.cpython-*.pyc
%{py3_sitescriptdir}/speedtest_cli-%{version}-py*.egg-info
