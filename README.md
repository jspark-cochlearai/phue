# sense-phue (sense-python + phue)

## What is sense-phue?

This is a python example to control Philips hue smart light bulb through sense API.  
Sense API provided by Cochlear.ai Ltd. is a powerful tool that enables machines to understand various sounds.  
Using this example, you can turn on and off the light bulb by whistling and change the color by finger snapping.  
Check the link below to see the demonstration:  
https://www.instagram.com/p/B75ewxdhdqD


## Environment setting
### 1. Install phue
Run  
```
$ easy_install phue
```
or
```
$ pip install phue
```

### 2. Portaudio

In order for sense-phue to get the audio stream from your microphone, port-audio is necessary.  
On MacOS, you can install it by
```
$ brew install portaudio
```

On Linux, 
```
$ apt-get update
$ apt-get install ffmpeg sox portaudio19-dev libssl-dev libcurl4-openssl-dev
```

### 3. Install python dependency

This repository was tested in python3.7.5 environment and the compatiblity check in other python versions is still in progress.  
Make sure to have install `pip` before execute the following code.

```
$ pip install -r test-requirements.txt
```

### 4. Get your sense API key

You need to get a key to use sense API. Visit https://cochlear.ai/beta-subscription/ and sign up for free.  
Then put the key inside example_stream.py file.

### 5. Get your Bridge's ip address

The IP address of the bridge can be obtained in the Philips hue mobile app.  
Please put the ip address inside example_stream.py file.

### 6. Set the light bulb index

If you have more than one light bulb, you can select which one to control with this example with the variable *idx*.  


## Launch example

Run
```
$ python example_stream.py
```

For further information, please refer to our API document: http://cochlear.ai/docs/.

## Reference
This repository is merely a combination of the two examples made by Cochlear.ai and Phue.  
For more information, please refer to the original sources.  

1. Phue library
https://github.com/studioimaginaire/phue

2. Sense API and the documentation by Cochlear.ai Ltd.  
https://github.com/cochlearai/sense-python  
http://cochlear.ai/docs/  


