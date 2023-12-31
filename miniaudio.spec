%define _empty_manifest_terminate_build 0
Name:           miniaudio
Version:        0.11.21
Release:        1
Summary:        Audio playback and capture library
Group:          System/Libraries
License:        MIT-0
URL:            https://miniaud.io/
Source0:        https://github.com/mackron/miniaudio/archive/%{version}/%{name}-%{version}.tar.gz
 
%package devel
Summary: %summary
Provides:       miniaudio-static = %{version}-%{release}
BuildArch:      noarch
 
%description
%summary
%description devel
%summary

%prep
%autosetup -n %{name}-%{version}
 
%build
 
%install
mkdir -p %{buildroot}%{_includedir}
install -p %{name}.h %{buildroot}%{_includedir}/
 
%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}.h
