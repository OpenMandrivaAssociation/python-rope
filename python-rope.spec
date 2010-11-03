%define module	rope
%define name	python-%{module}
%define version 0.9.3
%define release %mkrel 1

Summary:	Python refactoring library
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Python
Url:		http://rope.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
%py_requires -d

%description
Rope is a Python refactoring library. You can use rope as a library in other IDEs.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc COPYING README.txt docs/*
