def estimator(data):
		
	#Convert or check that 'timeToElapse' is in days
	if data['periodType'] == 'days':
		timeInDays = data['timeToElapse']
	elif data['periodType'] == 'weeks':
		timeInDays = data['timeToElapse'] * 7
	elif data['periodType'] == 'months':
		timeInDays = data['timeToElapse'] * 30


	#Estimates
	estimate = {
		'impact' : {
			'currentlyInfected' : data['reportedCases'] * 10,
			'infectionsByRequestedTime' : (data['reportedCases'] * 10) * (2 ** (timeInDays // 3)),
			
		},

		'severeImpact' : {
				'currentlyInfected' : data['reportedCases'] * 50,
				'infectionsByRequestedTime' :  (data['reportedCases'] * 50) * (2 ** (timeInDays // 3)),
				
		}

	}
	return estimate
