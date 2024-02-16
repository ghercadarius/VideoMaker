class apiKey:
    #val = "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"
    #make val private
    def __init__(self):
        self.val = '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'
    def get(self):
        return self.val
    def set(self, key):
        self.val = key