# -*- coding: utf-8 -*-
from functools import wraps
from ...stocks import timeSeries, timeSeriesDF
from ...common import _interval


@_interval(hours=4)
def _base(id, symbol='', **kwargs):
    '''internal'''
    kwargs['id'] = id
    kwargs['key'] = symbol or kwargs.pop('key', '')
    return timeSeries(**kwargs)


@_interval(hours=4)
def _baseDF(id, symbol='', **kwargs):
    '''internal'''
    kwargs['id'] = id
    kwargs['key'] = symbol or kwargs.pop('key', '')
    return timeSeriesDF(**kwargs)


@wraps(timeSeries)
def analystDays(symbol='', **kwargs):
    '''This is a meeting where company executives provide information about the company’s performance and its future prospects.

    https://iexcloud.io/docs/api/#analyst-days
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_ANALYST_DAY', symbol=symbol, **kwargs)


@wraps(timeSeries)
def analystDaysDF(symbol='', **kwargs):
    '''This is a meeting where company executives provide information about the company’s performance and its future prospects.

    https://iexcloud.io/docs/api/#analyst-days
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_ANALYST_DAY', symbol=symbol, **kwargs)


@wraps(timeSeries)
def boardOfDirectorsMeeting(symbol='', **kwargs):
    '''This is an end-point for getting information about a formal meeting of a company’s board of directors to establish corporate management related policies and to make decisions on major company issues.
    https://iexcloud.io/docs/api/#analyst-days
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_BOARD_OF_DIRECTORS_MEETING', symbol=symbol, **kwargs)


@wraps(timeSeries)
def boardOfDirectorsMeetingDF(symbol='', **kwargs):
    '''This is a meeting where company executives provide information about the company’s performance and its future prospects.
    https://iexcloud.io/docs/api/#board-of-directors-meeting
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_BOARD_OF_DIRECTORS_MEETING', symbol=symbol, **kwargs)


@wraps(timeSeries)
def businessUpdates(symbol='', **kwargs):
    '''This is a meeting orconference call in which company information is reviewed by one or more company executives.
    https://iexcloud.io/docs/api/#business-updates
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_BUSINESS_UPDATE', symbol=symbol, **kwargs)


@wraps(timeSeries)
def businessUpdatesDF(symbol='', **kwargs):
    '''This is a meeting orconference call in which company information is reviewed by one or more company executives.
    https://iexcloud.io/docs/api/#business-updates
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_BUSINESS_UPDATE', symbol=symbol, **kwargs)


@wraps(timeSeries)
def buybacks(symbol='', **kwargs):
    '''The repurchase of outstanding shares by a company to reduce the number of shares on the market.
    https://iexcloud.io/docs/api/#buybacks
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_BUYBACK', symbol=symbol, **kwargs)


@wraps(timeSeries)
def buybacksDF(symbol='', **kwargs):
    '''The repurchase of outstanding shares by a company to reduce the number of shares on the market.
    https://iexcloud.io/docs/api/#buybacks
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_BUYBACK', symbol=symbol, **kwargs)


@wraps(timeSeries)
def capitalMarketsDay(symbol='', **kwargs):
    '''This is a meeting where company executives provide information about the company’s performance and its future prospects.
    https://iexcloud.io/docs/api/#capital-markets-day
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_CAPITAL_MARKETS_DAY', symbol=symbol, **kwargs)


@wraps(timeSeries)
def capitalMarketsDayDF(symbol='', **kwargs):
    '''This is a meeting where company executives provide information about the company’s performance and its future prospects.
    https://iexcloud.io/docs/api/#capital-markets-day
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_CAPITAL_MARKETS_DAY', symbol=symbol, **kwargs)


@wraps(timeSeries)
def companyTravel(symbol='', **kwargs):
    '''This is a roadshow or bus tour event in which one or more company executives speaks to interested investors and analysts.
    https://iexcloud.io/docs/api/#company-travel
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_COMPANY_TRAVEL', symbol=symbol, **kwargs)


@wraps(timeSeries)
def companyTravelDF(symbol='', **kwargs):
    '''This is a roadshow or bus tour event in which one or more company executives speaks to interested investors and analysts.
    https://iexcloud.io/docs/api/#company-travel
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_COMPANY_TRAVEL', symbol=symbol, **kwargs)


