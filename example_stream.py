#################################################################################
# Copyright 2019 Cochlear.ai Ltd. All Rights Reserved.                          #
#                                                                               #
# This is an example to control Philips hue smart light bulb through sense API. #
# Human-generating sound events such as whistling or finger snapping sounds     #
# can be interpreted by sense API. In this example, you can turn on and off     #
# the light bulb by whistling and change the color by finger snapping.          #
# Check this link below to see the demonstration:                               #
# https://www.instagram.com/p/B8JUc0Ah4ep                                       #
#################################################################################

import json
import pprint
import time

from common.sense import SenseStreamer
from common.sense import sense_stream_request
from common.sense import sense_stream_response
import numpy as np
from phue import Bridge


def switch_color(color):
    # Color change rules
    if color == [1,0]:  # Red
        color_new = [0,1]
    elif color == [0,1]:  # Green
        color_new = [0,0]
    elif color == [0,0]:  # Blue
        color_new = [0.3,0.3]
    elif color == [0.3,0.3]:  # White
        color_new = [1,0]
    return color_new


# # Step 1: Phue settings
# If the app is not registered and the button is not pressed, 
# press the button and call connect() (this only needs to be run a single time)
b = Bridge('IP_ADDRESS_OF_YOUR_BRIDGE')
b.connect()
b.get_api()
lights = b.get_light_objects()
# The light index you want to control (0 ~ number_of_Phue - 1)
idx = 0


# # Step 2: Sense API-related parameters
apikey = 'YOUR_SENSE_API_KEY_HERE'
task = 'event'
prev_tag = ''
current_color = [0.3,0.3]  # Initial color is white


# # Step 3: Streaming begins
with SenseStreamer(task) as stream:
    audio_generator = stream.generator()
    requests = sense_stream_request(audio_generator,apikey,task)
    responses = sense_stream_response(requests)
    print('Listening...')
    
    for i in responses:
        mytag = json.loads(i.outputs)['result']['frames'][0]['tag']
        print('Detected event: {}'.format(mytag))

        # Action definition
        if prev_tag != mytag:
            # Whistle + already on : Reset the brightness to max
            # Whistle + currently off : Turn on and set the brightness to max
            if mytag == 'Whistling':
                if lights[idx].on == False:
                    lights[idx].on = True
                lights[idx].brightness = 255

            # Knock : turn off the light
            elif mytag == 'Knock' and lights[idx].on:
                lights[idx].on = False
            
            # Finger snap : change the color
            # (white -> r -> g -> b -> white ...)
            elif mytag == 'Finger_snap' and lights[idx].on:
                # Change the color
                current_color = switch_color(current_color)
                lights[idx].xy = current_color

            # Whisper: dim the light (or turn it off if it's too dark)
            elif mytag == 'Whisper':
                if lights[idx].brightness >= 100:
                    lights[idx].brightness -= 100
                else:
                    lights[idx].on = False

            elif mytag == 'Laughter':
                for n in range(3):
                    lights[idx].on = not lights[idx].on
                    time.sleep(0.5)
                lights[idx].on = not lights[idx].on

        prev_tag = mytag



