
text = 'Firm: CanaRx Services Inc  - 554740 - 02/26/2019URL:  https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/canarx-services-inc-554740-02262019Subject: Unapproved New Drugs/MisbrandedIssue Date: 02/26/2019Snippet: Letters'

print(text.index('Subject'))
print(text[text.index('Subject:'):text.index('Issue Date:')])