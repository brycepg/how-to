How to find files installed by a package on Linux
#################################################

Replace `Foo` with your package name.

Debian/Ubuntu
=============

::

    dpkg -L Foo

Centos/RHEL
===========

For a rpm package::

    rpm -qpl foo.rpm

For a package in yum::

    repoquery --installed -l Foo

remove `--installed` if you haven't installed the package yet.

Fedora 23+
==========

dnf repoquery Foo

