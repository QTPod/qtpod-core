#!/bin/bash

model="aspire"
model_dir="/usr/local/src/kaldi/egs/$model/s5"
fname=${1%.*}"_1ch_8khz.wav"
echo $fname

# preprocess the file
ffmpeg -i $1 -acodec pcm_s16le -ac 1 -ar 8000 $fname

# perform transcription
online2-wav-nnet3-latgen-faster \
  --online=false \
  --do-endpointing=false \
  --frame-subsampling-factor=3 \
  --config=$model_dir/exp/tdnn_7b_chain_online/conf/online.conf \
  --max-active=7000 \
  --beam=30 \
  --beam-delta=1.0 \
  --lattice-beam=10 \
  --acoustic-scale=1.0 \
  --word-symbol-table=$model_dir/exp/tdnn_7b_chain_online/graph_pp/words.txt \
  $model_dir/exp/tdnn_7b_chain_online/final.mdl \
  $model_dir/exp/tdnn_7b_chain_online/graph_pp/HCLG.fst \
  "ark:echo utterance-id1 utterance-id1|" \
  "scp:echo utterance-id1 $fname|" \
  "ark:/dev/null"
