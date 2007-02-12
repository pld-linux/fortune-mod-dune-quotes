Summary:	The Dune Series Fortunes
Summary(pl.UTF-8):   Zestaw fortunek z cytatami z Diuny
Name:		fortune-mod-dune-quotes
Version:	2.0.1
Release:	2
License:	Freeware
Group:		Applications/Games
Requires:	fortune-mod
Source0:	http://dune.s31.pl/%{name}.%{version}.tar.gz
# Source0-md5:	5821793a7754ca07a18c5c08656b7371
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's your
program. Fun-loving system administrators can add fortune to users'
.login files, so that the users get their dose of wisdom each time
they log in.

This package contains the Dune Chronicles pre-chapter quotes converted
to a fortune-mod form. Quotes from the pre-Dune novels, written by
F.Herbert's are also included.

%description -l pl.UTF-8
Fortune-mod zawiera wciąż popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochotę na odrobinę mądrości przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mogą dodać fortune do plików .login użytkowników tak,
by każdy otrzymał swoją dawkę mądrości przy logowaniu.

Ten pakiet zawiera cytaty poprzedzające rozdziały Kronik Diuny.
Dołączono również cytaty z prequeli, napisanych przez syna F.
Herberta.

%prep
%setup -q -n %{name}.%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/fortunes

install * $RPM_BUILD_ROOT%{_datadir}/games/fortunes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/fortunes/*
