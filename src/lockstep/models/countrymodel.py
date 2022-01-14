#
# Lockstep Software Development Kit for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Ted Spence <tspence@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @version    2022.2
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

"""
Country model for ISO-3166
"""
@dataclass
class CountryModel:
    name: str = None
    alpha2: str = None
    alpha3: str = None
    countryCode: int = None
    region: str = None
    subRegion: str = None
    intermediateRegion: str = None
    regionCode: int = None
    subRegionCode: int = None
    intermediateRegionCode: int = None
    frenchName: str = None
    aliases: str = None

