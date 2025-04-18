#################################################################################
# FOQUS Copyright (c) 2012 - 2025, by the software owners: Oak Ridge Institute
# for Science and Education (ORISE), TRIAD National Security, LLC., Lawrence
# Livermore National Security, LLC., The Regents of the University of
# California, through Lawrence Berkeley National Laboratory, Battelle Memorial
# Institute, Pacific Northwest Division through Pacific Northwest National
# Laboratory, Carnegie Mellon University, West Virginia University, Boston
# University, the Trustees of Princeton University, The University of Texas at
# Austin, URS Energy & Construction, Inc., et al.  All rights reserved.
#
# Please see the file LICENSE.md for full copyright and license information,
# respectively. This file is also available online at the URL
# "https://github.com/CCSI-Toolset/FOQUS".
#################################################################################
import subprocess


# ---------------------------------------
# ACOSSO fit function
# ---------------------------------------
def fit(
    rscriptPath, xdatfile, ydatfile, modelfile, order="2", cv="bic", categorical="auto"
):

    p = subprocess.Popen(
        [
            rscriptPath,
            "acosso_fit.R",
            xdatfile,
            ydatfile,
            modelfile,
            order,
            cv,
            categorical,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = p.communicate()
    #   print stdout
    #   print stderr

    return modelfile


# ---------------------------------------
# Example usage
# ---------------------------------------
rdsfile = fit(
    "C:\\Program Files\\R\\R-3.1.2\\bin\\x64\\Rscript.exe",
    "xdat.csv",
    "ydat.csv",
    "acosso_fit.rds",
)
# rdsfile = fit('xdat.csv','ydat.csv','acosso_fit.rds',categorical='[1,2]')
print(rdsfile)
