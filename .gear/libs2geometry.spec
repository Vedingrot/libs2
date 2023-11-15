Name: libs2geometry
Version: 0.10.0
Release: alt1

Summary: Computational geometry and spatial indexing on the sphere
License: Apache-2.0
Group: System/Libraries
URL: https://github.com/google/s2geometry

Source: %name-%version.tar

Patch0: %name-%version-alt-set-no-error.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libabseil-cpp-devel
BuildRequires: libssl-devel

%description
This is a package for manipulating geometric shapes.
Unlike many geometry libraries, S2 is primarily designed to work with spherical
geometry, i.e., shapes drawn on a sphere rather than on a planar 2D map.
This makes it especially suitable for working with geographic data.

%package devel
Summary: Development libraries and headers for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
Development libraries and headers for %name.

%prep
%setup
%patch0 -p1
#Set correct cpp standard
sed -i 's/CMAKE_CXX_STANDARD 11/CMAKE_CXX_STANDARD 17/' CMakeLists.txt

%build
%cmake \
    -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
    -DCMAKE_CXX_EXTENSIONS=ON

%cmake_build

%install
%cmake_install

%files
%_libdir/*.so*

%files devel
%_includedir/s2/

%changelog
* Wed Jul 05 2023 Alexander Burmatov <thatman@altlinux.org> 0.10.0-alt1
- Initial build for Sisyphus.
