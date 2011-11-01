Name:		texlive-context-french
Version:	20091011
Release:	1
Summary:	Support for writing French in ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-french
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-french.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-french.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-context
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Requires(post):	texlive-context.bin

%description
Deals with spacing around French punctuation.

%pre
    %_texmf_mtxrun_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mtxrun_post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_post
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/french/t-french.tex
%doc %{_texmfdistdir}/doc/context/third/french/french-demo.pdf
%doc %{_texmfdistdir}/doc/context/third/french/french-doc.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
