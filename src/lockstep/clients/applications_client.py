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

from lockstep.lockstep_response import LockstepResponse
from lockstep.models.applicationmodel import ApplicationModel

class ApplicationsClient:

    def __init__(self, client):
        self.client = client

    """
    Retrieves the Application with this identifier. 

    An Application represents a feature available to customers within 
    the Lockstep Platform. You can create Applications by working with 
    your Lockstep business development manager and publish them on the 
    platform so that customers can browse and find your Application on 
    the Lockstep Platform Marketplace. When a customer adds an 
    Application to their account, they obtain an AppEnrollment which 
    represents that customer's instance of this Application. The 
    customer-specific AppEnrollment contains a customer's configuration 
    data for the Application, which is not customer-specific. 

    See [Applications and 
    Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments) 
    for more information.

    Parameters
    ----------
    id : str
        The unique ID number of the Application to retrieve
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. Available collections: Notes, Attachments, 
        CustomFields
    """
    def retrieve_application(self, id: str, include: str) -> LockstepResponse:
        path = f"/api/v1/Applications/{id}"
        return self.client.send_request("GET", path, None, {id: str, include: str})

    """
    Updates an existing Application with the information supplied to 
    this PATCH call. 

    The PATCH method allows you to change specific values on the object 
    while leaving other values alone. As input you should supply a list 
    of field names and new values. For example, you can provide the 
    field name "IsActive" and specify the new value "False"; this API 
    will then change the value of IsActive to false. An Application 
    represents a feature available to customers within the Lockstep 
    Platform. You can create Applications by working with your Lockstep 
    business development manager and publish them on the platform so 
    that customers can browse and find your Application on the Lockstep 
    Platform Marketplace. When a customer adds an Application to their 
    account, they obtain an AppEnrollment which represents that 
    customer's instance of this Application. The customer-specific 
    AppEnrollment contains a customer's configuration data for the 
    Application, which is not customer-specific. 

    See [Applications and 
    Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments) 
    for more information.

    Parameters
    ----------
    id : str
        The unique ID number of the Application to update
    body : object
        A list of changes to apply to this Application
    """
    def update_application(self, id: str, body: object) -> LockstepResponse:
        path = f"/api/v1/Applications/{id}"
        return self.client.send_request("PATCH", path, body, {id: str, body: object})

    """
    Deletes the Application referred to by this unique identifier. 
    Information about this Application is retained but after the DELETE 
    call, this Application is no longer available for use on the 
    Lockstep Platform. An Application represents a feature available to 
    customers within the Lockstep Platform. You can create Applications 
    by working with your Lockstep business development manager and 
    publish them on the platform so that customers can browse and find 
    your Application on the Lockstep Platform Marketplace. When a 
    customer adds an Application to their account, they obtain an 
    AppEnrollment which represents that customer's instance of this 
    Application. The customer-specific AppEnrollment contains a 
    customer's configuration data for the Application, which is not 
    customer-specific. 

    See [Applications and 
    Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments) 
    for more information.

    Parameters
    ----------
    id : str
        The unique ID number of the Application to delete
    """
    def delete_application(self, id: str) -> LockstepResponse:
        path = f"/api/v1/Applications/{id}"
        return self.client.send_request("DELETE", path, None, {id: str})

    """
    Creates one or more Applications and returns the records as created. 
    Applications are universal and available across all accounts. 

    An Application represents a feature available to customers within 
    the Lockstep Platform. You can create Applications by working with 
    your Lockstep business development manager and publish them on the 
    platform so that customers can browse and find your Application on 
    the Lockstep Platform Marketplace. When a customer adds an 
    Application to their account, they obtain an AppEnrollment which 
    represents that customer's instance of this Application. The 
    customer-specific AppEnrollment contains a customer's configuration 
    data for the Application, which is not customer-specific. 

    See [Applications and 
    Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments) 
    for more information.

    Parameters
    ----------
    body : list[ApplicationModel]
        The Applications to create
    """
    def create_applications(self, body: list[ApplicationModel]) -> LockstepResponse:
        path = f"/api/v1/Applications"
        return self.client.send_request("POST", path, body, {body: list[ApplicationModel]})

    """
    Queries Applications on the Lockstep Platform using the specified 
    filtering, sorting, nested fetch, and pagination rules requested. 

    More information on querying can be found on the [Searchlight Query 
    Language](https://developer.lockstep.io/docs/querying-with-searchlight) 
    page on the Lockstep Developer website. An Application represents a 
    feature available to customers within the Lockstep Platform. You can 
    create Applications by working with your Lockstep business 
    development manager and publish them on the platform so that 
    customers can browse and find your Application on the Lockstep 
    Platform Marketplace. When a customer adds an Application to their 
    account, they obtain an AppEnrollment which represents that 
    customer's instance of this Application. The customer-specific 
    AppEnrollment contains a customer's configuration data for the 
    Application, which is not customer-specific. 

    See [Applications and 
    Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments) 
    for more information.

    Parameters
    ----------
    filter : str
        The filter for this query. See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. Available collections: Notes, Attachments, 
        CustomFields
    order : str
        The sort order for this query. See See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageSize : int
        The page size for results (default 200). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageNumber : int
        The page number for results (default 0). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    """
    def query_applications(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        path = f"/api/v1/Applications/query"
        return self.client.send_request("GET", path, None, {filter: str, include: str, order: str, pageSize: int, pageNumber: int})
