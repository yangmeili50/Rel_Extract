# -*- coding: utf-8 -*-
'''
'''
class Hyperparams:
    '''Hyperparameters'''
    # data
    data_base_dir = '../Data/TrainData/open_data/open_data'

    relid2target_path = '../Data/TrainData/open_data/open_data/relation2id.txt'

    sent2rel_train_path = '../Data/TrainData/open_data/open_data/sent_relation_train.txt'
    train_senteces_path = '../Data/TrainData/open_data/open_data/sent_train.txt'

    sent2rel_test_path = '../Data/TrainData/open_data/open_data/sent_relation_test.txt'
    test_senteces_path = '../Data/TrainData/open_data/open_data/sent_test.txt'

    sent2rel_dev_path = '../Data/TrainData/open_data/open_data/sent_relation_dev.txt'
    dev_senteces_path = '../Data/TrainData/open_data/open_data/sent_dev.txt'


    vocab_path = '../Data/TrainData/open_data/open_data/vocab_cnt.txt'
    class_num = 2

    # sampling num
    train_N = 200000
    dev_N = 3000


    # training
    batch_size = 256 # alias = N
    lr = 0.001 # learning rate. In paper, learning rate is adjusted to the global step.
    logdir = '../Model/Transformer_log/' # log directory

    save_per_batch = 100
    print_per_batch = 20

    # model
    maxlen = 30 # Maximum number of words in a sentence. alias = T.
                # Feel free to increase this if you are ambitious.
    min_cnt = 20 # words whose occurred less than min_cnt are encoded as <UNK>.
    hidden_units = 512 # alias = C
    num_blocks = 6 # number of encoder/decoder blocks
    num_epochs = 20
    num_heads = 8
    dropout_rate = 0.2
    sinusoid = False # If True, use sinusoid. If false, positional embedding.
    
    
    
    
