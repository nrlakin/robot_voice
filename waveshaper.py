import numpy as np

class Waveshaper():
    """
    Apply a transform to an audio signal; store transform as curve,
    use curve as lookup table.  Implementation of jQuery's WaveShaperNode
    API:
        http://webaudio.github.io/web-audio-api/#the-waveshapernode-interface
    """
    def __init__(self, curve):
        self.curve = curve
        self.n_bins = self.curve.shape[0]

    def transform(self, samples):
        # normalize to 0 < samples < 2
        max_val = np.max(np.abs(samples))
        if max_val >= 1.0:
            result = samples/np.max(np.abs(samples)) + 1.0
        else:
            result = samples + 1.0
        result = result * (self.n_bins-1)/2
        return self.curve[result.astype(np.int)]
