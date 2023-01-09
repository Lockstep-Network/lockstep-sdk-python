#
# Lockstep Platform SDK for Python
#
# (c) 2021-2023 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2023 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

@dataclass
class CountryModel:
    """
    Country model for ISO-3166
    """

    name: str | None = None
    alpha2: str | None = None
    alpha3: str | None = None
    countryCode: int | None = None
    region: str | None = None
    subRegion: str | None = None
    intermediateRegion: str | None = None
    regionCode: int | None = None
    subRegionCode: int | None = None
    intermediateRegionCode: int | None = None
    frenchName: str | None = None
    aliases: str | None = None

