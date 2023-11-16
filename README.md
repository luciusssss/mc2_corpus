# MC^2: A Multilingual Corpus of Minority Languages in China

We present MC^2, a **M**ultilingual **C**orpus of **M**inority Languages in **C**hina, which is the largest open-source corpus so far. This corpus encompasses four languages, i.e., Tibetan, Uyghur, Kazakh in the Kazakh Arabic script, and Mongolian in the traditional Mongolian script.

Our preprint is now on [Arxiv](https://arxiv.org/abs/2311.08348).

## Languages and Sizes

There are four minority languages in the dataset, and we report the dataset sizes below:

|                             | MC^2 (crawl) | MC^2 (full) |
| --------------------------- | ------------ | ----------- |
| **Tibetan**                 | 1.7G         | 2.2G        |
| **Uyghur**                  | 520M         | 736M        |
| **Kazakh (Arabic)**         | 397M         | 937M        |
| **Mongolian (Traditional)** | 874M         | 874M        |

MC^2 (crawl) denotes the subset of our newly-collected web crawls. MC^2 (full) is the complete set of MC^2, which additionally contains texts collected from existing resources.

## Dataset Structure

The dataset is in JSON format, with each line containing one entry with three keys: `title`, `text`, and `url`.

This is an example:

```
{
  "title":"پارتيانىڭ مەملەكەتتىك 19 - قۇرىلتايىنىڭ ورىنباسار باس حاتشىلارى",
  "text":"ليۋ چيباۋ، مىڭ جيانجۋ، جاۋ لىجي، لي جانشۋ\n\n\n(شينحۋا اگەنتتىگىنىڭ 17 - قازاندا بەيجيڭنەن بەرگەن حابارى)",
  "url":"kazakh.altxw.com\/system\/2017\/10\/24\/030007713.shtml"
}
```

## How to Obtain the Data

Our data mainly contains three parts.

You can download our web-crawled data from [Hugging Face](https://huggingface.co/datasets/pkupie/mc2_corpus).

For data from [CulturaX](https://huggingface.co/datasets/uonlp/CulturaX) and [Wikipedia](https://huggingface.co/datasets/graelo/wikipedia), you can download and then process them using scripts in this repository. We will upload our scripts soon.

## License Information

We released the data under the [Creative Commons CC0 license](http://creativecommons.org/publicdomain/zero/1.0/).

```
These data are released under this licensing scheme
We do not own any of the text from which these data have been extracted.
We license the data under the Creative Commons CC0 license ("no rights reserved") http://creativecommons.org/publicdomain/zero/1.0/
To the extent possible under law, Peking University has waived all copyright and related or neighboring rights to MC^2.

Should you consider that our data contains material that is owned by you and should therefore not be reproduced here, please:
* Clearly identify yourself, with detailed contact data such as an address, telephone number, or email address at which you can be contacted.
* Clearly identify the copyrighted work claimed to be infringed.
* Clearly identify the material that is claimed to be infringing and information reasonably sufficient to allow us to locate the material.

We will comply with legitimate requests by removing the affected sources from the next release of the corpus.
```

## Citation Information

```
@article{zhang2023mc2,
  title={MC^2: A Multilingual Corpus of Minority Languages in China},
  author={Chen Zhang and Mingxu Tao and Quzhe Huang and Jiuheng Lin and Zhibin Chen and Yansong Feng},
  journal={ArXiv},
  year={2023},
  volume={abs/2311.08348}
}
```

## Contributors

We thank [Chen Zhang](https://luciusssss.github.io/)\*, [Mingxu Tao](https://kobayashikanna01.github.io/)\*, [Quzhe Huang](https://andrewzhe.github.io/)\*, [Jiuheng Lin](https://github.com/Infinite-set)\*, [Zhibin Chen](https://zacharychenpk.github.io/), [Yansong Feng](https://yansongfeng.github.io/) for their contribution.

\* Equal Contribution
