class Television():
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL
        self.prev = 0

    def power(self):
        if self._status == False:
            self._status = True
        else:
            self._status = False
    
    def mute(self):
         if self._status == True:
            self._previous_volume = self._volume
            self._volume = self.MIN_VOLUME
            self._muted = True
        

    
    def channel_up(self):
        if self._status == True:
            if self._channel < self.MAX_CHANNEL:
                self._channel += 1
            else:
                self._channel = self.MIN_CHANNEL

    def channel_down(self):
        if self._status == True:
            if self._channel > self.MIN_CHANNEL:
                self._channel -= 1
            else:
                self._channel = self.MAX_CHANNEL

    def volume_down(self):
        if self._status == True:
            if self._volume > self.MIN_VOLUME:
                self._volume -= 1
            if self._muted == True:
                self._volume = self._previous_volume
                if self._volume > self.MIN_VOLUME:
                    self._volume -= 1

    def volume_up(self):
        if self._status == True:
            if self._volume < self.MAX_VOLUME:
                self._volume += 1
            if self._muted == True:
                self._volume = self._previous_volume
                if self._volume < self.MAX_VOLUME:
                    self._volume += 1

    def __str__(self):
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}\n"
