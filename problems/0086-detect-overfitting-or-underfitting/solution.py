def model_fit_quality(training_accuracy, test_accuracy):
	"""
	Determine if the model is overfitting, underfitting, or a good fit based on training and test accuracy.
	:param training_accuracy: float, training accuracy of the model (0 <= training_accuracy <= 1)
	:param test_accuracy: float, test accuracy of the model (0 <= test_accuracy <= 1)
	:return: int, one of '1', '-1', or '0'.
	"""
	# Your code here
    # 过拟合：训练准确率 - 测试准确率 > 0.2
    if training_accuracy - test_accuracy > 0.2:
        return 1
    # 欠拟合：两者都 < 0.7
    if training_accuracy < 0.7 and test_accuracy < 0.7:
        return -1
    # 其他情况：良好拟合
    return 0