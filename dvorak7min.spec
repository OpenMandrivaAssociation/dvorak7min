Name:		dvorak7min
Version:	1.6.1
Release:	%mkrel 1
Summary:	Typing tutor for dvorak keyboards
License:	GPLv2+
Group:		Games/Other
Source:		dvorak7min_1.6.1.orig.tar.gz
# debian patch
Patch0:		dvorak7min_1.6.1-9.diff.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
%description
dvorak7min is a typing tutor to help you learn dvorak.

%prep
%setup -q
%patch0 -p1

%build
%make

%install
%{__rm} -Rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__cp} -p %{name} %{buildroot}%{_bindir}

%clean
%{__rm} -Rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{_bindir}/%{name}
