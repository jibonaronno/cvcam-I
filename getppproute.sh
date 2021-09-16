#!/bin/bash
pppip.sh
sleep 10
pppstr=$(netstat -rn | grep ppp0)
if  [[ $pppstr == *"ppp0"* ]]; then
	echo "Found ppp"
	IP=$(netstat -rn | awk 'NR==3' | grep ppp0 | awk '{print $2}')
	if [[ $IP == "" ]]; then
		echo "ppp0 is not default"
		pppip=$(pppip.sh)
		if [[ $pppip == "NA" ]]; then
			echo "pppip not found"
		else
			echo "default route to ppp0"
			echo "sudo route del default" 
			sudo route del default
			sleep 3
			echo "sudo route add default gw $pppip"
			sudo route add default gw $pppip
		fi
	else
		echo "ppp0 is default : $IP"
	fi
else
	echo "NO PPP"
fi
