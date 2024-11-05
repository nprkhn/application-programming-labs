import os

class ImageIterator:
    def __init__(self, directory: str):
        self.images = [images for images in os.listdir(directory)]
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index <= len(self.images):
            self_next = self.images[self.index]
            self.index += 1

            return self_next
        else: raise StopIteration
