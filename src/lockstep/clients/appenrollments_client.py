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

from lockstep.lockstep_response import LockstepResponse
from lockstep.models.errorresult import ErrorResult
from lockstep.fetch_result import FetchResult
from lockstep.models.appenrollmentcustomfieldmodel import AppEnrollmentCustomFieldModel
from lockstep.models.appenrollmentmodel import AppEnrollmentModel
from lockstep.models.appenrollmentreconnectinfo import AppEnrollmentReconnectInfo
from lockstep.models.customfieldvaluemodel import CustomFieldValueModel
from lockstep.models.deleteresult import DeleteResult

class AppEnrollmentsClient:
    """
    API methods related to AppEnrollments
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_app_enrollment(self, id: str, include: str) -> LockstepResponse[AppEnrollmentModel]:
        """
        Retrieves the App Enrollment with this identifier.

        An App Enrollment represents an app that has been enrolled to
        the current account. When you sign up for an app using the
        Lockstep Platform, you obtain an enrollment record for that app.
        Example types of apps include connectors and feature enhancement
        apps. The App Enrollment object contains information about this
        app, its configuration, and settings.

        See [Applications and Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments)
        for more information.

        Parameters
        ----------
        id : str
            The unique ID number of the App Enrollment to retrieve
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: App,
            CustomFields, LastSync, LastSuccessfulSync
        """
        path = f"/api/v1/AppEnrollments/{id}"
        result = self.client.send_request("GET", path, None, {"include": include}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, AppEnrollmentModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_app_enrollment(self, id: str, body: object) -> LockstepResponse[AppEnrollmentModel]:
        """
        Updates an existing App Enrollment with the information supplied
        to this PATCH call.

        The PATCH method allows you to change specific values on the
        object while leaving other values alone. As input you should
        supply a list of field names and new values. For example, you
        can provide the field name "IsActive" and specify the new value
        "False"; this API will then change the value of IsActive to
        false.

        An App Enrollment represents an app that has been enrolled to
        the current account. When you sign up for an app using the
        Lockstep Platform, you obtain an enrollment record for that app.
        Example types of apps include connectors and feature enhancement
        apps. The App Enrollment object contains information about this
        app, its configuration, and settings.

        See [Applications and Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments)
        for more information.

        Parameters
        ----------
        id : str
            The unique ID number of the App Enrollment to update
        body : object
            A list of changes to apply to this App Enrollment
        """
        path = f"/api/v1/AppEnrollments/{id}"
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, AppEnrollmentModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_app_enrollment(self, id: str, removeEnrollmentData: bool) -> LockstepResponse[DeleteResult]:
        """
        Deletes the App Enrollment referred to by this unique
        identifier. An App Enrollment represents an app that has been
        enrolled to the current account. When you sign up for an app
        using the Lockstep Platform, you obtain an enrollment record for
        that app. Example types of apps include connectors and feature
        enhancement apps. The App Enrollment object contains information
        about this app, its configuration, and settings.

        See [Applications and Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments)
        for more information.

        Parameters
        ----------
        id : str
            The unique ID number of the App Enrollment to delete
        removeEnrollmentData : bool
            Option to remove all associated app enrollment data when
            deleting app enrollment (default false)
        """
        path = f"/api/v1/AppEnrollments/{id}"
        result = self.client.send_request("DELETE", path, None, {"removeEnrollmentData": removeEnrollmentData}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, DeleteResult(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_app_enrollments(self, startSync: bool, body: list[object]) -> LockstepResponse[list[AppEnrollmentModel]]:
        """
        Creates one or more App Enrollments within this account and
        returns the records as created.

        An App Enrollment represents an app that has been enrolled to
        the current account. When you sign up for an app using the
        Lockstep Platform, you obtain an enrollment record for that app.
        Example types of apps include connectors and feature enhancement
        apps. The App Enrollment object contains information about this
        app, its configuration, and settings.

        See [Applications and Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments)
        for more information.

        Parameters
        ----------
        startSync : bool
            Option to start sync immediately after creation of app
            enrollments (default false)
        body : list[object]
            The App Enrollments to create
        """
        path = "/api/v1/AppEnrollments"
        result = self.client.send_request("POST", path, body, {"startSync": startSync}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [AppEnrollmentModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def reconnect_app_enrollment(self, id: str, body: AppEnrollmentReconnectInfo) -> LockstepResponse[list[CustomFieldValueModel]]:
        """
        Updates the settings associated with this App Enrollment

        Parameters
        ----------
        id : str
            The id for the app enrollment
        body : AppEnrollmentReconnectInfo
            Information to reconnect the App Enrollment
        """
        path = f"/api/v1/AppEnrollments/{id}/reconnect"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [CustomFieldValueModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_app_enrollments(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[AppEnrollmentModel]]:
        """
        Queries App Enrollments for this account using the specified
        filtering, sorting, nested fetch, and pagination rules
        requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        An App Enrollment represents an app that has been enrolled to
        the current account. When you sign up for an app using the
        Lockstep Platform, you obtain an enrollment record for that app.
        Example types of apps include connectors and feature enhancement
        apps. The App Enrollment object contains information about this
        app, its configuration, and settings.

        See [Applications and Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments)
        for more information.

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: App,
            CustomFields, LastSync, LastSuccessfulSync
        order : str
            The sort order for this query. See See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageSize : int
            The page size for results (default 250, maximum of 500). See
            [Searchlight Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageNumber : int
            The page number for results (default 0). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        """
        path = "/api/v1/AppEnrollments/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), AppEnrollmentModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_enrollment_fields(self, id: str) -> LockstepResponse[FetchResult[AppEnrollmentCustomFieldModel]]:
        """
        Queries custom fields settings for app enrollment within the
        Lockstep platform using the specified filtering, sorting, nested
        fetch, and pagination rules requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        An App Enrollment represents an app that has been enrolled to
        the current account. When you sign up for an app using the
        Lockstep Platform, you obtain an enrollment record for that app.
        Example types of apps include connectors and feature enhancement
        apps. The App Enrollment object contains information about this
        app, its configuration, and settings.

        See [Applications and Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments)
        for more information.

        Parameters
        ----------
        id : str
            The unique ID number of the App Enrollment for which we
            retrieve custom fields
        """
        path = f"/api/v1/AppEnrollments/settings/{id}"
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), AppEnrollmentCustomFieldModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
