Summary:	UI for KDE Telepathy text messaging
Name:		ktp-text-ui
Version:	22.12.1
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		ktp-text-ui-logviewer-in-More-menu.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Designer)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5ScriptTools)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5WebKit)
BuildRequires:	cmake(Qt5WebEngine)
BuildRequires:	cmake(Qt5WebEngineWidgets)
BuildRequires:	cmake(Qt5TextToSpeech)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(TelepathyQt5)
BuildRequires:	cmake(TelepathyLoggerQt)
BuildRequires:	cmake(KTp)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5WebKit)
BuildRequires:	cmake(Qca-qt5)
BuildRequires:	cmake(AccountsQt5)
BuildRequires:	cmake(SignOnQt5)
BuildRequires:	cmake(KAccounts)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5People)
BuildRequires:	cmake(KF5IdleTime)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Sonnet)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Emoticons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	pkgconfig(shared-mime-info)

%description
UI for KDE Telepathy text messaging.

%files -f all.lang
%{_bindir}/ktp-log-viewer
%{_libdir}/libexec/ktp-adiumxtra-protocol-handler
%{_libdir}/libexec/ktp-text-ui
%{_libdir}/libktpchat.so
%{_libdir}/libktpimagesharer.so
%{_libdir}/qt5/plugins/kcm_ktp_chat_appearance.so
%{_libdir}/qt5/plugins/kcm_ktp_chat_behavior.so
%{_libdir}/qt5/plugins/kcm_ktp_chat_messages.so
%{_libdir}/qt5/plugins/kcm_ktp_chat_otr.so
%{_libdir}/qt5/plugins/kcm_ktp_logviewer_behavior.so
%{_libdir}/qt5/plugins/kcm_ktptextui_message_filter_emoticons.so
%{_libdir}/qt5/plugins/kcm_ktptextui_message_filter_latex.so
%{_libdir}/qt5/plugins/ktptextui_message_filter_bugzilla.so
%{_libdir}/qt5/plugins/ktptextui_message_filter_emoticons.so
%{_libdir}/qt5/plugins/ktptextui_message_filter_formatting.so
%{_libdir}/qt5/plugins/ktptextui_message_filter_geopoint.so
%{_libdir}/qt5/plugins/ktptextui_message_filter_highlight.so
%{_libdir}/qt5/plugins/ktptextui_message_filter_images.so
%{_libdir}/qt5/plugins/ktptextui_message_filter_latex.so
%{_libdir}/qt5/plugins/ktptextui_message_filter_otr.so
%{_libdir}/qt5/plugins/ktptextui_message_filter_searchexpansion.so
%{_libdir}/qt5/plugins/ktptextui_message_filter_tts.so
%{_libdir}/qt5/plugins/ktptextui_message_filter_urlexpansion.so
%{_libdir}/qt5/plugins/ktptextui_message_filter_youtube.so
%{_datadir}/applications/org.kde.ktplogviewer.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.TextUi.service
%{_datadir}/kservices5/adiumxtra.protocol
%{_datadir}/kservices5/kcm_ktp_chat_appearance.desktop
%{_datadir}/kservices5/kcm_ktp_chat_behavior.desktop
%{_datadir}/kservices5/kcm_ktp_chat_messages.desktop
%{_datadir}/kservices5/kcm_ktp_chat_otr.desktop
%{_datadir}/kservices5/kcm_ktp_logviewer_behavior.desktop
%{_datadir}/kservices5/kcm_ktptextui_message_filter_emoticons.desktop
%{_datadir}/kservices5/kcm_ktptextui_message_filter_latex.desktop
%{_datadir}/kservices5/ktptextui_message_filter_bugzilla.desktop
%{_datadir}/kservices5/ktptextui_message_filter_emoticons.desktop
%{_datadir}/kservices5/ktptextui_message_filter_formatting.desktop
%{_datadir}/kservices5/ktptextui_message_filter_geopoint.desktop
%{_datadir}/kservices5/ktptextui_message_filter_highlight.desktop
%{_datadir}/kservices5/ktptextui_message_filter_images.desktop
%{_datadir}/kservices5/ktptextui_message_filter_latex.desktop
%{_datadir}/kservices5/ktptextui_message_filter_otr.desktop
%{_datadir}/kservices5/ktptextui_message_filter_searchexpansion.desktop
%{_datadir}/kservices5/ktptextui_message_filter_tts.desktop
%{_datadir}/kservices5/ktptextui_message_filter_urlexpansion.desktop
%{_datadir}/kservices5/ktptextui_message_filter_youtube.desktop
%{_datadir}/kservicetypes5/ktptxtui_message_filter.desktop
%{_datadir}/ktelepathy
%{_datadir}/ktp-log-viewer
%{_datadir}/kxmlgui5/ktp-text-ui
%{_datadir}/telepathy/clients/KTp.TextUi.client


%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kcm_ktp_chat_appearance
%find_lang kcm_ktp_chat_behavior
%find_lang kcm_ktp_chat_messages
%find_lang kcm_ktp_chat_otr
%find_lang ktp-adiumxtra-protocol-handler
%find_lang ktp-filters
%find_lang ktp-log-viewer
%find_lang ktp-text-ui
%find_lang ktpchat
cat *.lang >all.lang
