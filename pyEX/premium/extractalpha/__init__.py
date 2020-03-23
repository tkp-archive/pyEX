# -*- coding: utf-8 -*-
from functools import wraps
from ...stocks import timeSeries, timeSeriesDF
from ...common import _expire, _UTC


@_expire(hour=3, tz=_UTC)
def _base(id, symbol='', **kwargs):
    '''internal'''
    kwargs['id'] = id
    kwargs['key'] = symbol or kwargs.pop('key', '')
    return timeSeries(**kwargs)


@_expire(hour=3, tz=_UTC)
def _baseDF(id, symbol='', **kwargs):
    '''internal'''
    kwargs['id'] = id
    kwargs['key'] = symbol or kwargs.pop('key', '')
    return timeSeriesDF(**kwargs)


@wraps(timeSeries)
def cam1(symbol='', **kwargs):
    '''
    The ExtractAlpha Cross-Asset Model 1 (CAM1) is an innovative quantitative stock selection model designed to capture the information contained in options market prices and volumes. The listed equity options market is composed of investors who on average are more informed and information-driven than their cash equity counterparts, due to the higher levels of conviction that are associated with levered bets. This results in a unique model which profits from gradual cross-asset information flows.
    In historical simulations, high-scoring stocks according to CAM1 outperform low-scoring stocks by 17% per annum with a market-neutral Sharpe ratio of 3.0 before transaction costs. CAM1 is particularly effective in volatile regimes and for mid- and small-cap stocks, and is best used in conjunction with other alpha signals with similar time horizons.
    History available from July 2005
    https://iexcloud.io/docs/api/#cross-asset-model-1
    '''
    return _base(id='PREMIUM_EXTRACT_ALPHA_CAM', symbol=symbol, **kwargs)


