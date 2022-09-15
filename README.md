# 模板目录
INESA AIIC AIMP 中工作流、工作区、任务和边车的模板目录。

## 快速上手
入门的话，最好先了解 AIMP 的 [概念](https://docs.dev.aimpcloud.cn)。

有关如何构建这些模板的更多信息，请参阅以下参考资料：

- [工作区模版](https://docs.onepanel.ai/docs/reference/workspaces/templates)
- [工作流模版](https://docs.onepanel.ai/docs/reference/workflows/templates)

## 目录概览

### 公开工作流模板
工作流模板由 YAML 定义和在 AIMP 中定义 DAG 的 Docker 映像组成。

📍如下工作流模板已经测试通过，并且可以在AIMP中部署. 
|工作流模板YAML文件位置|AIMP中工作流模板名称|描述|执行位置|
| ------------- | ------------- | ------------- | ------------- |
|✔[example models serving test](https://github.com/chuangxinyuan/aimp-examples/tree/master/aimp-serving)|aimp-serving-examples|参考 aimp-serving-test-flow.yaml，运行 aimp-serving-examples 工作流，选择 sample-name 下面的模型，然后执行，可以从流日志中查看相应的执行效果|AIMP中直接执行|
|✔[Hyperparameter tuning](https://github.com/chuangxinyuan/templates/blob/master/workflows/hyperparameter-tuning)|Hyperparameter Tuning Example|超参数调优工作流程使用 [NNI](https://github.com/microsoft/nni). 包含在 AIMP 部署中。超参数调优任务之后是 Metrics Writer 任务，因此您可以在任务信息窗格的 Artifacts 下查看最佳模型性能指标。| AIMP中直接执行|
|✔[PyTorch training](https://github.com/chuangxinyuan/templates/blob/master/workflows/pytorch-mnist-training)|PyTorch Training|使用 PyTorch 的简单 MNIST 训练示例。 模型训练任务之后是 Metrics Writer 任务，因此您可以在任务信息窗格的 Artifacts 下查看模型性能指标。包含在 AIMP 部署中。| AIMP中直接执行|
|✔[TensorFlow Object Detection training](https://github.com/chuangxinyuan/templates/blob/master/workflows/tf-object-detection-training) |TF Object Detection Training|目标检测模型训练的工作流程与 CVAT 完全集成并包含在 AIMP 部署中。pip 源已更改为清华源。 包含在 AIMP 部署中。| CVAT工作区中执行|

以下工作流模板还未经测试：
- [Albumentations data pre-processing](https://github.com/onepanelio/templates/blob/master/workflows/albumentations-preprocessing) - 这个工作流包含于 [TFOD](https://github.com/onepanelio/templates/tree/release-v0.18.0/workflows/tf-object-detection-training) 以及 [MaskRCNN](https://github.com/onepanelio/templates/tree/release-v0.18.0/workflows/maskrcnn-training) 训练工作流，并且允许您在训练之前对数据应用不同的增强。
- [Auto CVAT](https://github.com/onepanelio/templates/blob/master/workflows/auto-cvat) - 允许您通过创建 CVAT 实例并使用要标注的数据预先填充它们来自动化标注工作流。
- [MaskRCNN training](https://github.com/onepanelio/templates/blob/master/workflows/maskrcnn-training) - 语义分割模型训练的工作流与 CVAT 完全集成并包含在 AIMP 部署中。
- [TensorFlow training](https://github.com/onepanelio/templates/blob/master/workflows/tensorflow-mnist-training) - 使用 TensorFlow 的简单 MNIST 训练示例。

### 公开工作区模板
工作区模板由 YAML 定义和定义有状态实例的 Docker 映像组成，例如 JupyterLab、CVAT 和任何其他 IDE。

📍如下工作区模板已经测试通过，并且可以在AIMP中部署.  
|工作区模板YAML文件位置|AIMP中工作区模板名称|描述|执行位置|
| ------------- | ------------- | ------------- | ------------- |
|✔[CVAT](https://github.com/onepanelio/templates/blob/master/workspaces/cvat)|CVAT_1.6.0|用于计算机视觉的交互式视频和图像注释工具。| AIMP中直接执行|
|✔[JupyterLab](https://github.com/onepanelio/templates/blob/master/workspaces/jupyterlab)|JupyterLab|基于 Jupyter Notebook 的交互式和可重复计算的可扩展环境。| AIMP中直接执行|

以下工作流模板还未经测试：
- [Eclipse Theia](https://github.com/onepanelio/templates/blob/master/workspaces/theia) - 一个可扩展的平台，用于使用最先进的 Web 技术开发多语言云和桌面 IDE。
- [Ubuntu VNC](https://github.com/onepanelio/templates/blob/master/workspaces/vnc) (alpha) - 可在您的 Web 浏览器中访问的完整 Ubuntu 实例。
- [Visual Studio Code](https://github.com/onepanelio/templates/blob/master/workspaces/vscode) - 一个轻量级但功能强大的源代码编辑器，几乎支持所有内容。

### 边车
边车是扩展您的工作区或工作流任务的组件。

- [FileSyncer](https://github.com/onepanelio/templates/blob/master/sidecars/filesyncer) - 提供用于在工作区和默认对象存储之间同步文件的 API。
- [NNI Web UI](https://github.com/onepanelio/templates/blob/master/sidecars/nni-web-ui) - 为 NNI Web UI 提供代理，以便您可以查看超参数调整工作流中的实验。

### 任务
任务是工作流中的单个任务（DAG 中的节点）。

- [Metrics writer](https://github.com/onepanelio/templates/blob/master/tasks/metrics-writer) - 您可以包含在任何工作流模板中以保留最终指标的任务。
- [Slack notifications](https://github.com/onepanelio/templates/blob/master/tasks/slack-notify) - 您可以添加到任何工作流或工作区模板以向 Slack 发送通知的任务。
