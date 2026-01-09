# Predictive Lifecycle Demo

This purpose of this demo is to show off the full predictive model lifecycle in OpenShift AI. At present the use case is Homeowner's Insurance, with plans to expand in the near future.

## Pre-work

1. Run the Argo application. Once the 2 workbenches are online and all the pods are healthy, you can start the manual work.
2. Log into the `data-generation` workbench in OpenShift AI.
    1. Navigate into the `scripts/` directory, open `generate_data.ipynb` and execute all the cells. Verify that data was successfully created.
3. Log into the `build-model` workbench in OpenShift AI.
    1. Navigate into the `scripts/` directory, open `pipeline.ipynb`, and execute all the cells.
4. Navigate back into OpenShift AI and confirm that the pipeline is running and eventually succeeds.
5. Navigate to Models > Model registry, locate the registry that matches the name of your deployment ("predictive-lifecycle" by default).
    1. Locate the hoi model, and deploy it by your preferred method. The connection information will all automatically populate, so you only need to fill out the other information. The model will be served by OpenVINO as onnx. Check the boxes to deploy it with a route and token authentication. **Critically important, the Path must be `models/hoi`, i.e. drop the version at the end of the path.** This is a quirk in how OpenVINO works with KServe.
6. Log back into the `build-model` workbench.
    1. Run `endpoint.ipynb` in the `scripts/` directory to validate connectivity.

The pipeline that runs consists of three components: train the model, upload it to S3 (by way of MinIO), and register the model into the Model Registry.


## Demo Flow

I would recommend the following steps for this demo:
1. Show how you can create workbenches.
2. Show the `build-model` workbench to demonstrate JupyterLab and integrate with Kubeflow Pipelines.
3. Show the Kubeflow Pipelines.
    1. There is a parameter in `pipeline.ipynb` called `fresh_run`. If you want to demonstrate how KFP will utilize cached runs, leave this parameter the same as your setup run. If you want to show the full pipeline running, set this to any unique value - the parameter doesn't do anything but trick KFP into not using the cache.
4. Talk through how your pipelines can integrate natively with the model registries.
5. Show the model registry, and how easy it is to deploy models.
6. Show how then you can interact with the newly created model endpoint. If you use the defaults of the entire demo, all you will need to do is potentially change the model version in `endpoint.ipynb`.


## Notes

* The data is generated over a time period, so you will get different models if you train on different days. This is by design.