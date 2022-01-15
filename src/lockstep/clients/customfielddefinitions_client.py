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
from lockstep.models.customfielddefinitionmodel import CustomFieldDefinitionModel

class CustomFieldDefinitionsClient:

    def __init__(self, client):
        self.client = client

    """
    Retrieves the Custom Field Definition specified by this unique 
    identifier. 

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
    id : str
        The unique Lockstep Platform ID number of this Custom Field 
        Definition
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. No additional data collections are 
        currently defined on this object, but may be supported in the 
        future.
    """
    def retrieve_field_definition(self, id: str, include: str) -> LockstepResponse:
        path = f"/api/v1/CustomFieldDefinitions/{id}"
        return self.client.send_request("GET", path, None, {id: str, include: str})

    """
    Updates an existing Custom Field Definition with the information 
    supplied to this PATCH call. 

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
    id : str
        The unique Lockstep Platform ID number of the Custom Field 
        Definition to update
    body : object
        A list of changes to apply to this Custom Field Definition
    """
    def update_field_definition(self, id: str, body: object) -> LockstepResponse:
        path = f"/api/v1/CustomFieldDefinitions/{id}"
        return self.client.send_request("PATCH", path, body, {id: str, body: object})

    """
    Deletes the Custom Field Definition referred to by this unique 
    identifier. 

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
    id : str
        The unique Lockstep Platform ID number of the Custom Field 
        Definition to delete
    """
    def delete_field_definition(self, id: str) -> LockstepResponse:
        path = f"/api/v1/CustomFieldDefinitions/{id}"
        return self.client.send_request("DELETE", path, None, {id: str})

    """
    Creates one or more Custom Field Definitions and returns the records 
    as created. A Custom Field represents metadata added to an object 
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
    body : list[CustomFieldDefinitionModel]
        The Custom Field Definitions to create
    """
    def create_field_definitions(self, body: list[CustomFieldDefinitionModel]) -> LockstepResponse:
        path = f"/api/v1/CustomFieldDefinitions"
        return self.client.send_request("POST", path, body, {body: list[CustomFieldDefinitionModel]})

    """
    Queries Custom Field Definitions within the Lockstep platform using 
    the specified filtering, sorting, nested fetch, and pagination rules 
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
        elements to retrieve. No additional data collections are 
        currently defined on this object, but may be supported in the 
        future.
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
    def query_field_definitions(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        path = f"/api/v1/CustomFieldDefinitions/query"
        return self.client.send_request("GET", path, None, {filter: str, include: str, order: str, pageSize: int, pageNumber: int})
