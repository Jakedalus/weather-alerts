import forecastio

api_key = "fa3f3676521e03d9ae7ee9dd4f98257a"
lat = 40.2884 
lng = -75.2091

forecast = forecastio.load_forecast(api_key, lat, lng)

byDay = forecast.daily()
print "Week's Forecast:", byDay.summary
print "* * *"

now = forecast.currently()
print "Current Conditions:", now.summary, now.temperature
print "* * *"

tomorrow = byDay.data[1]
print "Tomorrow's Forecast:", tomorrow.summary

if abs(tomorrow.pressure - now.pressure) > 6:
	print "** ALERT: Fast pressure change", tomorrow.pressure, "hPa", "to" , now.pressure, "hPa"

#print tomorrow.pressure, now.pressure

for dailyData in byDay.data:
	print "----------------------"
	print dailyData.time
        print dailyData.summary
	print "* * *"
	print "High:", dailyData.temperatureHigh
	print "Low:", dailyData.temperatureLow
	print "Pressure:", dailyData.pressure
	print "Humidity:", dailyData.humidity
	print "Wind Speed:", dailyData.windSpeed
	print "UV Index:", dailyData.uvIndex
	print "Moon Phase:", dailyData.moonPhase
	if dailyData.precipIntensity > 0:
		print "Preciptitation:", dailyData.precipType
		print "Precipitation Intensity:", dailyData.precipIntensity
	print "Sunrise:", dailyData.sunriseTime
	print "Sunset:", dailyData.sunsetTime
