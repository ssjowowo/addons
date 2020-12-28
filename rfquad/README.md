# RF Quad

This addon was created to replicate commands from quad state transmitters since these cannot be sent using `rpi_rf` platform. 

The remote that sparked this addon is the **Dooya DC1600**, but any quad state remote can be replicated. Quad state commands consist of quad bits in the form of `0, 1, Q, F`.

Currently supported commands: open, closed, stop.

## Sniffing Commands

Commands can only be sniffed using arduino and [Raspi-Rollo](https://github.com/bjwelker/Raspi-Rollo/tree/master/Arduino/Rollo_Code_Receiver).

## Transmitter
For this addon, I am using the following transmitter and receiver module: [link](https://www.aliexpress.com/item/968306683.html)

Instruction on how to set the modules up can be found [here](https://pypi.org/project/rpi-rf/).
## Configuration

Configuration options:

| Option | Note | 
| -- | -- | 
| component | The device type component to create. Any type listed [here](https://www.home-assistant.io/docs/mqtt/discovery/) will work | 
| object_id | The object ID to be created in HA | 
| commands | The quad state RF commands to be used for each operation. Currently supported are open, close and stop commands | 
| mqtt | The MQTT configuration | 

    {
		"component": "cover",
		"object_id": "blinds",
		"operations": {
			"open": "",
			"close": "",
			"stop": "",
		},
		"mqtt": {
			"host": "core-mosquitto",
			"user": "",
			"password": ""
		}
	}

## Special thanks
https://pypi.org/project/rpi-rf/
https://github.com/WiringPi/WiringPi.git
https://github.com/bjwelker/Raspi-Rollo
Icons made by [Freepik](https://www.flaticon.com/authors/freepik) from [www.flaticon.com](https://www.flaticon.com)