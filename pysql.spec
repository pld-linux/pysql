Summary:	A full (and much more) replacement for sqlplus
Summary(pl.UTF-8):	Pełny (a nawet lepszy) zamiennik sqlplus
Name:		pysql
Version:	0.14
Release:	2
License:	GPL v2
Group:		Applications/Databases
Source0:	http://dl.sourceforge.net/pysql/%{name}-%{version}.tar.gz
# Source0-md5:	cfaef3afa0d7eaef2074f48b2a9df238
URL:		http://pysql.sourceforge.net/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-cx_Oracle
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PySQL aim to be a full (and much more) replacement for sqlplus. Some
ideas behind PySQL:
- really usable and not painful (history, completion, line edition...)
- high level function often used (search for tables, indexes, count,
  explain plan, list of sessions...)
- proper output for screen and file (csv ready for inclusion in
  spreadsheets)
- user defined macro ?

%description -l pl.UTF-8
PySQL jest w zamierzeniu pełnym (a nawet o wiele lepszym) zamiennikiem
narzędzia sqlplus. Niektóre idee PySQL-a:
- prawdziwa użyteczność bez bólu (historia, dopełnianie, edycja linii
  poleceń...)
- częste używanie funkcji wysokopoziomowych (wyszukiwanie tabel,
  indeksów, zliczanie, plan explain, lista sesji...)
- właściwe wyjście dla screena i pliku (zgodność z CSV do umieszczania
  w arkuszach kalkulacyjnych)
- zdefiniowane przez użytkownika makro ?

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
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
