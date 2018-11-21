%define module rope

Name:           python-%{module}
Version:        0.10.7
Release:        1
Summary:        Python refactoring library
Source0:        https://pypi.python.org/packages/7e/fc/702c0293b57edd4d70146e36f9413c40339a701a43c8fa6918fb9d834913/%{module}-%{version}.tar.gz
License:        GPLv2
Group:          Development/Python
Url:            http://rope.sourceforge.net/
BuildArch:      noarch

BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(python)

%description
Rope is a Python refactoring library. You can use rope as a library in other
IDEs.

%package -n python2-%{module}
Summary:        Python refactoring library
%{?python_provide:%python_provide python2-%{module}}

%description -n python2-%{module}
Rope is a Python refactoring library. You can use rope as a library in other
IDEs.

%prep
%autosetup -p1 -n %{module}-%{version}
cp -a . %{py3dir}

%build
pushd %{py3dir}
%py3_build
popd
%py2_build

%install
pushd %{py3dir}
%py3_install
popd
%py2_install 

%files -n python2-%{module}
%doc COPYING README.rst docs/*
%{python2_sitelib}/rope*

%files
%doc COPYING README.rst docs/*
%{python3_sitelib}/rope*
