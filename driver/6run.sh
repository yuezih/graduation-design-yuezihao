CUDA_VISIBLE_DEVICES=1 python train.py ../results_6/pretrain/model.json ../results_6/pretrain/path.json --is_train
#CUDA_VISIBLE_DEVICES=7 python train.py ../results_6/finetune/model.json ../results_6/finetune/path.json --is_train --resume_file ../results_6/pretrain/model/step.196000.th
#CUDA_VISIBLE_DEVICES=1 python train.py ../results_6/finetune/model.json ../results_6/finetune/path.json --eval_set tst --resume_file ../results_6/finetune/model/step.353000.th