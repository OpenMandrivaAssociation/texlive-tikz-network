Name:		texlive-tikz-network
Version:	51884
Release:	1
Summary:	Draw networks with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikz-network
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-network.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-network.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows the creation of images of complex networks
that are seamlessly integrated into the underlying LaTeX files.
The package requires datatool, etex, graphicx, tikz,
trimspaces, xifthen, and xkeyval.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikz-network
%doc %{_texmfdistdir}/doc/latex/tikz-network

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
