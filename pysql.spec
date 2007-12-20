Summary:	A full (and much more) replacement for sqlplus
Name:		pysql
Version:	0.11
Release:	1
License:	GPL v2
Group:		Applications/Databases
Source0:	http://dl.sourceforge.net/pysql/%{name}-%{version}.tar.gz
# Source0-md5:	35a3afa6c383dac8d9a8a4229b2da06b
URL:		http://pysql.sourceforge.net/
Requires:	python-cx_Oracle
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PySQL aim to be a full (and much more) replacement for sqlplus.
This projet start the 17th of august 2006. It is also a cool
pretext for coding in Python ;-) Some ideas behind PySQL :

* really usable and not painfull (history, completion, line edition...)
* high level function often used (search for tables, indexes, count,
  explain plan, list of sessions...)
* proper output for screen and file (csv ready for inclusion in spreadsheets)
* user defined macro ?

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog* README
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}/*.py[co]
%{py_sitescriptdir}/*.egg-info
