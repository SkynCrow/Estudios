# Configuración para Raspberry Pi B2

## Instalación de Drivers para D-Link DWA-123

Seguir las instrucciones de instalación de este [link](https://forums.raspberrypi.com/viewtopic.php?p=462982#p462982)

Se usaron los siguientes comandos:

    sudo wget http://downloads.fars-robotics.net/wifi-drivers/install-wifi -O /usr/bin/install-wifi
    sudo chmod +x /usr/bin/install-wifi
    sudo install-wifi -h
    sudo install-wifi -c
    sudo install-wifi 8011eu
    sudo shutdown -r

Luego se configuro la interfaz de red

    sudo nano /etc/network/interfaces

Copiar lo siguiente dentro

    source-directory /etc/network/interfaces.d
    iface lo inet loopback
    iface eth0 inet dhcp

    allow-hotplug wlan0
    auto wlan0

    iface wlan0 inet dhcp
    wpa-ssid "DEXTER"
    wpa-psk "marcopolo"
