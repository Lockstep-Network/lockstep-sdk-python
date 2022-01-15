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
# @version    2022.2.100.0
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#

import requests
import urllib.parse

class LockstepApi:
    from lockstep.lockstep_response import LockstepResponse

    """
    Construct a new LockstepApi client object
    """
    def __init__(self, env: str):
        from lockstep.clients.activities_client import ActivitiesClient
        from lockstep.clients.apikeys_client import ApiKeysClient
        from lockstep.clients.appenrollments_client import AppEnrollmentsClient
        from lockstep.clients.applications_client import ApplicationsClient
        from lockstep.clients.attachments_client import AttachmentsClient
        from lockstep.clients.codedefinitions_client import CodeDefinitionsClient
        from lockstep.clients.companies_client import CompaniesClient
        from lockstep.clients.contacts_client import ContactsClient
        from lockstep.clients.creditmemoapplied_client import CreditMemoAppliedClient
        from lockstep.clients.currencies_client import CurrenciesClient
        from lockstep.clients.customfielddefinitions_client import CustomFieldDefinitionsClient
        from lockstep.clients.customfieldvalues_client import CustomFieldValuesClient
        from lockstep.clients.definitions_client import DefinitionsClient
        from lockstep.clients.emails_client import EmailsClient
        from lockstep.clients.invoicehistory_client import InvoiceHistoryClient
        from lockstep.clients.invoices_client import InvoicesClient
        from lockstep.clients.leads_client import LeadsClient
        from lockstep.clients.notes_client import NotesClient
        from lockstep.clients.paymentapplications_client import PaymentApplicationsClient
        from lockstep.clients.payments_client import PaymentsClient
        from lockstep.clients.provisioning_client import ProvisioningClient
        from lockstep.clients.reports_client import ReportsClient
        from lockstep.clients.status_client import StatusClient
        from lockstep.clients.sync_client import SyncClient
        from lockstep.clients.useraccounts_client import UserAccountsClient
        from lockstep.clients.userroles_client import UserRolesClient
        self.activities = ActivitiesClient(self)
        self.apiKeys = ApiKeysClient(self)
        self.appEnrollments = AppEnrollmentsClient(self)
        self.applications = ApplicationsClient(self)
        self.attachments = AttachmentsClient(self)
        self.codeDefinitions = CodeDefinitionsClient(self)
        self.companies = CompaniesClient(self)
        self.contacts = ContactsClient(self)
        self.creditMemoApplied = CreditMemoAppliedClient(self)
        self.currencies = CurrenciesClient(self)
        self.customFieldDefinitions = CustomFieldDefinitionsClient(self)
        self.customFieldValues = CustomFieldValuesClient(self)
        self.definitions = DefinitionsClient(self)
        self.emails = EmailsClient(self)
        self.invoiceHistory = InvoiceHistoryClient(self)
        self.invoices = InvoicesClient(self)
        self.leads = LeadsClient(self)
        self.notes = NotesClient(self)
        self.paymentApplications = PaymentApplicationsClient(self)
        self.payments = PaymentsClient(self)
        self.provisioning = ProvisioningClient(self)
        self.reports = ReportsClient(self)
        self.status = StatusClient(self)
        self.sync = SyncClient(self)
        self.userAccounts = UserAccountsClient(self)
        self.userRoles = UserRolesClient(self)
        if env == "sbx":
            self.serverUrl = "https://api.sbx.lockstep.io/"
        elif env == "prd":
            self.serverUrl = "https://api.lockstep.io/"
        else:
            self.serverUrl = env
        self.version = "2022.2.100.0"

    """
    Configure this API client to use API Key authentication
    """
    def with_api_key(self, apiKey: str):
        self.apiKey = apiKey
        self.bearerToken = None
    
    """
    Configure this API client to use Bearer Token authentication
    """
    def with_bearer_token(self, bearerToken: str):
        self.apiKey = None
        self.bearerToken = bearerToken
    
    """
    Send a request and parse the result
    """
    def send_request(self, method: str, path: str, body: object, query_params: object) -> LockstepResponse:
        if query_params:
            url = urllib.parse.urljoin(self.serverUrl, path) + "?" + urllib.parse.urlencode(query_params)
        else:
            url = urllib.parse.urljoin(self.serverUrl, path)
        
        if self.apiKey:
            headers = {"Accept": "application/json", "Api-Key": self.apiKey}
        elif self.bearerToken:
            headers = {"Accept": "application/json", "Authorization": "Bearer " + self.bearerToken}
        else:
            headers = {"Accept": "application/json"}
    
        response = requests.request(method, url, headers=headers)
        return response.json()
        
