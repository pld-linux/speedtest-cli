Summary:	speedtest
Name:		speedtest-cli
Version:	0.2.5
Release:	1
License:	Apache
Group:		Networking
Source0:	http://github.com/sivel/speedtest-cli/archive/v%{version}.tar.gz
# Source0-md5:	16b447ef814b53dd566a2b70c581a31f
URL:		http://github.com/sivel/speedtest-cli
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-distribute
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command line interface for testing internet bandwidth using speedtest.net.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

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
%{py_sitescriptdir}/speedtest_cli.py*
%{py_sitescriptdir}/speedtest_cli-%{version}-py*.egg-info
