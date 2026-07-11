%global tl_name slideshow
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Generate slideshow with MetaPost
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/slideshow
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/slideshow.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/slideshow.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a means of creating presentations in MetaPost,
without intervention from other utilities (except a distiller). Such an
arrangement has its advantages (though there are disadvantages too).

