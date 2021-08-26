import torch
from torch import optim
from torch import nn
import optuna

from my_lib import tokenizer, load_dic, load_dataset
from my_class import textCNN, CreateDataset, Padsequence
from my_train import train_model, cal_loss_and_acc
from my_get_weight import get_weight

def objective(trial):
    dataset = load_dataset()
    word2id = load_dic()
    emb_weights = get_weight()
    
    emb_size = int(trial.suggest_discrete_uniform('emb_size', 100, 400, 1000))
    out_channels = int(trial.suggest_discrete_uniform('out_channels', 50, 200,
                                                      50))
    drop_rate = trial.suggest_discrete_uniform('drop_rate', 0.0, 0.5, 0.1)
    learning_rate = trial.suggest_discrete_uniform('learning_rate', 5e-4, 5e-2,
                                                   5e-4)
    momentum = trial.suggest_discrete_uniform('momentum', 0.5, 0.9, 0.1)
    batch_size = int(trial.suggest_discrete_uniform('batch_size', 16, 128, 16))

    vocab_size = len(set(word2id.values())) + 1
    padding_idx = len(set(word2id.values()))
    output_size = 4
    conv_params = [[2, 0], [3, 1], [4, 2]]
    num_epochs = 30

    model = textCNN(vocab_size, emb_size, padding_idx, output_size,
                    out_channels, conv_params, drop_rate,
                    emb_weights=emb_weights)

    loss_func = nn.CrossEntropyLoss()

    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate,
                                momentum=momentum)

    use_cuda = torch.cuda.is_available()
    device = 'cuda' if use_cuda else 'cpu'
    print(f'Using {device} device')

    log = train_model(dataset[0], dataset[1], batch_size, model,
                      loss_func, optimizer, num_epochs,
                      collate_fn=Padsequence(padding_idx), device=device,
                      use_cuda=use_cuda)

    loss_valid, _ = cal_loss_and_acc(model, dataset_valid, device,
                                     loss_func=loss_func, use_cuda=use_cuda)

    return loss_valid

def main():
    dataset = load_dataset()
    word2id = load_dic()
    emb_weights = get_weight()

    use_cuda = torch.cuda.is_available()
    device = 'cuda' if use_cuda else 'cpu'
    print(f'Using {device} device')

    study = optuna.create_study()
    study.optimize(objective, timeout=7200)

    print('Best Trial:')
    trial = study.best_trial
    print(' Value: {:.3f}'.format(trial.value))
    print(' Params: ')
    for key, value in trial.params.items():
        print('   {}: {}'.format(key, value))
    
    
    vocab_size = len(set(word2id.values())) + 1
    emb_size = int(trial.params['emb_size'])
    padding_idx = len(set(word2id.values()))
    output_size = 4
    out_channels = int(trial.params['out_channels'])
    conv_params = [[2, 0], [3, 1], [4, 2]]
    drop_rate = trial.params['drop_rate']
    learning_rate = trial.params['learning_rate']
    batch_size = int(trial.params['batch_size'])
    num_epochs = 30

    model = textCNN(vocab_size, emb_size, padding_idx, output_size,
                    out_channels, conv_params, drop_rate,
                    emb_weights=emb_weights)
    print(model)

    loss_func = nn.CrossEntropyLoss()

    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate,
                                momentum=0.9)

    log = train_model(dataset[0], dataset[1], batch_size, model, loss_func,
                      optimizer, num_epochs,
                      collate_fn=Padsequence(padding_idx), device=device,
                      use_cuda=use_cuda)

    _, acc_train = cal_loss_and_acc(model, dataset[0], device,
                                    use_cuda=use_cuda)
    _, acc_test = cal_loss_and_acc(model, dataset[2], device,
                                   use_cuda=use_cuda)
    print(f'正解率（学習データ）:{acc_train:.3f}')
    print(f'正解率（評価データ）:{acc_test:.3f}')


if __name__ == '__main__':
    main()
