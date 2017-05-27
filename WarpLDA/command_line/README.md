WarpLDA: https://github.com/thu-ml/warplda

0、基本语料
全量新闻语料：

经过分词(Jieba)、ID化
（并下载到本地）

— 模型训练：可参考官方文档  —

1、数据格式化
训练集格式化：
./format -input ../corpus/train -prefix train

测试数据集的格式化：
./format -input ../corpus/_test -vocab_in train.vocab -test -prefix test

2、主题模型训练
./warplda --prefix train --k 1000 --niter 500

3、预测
./warplda --prefix test --model train.model --inference -niter 40 --perplexity 10

— 训练和预测输出文件以及说明 --
字典文件：

主题可视化文件：

模型文件：

预测结果在：

— 转换为可视化模型 —

数据标注：（格式为）

（基于统计倒序）将预测结果输出为主题分布向量：

主题向量与title JOIN：

主题向量各主题 ID 转换为标记主题：
