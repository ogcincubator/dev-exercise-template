# README - Implementers of OGC API - Features 🚀

**This README file is aimed at implementers OGC API - Features (OAF). If your goal is to run the Module 3 assignment and publish data using OAF, please go to this [README](.README-publishers.md) file instead.**

If you would like to add support to another implementation of OAF, please follow the instructions bellow. OGC welcomes any OAF implementations that fullfil the requirements bellow, regardless of their license model. 

## Add another OAF implementation

Before starting, make sure that:

- ✅ *The OAF implementation is dockerised. If the software is not available through docker hub or another docker repository, please add a folder with the Dockerfile so that it can be build by the user.*
- ✅ *If a license is required, all the instructions in order to obtain and use that license are clearly stated.*
- ✅ *You agree with the [LICENSE](../LICENSE) on this repository. Although your software may have a different license, the files to create and run the service, along with the instructions should share the main license of the repository.*

1. Create a folder with your implementation. This folder should be placed under [./apps](.) and named after your OAF implementation (see [./pygeoapi](./pygeoapi/) example for reference).
2. Create a `data` sub folder within that folder, and place your vector dataset there, in a suitable format. The user should be able to ingest that format in the OGC API server, without additional processing. You are welcome to reuse [this](./pygeoapi/data/canada-hydat-daily-mean-02HC003.tinydb) dataset or to use a different one. 
3. Create a `docker-compose.yml` file on the root of that folder. That file should start the OGC API server, along with any other support services that may be required, and ingest and publish the dataset. If extra configuration parameters are needed (e.g.: license, credentials), it should be clearly explained how to obtain and use them. Additional configuration files can be placed on that folder, or sub-folders.
4. Comment relevant parts of the `docker-compose.yml` file and/or configuration files. The user should uncomment these parts, in order to run the implementation.
5. Create a `README` file on the root of that folder. Make sure that all the instructions to configure and run the implementation are clearly stated.
6. Add a job for testing that implementation on [./github/workflows/main.yml](../.github/workflows/main.yml). This job should start the services on the `docker-compose.yml` file and run the [cite tests](https://github.com/OSGeo/cite-runner). You can see an example [here](../.github/workflows/main.yml#L12).
7. After completing the steps bellow, please create a [Pull Request](https://github.com/ogcincubator/dev-exercise-template/pulls) to add an exercise with your implementation of OAF. We thank you in advance for your contribution! 🙏