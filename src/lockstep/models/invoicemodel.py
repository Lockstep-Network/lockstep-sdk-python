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


from dataclasses import dataclass
from lockstep.models.invoiceaddressmodel import InvoiceAddressModel
from lockstep.models.invoicelinemodel import InvoiceLineModel
from lockstep.models.invoicepaymentdetailmodel import InvoicePaymentDetailModel
from lockstep.models.notemodel import NoteModel
from lockstep.models.attachmentmodel import AttachmentModel
from lockstep.models.companymodel import CompanyModel
from lockstep.models.companymodel import CompanyModel
from lockstep.models.contactmodel import ContactModel
from lockstep.models.creditmemoinvoicemodel import CreditMemoInvoiceModel
from lockstep.models.customfieldvaluemodel import CustomFieldValueModel
from lockstep.models.customfielddefinitionmodel import CustomFieldDefinitionModel

@dataclass
class InvoiceModel:
    """
    An Invoice represents a bill sent from one company to another. The
    creator of the invoice is identified by the `CompanyId` field, and
    the recipient of the invoice is identified by the `CustomerId`
    field. Most invoices are uniquely identified both by a Lockstep
    Platform ID number and a customer ERP "key" that was generated by
    the system that originated the invoice. Invoices have a total amount
    and a due date, and when some payments have been made on the Invoice
    the `TotalAmount` and the `OutstandingBalanceAmount` may be
    different.
    """

    groupKey: str | None = None
    invoiceId: str | None = None
    companyId: str | None = None
    customerId: str | None = None
    erpKey: str | None = None
    purchaseOrderCode: str | None = None
    referenceCode: str | None = None
    salespersonCode: str | None = None
    salespersonName: str | None = None
    invoiceTypeCode: str | None = None
    invoiceStatusCode: str | None = None
    termsCode: str | None = None
    specialTerms: str | None = None
    currencyCode: str | None = None
    totalAmount: float | None = None
    salesTaxAmount: float | None = None
    discountAmount: float | None = None
    outstandingBalanceAmount: float | None = None
    invoiceDate: str | None = None
    discountDate: str | None = None
    postedDate: str | None = None
    invoiceClosedDate: str | None = None
    paymentDueDate: str | None = None
    importedDate: str | None = None
    primaryOriginAddressId: str | None = None
    primaryBillToAddressId: str | None = None
    primaryShipToAddressId: str | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None
    appEnrollmentId: str | None = None
    isVoided: bool | None = None
    inDispute: bool | None = None
    excludeFromAging: bool | None = None
    preferredDeliveryMethod: str | None = None
    addresses: list[InvoiceAddressModel] | None = None
    lines: list[InvoiceLineModel] | None = None
    payments: list[InvoicePaymentDetailModel] | None = None
    notes: list[NoteModel] | None = None
    attachments: list[AttachmentModel] | None = None
    company: CompanyModel | None = None
    customer: CompanyModel | None = None
    customerPrimaryContact: ContactModel | None = None
    creditMemos: list[CreditMemoInvoiceModel] | None = None
    customFieldValues: list[CustomFieldValueModel] | None = None
    customFieldDefinitions: list[CustomFieldDefinitionModel] | None = None

