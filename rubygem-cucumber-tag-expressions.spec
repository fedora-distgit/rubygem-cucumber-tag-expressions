# Generated from cucumber-tag-expressions-4.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name cucumber-tag-expressions

Name: rubygem-%{gem_name}
Version: 4.0.0
Release: 1%{?dist}
Summary: cucumber-tag-expressions-4.0.0
License: MIT
URL: https://cucumber.io/docs/cucumber/api/#tag-expressions
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.3
# BuildRequires: rubygem(rspec) >= 3.10
# BuildRequires: rubygem(rspec) < 4
# BuildRequires: rubygem(rspec) >= 3.10.0
BuildArch: noarch

%description
Cucumber tag expressions for ruby.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
pushd .%{gem_instdir}
# rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec

%changelog
* Thu Sep 09 2021 Jarek Prokop <jprokop@redhat.com> - 4.0.0-1
- Initial package
