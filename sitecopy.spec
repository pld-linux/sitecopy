Summary:	Tool for easily maintaining remote web sites
Name:		sitecopy
Version:	0.16.3
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.lyra.org/sitecopy/%{name}-%{version}.tar.gz
# Source0-md5:	df48499ad81b333a9d255c1709e09a1a
URL:		http://www.lyra.org/sitecopy/
BuildRequires:	neon-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sitecopy allows you to easily maintain remote Web sites.  The program
will upload files to the server which have changed locally, and delete
files from the server which have been removed locally, to keep the
remote site synchronized with the local site, with a single
command. sitecopy will also optionally try to spot files you move
locally, and move them remotely.  FTP and WebDAV servers are
supported.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_bindir}/sitecopy
%{_mandir}/man1/*
%{_mandir}/*/man1/*
%{_datadir}/sitecopy
%doc BUGS ChangeLog README README.gnome TODO NEWS THANKS doc/update.sh
