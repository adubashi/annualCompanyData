# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 21:34:31 2015

@author: aduba_000
"""

import companyAnnualData


proctorGamble = companyAnnualData.companyAnnualData("PG", "PWSvEbf4_oUssZ3WqynR")
#proctorGamble.companyCodes.printAnnualData()
proctorGamble.getAnnualData()
#proctorGamble.printAnnualData()
proctorGamble.exportToJSON()

