#
# Lockstep Platform SDK for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#

from lockstep.lockstep_response import LockstepResponse
from lockstep.models.errorresult import ErrorResult
from lockstep.fetch_result import FetchResult
from lockstep.models.publiccompanyprofilemodel import PublicCompanyProfileModel

class ProfilesClient:
    """
    API methods related to Profiles
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_public_company_profile(self, urlSlug: str) -> LockstepResponse[PublicCompanyProfileModel]:
        """
        Retrieves the Public Company Profile specified by the public url
        slug.

        A Public Company Profile makes available the following
        information: <list type="bullet"><item>Company
        Name</item><item>Company Logo
        Url</item><item>Description</item><item>Website</item></list>

        Parameters
        ----------
        urlSlug : str

        """
        path = f"/api/v1/Profiles/companies/{urlSlug}"
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, PublicCompanyProfileModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def query_public_company_profiles(self, filter: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[PublicCompanyProfileModel]]:
        """
        Queries Public Company Profiles <p> More information on querying
        can be found on the [Searchlight Query
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website. </p><p> A Public Company
        Profile makes available the following information:

        <list type="bullet"><item>`Company Name` </item><item>`Company
        Logo Url` </item><item>`Description` </item><item>`Website`
        </item></list></p>

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        order : str
            The sort order for the results, in the [Searchlight order
            syntax](https://github.com/tspence/csharp-searchlight).
        pageSize : int
            The page size for results (default 200, maximum of 10,000)
        pageNumber : int
            The page number for results (default 0)
        """
        path = "/api/v1/Profiles/companies/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult[PublicCompanyProfileModel](**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))
