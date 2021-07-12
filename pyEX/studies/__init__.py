# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from .peercorrelation import peerCorrelation, peerCorrelationPlot
from .returns import dailyReturns, returns

try:
    from .technicals import *
except ImportError:
    ht_dcperiod = None
    ht_dcphase = None
    ht_phasor = None
    ht_sine = None
    ht_trendmode = None

    acos = None
    asin = None
    atan = None
    ceil = None
    cos = None
    cosh = None
    exp = None
    floor = None
    ln = None
    log10 = None
    sin = None
    sinh = None
    sqrt = None
    tan = None
    tanh = None
    add = None
    div = None
    max = None
    maxindex = None
    min = None
    minindex = None
    minmax = None
    minmaxindex = None
    mult = None
    sub = None
    sum = None

    adx = None
    adxr = None
    apo = None
    aroon = None
    aroonosc = None
    bop = None
    cci = None
    cmo = None
    dx = None
    macd = None
    macdext = None
    mfi = None
    minus_di = None
    minus_dm = None
    mom = None
    plus_di = None
    plus_dm = None
    ppo = None
    roc = None
    rocp = None
    rocr = None
    rocr100 = None
    rsi = None
    stoch = None
    stochf = None
    stochrsi = None
    trix = None
    ultosc = None
    willr = None

    bollinger = None
    dema = None
    ema = None
    ht_trendline = None
    kama = None
    mama = None
    mavp = None
    midpoint = None
    midpice = None
    sar = None
    sarext = None
    sma = None
    t3 = None
    tema = None
    trima = None
    wma = None

    cdl2crows = None
    cdl3blackcrows = None
    cdl3inside = None
    cdl3linestrike = None
    cdl3outside = None
    cdl3starsinsouth = None
    cdl3whitesoldiers = None
    cdlabandonedbaby = None
    cdladvanceblock = None
    cdlbelthold = None
    cdlbreakaway = None
    cdlclosingmarubozu = None
    cdlconcealbabyswallow = None
    cdlcounterattack = None
    cdldarkcloudcover = None
    cdldoji = None
    cdldojistar = None
    cdldragonflydoji = None
    cdlengulfing = None
    cdleveningdojistar = None
    cdleveningstar = None
    cdlgapsidesidewhite = None
    cdlgravestonedoji = None
    cdlhammer = None
    cdlhangingman = None
    cdlharami = None
    cdlharamicross = None
    cdlhighwave = None
    cdlhikkake = None
    cdlhikkakemod = None
    cdlhomingpigeon = None
    cdlidentical3crows = None
    cdlinneck = None
    cdlinvertedhammer = None
    cdlkicking = None
    cdlkickingbylength = None
    cdlladderbottom = None
    cdllongleggeddoji = None
    cdllongline = None
    cdlmarubozu = None
    cdlmatchinglow = None
    cdlmathold = None
    cdlmorningdojistar = None
    cdlmorningstar = None
    cdlonneck = None
    cdlpiercing = None
    cdlrickshawman = None
    cdlrisefall3methods = None
    cdlseparatinglines = None
    cdlshootingstar = None
    cdlshortline = None
    cdlspinningtop = None
    cdlstalledpattern = None
    cdlsticksandwich = None
    cdltakuri = None
    cdltasukigap = None
    cdlthrusting = None
    cdltristar = None
    cdlunique3river = None
    cdlxsidegap3methods = None

    avgprice = None
    medprice = None
    typprice = None
    wclprice = None

    beta = None
    correl = None
    linearreg = None
    linearreg_angle = None
    linearreg_intercept = None
    linearreg_slope = None
    stddev = None
    tsf = None
    var = None

    atr = None
    natr = None
    trange = None

    ad = None
    adosc = None
    obv = None

from .yieldcurve import yieldCurve
