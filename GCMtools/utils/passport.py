# ==============================================================
#                         Passport file
# ==============================================================
#  This file is used to classify input data. All functionalities
#  here return a boolean which states True if the given input
#  dataset fulfills all the classification requirements of the
#  given function. The check for a basic function will raise a
#  value error if the conditions are not fulfilled.
# ==============================================================

import GCMtools.core.writer as wrt
from GCMtools.core.const import VARNAMES as c


def is_the_data_basic(dataset):
    """
    Check if the dataset fulfills the minimal requirements for
    a dataset to be used with GCMtools. If not, this function
    raises a Value error.

    Parameters
    ----------
    dataset : xarray.Dataset
        Short description of the variable.

    Returns
    -------
    bool
        Returns true if the dataset fulfills the basic
        requirements or raises a Value error if not.
    """

    # general information
    __author__ = 'Sven Kiefer'

    # set up trigger variable
    is_the_data_ok = True

    # get names of all data variables and attributes
    data_variables = list(dataset.keys())
    data_coords = list(dataset.coords)
    data_attributes = dataset.attrs

    to_be_checked_coords = [c['lon'], c['lat'], c['Z'], c['time']]

    for dim in to_be_checked_coords:
        if dim not in data_coords:
            is_the_data_ok = False
            wrt.write_status('E-INFO', 'The dataset "' + str(dataset.attrs['tag']) + '" does ' +
                             f'not contain {dim} information and ' +
                             'therefore does not qualify as a basic GCM dataset.')

    if c['T'] not in data_variables:
        is_the_data_ok = False
        wrt.write_status('E-INFO', 'The dataset "' + str(dataset.attrs['tag']) + '" does ' +
                         f'not contain {c["T"]} (temperature) information and ' +
                         'therefore does not qualify as a basic GCM dataset.')

    if c['U'] not in data_variables:
        is_the_data_ok = False
        wrt.write_status('E-INFO', 'The dataset "' + str(dataset.attrs['tag']) + '" does ' +
                         f'not contain {c["U"]} (equatorial wind) information and ' +
                         'therefore does not qualify as a basic GCM dataset.')

    if c['V'] not in data_variables:
        is_the_data_ok = False
        wrt.write_status('E-INFO', 'The dataset "' + str(dataset.attrs['tag']) + '" does ' +
                         f'not contain {c["V"]} (polar wind) information and ' +
                         'therefore does not qualify as a basic GCM dataset.')

    if c['W'] not in data_variables:
        is_the_data_ok = False
        wrt.write_status('E-INFO', 'The dataset "' + str(dataset.attrs['tag']) + '" does ' +
                         f'not contain {c["W"]} (vertical wind) information and ' +
                         'therefore does not qualify as a basic GCM dataset.')

    if c['g'] not in data_attributes:
        is_the_data_ok = False
        wrt.write_status('E-INFO', 'The dataset "' + str(dataset.attrs['tag']) + '" does ' +
                         f'not contain {c["g"]} (avarage gravity) information and ' +
                         'therefore does not qualify as a basic GCM dataset.')

    if c['P_rot'] not in data_attributes:
        is_the_data_ok = False
        wrt.write_status('E-INFO', 'The dataset "' + str(dataset.attrs['tag']) + '" does ' +
                         f'not contain {c["P_rot"]} (rotational period) information and ' +
                         'therefore does not qualify as a basic GCM dataset.')

    if c['P_orb'] not in data_attributes:
        is_the_data_ok = False
        wrt.write_status('E-INFO', 'The dataset "' + str(dataset.attrs['tag']) + '" does ' +
                         f'not contain {c["P_orb"]} (orbital period) information and ' +
                         'therefore does not qualify as a basic GCM dataset.')

    if c['R_p'] not in data_attributes:
        is_the_data_ok = False
        wrt.write_status('E-INFO', 'The dataset "' + str(dataset.attrs['tag']) + '" does ' +
                         f'not contain {c["R_p"]} (planet radius) information and ' +
                         'therefore does not qualify as a basic GCM dataset.')

    if not is_the_data_ok:
        wrt.write_status('ERROR', 'The data does not fulfill the ' +
                         'requirements for a basic dataset.')

    # dataset fulfilled all checks
    return True


def is_the_data_cloudy(dataset):
    """
    Check if the dataset fulfills the minimal requirements for
    a dataset to be used with GCMtools.

    Parameters
    ----------
    dataset : xarray.Dataset
        Short description of the variable.

    Returns
    -------
    bool
        Returns true if the dataset fulfills the basic
        requirements or False if not.
    """

    # general information
    __author__ = 'Sven Kiefer'

    # check first if the dataset fulfills the basic requirements
    is_the_data_basic(dataset)

    # get names of all data variables and attributes
    data_variables = list(dataset.keys())

    # variable to check if everything is OK
    is_the_data_ok = True

    if 'ClAb' not in data_variables:
        wrt.write_status('WARN', 'ClAb (cloud abundance) is missing from the dataset '
                         + str(dataset.attrs['tag']))
        is_the_data_ok = False

    if 'ClDr' not in data_variables:
        wrt.write_status('WARN', 'ClDr (cloud particle radius) is missing from the dataset '
                         + str(dataset.attrs['tag']))
        is_the_data_ok = False

    if 'ClKs' not in data_variables:
        wrt.write_status('WARN', 'ClKs (cloud scattering opacity) is missing from the dataset '
                         + str(dataset.attrs['tag']))
        is_the_data_ok = False

    if 'ClKa' not in data_variables:
        wrt.write_status('WARN', 'ClKa (cloud absorption opacity) is missing from the dataset '
                         + str(dataset.attrs['tag']))
        is_the_data_ok = False

    # return status of the check
    return is_the_data_ok
