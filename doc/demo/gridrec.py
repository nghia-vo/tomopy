#!/usr/bin/env python
from __future__ import print_function

if __name__ == '__main__':

    # Set path to the micro-CT data to reconstruct.

    # Select the sinogram range to reconstruct.
    end = 2

    # Read the APS 2-BM 0r 32-ID raw data.

    # Set data collection angles as equally spaced between 0-180 degrees.

    # Set data collection angles as equally spaced between 0-180 degrees.

    # Set data collection angles as equally spaced between 0-180 degrees.

    proj = tomopy.minus_log(proj)

    # Reconstruct object using Gridrec algorithm.

    # Mask each reconstructed slice with a circle.

    # Write data as stack of TIFs.