import pandas as pd
from mock import MagicMock

C = MagicMock()
S = "AAPL"

C.chartDF.return_value = pd.DataFrame(
    {
        "open": [1.0, 2.0, 3.0, 4.0],
        "close": [1.0, 2.0, 3.0, 4.0],
        "high": [1.0, 2.0, 3.0, 4.0],
        "low": [1.0, 2.0, 3.0, 4.0],
    }
)


class TestAPI:
    def test_peercorrelation(self):
        from pyEX.studies import peerCorrelation

        peerCorrelation(C, S, "6m")

    def test_bollinger(self):
        from pyEX.studies import bollinger

        bollinger(C, S, "6m")

    def test_emasma(self):
        from pyEX.studies import ema, sma, dema

        ema(C, S)
        ema(C, S, periods=30)
        ema(C, S, periods=[30, 45])
        dema(C, S)
        dema(C, S, periods=30)
        dema(C, S, periods=[30, 45])
        sma(C, S)
        sma(C, S, periods=30)
        sma(C, S, periods=[30, 45])

    def test_sar(self):
        from pyEX.studies import sar

        sar(C, S)

    def test_rsi(self):
        from pyEX.studies import rsi

        rsi(C, S)
