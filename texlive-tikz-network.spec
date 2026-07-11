%global tl_name tikz-network
%global tl_revision 51884

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Draw networks with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-network
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-network.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-network.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows the creation of images of complex networks that are
seamlessly integrated into the underlying LaTeX files. The package
requires datatool, etex, graphicx, tikz, trimspaces, xifthen, and
xkeyval.

