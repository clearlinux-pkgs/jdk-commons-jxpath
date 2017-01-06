#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jdk-commons-jxpath
Version  : 1.3
Release  : 3
URL      : http://www.apache.org/dist/commons/jxpath/source/commons-jxpath-1.3-src.tar.gz
Source0  : http://www.apache.org/dist/commons/jxpath/source/commons-jxpath-1.3-src.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-commons-jxpath-data
BuildRequires : apache-ant
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-apache-parent
BuildRequires : jdk-aqute-bndlib
BuildRequires : jdk-atinject
BuildRequires : jdk-bsh
BuildRequires : jdk-build-helper-maven-plugin
BuildRequires : jdk-buildnumber-maven-plugin
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-beanutils
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-digester
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-commons-parent
BuildRequires : jdk-commons-validator
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-integration-tools
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-eclipse-eclipse
BuildRequires : jdk-eclipse-osgi
BuildRequires : jdk-eclipse-osgi-services
BuildRequires : jdk-enforcer
BuildRequires : jdk-felix
BuildRequires : jdk-felix-bundlerepository
BuildRequires : jdk-felix-framework
BuildRequires : jdk-felix-osgi-foundation
BuildRequires : jdk-felix-utils
BuildRequires : jdk-glassfish-jsp-api
BuildRequires : jdk-glassfish-servlet-api
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-hamcrest
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jdom
BuildRequires : jdk-jna
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-junit4
BuildRequires : jdk-kxml
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-antrun-plugin
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-artifact-resolver
BuildRequires : jdk-maven-bundle-plugin
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-dependency-tree
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-jar-plugin
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-plugin-testing
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-remote-resources-plugin
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-reporting-exec
BuildRequires : jdk-maven-reporting-impl
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-scm
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-maven-site-plugin
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-osgi-compendium
BuildRequires : jdk-osgi-core
BuildRequires : jdk-parboiled
BuildRequires : jdk-pegdown
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-resources
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy-java
BuildRequires : jdk-surefire
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xerces-j2
BuildRequires : jdk-xml-apis
BuildRequires : jdk-xmlunit
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn
Patch1: commons-jxpath-mockrunner.patch

%description
No detailed description available

%package data
Summary: data components for the jdk-commons-jxpath package.
Group: Data

%description data
data components for the jdk-commons-jxpath package.


%prep
%setup -q -n commons-jxpath-1.3-src
%patch1 -p1

python3 /usr/share/java-utils/mvn_file.py ":{*}" apache-commons-jxpath @1
python3 /usr/share/java-utils/mvn_alias.py : org.apache.commons:
python3 /usr/share/java-utils/pom_editor.py pom_xpath_inject   'pom:properties' \
'<commons.osgi.import>org.apache.commons.beanutils;resolution:="optional",org.jdom*;resolution:="optional",org.w3c.dom;resolution:="optional",*</commons.osgi.import>'

%build
python3 /usr/share/java-utils/mvn_build.py -f

%install
xmvn-install  -R .xmvn-reactor -n apache-commons-jxpath -d %{buildroot}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/apache-commons-jxpath.jar
/usr/share/java/commons-jxpath.jar
/usr/share/maven-metadata/apache-commons-jxpath.xml
/usr/share/maven-poms/apache-commons-jxpath.pom
/usr/share/maven-poms/commons-jxpath.pom
