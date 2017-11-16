#rpmbuild must define %{name} %{version} %{release}
Name: %{name}
Version: %{version}
Release: %{release}
Summary: %{name}
License: copyright
Group: Development/Tools
Packager: woniu17<qinglucklin@foxmail.com>
URL: http://m.linqingxiang.com/
Source0: %{name}-%{version}-%{release}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%define __debug_install_post: >/dev/null
%define __strip: /usr/bin/echo_none
%define debug_package %{nil}


%description
This is desc of %{name}

%package devel
Summary: %{name} lib
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Header files and libraries of %{name}

%prep
%setup -c %{name}-%{version}

%build
# ./configure --prefix=/usr/local/%{name}
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot}  install

%clean
rm -rf %{buildroot}

%pre

%post

echo "%{name} is already installed!"

%preun

%postun

echo "%{name} is already uninstalled!"


%files
%defattr(-,root,root)
/usr/local/%{name}/*

%changelog
