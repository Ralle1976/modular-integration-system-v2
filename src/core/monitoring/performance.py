class PerformanceMonitor:
    def __init__(self):
        self.metrics = {}
        self.alert_thresholds = {}
        self.alert_callbacks = []
...