%define upstream_name    latest
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Use the latest Perl features
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: perl(version)
BuildRequires: perl(Module::Build)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Provides: perl(latest)

%description
The line

  use latest;

is roughly equivalent to

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


