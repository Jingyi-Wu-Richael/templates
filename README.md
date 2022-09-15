# 模板目录
INESA AIIC AIMP 中工作流、工作区、任务和边车的模板目录。

## 快速上手
入门的话，最好先了解 AIMP 的 [概念](https://docs.dev.aimpcloud.cn) first.

See the following references for more information on how to build these templates:

- [Workspaces templates](https://docs.onepanel.ai/docs/reference/workspaces/templates)
- [Workflows templates](https://docs.onepanel.ai/docs/reference/workflows/templates)

## Catalog overview

### 公开工作流模板
Workflow Templates consist of YAML definitions and Docker images that define a DAG in AIMP.

📍如下工作流模板已经测试通过，并且可以在AIMP中部署. 
|工作流模板YAML文件位置|AIMP中工作流模板名称|描述|执行位置|
| ------------- | ------------- | ------------- | ------------- |
|✔[example models serving test](https://github.com/chuangxinyuan/aimp-examples/tree/master/aimp-serving)|aimp-serving-examples|参考aimp-serving-test-flow.yaml，运行aimp-serving-examples 工作流，选择sample-name 下面的模型，然后执行，可以从流日志中查看相应的执行效果|AIMP中直接执行|
|✔[Hyperparameter tuning](https://github.com/chuangxinyuan/templates/blob/master/workflows/hyperparameter-tuning)|Hyperparameter Tuning Example|Hyperparameter tuning Workflow using [NNI](https://github.com/microsoft/nni). Included in AIMP deployment. Hyperparameter tuning task is followed by a Metrics Writer task, so that you can view the best model performance metrics under Artifacts in the task info pane. Included in AIMP deployment.| AIMP中直接执行|
|✔[PyTorch training](https://github.com/chuangxinyuan/templates/blob/master/workflows/pytorch-mnist-training)|PyTorch Training|Simple MNIST training example using PyTorch. Model training task is followed by a Metrics Writer task, so that you can view model performance metrics under Artifacts in the task info pane.Included in AIMP deployment.| AIMP中直接执行|
|✔[TensorFlow Object Detection training](https://github.com/chuangxinyuan/templates/blob/master/workflows/tf-object-detection-training) |TF Object Detection Training|Workflow for object detection model training fully integrated with CVAT and included in AIMP deployment. The pip source has been changed to Tsinghua Source. Included in AIMP deployment.| CVAT工作区中执行|

The following workflow templates have not been tested
- [Albumentations data pre-processing](https://github.com/onepanelio/templates/blob/master/workflows/albumentations-preprocessing) - This Workflow is included in [TFOD](https://github.com/onepanelio/templates/tree/release-v0.18.0/workflows/tf-object-detection-training) and [MaskRCNN](https://github.com/onepanelio/templates/tree/release-v0.18.0/workflows/maskrcnn-training) training Workflows and allows you to apply different augmentations to your data before training.
- [Auto CVAT](https://github.com/onepanelio/templates/blob/master/workflows/auto-cvat) - Allows you to automate your annotation workflow by creating CVAT instances and pre-populating them with data to be annotated.
- [MaskRCNN training](https://github.com/onepanelio/templates/blob/master/workflows/maskrcnn-training) - Workflow for semantic segmentation model training fully integrated with CVAT and included in Onepanel deployment.
- [TensorFlow training](https://github.com/onepanelio/templates/blob/master/workflows/tensorflow-mnist-training) - Simple MNIST training example using TensorFlow.

### 公开工作区模板
Workspace Templates consist of YAML definitions and Docker images that define stateful instances like JupyterLab, CVAT and any other IDE.

📍如下工作区模板已经测试通过，并且可以在AIMP中部署.  
|工作区模板YAML文件位置|AIMP中工作区模板名称|描述|执行位置|
| ------------- | ------------- | ------------- | ------------- |
|✔[CVAT](https://github.com/onepanelio/templates/blob/master/workspaces/cvat)|CVAT_1.6.0|An interactive video and image annotation tool for computer vision.| AIMP中直接执行|
|✔[JupyterLab](https://github.com/onepanelio/templates/blob/master/workspaces/jupyterlab)|JupyterLab|An extensible environment for interactive and reproducible computing, based on Jupyter Notebook.| AIMP中直接执行|

The following workspace templates have not been tested
- [Eclipse Theia](https://github.com/onepanelio/templates/blob/master/workspaces/theia) - An extensible platform to develop multi-language cloud and desktop IDEs with state-of-the-art web technologies.
- [Ubuntu VNC](https://github.com/onepanelio/templates/blob/master/workspaces/vnc) (alpha) - A full Ubuntu instance accessible in your web browser.
- [Visual Studio Code](https://github.com/onepanelio/templates/blob/master/workspaces/vscode) - A lightweight but powerful source code editor which has support for just about everything. 

### Sidecars
Sidecars are components that extend your Workspace or Workflow Tasks.

- [FileSyncer](https://github.com/onepanelio/templates/blob/master/sidecars/filesyncer) - Provides the APIs to sync files between Workspaces and default object storage.
- [NNI Web UI](https://github.com/onepanelio/templates/blob/master/sidecars/nni-web-ui) - Provides a proxy to NNI Web UI so that you can see the experiments in your hyperparameter tuning Workflows.

### Tasks
Tasks are the individual tasks in your Workflow (nodes in your DAG).

- [Metrics writer](https://github.com/onepanelio/templates/blob/master/tasks/metrics-writer) - Task you can include to any Workflow Template to persist final metrics.
- [Slack notifications](https://github.com/onepanelio/templates/blob/master/tasks/slack-notify) - Task you can add to any Workflow or Workspace Template to send notifications to Slack.
