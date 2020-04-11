def estimator(data):
		
	#Convert or check that 'timeToElapse' is in days
	if data['periodType'] == 'days':
		timeInDays = data['timeToElapse']
	elif data['periodType'] == 'weeks':
		timeInDays = data['timeToElapse'] * 7
	elif data['periodType'] == 'months':
		timeInDays = data['timeToElapse'] * 30

	#Compute estimates:
	##Impact computation
	impactCurrentlyInfected = data['reportedCases'] * 10
	impactInfectionsByRequestedTime = (data['reportedCases'] * 10) * (2 ** (timeInDays // 3))
	impactSevereCasesByRequestedTime = 0.15 * (data['reportedCases'] * 10) * (2 ** (timeInDays // 3))
	impactHospitalBedsByRequestedTime = (0.35 * data['totalHospitalBeds']) - impactSevereCasesByRequestedTime

	#Compute estimates:
	##Severe Impact computation
	severeImpactCurrentlyInfected = data['reportedCases'] * 50
	severeImpactInfectionsByRequestedTime = (data['reportedCases'] * 50) * (2 ** (timeInDays // 3))
	severeImpactSevereCasesByRequestedTime =  0.15 * (data['reportedCases'] * 50) * (2 ** (timeInDays // 3))
	severeImpactHospitalBedsByRequestedTime = (0.35 * data['totalHospitalBeds']) - severeImpactSevereCasesByRequestedTime

	#Estimates
	estimate = {
		'impact' : {
			'currentlyInfected' : impactCurrentlyInfected,
			'infectionsByRequestedTime' : impactInfectionsByRequestedTime,
			'severeCasesByRequestedTime' : impactSevereCasesByRequestedTime,
			'HospitalBedsByRequestedTime' : impactHospitalBedsByRequestedTime
		},

		'severeImpact' : {
				'currentlyInfected' : severeImpactCurrentlyInfected,
				'infectionsByRequestedTime' :  severeImpactInfectionsByRequestedTime,
				'severeCasesByRequestedTime' : severeImpactSevereCasesByRequestedTime,
				'HospitalBedsByRequestedTime' : severeImpactHospitalBedsByRequestedTime
		}

	}
	return estimate
