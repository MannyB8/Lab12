class Television():
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        '''
        When called this function sets up the instance variables.
        '''
        self._status: bool = False
        self._muted: bool = False
        self._volume: int = self.MIN_VOLUME
        self._channel: int = self.MIN_CHANNEL
        self.prev: int = 0

    def power(self):
        """
        When called this function turns the tv on and off.
        """
        if self._status == False:
            self._status = True
        else:
            self._status = False
    
    def mute(self):
         '''
         When called this function mutes the volume on the tv if it is on.
         '''
         if self._status == True:
            self._previous_volume = self._volume
            self._volume = self.MIN_VOLUME
            self._muted = True
        

    
    def channel_up(self):
        '''
         When called this function moves the channel up one. If the channel is equal to the max it returns to the lowest channel.
        '''
        if self._status == True:
            if self._channel < self.MAX_CHANNEL:
                self._channel += 1
            else:
                self._channel = self.MIN_CHANNEL

    def channel_down(self):
        '''
         When called this function moves the channel down one. If the channel is equal to the minimum it returns to the highest channel.
        '''
        if self._status == True:
            if self._channel > self.MIN_CHANNEL:
                self._channel -= 1
            else:
                self._channel = self.MAX_CHANNEL

    def volume_down(self):
        '''
         When called this function moves the volume down one.
        '''
        if self._status == True:
            if self._volume > self.MIN_VOLUME:
                self._volume -= 1
            if self._muted == True:
                self._volume = self._previous_volume
                if self._volume > self.MIN_VOLUME:
                    self._volume -= 1

    def volume_up(self):
        '''
         When called this function moves the volume up one.
        '''
        if self._status == True:
            if self._volume < self.MAX_VOLUME:
                self._volume += 1
            if self._muted == True:
                self._volume = self._previous_volume
                if self._volume < self.MAX_VOLUME:
                    self._volume += 1

    def __str__(self):
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}\n"
