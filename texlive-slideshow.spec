Name:		texlive-slideshow
Version:	15878
Release:	2
Summary:	Generate slideshow with MetaPost
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/slideshow
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/slideshow.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/slideshow.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a means of creating presentations in
MetaPost, without intervention from other utilities (except a
distiller). Such an arrangement has its advantages (though
there are disadvantages too).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/slideshow/pathalong.mp
%{_texmfdistdir}/metapost/slideshow/slideshow.mp
%{_texmfdistdir}/metapost/slideshow/sshowex.mp
%{_texmfdistdir}/metapost/slideshow/sshowex2.mp
%{_texmfdistdir}/metapost/slideshow/sshowex3.mp
%{_texmfdistdir}/metapost/slideshow/sshowintro.mp
%doc %{_texmfdistdir}/doc/metapost/slideshow/slideshow.txt
%doc %{_texmfdistdir}/doc/metapost/slideshow/sshowex.pdf
%doc %{_texmfdistdir}/doc/metapost/slideshow/sshowex2.pdf
%doc %{_texmfdistdir}/doc/metapost/slideshow/sshowex3.pdf
%doc %{_texmfdistdir}/doc/metapost/slideshow/sshowintro.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
