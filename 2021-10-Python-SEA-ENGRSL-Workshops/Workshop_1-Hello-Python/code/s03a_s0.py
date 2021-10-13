if host.connected:
	for port in commonPorts:
		if poll(host, port) == "ONLINE":
			openPorts.append(port)
		else:
			closedCount += 1
else:
	...
