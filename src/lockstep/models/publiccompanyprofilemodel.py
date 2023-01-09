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
class PublicCompanyProfileModel:
    """
    Contains Public Company Profile data.
    """

    companyId: str | None = None
    companyName: str | None = None
    companyLogoUrl: str | None = None
    website: str | None = None
    description: str | None = None
    publicUrlSlug: str | None = None

