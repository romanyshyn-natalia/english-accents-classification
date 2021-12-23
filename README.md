# Accent classification  for native and non-native English speakers
Signal Processing Course project

Briefly, the accent is the way you sound when you speak. Accent classification task identifies the accent being spoken 
by a person so that the correct words being spoken can be identified by further processing since the same noises can 
mean entirely different words in different accents of the same language.


## Installation
To install from our github repository, you can do:
```bash
git clone https://github.com/romanyshyn-natalia/english-accents-classification.git
cd english-accents-classification
```

## Requirements
The following command installs all necessary packages:
```bash
pip install -r requirements.txt
```

## Dataset
I utilized the AccentDB that has three datasets that can be downloaded from [here](https://accentdb.github.io/#dataset).

| Title | Description | Notes |
|:--------- | :---------- | --------: |
|**accentdb_core**| 4 non-native Indian English accents collected by authors.   | 6,587 files   |
|**accentdb_extended**| Samples for 5 English Accents + 4 accents from accentdb_core. |   19,111 files|
|**accentdb_raw**| Raw and unprocessed recordings for the core dataset. | 11 files |

For the current research, 742 samples for speaker_1 from **accentdb_extended**| version was used. You can download the updated version of the dataset using this [link](https://drive.google.com/drive/u/0/folders/1ffLuWXmQ6LPqMLYMBa6Qh6hwnGs9pqIb).

## Experiment steps
- data exploration and preprocessing;
- MFCC features extraction;
- defining CNN model for classification;
- training and inferense;
- results analysis.

## Results
Wirh split of 70:30 between training and validation sets and, after the training with five epochs, the accuracy during the inference is 98%, which is quite remarkable.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.
