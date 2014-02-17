Summary:	speedtest
Name:		speedtest-cli
Version:	0.2.4
Release:	1
License:	Apache
Group:		Networking
Source0:	http://github.com/sivel/speedtest-cli/archive/v%{version}.tar.gz
# Source0-md5:	229fc4c6ca702e5f5abdeabfb630efc7
URL:		http://github.com/sivel/speedtest-cli
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-distribute
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		bash_compdir	%{_datadir}/bash-completion/completions

%description
speedtest-cli - command line interface to speedtest.net.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/speedtest
%attr(755,root,root) %{_bindir}/speedtest-cli
%{py_sitescriptdir}/speedtest_cli.py*
%{py_sitescriptdir}/speedtest_cli-%{version}-py*.egg-info
