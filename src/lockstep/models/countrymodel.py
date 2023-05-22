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

    name: object | None = None
    alpha2: object | None = None
    alpha3: object | None = None
    countryCode: object | None = None
    region: object | None = None
    subRegion: object | None = None
    intermediateRegion: object | None = None
    regionCode: object | None = None
    subRegionCode: object | None = None
    intermediateRegionCode: object | None = None
    frenchName: object | None = None
    aliases: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
