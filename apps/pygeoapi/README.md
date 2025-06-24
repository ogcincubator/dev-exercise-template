# pygeoapi

This repository contains the necessary files to standup an implementation of pygeoapi and publish the data on the [data](./data) folder.

[pygeoapi](https://pygeoapi.io/) is a Python server implementation of the OGC API suite of standards. It is a Reference Implementation for OGC API - Features, OGC API - Tiles and OGC API - Environmental Data Retrieval, and compliance certified for OGC API - Processes.

You can learn more about pygeoapi in the [Diving into pygeoapi Workshop](https://dive.pygeoapi.io/).

## Quick-Start

Start the server with:

```bash
docker compose --env-file .env up
```

Or, if you want to run it in the background:

```bash
docker compose --env-file .env up -d
```

The landing page is available at: http://localhost:5001/

```bash
curl -I http://localhost:5001/
```

## About the Data

On the [data](./data) folder you will find an tinydb database containing daily means of water level or flow. The daily mean is the average of all unit values for a given day. This dataset is provided by the [National Hydrological Service (NHS) of Canada](https://wateroffice.ec.gc.ca/).
