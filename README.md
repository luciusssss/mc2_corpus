# MC$^2$: Multilingual Corpus of Minority Languages in China

We present MC$^2$, a **M**ultilingual **C**orpus of **M**inority Languages in **C**hina, which is the largest open-source corpus so far. This corpus encompasses four languages, namely Tibetan, Uyghur, Kazakh written in the Kazakh Arabic script, and Mongolian written in the traditional Mongolian script.

## Languages and Sizes

There are four minority languages in dataset, and we report the dataset sizes below:

|                             | MC$^2$ (crawl) | MC$^2$ (full) |
| --------------------------- | -------------- | ------------- |
| **Tibetan**                 | 1.7G           | 2.2G          |
| **Uyghur**                  | 520M           | 736M          |
| **Kazakh (Arabic)**         | 397M           | 937M          |
| **Mongolian (Traditional)** | 874M           | 874M          |

MC$^2$ (crawl) denotes the subset of our newly-collected web crawls. MC$^2$ (full) is the complete set of MC$^2$, which additionally contains texts collected from existing resources.

## Dataset Structure

The dataset has json format, with each line contains one entry with three keys: title, text and url.

This is an example:

```
{"title":"پارتيانىڭ مەملەكەتتىك 19 - قۇرىلتايىنىڭ ورىنباسار باس حاتشىلارى","text":"ليۋ چيباۋ، مىڭ جيانجۋ، جاۋ لىجي، لي جانشۋ\n\n\n(شينحۋا اگەنتتىگىنىڭ 17 - قازاندا بەيجيڭنەن بەرگەن حابارى)","url":"kazakh.altxw.com\/system\/2017\/10\/24\/030007713.shtml"}
```

## How to Obtain the Data

Our data mainly contains three parts.

We provide the [download link of our web-crawled data](https://huggingface.co/datasets/pkupie/mc2_corpus).

For data from [Culturax](https://huggingface.co/datasets/uonlp/CulturaX) and [WikiPedia](https://huggingface.co/datasets/graelo/wikipedia), you can download and then process them using scripts in this repository.

We will upload our scripts soon.

## License Information

We released the data under the [Creative Commons CC0 license](http://creativecommons.org/publicdomain/zero/1.0/).

```
These data are released under this licensing scheme
We do not own any of the text from which these data has been extracted.
We license the data under the Creative Commons CC0 license ("no rights reserved") http://creativecommons.org/publicdomain/zero/1.0/
To the extent possible under law, Peking University have waived all copyright and related or neighboring rights to MC^2
This work is published from: China.

Should you consider that our data contains material that is owned by you and should therefore not be reproduced here, please:
* Clearly identify yourself, with detailed contact data such as an address, telephone number or email address at which you can be contacted.
* Clearly identify the copyrighted work claimed to be infringed.
* Clearly identify the material that is claimed to be infringing and information reasonably sufficient to allow us to locate the material.

We will comply to legitimate requests by removing the affected sources from the next release of the corpus.
```

## Citation Information

TBA

## Contributors

We thank [Chen Zhang](https://luciusssss.github.io/)\*, [Mingxu Tao](https://kobayashikanna01.github.io/)\*, [Quzhe Huang](https://andrewzhe.github.io/)\*, [Jiuheng Lin](https://github.com/Infinite-set)\*, [Zhibin Chen](https://zacharychenpk.github.io/), [Yansong Feng](https://yansongfeng.github.io/) for their contribution.

\* Equal Contribution
