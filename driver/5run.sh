#CUDA_VISIBLE_DEVICES=2 python train.py ../results_5/pretrain/model.json ../results_5/pretrain/path.json --is_train
#CUDA_VISIBLE_DEVICES=7 python train.py ../results_5/finetune/model.json ../results_5/finetune/path.json --is_train --resume_file ../results_5/finetune/model/step.499000.th
CUDA_VISIBLE_DEVICES=5 python train.py ../results_5/finetune/model.json ../results_5/finetune/path.json --eval_set tst --resume_file ../results_5/finetune/model/step.302000.th