%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define _sourcedir  %{expand:%%(pwd)}
%define _binaries_in_noarch_packages_terminate_build   0

Name:       python-rados-utils
Version:	%(git describe HEAD | sed 's/\-.*$//')
Release:	%(git describe HEAD | awk 'BEGIN{FS=OFS="-"} NF>1{$1="";sub(/^- */, "")}'1 | sed 's/^/-/' | sed 's/\-/_/g' | sed 's/.//')%{?dist}
Summary:	Python RADOS utilities for performing operations on a RADOS/ceph cluster.

Group:		Storage/System
License:	GPLv2
URL:		https://github.com/bryanapperson/python-rados-utils
BuildArch:  noarch

Requires:	python >= 2.7, python-rados >= 0.94
BuildRequires:	python >= 2.7, python-rados >= 0.94

%description
Python RADOS utilities for performing operations on a RADOS/ceph cluster.

%build
echo "RPM_SOURCE_DIR: ${RPM_SOURCE_DIR}"
%{__python} ${RPM_SOURCE_DIR}/setup.py build --sourcedir ${RPM_SOURCE_DIR}/

%install
echo "RPM_SOURCE_DIR: ${RPM_SOURCE_DIR}"
echo "%%defattr(-, root, root)" >MANIFEST
%{__python} ${RPM_SOURCE_DIR}/setup.py install --sourcedir ${RPM_SOURCE_DIR}/ -O1 --skip-build --root ${RPM_BUILD_ROOT}
(cd ${RPM_BUILD_ROOT}; find . -type f -or -type l | sed -e s/^.// -e /^$/d) >>MANIFEST

%pre

%post

%postun

%clean
rm -rf ${RPM_BUILD_ROOT} MANIFEST

%files -f MANIFEST

%changelog