@wraps(timeSeries)
def filingDueDates(symbol='', **kwargs):
    '''This is an estimated date, based on historical trends for this company in which a company must file the appropriate Form for the quarter/year or file for an extension.
    https://iexcloud.io/docs/api/#filing-due-dates
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_FILING_DUE_DATE', symbol=symbol, **kwargs)


@wraps(timeSeries)
def filingDueDatesDF(symbol='', **kwargs):
    '''This is an estimated date, based on historical trends for this company in which a company must file the appropriate Form for the quarter/year or file for an extension.
    https://iexcloud.io/docs/api/#filing-due-dates
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_FILING_DUE_DATE', symbol=symbol, **kwargs)


@wraps(timeSeries)
def fiscalQuarterEnd(symbol='', **kwargs):
    '''This is a forecasted quarterly ending announcement date for a company. This may or may not correspond to a calendar quarter.
    https://iexcloud.io/docs/api/#fiscal-quarter-end
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_FISCAL_QUARTER_END_DATE', symbol=symbol, **kwargs)


@wraps(timeSeries)
def fiscalQuarterEndDF(symbol='', **kwargs):
    '''This is a forecasted quarterly ending announcement date for a company. This may or may not correspond to a calendar quarter.
    https://iexcloud.io/docs/api/#fiscal-quarter-end
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_FISCAL_QUARTER_END_DATE', symbol=symbol, **kwargs)


@wraps(timeSeries)
def forum(symbol='', **kwargs):
    '''This is a meeting where ideas and views of a business nature can be exchanged.
    https://iexcloud.io/docs/api/#forum
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_FORUM', symbol=symbol, **kwargs)


@wraps(timeSeries)
def forumDF(symbol='', **kwargs):
    '''This is a meeting where ideas and views of a business nature can be exchanged.
    https://iexcloud.io/docs/api/#forum
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_FORUM', symbol=symbol, **kwargs)


@wraps(timeSeries)
def generalConference(symbol='', **kwargs):
    '''This is a formal meeting in which representatives of many companies gather to discuss ideas or issues related to a particular topic or business, usually held for several days. This item indicates at least one representative from the company will be presenting at the conference on the specified date and time. Note: Conference details include full Conference dates.
    https://iexcloud.io/docs/api/#general-conference
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_GENERAL_CONFERENCE', symbol=symbol, **kwargs)


@wraps(timeSeries)
def generalConferenceDF(symbol='', **kwargs):
    '''This is a formal meeting in which representatives of many companies gather to discuss ideas or issues related to a particular topic or business, usually held for several days. This item indicates at least one representative from the company will be presenting at the conference on the specified date and time. Note: Conference details include full Conference dates.
    https://iexcloud.io/docs/api/#general-conference
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_GENERAL_CONFERENCE', symbol=symbol, **kwargs)


@wraps(timeSeries)
def fdaAdvisoryCommitteeMeetings(symbol='', **kwargs):
    '''The FDA uses 50 committees and panels to obtain independent expert advice on scientific, technical, and policy matters
    https://iexcloud.io/docs/api/#fda-advisory-committee-meetings
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_STOCK_SPECIFIC_FDA_ADVISORY_COMMITTEE_MEETING', symbol=symbol, **kwargs)


@wraps(timeSeries)
def fdaAdvisoryCommitteeMeetingsDF(symbol='', **kwargs):
    '''The FDA uses 50 committees and panels to obtain independent expert advice on scientific, technical, and policy matters
    https://iexcloud.io/docs/api/#fda-advisory-committee-meetings
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_STOCK_SPECIFIC_FDA_ADVISORY_COMMITTEE_MEETING', symbol=symbol, **kwargs)


@wraps(timeSeries)
def holidaysWSH(symbol='', **kwargs):
    '''This returns a list of market holidays.
    https://iexcloud.io/docs/api/#holidays
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_HOLIDAYS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def holidaysWSHDF(symbol='', **kwargs):
    '''This returns a list of market holidays.
    https://iexcloud.io/docs/api/#holidays
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_HOLIDAYS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def indexChanges(symbol='', **kwargs):
    '''This shows additions and removals from various indexes for particular stocks.
    https://iexcloud.io/docs/api/#index-changes
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_INDEX_CHANGE', symbol=symbol, **kwargs)


@wraps(timeSeries)
def indexChangesDF(symbol='', **kwargs):
    '''This shows additions and removals from various indexes for particular stocks.
    https://iexcloud.io/docs/api/#index-changes
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_INDEX_CHANGE', symbol=symbol, **kwargs)


