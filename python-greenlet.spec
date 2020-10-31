Name:            python-greenlet
Version:         0.4.14
Release:         4
Summary:         lightweight coroutines for in-process concurrent programming
License:         MIT
URL:             https://github.com/python-greenlet/greenlet
Source0:         https://github.com/python-greenlet/greenlet/archive/0.4.14.tar.gz

BuildRequires:   python3-devel python3-setuptools
BuildRequires:   gcc-c++

%description
The greenlet package is a spin-off of Stackless, a version of CPython
that supports micro-threads called "tasklets". Tasklets run pseudo-concurrently
(typically in a single or a few OS-level threads) and are synchronized
with data exchanges on "channels".

%package -n python3-greenlet
Summary:         lightweight coroutines for in-process concurrent programming
%{?python_provide:%python_provide python3-greenlet}

%description -n python3-greenlet
The greenlet package of python 3 version.

%package -n python3-greenlet-devel
Summary:         Development files for python3-greenlet
Requires:        python3-greenlet%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-greenlet-devel}

%description -n python3-greenlet-devel
This package contains libraries and headier files for developing applications
that use python3-greenlet.

%prep
%autosetup -n greenlet-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-greenlet
%defattr(-,root,root)
%license LICENSE LICENSE.PSF
%doc AUTHORS NEWS README.rst
%{python3_sitearch}/*

%files -n python3-greenlet-devel
%defattr(-,root,root)
%{_includedir}/python%{python3_version}*/greenlet/

%changelog
* Thu Oct 29 2020 tianwei <tianwei12@huawei.com> - 0.4.14-4
- delete python2 require

* Tue Sep 8 2020 liuweibo <liuweibo10@huawei.com> - 0.4.14-3
- Fix Source0

* Mon Dec 9 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.4.14-2
- Package init
