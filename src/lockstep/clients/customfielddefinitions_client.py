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
from lockstep.models.actionresultmodel import ActionResultModel
from lockstep.models.customfielddefinitionmodel import CustomFieldDefinitionModel

class CustomFieldDefinitionsClient:
    """
    API methods related to CustomFieldDefinitions
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_field_definition(self, id: str, include: str) -> LockstepResponse[CustomFieldDefinitionModel]:
        """
        Retrieves the Custom Field Definition specified by this unique
        identifier.

        A Custom Field represents metadata added to an object within the
        Lockstep Platform. Lockstep provides a core definition for each
        object. The core definition is intended to represent a level of
        compatibility that provides support across most accounting
        systems and products. When a user or developer requires
        information beyond this core definition, you can use Custom
        Fields to represent this information.

        See [Extensibility](https://developer.lockstep.io/docs/extensibility)
        for more information.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of this Custom Field
            Definition
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. No additional data collections are
            currently defined on this object, but may be supported in
            the future.
        """
        path = f"/api/v1/CustomFieldDefinitions/{id}"
        result = self.client.send_request("GET", path, None, {"include": include}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, CustomFieldDefinitionModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_field_definition(self, id: str, body: object) -> LockstepResponse[CustomFieldDefinitionModel]:
        """
        Updates an existing Custom Field Definition with the information
        supplied to this PATCH call.

        The PATCH method allows you to change specific values on the
        object while leaving other values alone. As input you should
        supply a list of field names and new values. If you do not
        provide the name of a field, that field will remain unchanged.
        This allows you to ensure that you are only updating the
        specific fields desired.

        A Custom Field represents metadata added to an object within the
        Lockstep Platform. Lockstep provides a core definition for each
        object. The core definition is intended to represent a level of
        compatibility that provides support across most accounting
        systems and products. When a user or developer requires
        information beyond this core definition, you can use Custom
        Fields to represent this information.

        See [Extensibility](https://developer.lockstep.io/docs/extensibility)
        for more information.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Custom Field
            Definition to update
        body : object
            A list of changes to apply to this Custom Field Definition
        """
        path = f"/api/v1/CustomFieldDefinitions/{id}"
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, CustomFieldDefinitionModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_field_definition(self, id: str) -> LockstepResponse[ActionResultModel]:
        """
        Deletes the Custom Field Definition referred to by this unique
        identifier.

        A Custom Field represents metadata added to an object within the
        Lockstep Platform. Lockstep provides a core definition for each
        object. The core definition is intended to represent a level of
        compatibility that provides support across most accounting
        systems and products. When a user or developer requires
        information beyond this core definition, you can use Custom
        Fields to represent this information.

        See [Extensibility](https://developer.lockstep.io/docs/extensibility)
        for more information.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Custom Field
            Definition to delete
        """
        path = f"/api/v1/CustomFieldDefinitions/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ActionResultModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_field_definitions(self, body: list[object]) -> LockstepResponse[list[CustomFieldDefinitionModel]]:
        """
        Creates one or more Custom Field Definitions and returns the
        records as created.

        A Custom Field represents metadata added to an object within the
        Lockstep Platform. Lockstep provides a core definition for each
        object. The core definition is intended to represent a level of
        compatibility that provides support across most accounting
        systems and products. When a user or developer requires
        information beyond this core definition, you can use Custom
        Fields to represent this information.

        See [Extensibility](https://developer.lockstep.io/docs/extensibility)
        for more information.

        Parameters
        ----------
        body : list[object]
            The Custom Field Definitions to create
        """
        path = "/api/v1/CustomFieldDefinitions"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [CustomFieldDefinitionModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_field_definitions(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[CustomFieldDefinitionModel]]:
        """
        Queries Custom Field Definitions within the Lockstep platform
        using the specified filtering, sorting, nested fetch, and
        pagination rules requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        A Custom Field represents metadata added to an object within the
        Lockstep Platform. Lockstep provides a core definition for each
        object. The core definition is intended to represent a level of
        compatibility that provides support across most accounting
        systems and products. When a user or developer requires
        information beyond this core definition, you can use Custom
        Fields to represent this information.

        See [Extensibility](https://developer.lockstep.io/docs/extensibility)
        for more information.

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. No additional data collections are
            currently defined on this object, but may be supported in
            the future.
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
        path = "/api/v1/CustomFieldDefinitions/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), CustomFieldDefinitionModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