@wraps(timeSeries)
def iposWSH(symbol='', **kwargs):
    '''Get a list of upcoming IPOs.
    https://iexcloud.io/docs/api/#ipos
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_INITIAL_PUBLIC_OFFERING', symbol=symbol, **kwargs)


@wraps(timeSeries)
def iposWSHDF(symbol='', **kwargs):
    '''Get a list of upcoming IPOs.
    https://iexcloud.io/docs/api/#ipos
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_INITIAL_PUBLIC_OFFERING', symbol=symbol, **kwargs)


@wraps(timeSeries)
def legalActions(symbol='', **kwargs):
    '''These are legal actions where an individual represents a group in a court claim. The judgment from the suit is for all the members of the group or class.
    https://iexcloud.io/docs/api/#legal-actions
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_LEGAL_ACTIONS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def legalActionsDF(symbol='', **kwargs):
    '''These are legal actions where an individual represents a group in a court claim. The judgment from the suit is for all the members of the group or class.
    https://iexcloud.io/docs/api/#legal-actions
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_LEGAL_ACTIONS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def mergersAndAcquisitions(symbol='', **kwargs):
    '''These are a type of corporate action in which two companies combine to form a single company, or one company is taken over by another.
    https://iexcloud.io/docs/api/#mergers-acquisitions
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_MERGER_ACQUISITIONS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def mergersAndAcquisitionsDF(symbol='', **kwargs):
    '''These are a type of corporate action in which two companies combine to form a single company, or one company is taken over by another.
    https://iexcloud.io/docs/api/#mergers-acquisitions
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_MERGER_ACQUISITIONS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def productEvents(symbol='', **kwargs):
    '''Represents movie and video releases. This is the date on which a movie distributor plans to release a movie to theaters
    https://iexcloud.io/docs/api/#product-events
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_PRODUCT_EVENTS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def productEventsDF(symbol='', **kwargs):
    '''Represents movie and video releases. This is the date on which a movie distributor plans to release a movie to theaters
    https://iexcloud.io/docs/api/#product-events
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_PRODUCT_EVENTS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def researchAndDevelopmentDays(symbol='', **kwargs):
    '''This is a day in which investors and analysts can meet with a company’s R&D representatives to learn more about new or improved products and services.
    https://iexcloud.io/docs/api/#research-and-development-days
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_RD_DAY', symbol=symbol, **kwargs)


@wraps(timeSeries)
def researchAndDevelopmentDaysDF(symbol='', **kwargs):
    '''This is a day in which investors and analysts can meet with a company’s R&D representatives to learn more about new or improved products and services.
    https://iexcloud.io/docs/api/#research-and-development-days
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_RD_DAY', symbol=symbol, **kwargs)


@wraps(timeSeries)
def sameStoreSales(symbol='', **kwargs):
    '''Same-store sales, also referred to as comparable-store sales, SSS or identical-store sales, is a financial metric that companies in the retail industry use to evaluate the total dollar amount of sales in the company’s stores that have been operating for a year or more.
    https://iexcloud.io/docs/api/#same-store-sales
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_SAME_STORE_SALES', symbol=symbol, **kwargs)


@wraps(timeSeries)
def sameStoreSalesDF(symbol='', **kwargs):
    '''Same-store sales, also referred to as comparable-store sales, SSS or identical-store sales, is a financial metric that companies in the retail industry use to evaluate the total dollar amount of sales in the company’s stores that have been operating for a year or more.
    https://iexcloud.io/docs/api/#same-store-sales
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_SAME_STORE_SALES', symbol=symbol, **kwargs)


@wraps(timeSeries)
def secondaryOfferings(symbol='', **kwargs):
    '''Secondary Offerings are the issuance of new stock for public sale from a company that has already made its initial public offering (IPO).
    Usually, these kinds of public offerings are made by companies wishing to refinance, or raise capital for growth.
    Money raised from these kinds of secondary offerings goes to the company, through the investment bank that underwrites the offering.
    Investment banks are issued an allotment, and possibly an overallotment which they may choose to exercise if there is a strong possibility of making money on the spread between the allotment price and the selling price of the securities. Short Selling is prohibited during the period of the secondary offering.
    https://iexcloud.io/docs/api/#secondary-offerings
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_SECONDARY_OFFERING', symbol=symbol, **kwargs)


@wraps(timeSeries)
def secondaryOfferingsDF(symbol='', **kwargs):
    '''Secondary Offerings are the issuance of new stock for public sale from a company that has already made its initial public offering (IPO).
    Usually, these kinds of public offerings are made by companies wishing to refinance, or raise capital for growth.
    Money raised from these kinds of secondary offerings goes to the company, through the investment bank that underwrites the offering.
    Investment banks are issued an allotment, and possibly an overallotment which they may choose to exercise if there is a strong possibility of making money on the spread between the allotment price and the selling price of the securities. Short Selling is prohibited during the period of the secondary offering.
    https://iexcloud.io/docs/api/#secondary-offerings
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_SECONDARY_OFFERING', symbol=symbol, **kwargs)


