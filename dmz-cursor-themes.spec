Name:           dmz-cursor-themes
Version:        0.4
Release:        4%{?dist}
Summary:        X cursors themes

Group:          User Interface/Desktops
License:        CC-BY-SA
URL:            http://jimmac.musichall.cz/themes.php?skin=7

%define checkout 0359f226

# NB: The tarball needs to be generated first, so the first download will fail.
#     Generating takes about 30s - 1 minute.
# wget http://gitorious.org/opensuse/art/archive-tarball/%{checkout}
# tar xzf %{checkout}
# cd opensuse-art/cursors
# tar chof - dmz dmz-aa | bzip2 -9 -c > dmz-cursor-themes-%{checkout}.tar.bz2
Source0:        dmz-cursor-themes-%{checkout}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Obsoletes:      bluecurve-cursor-theme

%description
An X cursors theme by Jakub Steiner used by OpenSUSE.

%prep
%setup -q -c dmz-cursor-themes-%{version}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_datadir}/icons/dmz
cp -pr dmz/xcursors %{buildroot}/%{_datadir}/icons/dmz/cursors
mkdir -p %{buildroot}/%{_datadir}/icons/dmz-aa
cp -pr dmz-aa/xcursors %{buildroot}/%{_datadir}/icons/dmz-aa/cursors

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc dmz/COPYING
%{_datadir}/icons/dmz/
%{_datadir}/icons/dmz-aa/

%changelog
* Tue May 04 2010 Ray Strode <rstrode@redhat.com> 0.4-4
- Add obsoletes to add upgrade path
  Resolves: #559765

* Tue Feb 16 2010 Benjamin Otte <otte@redhat.com> 0.4-3
- Update to new snapshot
- Change to new license CC-BY-SA

* Tue Feb 16 2010 Benjamin Otte <otte@redhat.com> 0.4-2
- Correct source download information

* Mon Feb 15 2010 Benjamin Otte <otte@redhat.com> 0.4-1
- Initial packaging
