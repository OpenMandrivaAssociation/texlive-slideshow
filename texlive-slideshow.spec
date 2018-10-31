# revision 15878
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/slideshow
# catalog-date 2008-12-04 14:14:32 +0100
# catalog-license other-free
# catalog-version 1.0
Name:		texlive-slideshow
Version:	1.0
Release:	11
Summary:	Generate slideshow with MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/slideshow
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/slideshow.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/slideshow.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 756069
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719551
- texlive-slideshow
- texlive-slideshow
- texlive-slideshow
- texlive-slideshow

