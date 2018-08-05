Summary:	speedtest
Name:		speedtest-cli
Version:	2.0.2
Release:	1
License:	Apache
Group:		Networking
Source0:	http://github.com/sivel/speedtest-cli/archive/v%{version}.tar.gz
# Source0-md5:	3943d71172eaec3f882a020f3d5fae56
URL:		http://github.com/sivel/speedtest-cli
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-distribute
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command line interface for testing internet bandwidth using speedtest.net.

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install
%py_postclean

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
%{py_sitescriptdir}/speedtest.py*
%{py_sitescriptdir}/speedtest_cli-%{version}-py*.egg-info
