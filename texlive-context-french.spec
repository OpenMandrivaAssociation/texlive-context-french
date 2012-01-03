# revision 24582
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-french
# catalog-date 2011-11-10 06:26:05 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-context-french
Version:	20111110
Release:	2
Summary:	Support for writing French in ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-french
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-french.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-french.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context
Requires:	texlive-context

%description
Deals with spacing around French punctuation; the package is
distributed for ConTeXt Mark iv only.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/french/t-french.mkiv
%doc %{_texmfdistdir}/doc/context/third/french/french-demo.pdf
%doc %{_texmfdistdir}/doc/context/third/french/french-doc.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
