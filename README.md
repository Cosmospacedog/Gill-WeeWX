![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fgillinstruments.com%2Fwp-content%2Fuploads%2F2022%2F01%2FMetConnect.webp&f=1&nofb=1&ipt=be72c154252269260f86fff4c768289b09bc363744aa8df8d65824b53d2cfdf6)
# Gill-WeeWX
This driver facilitates the processing of gill MetConnect weather systems for ingestion into WeeWX.  

This driver has been tested with the Gill MX400, MX500, MX550 and MX600 models, however more may be compatible and feel free to contribute further compatibility.

## Installing
Installation can be either done via the .tar file in releases with:

```
weewx extension install --yes Gill-WeeWX.tar
```

or by pasting the ``'bin'`` folder from the source code into WeeWX and adding the config outlined in ``installer.py`` to ``weewx.conf``.

## Operating
To connect a gill device - first set it up using [Gill MetSet](https://gillinstruments.com/downloads/metset-download-form/) and download your associated ``.mcf`` config file.  

Then, paste the IPv4 and TCP port of your unit along with the path to your config file(make sure WeeWX can access the folder) under the sections outlined.

Finally - in config set your station type to ``Gill`` and enable any relevant units your system is transmitting.
