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
# @version    2021.39
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#

from src.clients.activities_client import ActivitiesClient
from src.clients.apikeys_client import ApiKeysClient
from src.clients.appenrollments_client import AppEnrollmentsClient
from src.clients.applications_client import ApplicationsClient
from src.clients.attachments_client import AttachmentsClient
from src.clients.codedefinitions_client import CodeDefinitionsClient
from src.clients.companies_client import CompaniesClient
from src.clients.contacts_client import ContactsClient
from src.clients.creditmemoapplied_client import CreditMemoAppliedClient
from src.clients.currencies_client import CurrenciesClient
from src.clients.customfielddefinitions_client import CustomFieldDefinitionsClient
from src.clients.customfieldvalues_client import CustomFieldValuesClient
from src.clients.definitions_client import DefinitionsClient
from src.clients.emails_client import EmailsClient
from src.clients.invoicehistory_client import InvoiceHistoryClient
from src.clients.invoices_client import InvoicesClient
from src.clients.leads_client import LeadsClient
from src.clients.migration_client import MigrationClient
from src.clients.notes_client import NotesClient
from src.clients.paymentapplications_client import PaymentApplicationsClient
from src.clients.payments_client import PaymentsClient
from src.clients.provisioning_client import ProvisioningClient
from src.clients.reports_client import ReportsClient
from src.clients.status_client import StatusClient
from src.clients.sync_client import SyncClient
from src.clients.useraccounts_client import UserAccountsClient
from src.clients.userroles_client import UserRolesClient
from src.models.lockstep_response import LockstepResponse
import requests
import urllib.parse

class LockstepApi():

    """
    Construct a new LockstepApi client object
    """
    def __init__(self, env: str):
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
        self.migration = MigrationClient(self)
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
        self.version = "2021.39"

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
        return response
        