@wraps(timeSeries)
def seminars(symbol='', **kwargs):
    '''This is an educational event that features one or more subject matter experts delivering information via lecture and discussion.
    https://iexcloud.io/docs/api/#seminars
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_SEMINAR', symbol=symbol, **kwargs)


@wraps(timeSeries)
def seminarsDF(symbol='', **kwargs):
    '''This is an educational event that features one or more subject matter experts delivering information via lecture and discussion.
    https://iexcloud.io/docs/api/#seminars
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_SEMINAR', symbol=symbol, **kwargs)


@wraps(timeSeries)
def shareholderMeetings(symbol='', **kwargs):
    '''This is a meeting, held at least annually, to elect members to the board of directors and hear reports on the business’ financial situation as well as new policy initiatives from the corporation’s management.
    https://iexcloud.io/docs/api/#shareholder-meetings
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_SHAREHOLDER_MEETING', symbol=symbol, **kwargs)


@wraps(timeSeries)
def shareholderMeetingsDF(symbol='', **kwargs):
    '''This is a meeting, held at least annually, to elect members to the board of directors and hear reports on the business’ financial situation as well as new policy initiatives from the corporation’s management.
    https://iexcloud.io/docs/api/#shareholder-meetings
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_SHAREHOLDER_MEETING', symbol=symbol, **kwargs)


@wraps(timeSeries)
def summitMeetings(symbol='', **kwargs):
    '''This is a gathering of people who are interested in the same business subject or topic.
    https://iexcloud.io/docs/api/#summit-meetings
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_SUMMIT_MEETING', symbol=symbol, **kwargs)


@wraps(timeSeries)
def summitMeetingsDF(symbol='', **kwargs):
    '''This is a gathering of people who are interested in the same business subject or topic.
    https://iexcloud.io/docs/api/#summit-meetings
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_SUMMIT_MEETING', symbol=symbol, **kwargs)


@wraps(timeSeries)
def tradeShows(symbol='', **kwargs):
    '''This is a large gathering in which different companies in a particular field or industry show their products to possible customers.
    https://iexcloud.io/docs/api/#trade-shows
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_TRADE_SHOW', symbol=symbol, **kwargs)


@wraps(timeSeries)
def tradeShowsDF(symbol='', **kwargs):
    '''This is a large gathering in which different companies in a particular field or industry show their products to possible customers.
    https://iexcloud.io/docs/api/#trade-shows
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_TRADE_SHOW', symbol=symbol, **kwargs)


@wraps(timeSeries)
def witchingHours(symbol='', **kwargs):
    '''This is when option contracts and futures contracts expire on the exact same day.
    https://iexcloud.io/docs/api/#witching-hours
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_WITCHING_HOURS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def witchingHoursDF(symbol='', **kwargs):
    '''This is when option contracts and futures contracts expire on the exact same day.
    https://iexcloud.io/docs/api/#witching-hours
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_WITCHING_HOURS', symbol=symbol, **kwargs)


@wraps(timeSeries)
def workshops(symbol='', **kwargs):
    '''This is a meeting or series of meetings at which a group of people engage in discussion and activity on a particular subject, product or service to gain hands-on experience.
    https://iexcloud.io/docs/api/#workshops
    '''
    return _base(id='PREMIUM_WALLSTREETHORIZON_WORKSHOP', symbol=symbol, **kwargs)


@wraps(timeSeries)
def workshopsDF(symbol='', **kwargs):
    '''This is a meeting or series of meetings at which a group of people engage in discussion and activity on a particular subject, product or service to gain hands-on experience.
    https://iexcloud.io/docs/api/#workshops
    '''
    return _baseDF(id='PREMIUM_WALLSTREETHORIZON_WORKSHOP', symbol=symbol, **kwargs)
