#!/usr/bin/env python
import deepspeech_frontend
import os.path
import requests
 
deepspeech_frontend.app.run(debug=True, host="0.0.0.0",port=5555)
