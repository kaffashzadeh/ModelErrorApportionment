# ModelErrorApportionment

[![DOI](https://zenodo.org/badge/489897422.svg)](https://zenodo.org/badge/latestdoi/489897422)

This is a scripts to evaluate a model outputs using a comprehensive indicator, i.e.
mean square error and its apportions.

**How to run it?**

After obtaining the package on your system, to run: 

- on a terminal
> cd ModelErrorApportionment/src

> python3 MEA.py

- import to another script:

> from MEA import ApportionError

> ApportionError(file_name_obs='temp_obs', file_name_model='temp_m1').run()


More details of the methodology along with an example are provided in: 
[An Intercomparison of two Reanalysis Datasets CAMS vs. ERA5](https://www.nigsconference.ir/article_8614.pdf)