@wraps(timeSeries)
def cam1DF(symbol='', **kwargs):
    '''
    The ExtractAlpha Cross-Asset Model 1 (CAM1) is an innovative quantitative stock selection model designed to capture the information contained in options market prices and volumes. The listed equity options market is composed of investors who on average are more informed and information-driven than their cash equity counterparts, due to the higher levels of conviction that are associated with levered bets. This results in a unique model which profits from gradual cross-asset information flows.
    In historical simulations, high-scoring stocks according to CAM1 outperform low-scoring stocks by 17% per annum with a market-neutral Sharpe ratio of 3.0 before transaction costs. CAM1 is particularly effective in volatile regimes and for mid- and small-cap stocks, and is best used in conjunction with other alpha signals with similar time horizons.
    History available from July 2005
    https://iexcloud.io/docs/api/#cross-asset-model-1
    '''
    return _baseDF(id='PREMIUM_EXTRACT_ALPHA_CAM', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgCFPBComplaints(symbol='', **kwargs):
    '''Financial firms have been under scrutiny for their business practices since the Global Financial Crisis. The Consumer Financial Protection Bureau’s Consumer Complaint Database is a collection of complaints on a range of consumer financial products and services, sent to companies for response. The Consumer Financial Protection Board doesn’t verify all the facts alleged in these complaints, but we take steps to confirm a commercial relationship between the consumer and the company.

    Since the CFPB started accepting complaints in July 2011, they have helped consumers connect with financial companies to understand issues with their mortgages, fix errors on their credit reports, stop harassment from debt collectors, and get direct responses about problems with their credit cards, checking and savings accounts, student loans, and more.
    The database generally updates daily, and contains certain information for each complaint, including the source of the complaint, the date of submission, and the company the complaint was sent to for response. The database also includes information about the actions taken by the company in response to the complaint, such as, whether the company’s response was timely and how the company responded. If the consumer opts to share it and after we take steps to remove personal information, we publish the consumer’s description of what happened. Companies also have the option to select a public response. Complaints referred to other regulators, such as complaints about depository institutions with less than $10 billion in assets, are not published in the Consumer Complaint Database.
    History available from 2011
    https://iexcloud.io/docs/api/#esg-cfpb-complaints
    '''
    kwargs['subkey'] = '1'
    return _base(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgCFPBComplaintsDF(symbol='', **kwargs):
    '''Financial firms have been under scrutiny for their business practices since the Global Financial Crisis. The Consumer Financial Protection Bureau’s Consumer Complaint Database is a collection of complaints on a range of consumer financial products and services, sent to companies for response. The Consumer Financial Protection Board doesn’t verify all the facts alleged in these complaints, but we take steps to confirm a commercial relationship between the consumer and the company.
    Since the CFPB started accepting complaints in July 2011, they have helped consumers connect with financial companies to understand issues with their mortgages, fix errors on their credit reports, stop harassment from debt collectors, and get direct responses about problems with their credit cards, checking and savings accounts, student loans, and more.
    The database generally updates daily, and contains certain information for each complaint, including the source of the complaint, the date of submission, and the company the complaint was sent to for response. The database also includes information about the actions taken by the company in response to the complaint, such as, whether the company’s response was timely and how the company responded. If the consumer opts to share it and after we take steps to remove personal information, we publish the consumer’s description of what happened. Companies also have the option to select a public response. Complaints referred to other regulators, such as complaints about depository institutions with less than $10 billion in assets, are not published in the Consumer Complaint Database.
    History available from 2011
    https://iexcloud.io/docs/api/#esg-cfpb-complaints
    '''
    kwargs['subkey'] = '1'
    return _baseDF(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgCPSCRecalls(symbol='', **kwargs):
    '''Product recalls can be a sign that a company did not employ sufficient safety or quality standards when releasing its products. A product recall can have significant negative impact on a company’s brand, sales, and stock price [Kin, Shenoy, and Subramaniam, 2013]. CPSC is charged with protecting the public from unreasonable risks of injury or death associated with the use of the thousands of types of consumer products under the agency’s jurisdiction. CPSC is committed to protecting consumers and families from products that pose a fire, electrical, chemical, or mechanical hazard.
    Note that CPSC recalls data is collected from multiple different data formats and so the available fields will vary substantially across records in their availability.
    Future versions may include consumers’ reports on product safety-related incidents.
    History available from 1974
    https://iexcloud.io/docs/api/#esg-cpsc-recalls
    '''
    kwargs['subkey'] = '5'
    return _base(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgCPSCRecallsDF(symbol='', **kwargs):
    '''Financial firms have been under scrutiny for their business practices since the Global Financial Crisis. The Consumer Financial Protection Bureau’s Consumer Complaint Database is a collection of complaints on a range of consumer financial products and services, sent to companies for response. The Consumer Financial Protection Board doesn’t verify all the facts alleged in these complaints, but we take steps to confirm a commercial relationship between the consumer and the company.
    Since the CFPB started accepting complaints in July 2011, they have helped consumers connect with financial companies to understand issues with their mortgages, fix errors on their credit reports, stop harassment from debt collectors, and get direct responses about problems with their credit cards, checking and savings accounts, student loans, and more.
    The database generally updates daily, and contains certain information for each complaint, including the source of the complaint, the date of submission, and the company the complaint was sent to for response. The database also includes information about the actions taken by the company in response to the complaint, such as, whether the company’s response was timely and how the company responded. If the consumer opts to share it and after we take steps to remove personal information, we publish the consumer’s description of what happened. Companies also have the option to select a public response. Complaints referred to other regulators, such as complaints about depository institutions with less than $10 billion in assets, are not published in the Consumer Complaint Database.
    History available from 2011
    https://iexcloud.io/docs/api/#esg-cfpb-complaints
    '''
    kwargs['subkey'] = '5'
    return _baseDF(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgDOLVisaApplications(symbol='', **kwargs):
    '''Companies often hire foreign knowledge workers if they wish to invest in innovation. Hiring foreign workers for employment in the U.S. normally requires approval from several government agencies. First, employers must seek labor certification through the U.S. Department of Labor (DOL). Once the application is certified (approved), the employer must petition the U.S. Citizenship and Immigration Services (CIS) for a visa. Approval by DOL does not guarantee a visa issuance. The Department of State (DOS) will issue an immigrant visa number to the foreign worker for U.S. entry.
    The Office of Foreign Labor Certification (OFLC) Disclosure Data consists of select extracted data fields from application tables within OFLC case management systems. Each Excel file is cumulative, containing unique records identified by the applicable OFLC case number based on the most recent date a case determination decision was issued.
    This endpoint includes data on Permanent and H-1B visas only. The H-1B program allows employers to temporarily employ foreign workers in the U.S. on a nonimmigrant basis in specialty occupations or as fashion models of distinguished merit and ability. A specialty occupation requires the theoretical and practical application of a body of specialized knowledge and a bachelor’s degree or the equivalent in the specific specialty (e.g. sciences, medicine, health care, education, biotechnology, and business specialties, etc.).
    Note that because of the different data structures available by year and across application type (H1B and PERM), the density of many of these fields will vary substantially across the dataset.
    History available from 1999
    https://iexcloud.io/docs/api/#esg-dol-visa-applications
    '''
    kwargs['subkey'] = '8'
    return _base(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgDOLVisaApplicationsDF(symbol='', **kwargs):
    '''Companies often hire foreign knowledge workers if they wish to invest in innovation. Hiring foreign workers for employment in the U.S. normally requires approval from several government agencies. First, employers must seek labor certification through the U.S. Department of Labor (DOL). Once the application is certified (approved), the employer must petition the U.S. Citizenship and Immigration Services (CIS) for a visa. Approval by DOL does not guarantee a visa issuance. The Department of State (DOS) will issue an immigrant visa number to the foreign worker for U.S. entry.
    The Office of Foreign Labor Certification (OFLC) Disclosure Data consists of select extracted data fields from application tables within OFLC case management systems. Each Excel file is cumulative, containing unique records identified by the applicable OFLC case number based on the most recent date a case determination decision was issued.
    This endpoint includes data on Permanent and H-1B visas only. The H-1B program allows employers to temporarily employ foreign workers in the U.S. on a nonimmigrant basis in specialty occupations or as fashion models of distinguished merit and ability. A specialty occupation requires the theoretical and practical application of a body of specialized knowledge and a bachelor’s degree or the equivalent in the specific specialty (e.g. sciences, medicine, health care, education, biotechnology, and business specialties, etc.).
    Note that because of the different data structures available by year and across application type (H1B and PERM), the density of many of these fields will vary substantially across the dataset.
    History available from 1999
    https://iexcloud.io/docs/api/#esg-dol-visa-applications
    '''
    kwargs['subkey'] = '8'
    return _baseDF(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgEPAEnforcements(symbol='', **kwargs):
    '''Violations of Environmental Protection Agency regulations can indicate a company’s negligence in its environmental and emissions standards, or a disregard for regulatory risks.
    The Enforcement and Compliance History Online (ECHO) system incorporates Federal enforcement and compliance (FE&C) data from the Integrated Compliance Information System (ICIS), used to track federal enforcement cases. ICIS contains information on federal administrative and federal judicial cases under the following environmental statutes: the Clean Air Act (CAA), the Clean Water Act (CWA), the Resource Conservation and Recovery Act (RCRA), the Emergency Planning and Community Right-to-Know Act (EPCRA) Section 313, the Toxic Substances Control Act (TSCA), the Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA), the Comprehensive Environmental Response, Compensation, and Liability Act (CERCLA or Superfund), the Safe Drinking Water Act (SDWA), and the Marine Protection, Research, and Sanctuaries Act (MPRSA).
    ICIS is a case activity tracking and management system for civil, judicial, and administrative federal EPA enforcement cases. Case information is supplied and updated by EPA’s Offices of Regional Counsel and Office of Civil Enforcement case attorneys. The basic structure of an ICIS FE&C record focuses on an enforcement case. It is assigned a case number and a case name which identifies the defendant (or principal defendant if more than one is named in the complaint). For administrative actions, the record includes the nature of the violation, statute(s) involved, and milestone dates (e.g., the date the order was issued). Judicial actions contain information similar to that for administrative actions, but include more detailed milestone dates.
    Data is organized around two concepts: the enforcement case and a resulting settlement(s) (enforcement conclusion). Enforcement case data describe the enforcement action from initiation through to its conclusion. If multiple defendants, facilities, and/or violations are cited in the case, then a single case may result in multiple settlements. These case conclusions describe what has been ordered and/or agreed upon to be performed to address violations identified by the case complaint.
    History available from 1975
    https://iexcloud.io/docs/api/#esg-epa-enforcements
    '''
    kwargs['subkey'] = '2'
    return _base(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgEPAEnforcementsDF(symbol='', **kwargs):
    '''Violations of Environmental Protection Agency regulations can indicate a company’s negligence in its environmental and emissions standards, or a disregard for regulatory risks.
    The Enforcement and Compliance History Online (ECHO) system incorporates Federal enforcement and compliance (FE&C) data from the Integrated Compliance Information System (ICIS), used to track federal enforcement cases. ICIS contains information on federal administrative and federal judicial cases under the following environmental statutes: the Clean Air Act (CAA), the Clean Water Act (CWA), the Resource Conservation and Recovery Act (RCRA), the Emergency Planning and Community Right-to-Know Act (EPCRA) Section 313, the Toxic Substances Control Act (TSCA), the Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA), the Comprehensive Environmental Response, Compensation, and Liability Act (CERCLA or Superfund), the Safe Drinking Water Act (SDWA), and the Marine Protection, Research, and Sanctuaries Act (MPRSA).
    ICIS is a case activity tracking and management system for civil, judicial, and administrative federal EPA enforcement cases. Case information is supplied and updated by EPA’s Offices of Regional Counsel and Office of Civil Enforcement case attorneys. The basic structure of an ICIS FE&C record focuses on an enforcement case. It is assigned a case number and a case name which identifies the defendant (or principal defendant if more than one is named in the complaint). For administrative actions, the record includes the nature of the violation, statute(s) involved, and milestone dates (e.g., the date the order was issued). Judicial actions contain information similar to that for administrative actions, but include more detailed milestone dates.
    Data is organized around two concepts: the enforcement case and a resulting settlement(s) (enforcement conclusion). Enforcement case data describe the enforcement action from initiation through to its conclusion. If multiple defendants, facilities, and/or violations are cited in the case, then a single case may result in multiple settlements. These case conclusions describe what has been ordered and/or agreed upon to be performed to address violations identified by the case complaint.
    History available from 1975
    https://iexcloud.io/docs/api/#esg-epa-enforcements
    '''
    kwargs['subkey'] = '2'
    return _baseDF(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgEPAMilestones(symbol='', **kwargs):
    '''As described in EPA Enforcements, but including all milestones for an EPA violation event, not just enforcement actions.
    History available from 1975
    https://iexcloud.io/docs/api/#esg-epa-milestones
    '''
    kwargs['subkey'] = '3'
    return _base(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgEPAMilestonesDF(symbol='', **kwargs):
    '''As described in EPA Enforcements, but including all milestones for an EPA violation event, not just enforcement actions.
    History available from 1975
    https://iexcloud.io/docs/api/#esg-epa-milestones
    '''
    kwargs['subkey'] = '3'
    return _baseDF(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgFECIndividualCampaingContributions(symbol='', **kwargs):
    '''Individuals often contribute to political campaigns, and when doing so they are asked to disclose their employer. The individual contributions file contains each campaign contribution from an individual to a federal committee. The files for the current election cycle plus the two most recent election cycles are regularly updated.
    History available from 1997
    https://iexcloud.io/docs/api/#esg-fec-individual-campaign-contributions
    '''
    kwargs['subkey'] = '7'
    return _base(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgFECIndividualCampaingContributionsDF(symbol='', **kwargs):
    '''Individuals often contribute to political campaigns, and when doing so they are asked to disclose their employer. The individual contributions file contains each campaign contribution from an individual to a federal committee. The files for the current election cycle plus the two most recent election cycles are regularly updated.
    History available from 1997
    https://iexcloud.io/docs/api/#esg-fec-individual-campaign-contributions
    '''
    kwargs['subkey'] = '7'
    return _baseDF(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgOSHAInspections(symbol='', **kwargs):
    '''Workplace injuries can be an indication of a company’s under investment in worker safety and reasonable working conditions. The dataset consists of inspection case detail for Occupational Safety and Health Administration (OSHA) inspections. The dataset includes information regarding the impetus for conducting the inspections, which are often prompted by workplace accidents, injuries, and fatalities.
    Future versions may include data on the workplace injuries themselves.
    History available from 1972
    https://iexcloud.io/docs/api/#esg-osha-inspections
    '''
    kwargs['subkey'] = '4'
    return _base(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgOSHAInspectionsDF(symbol='', **kwargs):
    '''Workplace injuries can be an indication of a company’s under investment in worker safety and reasonable working conditions. The dataset consists of inspection case detail for Occupational Safety and Health Administration (OSHA) inspections. The dataset includes information regarding the impetus for conducting the inspections, which are often prompted by workplace accidents, injuries, and fatalities.
    Future versions may include data on the workplace injuries themselves.
    History available from 1972
    https://iexcloud.io/docs/api/#esg-osha-inspections
    '''
    kwargs['subkey'] = '4'
    return _baseDF(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgSenateLobbying(symbol='', **kwargs):
    '''Companies often employ lobbyists to influence legislation in their favor, and lobbying can be a very high ROI activity for a company [Hutchens, Rego, and Sheneman, 2016]. Under the Lobbying Disclosure Act, in-house and outside lobbyists must file quarterly reports describing lobbying activity. These reports disclose the amount spent on lobbying. The lobbying data is compiled using the lobbying disclosure reports filed with the Secretary of the Senate’s Office of Public Records (SOPR). Quarterly reports are due on the 20th day of January, April, July, and October. Lobbying firms are required to provide a good- faith estimate rounded to the nearest $10,000 of all lobbying-related income from their clients in each quarter. Total spending on lobbying activities are reported each quarter, but are not broken down by how much was spent on a particular issue or bill.
    History available from 1999
    https://iexcloud.io/docs/api/#esg-senate-lobbying
    '''
    kwargs['subkey'] = '6'
    return _base(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgSenateLobbyingDF(symbol='', **kwargs):
    '''Companies often employ lobbyists to influence legislation in their favor, and lobbying can be a very high ROI activity for a company [Hutchens, Rego, and Sheneman, 2016]. Under the Lobbying Disclosure Act, in-house and outside lobbyists must file quarterly reports describing lobbying activity. These reports disclose the amount spent on lobbying. The lobbying data is compiled using the lobbying disclosure reports filed with the Secretary of the Senate’s Office of Public Records (SOPR). Quarterly reports are due on the 20th day of January, April, July, and October. Lobbying firms are required to provide a good- faith estimate rounded to the nearest $10,000 of all lobbying-related income from their clients in each quarter. Total spending on lobbying activities are reported each quarter, but are not broken down by how much was spent on a particular issue or bill.
    History available from 1999
    https://iexcloud.io/docs/api/#esg-senate-lobbying
    '''
    kwargs['subkey'] = '6'
    return _baseDF(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgUSASpending(symbol='', **kwargs):
    '''Companies seek government contracts as these are very sticky sources of revenue. The Federal Funding Accountability and Transparency Act of 2006 (FFATA) requires that federal contract, grant, loan, and other financial assistance awards of more than $25,000 be displayed on a searchable, publicly accessible website. As a matter of discretion, the data set also contains certain federal contracts of more than $3,000.
    All the data on prime recipient transactions is submited by the federal agencies making federal contract, grant, loan, and other financial assistance awards. Agencies are required to submit data within 30 days of making the award or after making a modification or amendment to an award. The exception is the Department of Defense which delays its submission by 90 days to protect operations.
    History available from 1995
    https://iexcloud.io/docs/api/#esg-usa-spending
    '''
    kwargs['subkey'] = '9'
    return _base(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgUSASpendingDF(symbol='', **kwargs):
    '''Companies seek government contracts as these are very sticky sources of revenue. The Federal Funding Accountability and Transparency Act of 2006 (FFATA) requires that federal contract, grant, loan, and other financial assistance awards of more than $25,000 be displayed on a searchable, publicly accessible website. As a matter of discretion, the data set also contains certain federal contracts of more than $3,000.
    All the data on prime recipient transactions is submited by the federal agencies making federal contract, grant, loan, and other financial assistance awards. Agencies are required to submit data within 30 days of making the award or after making a modification or amendment to an award. The exception is the Department of Defense which delays its submission by 90 days to protect operations.
    History available from 1995
    https://iexcloud.io/docs/api/#esg-usa-spending
    '''
    kwargs['subkey'] = '9'
    return _baseDF(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgUSPTOPatentApplications(symbol='', **kwargs):
    '''Patent applications and grants are indications that a company is investing in future innovation [Hirshleifer, Hsu, and Li, 2013]. The United States Patent and Trademark Office (USPTO) is the federal agency for granting U.S. patents and registering trademarks. Patent applications data is issued weekly on Thursdays.
    Future versions may contain more detail on the content of patent applications.
    History available from 2002
    https://iexcloud.io/docs/api/#esg-uspto-patent-applications
    '''
    kwargs['subkey'] = '10'
    return _base(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgUSPTOPatentApplicationsDF(symbol='', **kwargs):
    '''Patent applications and grants are indications that a company is investing in future innovation [Hirshleifer, Hsu, and Li, 2013]. The United States Patent and Trademark Office (USPTO) is the federal agency for granting U.S. patents and registering trademarks. Patent applications data is issued weekly on Thursdays.
    Future versions may contain more detail on the content of patent applications.
    History available from 2002
    https://iexcloud.io/docs/api/#esg-uspto-patent-applications
    '''
    kwargs['subkey'] = '10'
    return _baseDF(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgUSPTOPatentGrants(symbol='', **kwargs):
    '''Patent grants are indications that a company has successfully signaled that it values its IP, that its IP is unique in the eyes of the USPTO, and that its initial patent application was a reasonable one.
    Patent grants data is issued weekly on Tuesdays.
    Currently only the first three assignees listed on the patent are included. Future versions may contain more detail on the content of patent grants, including assignees beyond the first three listed on the grant.
    History available from 2002
    https://iexcloud.io/docs/api/#esg-uspto-patent-grants
    '''
    kwargs['subkey'] = '10'
    return _base(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def esgUSPTOPatentGrantsDF(symbol='', **kwargs):
    '''Patent grants are indications that a company has successfully signaled that it values its IP, that its IP is unique in the eyes of the USPTO, and that its initial patent application was a reasonable one.
    Patent grants data is issued weekly on Tuesdays.
    Currently only the first three assignees listed on the patent are included. Future versions may contain more detail on the content of patent grants, including assignees beyond the first three listed on the grant.
    History available from 2002
    https://iexcloud.io/docs/api/#esg-uspto-patent-grants
    '''
    kwargs['subkey'] = '10'
    return _baseDF(id='PREMIUM_EXTRACT_ALPHA_ESG', symbol=symbol, **kwargs)


@wraps(timeSeries)
def tacticalModel1(symbol='', **kwargs):
    '''The ExtractAlpha Tactical Model 1 (TM1) is a quantitative stock selection model designed to capture the technical dynamics of single US equities over one to ten trading day horizons. TM1 is a tactical factor, in that it can assist a longer- horizon investor in timing their entry or exit points, or be used in combination with existing systematic or qualitative strategies with similar holding periods.
    In historical simulations, high-scoring stocks according to TM1 outperform low- scoring stocks by 59% per annum with a market-neutral Sharpe ratio of 4.4 before transaction costs, versus 25% and a Sharpe of 1.1 for a basic reversal factor with comparable turnover. Unlike many quantitative stock selection factors, TM1 exhibits comparable returns for large-cap stocks and small-cap stocks, and it is particularly effective in volatile regimes.
    TM1’s alpha is realized between one and ten days, and so may not be appropriate as a signal on which to trade directly for some investment managers with long horizons or large AUMs. However TM1 could be used to time trades that a longer-horizon strategy would enter regardless, thereby improving the price of the entry and exit points without incurring incremental transaction costs.
    A basic fundamental and momentum strategy with annual net returns of 5.5%, a net Sharpe Ratio of 0.55, and daily turnover of 6.4% can be improved to annual net returns of 10.0% and a net Sharpe Ratio of 0.97, with a slight reduction of turnover, by implementing simple TM1-based entry and exit rules. The value added is very consistent over time, offers drawdown protection in volatile markets, and survives reasonable transaction cost and latency assumptions.
    TM1 is therefore effective as a tactical overlay which can improve risk-adjusted returns without unduly influencing the underlying strategy. The implementation could be as straightforward as a daily pre-trade screen on position entries and exits prior to the open.
    History available from January 2000
    https://iexcloud.io/docs/api/#tactical-model-1
    '''
    return _base(id='PREMIUM_EXTRACT_ALPHA_TM', symbol=symbol, **kwargs)


@wraps(timeSeries)
def tacticalModel1DF(symbol='', **kwargs):
    '''The ExtractAlpha Tactical Model 1 (TM1) is a quantitative stock selection model designed to capture the technical dynamics of single US equities over one to ten trading day horizons. TM1 is a tactical factor, in that it can assist a longer- horizon investor in timing their entry or exit points, or be used in combination with existing systematic or qualitative strategies with similar holding periods.
    In historical simulations, high-scoring stocks according to TM1 outperform low- scoring stocks by 59% per annum with a market-neutral Sharpe ratio of 4.4 before transaction costs, versus 25% and a Sharpe of 1.1 for a basic reversal factor with comparable turnover. Unlike many quantitative stock selection factors, TM1 exhibits comparable returns for large-cap stocks and small-cap stocks, and it is particularly effective in volatile regimes.
    TM1’s alpha is realized between one and ten days, and so may not be appropriate as a signal on which to trade directly for some investment managers with long horizons or large AUMs. However TM1 could be used to time trades that a longer-horizon strategy would enter regardless, thereby improving the price of the entry and exit points without incurring incremental transaction costs.
    A basic fundamental and momentum strategy with annual net returns of 5.5%, a net Sharpe Ratio of 0.55, and daily turnover of 6.4% can be improved to annual net returns of 10.0% and a net Sharpe Ratio of 0.97, with a slight reduction of turnover, by implementing simple TM1-based entry and exit rules. The value added is very consistent over time, offers drawdown protection in volatile markets, and survives reasonable transaction cost and latency assumptions.
    TM1 is therefore effective as a tactical overlay which can improve risk-adjusted returns without unduly influencing the underlying strategy. The implementation could be as straightforward as a daily pre-trade screen on position entries and exits prior to the open.
    History available from January 2000
    https://iexcloud.io/docs/api/#tactical-model-1
    '''
    return _baseDF(id='PREMIUM_EXTRACT_ALPHA_TM', symbol=symbol, **kwargs)
