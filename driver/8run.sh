#CUDA_VISIBLE_DEVICES=3 python train.py ../results_8/pretrain/model.json ../results_8/pretrain/path.json --is_train
CUDA_VISIBLE_DEVICES=3 python train.py ../results_8/finetune/model.json ../results_8/finetune/path.json --is_train --resume_file ../results_3/pretrain/model/step.152000.th
#CUDA_VISIBLE_DEVICES=6 python train.py ../results_8/finetune/model.json ../results_8/finetune/path.json --eval_set tst --resume_file ../results_3/finetune/model/step.121000.th