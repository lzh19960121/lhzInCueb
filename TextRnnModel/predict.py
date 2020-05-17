# coding: utf-8
# 来源：张京老师 修改：刘华振
# 没有能力维护的代码，只能调用
from __future__ import print_function

import os
import tensorflow as tf
import tensorflow.contrib.keras as kr

from TextRnnModel.rnn_model import TRNNConfig, TextRNN
from TextRnnModel.data.question_loader import read_category, read_vocab


try:
    bool(type(unicode))
except NameError:
    unicode = str


vocab_dir = r"C:\inetpub\wwwroot\AnswerQuestionSystem\TextRnnModel\data\question\question.vocab.txt"
save_path = r'C:\inetpub\wwwroot\AnswerQuestionSystem\TextRnnModel\checkpoints\textrnn\best_validation'


class CnnModel:
    def __init__(self):
        self.config = TRNNConfig()
        self.categories, self.cat_to_id = read_category()
        self.words, self.word_to_id = read_vocab(vocab_dir)
        self.config.vocab_size = len(self.words)
        self.model = TextRNN(self.config)

        self.session = tf.Session()
        self.session.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        saver.restore(sess=self.session, save_path=save_path)  # 读取保存的模型

    def predict(self, message):
        # 支持不论在python2还是python3下训练的模型都可以在2或者3的环境下运行
        content = unicode(message)
        data = [self.word_to_id[x] for x in content if x in self.word_to_id]

        feed_dict = {
            self.model.input_x: kr.preprocessing.sequence.pad_sequences([data], self.config.seq_length),
            self.model.keep_prob: 1.0
        }

        y_pred_cls = self.session.run(self.model.y_pred_cls, feed_dict=feed_dict)
        return self.categories[y_pred_cls[0]]


if __name__ == '__main__':
    cnn_model = CnnModel()
    print(cnn_model.predict("asdasdasdasd"))