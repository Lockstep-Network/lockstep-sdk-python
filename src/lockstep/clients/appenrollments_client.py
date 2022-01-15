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
from lockstep.models.appenrollmentmodel import AppEnrollmentModel

class AppEnrollmentsClient:

    def __init__(self, client):
        self.client = client

    """
    Retrieves the App Enrollment with this identifier. 

    An App Enrollment represents an app that has been enrolled to the 
    current account. When you sign up for an app using the Lockstep 
    Platform, you obtain an enrollment record for that app. Example 
    types of apps include connectors and feature enhancement apps. The 
    App Enrollment object contains information about this app, its 
    configuration, and settings. 

    See [Applications and 
    Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments) 
    for more information.

    Parameters
    ----------
    id : str
        The unique ID number of the App Enrollment to retrieve
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. Available collections: App, CustomFields
    """
    def retrieve_app_enrollment(self, id: str, include: str) -> LockstepResponse:
        path = f"/api/v1/AppEnrollments/{id}"
        return self.client.send_request("GET", path, None, {id: str, include: str})

    """
    Updates an existing App Enrollment with the information supplied to 
    this PATCH call. 

    The PATCH method allows you to change specific values on the object 
    while leaving other values alone. As input you should supply a list 
    of field names and new values. For example, you can provide the 
    field name "IsActive" and specify the new value "False"; this API 
    will then change the value of IsActive to false. 

    An App Enrollment represents an app that has been enrolled to the 
    current account. When you sign up for an app using the Lockstep 
    Platform, you obtain an enrollment record for that app. Example 
    types of apps include connectors and feature enhancement apps. The 
    App Enrollment object contains information about this app, its 
    configuration, and settings. 

    See [Applications and 
    Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments) 
    for more information.

    Parameters
    ----------
    id : str
        The unique ID number of the App Enrollment to update
    body : object
        A list of changes to apply to this App Enrollment
    """
    def update_app_enrollment(self, id: str, body: object) -> LockstepResponse:
        path = f"/api/v1/AppEnrollments/{id}"
        return self.client.send_request("PATCH", path, body, {id: str, body: object})

    """
    Deletes the App Enrollment referred to by this unique identifier. An 
    App Enrollment represents an app that has been enrolled to the 
    current account. When you sign up for an app using the Lockstep 
    Platform, you obtain an enrollment record for that app. Example 
    types of apps include connectors and feature enhancement apps. The 
    App Enrollment object contains information about this app, its 
    configuration, and settings. 

    See [Applications and 
    Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments) 
    for more information.

    Parameters
    ----------
    id : str
        The unique ID number of the App Enrollment to delete
    removeEnrollmentData : bool
        Option to remove all associated app enrollment data when 
        deleting app enrollment (default false)
    """
    def delete_app_enrollment(self, id: str, removeEnrollmentData: bool) -> LockstepResponse:
        path = f"/api/v1/AppEnrollments/{id}"
        return self.client.send_request("DELETE", path, None, {id: str, removeEnrollmentData: bool})

    """
    Creates one or more App Enrollments within this account and returns 
    the records as created. 

    An App Enrollment represents an app that has been enrolled to the 
    current account. When you sign up for an app using the Lockstep 
    Platform, you obtain an enrollment record for that app. Example 
    types of apps include connectors and feature enhancement apps. The 
    App Enrollment object contains information about this app, its 
    configuration, and settings. 

    See [Applications and 
    Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments) 
    for more information.

    Parameters
    ----------
    body : list[AppEnrollmentModel]
        The App Enrollments to create
    """
    def create_app_enrollments(self, body: list[AppEnrollmentModel]) -> LockstepResponse:
        path = f"/api/v1/AppEnrollments"
        return self.client.send_request("POST", path, body, {body: list[AppEnrollmentModel]})

    """
    Queries App Enrollments for this account using the specified 
    filtering, sorting, nested fetch, and pagination rules requested. 

    More information on querying can be found on the [Searchlight Query 
    Language](https://developer.lockstep.io/docs/querying-with-searchlight) 
    page on the Lockstep Developer website. 

    An App Enrollment represents an app that has been enrolled to the 
    current account. When you sign up for an app using the Lockstep 
    Platform, you obtain an enrollment record for that app. Example 
    types of apps include connectors and feature enhancement apps. The 
    App Enrollment object contains information about this app, its 
    configuration, and settings. 

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
        elements to retrieve. Available collections: App, CustomFields, 
        LastSync
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
    def query_app_enrollments(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        path = f"/api/v1/AppEnrollments/query"
        return self.client.send_request("GET", path, None, {filter: str, include: str, order: str, pageSize: int, pageNumber: int})

    """
    Queries custom fields settings for app enrollment within the 
    Lockstep platform using the specified filtering, sorting, nested 
    fetch, and pagination rules requested. 

    More information on querying can be found on the [Searchlight Query 
    Language](https://developer.lockstep.io/docs/querying-with-searchlight) 
    page on the Lockstep Developer website. 

    An App Enrollment represents an app that has been enrolled to the 
    current account. When you sign up for an app using the Lockstep 
    Platform, you obtain an enrollment record for that app. Example 
    types of apps include connectors and feature enhancement apps. The 
    App Enrollment object contains information about this app, its 
    configuration, and settings. 

    See [Applications and 
    Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments) 
    for more information.

    Parameters
    ----------
    id : str
        The unique ID number of the App Enrollment for which we retrieve 
        custom fields
    """
    def query_enrollment_fields(self, id: str) -> LockstepResponse:
        path = f"/api/v1/AppEnrollments/settings/{id}"
        return self.client.send_request("GET", path, None, {id: str})
