#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyhs100
Version  : 0.3.5
Release  : 17
URL      : https://files.pythonhosted.org/packages/a5/e3/4f95f6b73fa3cf50be81ca9331a8598f46d296e836558b361991a26b9644/pyHS100-0.3.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/a5/e3/4f95f6b73fa3cf50be81ca9331a8598f46d296e836558b361991a26b9644/pyHS100-0.3.5.tar.gz
Summary  : Interface for TPLink HS1xx plugs, HS2xx wall switches & LB1xx bulbs
Group    : Development/Tools
License  : GPL-3.0
Requires: pyhs100-bin = %{version}-%{release}
Requires: pyhs100-python = %{version}-%{release}
Requires: pyhs100-python3 = %{version}-%{release}
Requires: click
Requires: click-datetime
BuildRequires : buildreq-distutils3
BuildRequires : click
BuildRequires : click-datetime
Patch1: no-typing.patch

%description
# pyHS100
[![PyPI version](https://badge.fury.io/py/pyHS100.svg)](https://badge.fury.io/py/pyHS100)
[![Build Status](https://travis-ci.org/GadgetReactor/pyHS100.svg?branch=master)](https://travis-ci.org/GadgetReactor/pyHS100)
[![Coverage Status](https://coveralls.io/repos/github/GadgetReactor/pyHS100/badge.svg?branch=master)](https://coveralls.io/github/GadgetReactor/pyHS100?branch=master)
[![Reviewed by Hound](https://img.shields.io/badge/Reviewed_by-Hound-8E64B0.svg)](https://houndci.com)

%package bin
Summary: bin components for the pyhs100 package.
Group: Binaries

%description bin
bin components for the pyhs100 package.


%package python
Summary: python components for the pyhs100 package.
Group: Default
Requires: pyhs100-python3 = %{version}-%{release}

%description python
python components for the pyhs100 package.


%package python3
Summary: python3 components for the pyhs100 package.
Group: Default
Requires: python3-core
Provides: pypi(pyhs100)
Requires: pypi(click)
Requires: pypi(click_datetime)

%description python3
python3 components for the pyhs100 package.


%prep
%setup -q -n pyHS100-0.3.5
cd %{_builddir}/pyHS100-0.3.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588285410
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyhs100

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
