%define	_ver	%(echo %{version} | tr . -)
Summary:	DISTRHO audio plugins
Name:		DISTRHO-Ports
Version:	2018.04.16
Release:	2
License:	GPL v2, LGPL v3
Group:		Applications/Sound
#Source0Download: https://github.com/DISTRHO/DISTRHO-Ports/releases
Source0:	https://github.com/DISTRHO/DISTRHO-Ports/archive/%{_ver}/%{name}-%{_ver}.tar.gz
# Source0-md5:	3c4769f4f05f43d32adec42b623ec7f5
Patch0:		premake.patch
URL:		http://plugin.org.uk/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	freetype-devel
BuildRequires:	pkgconfig
BuildRequires:	premake3
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/(lv2|vst)

%description
Set of closs-platfrom audio plugins from the DISTRHO project.:

%package lv2
Summary:	DISTRHO audio LV2 plugins
Group:		Applications/Sound

%description lv2
Set of closs-platfrom audio plugins from the DISTRHO project.:

%package vst
Summary:	DISTRHO audio VST plugins
Group:		Applications/Sound

%description vst
Set of closs-platfrom audio plugins from the DISTRHO project.:

%prep
%setup -q -n %{name}-%{_ver}
%patch0 -p1

%build
CXXFLAGS="%{rpmcppflags} %{rpmcxxflags}" \
LDFLAGS="%{rpmldflags}" \
scripts/premake-update.sh linux

%{__make} \
	verbose=1 \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}
%{__cp} -a bin/* $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files lv2
%defattr(644,root,root,755)
%doc README.md
%dir %{_libdir}/lv2/*.lv2
%{_libdir}/lv2/*.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/*.lv2/*.so

%files vst
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/vst/*.so
