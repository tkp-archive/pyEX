
def makeTick(open, high, low, close, volume, count=100):
    '''generate a random path from `open` to `close`,
    touching both `high` and `low`, over a total volume
    of `volume` points.

    volumes->
        sample `count` elements from uniform,
        scale to `count` in whole number increments

    options:
        open-high-low-close
        open-low-close-high
        open-high-close (low is open)
        open-high-close (low is close)
        open-low-close  (high is open)
        open-low-close (high is close)
        open-close (high is open, low is close)
        open-close (low is open, high is close)
    '''
    pass
