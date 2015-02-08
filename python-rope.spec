%define module	rope

Summary:	Python refactoring library
Name:		python-%{module}
Version:	0.10.2
Release:	1
License:	GPLv2
Group:		Development/Python
Url:		http://rope.sourceforge.net/
Source0:	%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  python2-devel
BuildRequires:	python2-setuptools

%description
Rope is a Python refactoring library. You can use
rope as a library in other IDEs.

%prep
%setup -qn %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python2 setup.py install --root=%{buildroot} --record=FILE_LIST

%files -f FILE_LIST
%doc COPYING README.rst docs/*

