import argparse
from test_gen import SentenceGenerator


def parse():
    parser = argparse.ArgumentParser(description="tree transformer")
    parser.add_argument('-no_cuda', action='store_true', help="Don't use GPUs.")
    parser.add_argument('-model_dir', default='train_model', help='output model weight dir')
    parser.add_argument('-seq_length', type=int, default=50, help='sequence length')
    parser.add_argument('-batch_size', type=int, default=64, help='batch size')
    parser.add_argument('-num_step', type=int, default=100000, help='sequence length')
    parser.add_argument('-data_dir', default='data_dir', help='data dir')
    parser.add_argument('-load', action='store_true', help='load pretrained model')
    parser.add_argument('-train', action='store_true', help='whether train the model')
    parser.add_argument('-test', action='store_true', help='whether test')
    parser.add_argument('-valid_path', default='data/valid.txt', help='validation data path')
    parser.add_argument('-train_path', default='data/train.txt', help='training data path')
    parser.add_argument('-test_path', default='data/test.txt', help='testing data path')
    parser.add_argument('-mode', default='sequential', help='generation mode')
    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parse()
    sent_gen = SentenceGenerator(args)

    n_samples = 5
    batch_size = 5
    max_len = 15
    # top_k = 100
    top_k = 10
    temperature = 1.0
    leed_out_len = 5  # max_len
    burnin = 250
    sample = True
    max_iter = 500

    # Choose the prefix context
    seed_text = "The plant".split()
    bert_sents = sent_gen.generate(n_samples, seed_text=seed_text, batch_size=batch_size, max_len=max_len,
                                   generation_mode=args.mode,
                                   sample=sample, top_k=top_k, temperature=temperature, burnin=burnin,
                                   max_iter=max_iter, leed_out_len=leed_out_len)

    for sent in bert_sents:
        sent_gen.printer(sent.split(), should_detokenize=True)
