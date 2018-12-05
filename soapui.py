#! /usr/bin/env python		#Allow Unix shell to execute as a Python script
# _*_ coding: UTF-8 _*_		#Enable unicode encoding

__author__ = "Ian Pottinger"
__date__ = "20/12/2012"
__contact__ = "ianpottinger@me.com"
__version__ = "1.3.5.7.9 even avoidance"
__credits__ = "Commonly known as Potts"
__copyright__ = "Copyleft for balance"
__license__ = "Whatever Potts Decides"
__metadata__ = [__author__, __date__, __contact__, __version__,
                __credits__, __copyright__, __license__]

import requests

DEBUG_MODE = True
if DEBUG_MODE:
    import pdb
    #pdb.set_trace()
    import logging
    FORMAT = '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'
    logging.basicConfig(level = logging.INFO, format = FORMAT)
    #logging.basicConfig(level = logging.WARNING, format = FORMAT)
    #logging.basicConfig(level = logging.DEBUG, format = FORMAT)
    #logging.basicConfig(level = logging.ERROR, format = FORMAT)
    #logging.basicConfig(level = logging.CRITICAL, format = FORMAT)



url="https://orderingwebservices.externaltest.immform.org.uk/OrderService.svc?wsdl"
#headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml'}
body = """<?xml version="1.0" encoding="UTF-8"?>
         <SOAP-ENV:Envelope xmlns:ns0="http://ws.cdyne.com/WeatherWS/" xmlns:ns1="http://schemas.xmlsoap.org/soap/envelope/" 
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
            <SOAP-ENV:Header/>
              <ns1:Body><ns0:GetWeatherInformation/></ns1:Body>
         </SOAP-ENV:Envelope>"""

response = requests.post(url,data=body,headers=headers)
print (response.content)
