class Heart:
    def __init__(self, heart_rate=72, stroke_volume=70):
        self.heart_rate = heart_rate  # Beats per minute
        self.stroke_volume = stroke_volume  # mL per beat
        self.output = 0  # Blood flow (mL/min)

    def pump(self):
        # Calculate blood flow per minute
        self.output = self.heart_rate * self.stroke_volume
        print(f"Heart pumping: {self.output} mL/min")