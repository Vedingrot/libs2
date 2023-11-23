# s2geometry must be configured to use the same C++ version that
# abseil uses.
%define cxx_standard 17

Name: libs2geometry
Version: 0.10.0.0.33.7773d
Release: alt1

Summary: Computational geometry and spatial indexing on the sphere
License: Apache-2.0
Group: System/Libraries
URL: https://github.com/google/s2geometry

Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: %name-ignore-certain-class-memaccess-warning.patch
Patch2: %name-suppress-multiline-comment-warnings.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libabseil-cpp-devel
BuildRequires: libssl-devel

%description
This is a package for manipulating geometric shapes.  Unlike many
geometry libraries, S2 is primarily designed to work with spherical
geometry, i.e., shapes drawn on a sphere rather than on a planar
2D map.  This makes it especially suitable for working with geographic
data.

%package devel
Summary: Development libraries and headers for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
Development libraries and headers for %name.

%prep
%setup
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
%cmake \
    -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
    -DCMAKE_CXX_EXTENSIONS=ON \
    -DCMAKE_CXX_STANDARD=%cxx_standard

%cmake_build

%install
%cmake_install

%files
%_libdir/*.so*

%files devel
%_includedir/s2/

%changelog
* Thu Nov 23 2023 Egor Shestakov <ved@altlinux.org> 0.10.0.0.33.7773d-alt1
- Initial build.
