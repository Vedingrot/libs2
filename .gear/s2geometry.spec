%define lname s2geometry
%define libsover 0
%define libs2geometry lib%lname%libsover
Name: %lname
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
Summary: Development libraries and headers for %lname
Group: Development/Other
Provides: %libs2geometry-devel = %EVR
Obsoletes: %libs2geometry-devel < %EVR

%description devel
Development libraries and headers for %lname.

%package -n %libs2geometry
Summary: %lname library
Group: System/Libraries

%description -n %libs2geometry
%lname library.

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

%files -n %libs2geometry
%_libdir/libs2*.so.%libsover
%_libdir/libs2*.so.%libsover.*

%files devel
%_libdir/*.so
%_includedir/s2/

%changelog
* Wed Jul 05 2023 Alexander Burmatov <thatman@altlinux.org> 0.10.0-alt1
- Initial build for Sisyphus.