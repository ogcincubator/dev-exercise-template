# README - Implementers of OGC API - Features 🚀

**This README is aimed at implementers OGC API - Features. If your goal is to run the Module 3 assignment and publish data using OGC API - Features, please go to this [README](.README-publishers.md) instead.**

If you would like to add support to another implementation of OGC API - Features, please follow the instructions below. OGC welcomes any OGC API - Features implementations that fullfil the requirements below, regardless of their license model. 

## Add another OGC API - Features implementation

Before starting, make sure that:

- ✅ *The OGC API - Features implementation is Dockerised. If the software is not available through DockerHub or another Docker repository, please add a directory with a `Dockerfile` so that it can be built by the user.*
- ✅ *If a license is required, all the instructions in order to obtain and use that license are clearly described.*
- ✅ *You agree with the [LICENSE](../LICENSE) on this repository. Although your software may have a different license, the files to create and run the service, along with the instructions should share the main license of the repository.*

1. Create a directory with your implementation. This directory should be placed under [./apps](.) and named after your OGC API - Features implementation (see [./pygeoapi](./pygeoapi/) example for reference).
2. Create a `data` sub-directory within that directory, and place your vector dataset there, in a suitable format. The user should be able to ingest that format in the OGC API server, without additional processing. You are welcome to reuse [this](./pygeoapi/data/canada-hydat-daily-mean-02HC003.tinydb) dataset or to use a different one. 
3. Create a `docker-compose.yml` file in the root of that directory. That file should start the OGC API server, along with any other support services that may be required, and ingest and publish the dataset. If extra configuration parameters are needed (e.g.: license, credentials), it should be clearly explained how to obtain and use them. Additional configuration files can be placed on that directory, or sub-directories.
4. Comment relevant parts of the `docker-compose.yml` file and/or configuration files. The user should uncomment these parts, in order to run the implementation successfully.
5. Create a `README` file in the root of that directory. Make sure that all the instructions to configure and run the implementation are clearly described.
6. Add your implementation to the Implementations section of the [README](README-publishers.md#implementations) file on this directory. 
7. Add a job for testing that implementation on [./github/workflows/main.yml](../.github/workflows/main.yml). This job should start the services in the `docker-compose.yml` file and run the [cite tests](https://github.com/OSGeo/cite-runner). You can see an example [here](../.github/workflows/main.yml#L12).
8. After completing the steps below, please create a [Pull Request](https://github.com/ogcincubator/dev-exercise-template/pulls) to add an exercise with your implementation of OGC API - Features.

We thank you in advance for your contribution! 🙏
