##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class RDownloader(RPackage):
    """Provides a wrapper for the download.file function, making it possible to
       download files over HTTPS on Windows, Mac OS X, and other Unix-like
       platforms. The 'RCurl' package provides this functionality
       (and much more) but can be difficult to install because it must be
       compiled with external dependencies. This package has no external
       dependencies, so it is much easier to install."""

    homepage = "https://cran.rstudio.com/web/packages/downloader/index.html"
    url      = "https://cran.rstudio.com/src/contrib/downloader_0.4.tar.gz"
    list_url = homepage

    version('0.4', 'f26daf8fbeb29a1882bf102f62008594')

    depends_on('r-digest', type=('build', 'run'))
