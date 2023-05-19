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
from lockstep.models.webhookrulemodel import WebhookRuleModel

class WebhookRulesClient:
    """
    API methods related to WebhookRules
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_webhook_rule(self, id: str) -> LockstepResponse[WebhookRuleModel]:
        """
        Retrieves the Webhook Rule specified by this unique identifier.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of this Webhook Rule
        """
        path = f"/api/v1/WebhookRules/{id}"
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, WebhookRuleModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_webhook_rule(self, id: str, body: object) -> LockstepResponse[WebhookRuleModel]:
        """
        Updates a webhook rule that matches the specified id with the
        requested information.

        The PATCH method allows you to change specific values on the
        object while leaving other values alone. As input you should
        supply a list of field names and new values. If you do not
        provide the name of a field, that field will remain unchanged.
        This allows you to ensure that you are only updating the
        specific fields desired.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Webhook Rule
            to update.
        body : object
            A list of changes to apply to this Webhook Rule
        """
        path = f"/api/v1/WebhookRules/{id}"
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, WebhookRuleModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_webhook_rule(self, id: str) -> LockstepResponse[ActionResultModel]:
        """
        Deletes the Webhook Rule referred to by this unique identifier.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Webhook Rule
            to delete.
        """
        path = f"/api/v1/WebhookRules/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ActionResultModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_webhook_rules(self, body: list[object]) -> LockstepResponse[list[WebhookRuleModel]]:
        """
        Creates one or more webhook rules from a given model.

        Parameters
        ----------
        body : list[object]
            The Webhook Rules to create
        """
        path = "/api/v1/WebhookRules"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [WebhookRuleModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_webhook_rules(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[WebhookRuleModel]]:
        """
        Queries Webhook Rules for this account using the specified
        filtering, sorting, and pagination rules requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. No collections are currently available
            but may be offered in the future
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
        path = "/api/v1/WebhookRules/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), WebhookRuleModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
