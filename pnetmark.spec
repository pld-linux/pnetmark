%define		pnet_ver	0.8.0
Summary:	PNetMark - benchmarking tool for Common Language Runtime (CLR) environments
Summary(pl.UTF-8):	PNetMark - narzędzie do pomiaru wydajności środowisk CLR (Common Language Runtime)
Name:		pnetmark
Version:	0.0.6
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://download.savannah.gnu.org/releases/dotgnu-pnet/%{name}-%{version}.tar.gz
# Source0-md5:	e23c06fb48495ef1ade0fa5c700283f2
URL:		http://www.gnu.org/software/dotgnu/pnet.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
# required tools: cscc ilrun csdoc2html
BuildRequires:	pnet-compiler-csharp >= %{pnet_ver}
BuildRequires:	pnet-interpreter >= %{pnet_ver}
BuildRequires:	pnet-tools >= %{pnet_ver}
BuildRequires:	pnetlib-base >= %{pnet_ver}
Requires:	pnetlib-base >= %{pnet_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PNetMark is a benchmarking tool for Common Language Runtime (CLR)
environments. It is loosely based on the techniques used by the
CaffeineMark to benchmark Java.

%description -l pl.UTF-8
PNetMark to narzędzie do pomiaru wydajności środowisk CLR (Common
Language Runtime). Jest luźno oparty na technikach używanych w
CaffeineMark służącym do testowania wydajności Javy.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-pnetlib=%{_libdir}/cscc/lib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/cscc/lib

install linpack/linpack.exe scimark2/scimark2.exe src/pnetmark.exe $RPM_BUILD_ROOT%{_libdir}/cscc/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/*.html
%{_libdir}/cscc/lib/linpack.exe
%{_libdir}/cscc/lib/pnetmark.exe
%{_libdir}/cscc/lib/scimark2.exe
