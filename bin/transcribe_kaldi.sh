#!/bin/bash

# default model = aspire
[[ -z "$2" ]] && model="aspire" || model="$2"
model_path="/usr/local/src/kaldi/egs/$model/s5"
graph_path=$model_path/exp/tdnn_7b_chain_online/graph_pp

# path and filenames
base_fname=${1%.*}
wav_fname=$base_fname"_1ch_8khz.wav"
lat_fname=$base_fname".lat"
ctm_fname=$base_fname".ctm"

# preprocess the file
ffmpeg -i $1 -acodec pcm_s16le -ac 1 -ar 8000 $wav_fname -y

# perform transcription
online2-wav-nnet3-latgen-faster \
    --acoustic-scale=1.0 \
    --beam=15 \
    --beam-delta=1.0 \
    --config=$model_path/exp/tdnn_7b_chain_online/conf/online.conf \
    --do-endpointing=false \
    --frame-subsampling-factor=3 \
    --max-active=7000 \
    --online=false \
    --word-symbol-table=$graph_path/words.txt \
    $model_path/exp/tdnn_7b_chain_online/final.mdl \
    $graph_path/HCLG.fst \
    "ark:echo utterance-id1 utterance-id1|" \
    "scp:echo utterance-id1 $wav_fname|" \
    "ark,t:$lat_fname"

lattice-1best \
    --lm-scale=0.8 \
    ark:$lat_fname \
    ark:- | \
lattice-align-words \
    $model_path/exp/tdnn_7b_chain_online/graph_pp/phones/word_boundary.int \
    $model_path/exp/tdnn_7b_chain_online/final.mdl \
    ark:- \
    ark:- | \
nbest-to-ctm \
    --frame-shift=0.01 \
    --print-silence=false \
    ark:- - | \
int2sym.pl \
    -f 5 \
    $model_path/exp/tdnn_7b_chain_online/graph_pp/words.txt \
    > $ctm_fname

