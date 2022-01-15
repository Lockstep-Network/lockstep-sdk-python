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
from lockstep.models.customfieldvaluemodel import CustomFieldValueModel

class CustomFieldValuesClient:

    def __init__(self, client):
        self.client = client

    """
    Retrieves all Custom Field Definitions. 

    A Custom Field represents metadata added to an object within the 
    Lockstep Platform. Lockstep provides a core definition for each 
    object. The core definition is intended to represent a level of 
    compatibility that provides support across most accounting systems 
    and products. When a user or developer requires information beyond 
    this core definition, you can use Custom Fields to represent this 
    information. See 
    [Extensibility](https://developer.lockstep.io/docs/extensibility) 
    for more information.

    Parameters
    ----------
    definitionId : str
        The unique Lockstep Platform ID number of the Custom Field 
        Definition for the Custom Field Value to retrieve.
    recordKey : str
        The unique Lockstep Platform ID number of the Lockstep Platform 
        object the Custom Field Value is attached to.
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. Available collections: 
        CustomFieldDefinition
    """
    def retrieve_field(self, definitionId: str, recordKey: str, include: str) -> LockstepResponse:
        path = f"/api/v1/CustomFieldValues/{definitionId}/{recordKey}"
        return self.client.send_request("GET", path, None, {definitionId: str, recordKey: str, include: str})

    """
    Updates an existing Custom Field with the information supplied to 
    this PATCH call. 

    The PATCH method allows you to change specific values on the object 
    while leaving other values alone. As input you should supply a list 
    of field names and new values. If you do not provide the name of a 
    field, that field will remain unchanged. This allows you to ensure 
    that you are only updating the specific fields desired. 

    A Custom Field represents metadata added to an object within the 
    Lockstep Platform. Lockstep provides a core definition for each 
    object. The core definition is intended to represent a level of 
    compatibility that provides support across most accounting systems 
    and products. When a user or developer requires information beyond 
    this core definition, you can use Custom Fields to represent this 
    information. See 
    [Extensibility](https://developer.lockstep.io/docs/extensibility) 
    for more information.

    Parameters
    ----------
    definitionId : str
        The unique Lockstep Platform ID number of the Custom Field 
        Definition for the Custom Field Value to retrieve.
    recordKey : str
        The unique Lockstep Platform ID number of the Lockstep Platform 
        object the Custom Field Value is attached to.
    body : object
        A list of changes to apply to this Custom Field
    """
    def update_field(self, definitionId: str, recordKey: str, body: object) -> LockstepResponse:
        path = f"/api/v1/CustomFieldValues/{definitionId}/{recordKey}"
        return self.client.send_request("PATCH", path, body, {definitionId: str, recordKey: str, body: object})

    """
    Deletes the Custom Field referred to by this unique identifier. 

    A Custom Field represents metadata added to an object within the 
    Lockstep Platform. Lockstep provides a core definition for each 
    object. The core definition is intended to represent a level of 
    compatibility that provides support across most accounting systems 
    and products. When a user or developer requires information beyond 
    this core definition, you can use Custom Fields to represent this 
    information. See 
    [Extensibility](https://developer.lockstep.io/docs/extensibility) 
    for more information.

    Parameters
    ----------
    definitionId : str
        The unique Lockstep Platform ID number of the Custom Field 
        Definition for the Custom Field Value to retrieve.
    recordKey : str
        The unique Lockstep Platform ID number of the Lockstep Platform 
        object the Custom Field Value is attached to.
    """
    def delete_field(self, definitionId: str, recordKey: str) -> LockstepResponse:
        path = f"/api/v1/CustomFieldValues/{definitionId}/{recordKey}"
        return self.client.send_request("DELETE", path, None, {definitionId: str, recordKey: str})

    """
    Creates one or more Custom Fields and returns the records as 
    created. A Custom Field represents metadata added to an object 
    within the Lockstep Platform. Lockstep provides a core definition 
    for each object. The core definition is intended to represent a 
    level of compatibility that provides support across most accounting 
    systems and products. When a user or developer requires information 
    beyond this core definition, you can use Custom Fields to represent 
    this information. See 
    [Extensibility](https://developer.lockstep.io/docs/extensibility) 
    for more information.

    Parameters
    ----------
    body : list[CustomFieldValueModel]
        The Custom Fields to create
    """
    def create_fields(self, body: list[CustomFieldValueModel]) -> LockstepResponse:
        path = f"/api/v1/CustomFieldValues"
        return self.client.send_request("POST", path, body, {body: list[CustomFieldValueModel]})

    """
    Queries Custom Fields within the Lockstep platform using the 
    specified filtering, sorting, nested fetch, and pagination rules 
    requested. 

    More information on querying can be found on the [Searchlight Query 
    Language](https://developer.lockstep.io/docs/querying-with-searchlight) 
    page on the Lockstep Developer website. 

    A Custom Field represents metadata added to an object within the 
    Lockstep Platform. Lockstep provides a core definition for each 
    object. The core definition is intended to represent a level of 
    compatibility that provides support across most accounting systems 
    and products. When a user or developer requires information beyond 
    this core definition, you can use Custom Fields to represent this 
    information. See 
    [Extensibility](https://developer.lockstep.io/docs/extensibility) 
    for more information.

    Parameters
    ----------
    filter : str
        The filter for this query. See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. Available collections: 
        CustomFieldDefinition
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
    def query_fields(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        path = f"/api/v1/CustomFieldValues/query"
        return self.client.send_request("GET", path, None, {filter: str, include: str, order: str, pageSize: int, pageNumber: int})
