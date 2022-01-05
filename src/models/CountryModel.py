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
# @version    2021.39
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#




# Country model for ISO-3166
class CountryModel:
    name: str
    alpha2: str
    alpha3: str
    countryCode: int
    region: str
    subRegion: str
    intermediateRegion: str
    regionCode: int
    subRegionCode: int
    intermediateRegionCode: int
    frenchName: str
    aliases: str

