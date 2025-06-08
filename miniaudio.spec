Summary:		An audio playback and capture library in a single header file
Name:		miniaudio
Version:		0.11.22
Release:		1
License:		MIT-0
Group:		System/Libraries
Url:		https://miniaud.io/
Source0:	https://github.com/mackron/miniaudio/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:		noarch

%description
An audio playback and capture library in a single source file.  It is written
in C with no dependencies except the standard library and should compile
clean on all major compilers without the need to install any additional
development packages.
Features:
* Simple build system with no external dependencies.
* Simple and flexible API.
* Low-level API for direct access to raw audio data.
* High-level API for sound management, mixing, effects and 3D spatialization.
* Flexible node graph system for advanced mixing and effect processing.
* Resource management for loading sound files.
* Decoding, with built-in support for WAV, FLAC and MP3, also custom decoders.
* Encoding (WAV only).
* Data conversion.
* Resampling, including custom resamplers.
* Channel mapping.
* Basic generation of waveforms and noise.
* Basic effects and filters.

%files
# Nothing: there is only the header file

#-----------------------------------------------------------------------------
 
%package devel
Summary:		An audio playback and capture library in a single header file
Group:		Development/C
Provides:		miniaudio-static = %{version}-%{release}
BuildArch:		noarch

%description devel
An audio playback and capture library in a single source file.  It is written
in C with no dependencies except the standard library and should compile
clean on all major compilers without the need to install any additional
development packages.
This package contais the header file for using %{name}.

%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}.h

#-----------------------------------------------------------------------------

%prep
%autosetup -n %{name}-%{version}


%build
# Nothing to do


%install
mkdir -p %{buildroot}%{_includedir}
install -p -m 0644 %{name}.h %{buildroot}%{_includedir}/

