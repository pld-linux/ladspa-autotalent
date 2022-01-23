Summary:	Real-time pitch correction plugin for LADSPA
Summary(pl.UTF-8):	Wtyczka LADSPA do korekcji wysokości dźwięków w czasie rzeczywistym
Name:		ladspa-autotalent
Version:	0.2
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://tombaran.info/autotalent-%{version}.tar.gz
# Source0-md5:	f59443efc6ce0f4b46be86933db33acd
URL:		http://tombaran.info/autotalent.html
BuildRequires:	ladspa-devel
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Autotalent began as the result of a week of recreational signal
processing in May 2009. It's a real-time pitch correction plugin. You
specify the notes that a singer is allowed to hit, and Autotalent
makes sure that they do. You can also use Autotalent for more exotic
effects, like the Cher / T-Pain effect, making your voice sound like a
chiptune, adding artificial vibrato, or messing with your formants.
Autotalent can also be used as a harmonizer that knows how to sing in
the scale with you. Or, you can use Autotalent to change the scale of
a melody between major and minor or to change the musical mode.

%description -l pl.UTF-8
Początki wtyczki Autotalent to wynik tygodniowego rozrywkowego
przetwarzania sygnału w maju 2009. Jest to wtyczka do korekcji
wysokości dźwięków w czasie rzeczywistym. Określa się, w jakie nuty
śpiewający może trafiać, a Autotalent zapewnia, że tak będzie. Można
wtyczki używać też do bardziej egzotycznych efektów, takich jak efekt
Cher / T-Pain, powodujący, że głos brzmi jak melodia elektroniczna
poprzez dodanie sztucznego vibrato albo zaburzając formanty.
Autotalent może działać też jako harmonizer świadomy, jak śpiewać w
tej samej skali. Można też użyć jej do zmiany skali melodii między
majorową a minorową lub zmiany stylu muzycznego.

%prep
%setup -q -n autotalent-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -c -fPIC -DPIC" \
	LDFLAGS="%{rpmldflags} -nostartfiles -shared -Wl,-Bsymbolic -lc -lm -lrt" \

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ladspa

cp -p *.so $RPM_BUILD_ROOT%{_libdir}/ladspa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING*
%attr(755,root,root) %{_libdir}/ladspa/autotalent.so
