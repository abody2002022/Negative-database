class AISDetector:
    def __init__(self, pattern):
        self.pattern = pattern

    def match(self, input_pattern):
        # Compare the input pattern to the detector pattern
        if self.pattern == input_pattern:
            return True
        else:
            return False

# Create some example detector patterns
detector1 = AISDetector("001010")
detector2 = AISDetector("111000")
detector3 = AISDetector("101010")

# Input pattern to test against detectors
input_pattern = "001010"

# Check if the input pattern matches any of the detectors
detectors = [detector1, detector2, detector3]
for detector in detectors:
    if detector.match(input_pattern):
        print(f"Input pattern matches detector pattern: {detector.pattern}")
    else:
        print(f"Input pattern does not match detector pattern: {detector.pattern}")
